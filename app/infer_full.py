import random
from typing import Tuple
import cv2
from fastapi import HTTPException, status
import torch
import numpy as np
from PIL import Image
import diffusers
from diffusers import LCMScheduler
from diffusers.utils import load_image
from diffusers.models import ControlNetModel
from diffusers.pipelines.controlnet.multicontrolnet import MultiControlNetModel
from insightface.app import FaceAnalysis
from .pipeline_stable_diffusion_xl_instantid_full import StableDiffusionXLInstantIDPipeline, draw_kps
from .style_template import styles
from controlnet_aux import MidasDetector
from .model_util import get_torch_device, load_models_xl
from huggingface_hub import hf_hub_download

# global variables
device = get_torch_device()
dtype = torch.float16 if str(device).__contains__("cuda") else torch.float32
MAX_SEED = np.iinfo(np.int32).max
STYLE_NAMES = list(styles.keys())
DEFAULT_STYLE_NAME = "Watercolor"

def convert_from_cv2_to_image(img: np.ndarray) -> Image:
        return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

def convert_from_image_to_cv2(img: Image) -> np.ndarray:
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def resize_img(input_image, max_side=1280, min_side=1024, size=None, 
               pad_to_max_side=False, mode=Image.BILINEAR, base_pixel_number=64):

    w, h = input_image.size
    if size is not None:
        w_resize_new, h_resize_new = size
    else:
        ratio = min_side / min(h, w)
        w, h = round(ratio*w), round(ratio*h)
        ratio = max_side / max(h, w)
        input_image = input_image.resize([round(ratio*w), round(ratio*h)], mode)
        w_resize_new = (round(ratio * w) // base_pixel_number) * base_pixel_number
        h_resize_new = (round(ratio * h) // base_pixel_number) * base_pixel_number
    input_image = input_image.resize([w_resize_new, h_resize_new], mode)

    if pad_to_max_side:
        res = np.ones([max_side, max_side, 3], dtype=np.uint8) * 255
        offset_x = (max_side - w_resize_new) // 2
        offset_y = (max_side - h_resize_new) // 2
        res[offset_y:offset_y+h_resize_new, offset_x:offset_x+w_resize_new] = np.array(input_image)
        input_image = Image.fromarray(res)
    return input_image


# Load face encoder
app = FaceAnalysis(name='antelopev2', root='./', providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

# Path to InstantID models
face_adapter = f'./checkpoints/ip-adapter.bin'
controlnet_path = f'./checkpoints/ControlNetModel'
controlnet_depth_path = f'diffusers/controlnet-depth-sdxl-1.0-small'

# Load depth detector
midas = MidasDetector.from_pretrained("lllyasviel/Annotators")

# Load pipeline (old)
# controlnet_list = [controlnet_path, controlnet_depth_path]
# controlnet_model_list = []
# for controlnet_path in controlnet_list:
#     controlnet = ControlNetModel.from_pretrained(controlnet_path, torch_dtype=dtype)
#     controlnet_model_list.append(controlnet)
# controlnet = MultiControlNetModel(controlnet_model_list)

# pipe = StableDiffusionXLInstantIDPipeline.from_pretrained(
#     base_model_path,
#     controlnet=controlnet,
#     torch_dtype=dtype,
# )

# Load pipeline
controlnet = ControlNetModel.from_pretrained(controlnet_path, torch_dtype=dtype)

# base_model_path = 'stabilityai/stable-diffusion-xl-base-1.0'
base_model_path = 'wangqixun/YamerMIX_v8'

if base_model_path.endswith(
        ".ckpt"
    ) or base_model_path.endswith(".safetensors"):
        scheduler_kwargs = hf_hub_download(
            repo_id="wangqixun/YamerMIX_v8",
            subfolder="scheduler",
            filename="scheduler_config.json",
        )

        (tokenizers, text_encoders, unet, _, vae) = load_models_xl(
            base_model_path=base_model_path,
            scheduler_name=None,
            weight_dtype=dtype,
        )

        scheduler = diffusers.EulerDiscreteScheduler.from_config(scheduler_kwargs)
        pipe = StableDiffusionXLInstantIDPipeline(
            vae=vae,
            text_encoder=text_encoders[0],
            text_encoder_2=text_encoders[1],
            tokenizer=tokenizers[0],
            tokenizer_2=tokenizers[1],
            unet=unet,
            scheduler=scheduler,
            controlnet=controlnet,
        ).to(device)

else:
    pipe = StableDiffusionXLInstantIDPipeline.from_pretrained(
        base_model_path,
        controlnet=controlnet,
        torch_dtype=dtype,
        safety_checker=None,
        feature_extractor=None,
    ).to(device)

    pipe.scheduler = diffusers.EulerDiscreteScheduler.from_config(pipe.scheduler.config)

pipe.cuda()
pipe.load_ip_adapter_instantid(face_adapter)
pipe.load_lora_weights("latent-consistency/lcm-lora-sdxl")
pipe.disable_lora()

def apply_style(style_name: str, positive: str, negative: str = "") -> Tuple[str, str]:
        p, n = styles.get(style_name, styles[DEFAULT_STYLE_NAME])
        return p.replace("{prompt}", positive), n + ' ' + negative

def generate_image(face_image_path, pose_image_path, prompt, negative_prompt, style_name, num_steps, identitynet_strength_ratio, adapter_strength_ratio, guidance_scale, enable_LCM=True, enhance_face_region=True):
        face_error = HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot find any input face image! Please upload an image containing a face.",
            )
        
        if enable_LCM:
            pipe.enable_lora()
            pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
        else:
            pipe.disable_lora()
            pipe.scheduler = diffusers.EulerDiscreteScheduler.from_config(pipe.scheduler.config)
    
        if face_image_path is None:
            raise face_error
        
        if prompt is None:
            prompt = "a person"
        
        # apply the style template
        print(f">>>>>{face_image_path}")
        prompt, negative_prompt = apply_style(style_name, prompt, negative_prompt)
        
        face_image = load_image(face_image_path)
        print(f">>>>>{face_image}")
        face_image = resize_img(face_image)
        face_image_cv2 = convert_from_image_to_cv2(face_image)
        height, width, _ = face_image_cv2.shape
        
        # Extract face features
        face_info = app.get(face_image_cv2)
        
        if len(face_info) == 0:
            raise face_error
        
        face_info = sorted(face_info, key=lambda x:(x['bbox'][2]-x['bbox'][0])*(x['bbox'][3]-x['bbox'][1]))[-1]  # only use the maximum face
        face_emb = face_info['embedding']
        face_kps = draw_kps(convert_from_cv2_to_image(face_image_cv2), face_info['kps'])
        
        if pose_image_path is not None:
            pose_image = load_image(pose_image_path)
            pose_image = resize_img(pose_image)
            pose_image_cv2 = convert_from_image_to_cv2(pose_image)
            
            face_info = app.get(pose_image_cv2)
            
            if len(face_info) == 0:
                raise face_error
            
            face_info = face_info[-1]
            face_kps = draw_kps(pose_image, face_info['kps'])
            
            width, height = face_kps.size

        if enhance_face_region:
            control_mask = np.zeros([height, width, 3])
            x1, y1, x2, y2 = face_info["bbox"]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            control_mask[y1:y2, x1:x2] = 255
            control_mask = Image.fromarray(control_mask.astype(np.uint8))
        else:
            control_mask = None


        seed = random.randint(0, MAX_SEED)

        generator = torch.Generator(device=device).manual_seed(seed)
        
        print("Start inference...")
        print(f"[Debug] Prompt: {prompt}, \n[Debug] Neg Prompt: {negative_prompt}")
        
        pipe.set_ip_adapter_scale(adapter_strength_ratio)
        image = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            image_embeds=face_emb,
            image=face_kps,
            control_mask=control_mask,
            controlnet_conditioning_scale=float(identitynet_strength_ratio),
            num_inference_steps=num_steps,
            guidance_scale=guidance_scale,
            height=height,
            width=width,
            generator=generator
        ).images[0]

        image.save(f"{face_image_path}-gen.jpg")
        return image