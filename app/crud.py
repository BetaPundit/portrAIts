import cv2
from fastapi.responses import FileResponse
import numpy as np
from PIL import Image
from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from . import models, schemas, auth
import os
from .infer_full import generate_image

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserSchema, hashed_password: str):
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user or not auth.verify_password(password, user.password):
        return False
    return user

def save_image(file: UploadFile, filename: str):
    directory = './images/'
    if not os.path.isdir(directory):
        os.mkdir(directory)
    
    # file_format = file.filename.split('.')[-1]
    # file_path = os.path.join(directory, f"{filename}.{file_format}")
    file_path = os.path.join(directory, filename)
    
    try:
        with open(file_path, 'wb') as f:
            while contents := file.file.read():
                f.write(contents)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="There was an error uploading the file",
        )
    finally:
        file.file.close()

def generate_portrait(filename: str, prompt: str="A person", style_name: str="Watercolor"):
    directory = './images/'
    file_path = os.path.join(directory, filename)
    negative_prompt = "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed photo, deformed body, anthropomorphic cat, monochrome, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green"

    generate_image(face_image_path=file_path, pose_image_path=None, prompt=prompt, negative_prompt=negative_prompt, style_name=style_name, guidance_scale=0, num_steps=5, identitynet_strength_ratio=0.80, adapter_strength_ratio=0.80)
    
    generated_image_file = FileResponse(f"{file_path}-gen.jpg", media_type="image/png")

    return generated_image_file