style_list = [
    {
        "name": "(No style)",
        "prompt": "{prompt}",
        "negative_prompt": "",
    },
    {
        "name": "Watercolor",
        "prompt": "watercolor painting, {prompt}. vibrant, beautiful, painterly, detailed, textural, artistic",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy",
    },
    {
        "name": "Film Noir",
        "prompt": "film noir style, ink sketch|vector, {prompt} highly detailed, sharp focus, ultra sharpness, monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Neon",
        "prompt": "masterpiece painting, buildings in the backdrop, kaleidoscope, lilac orange blue cream fuchsia bright vivid gradient colors, the scene is cinematic, {prompt}, emotional realism, double exposure, watercolor ink pencil, graded wash, color layering, magic realism, figurative painting, intricate motifs, organic tracery, polished",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Jungle",
        "prompt": 'waist-up "{prompt} in a Jungle" by Syd Mead, tangerine cold color palette, muted colors, detailed, 8k,photo r3al,dripping paint,3d toon style,3d style,Movie Still',
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Mars",
        "prompt": "{prompt}, Post-apocalyptic. Mars Colony, Scavengers roam the wastelands searching for valuable resources, rovers, bright morning sunlight shining, (detailed) (intricate) (8k) (HDR) (cinematic lighting) (sharp focus)",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Vibrant Color",
        "prompt": "vibrant colorful, ink sketch|vector|2d colors, at nightfall, sharp focus, {prompt}, highly detailed, sharp focus, the clouds,colorful,ultra sharpness",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Snow",
        "prompt": "cinema 4d render, {prompt}, high contrast, vibrant and saturated, sico style, surrounded by magical glow,floating ice shards, snow crystals, cold, windy background, frozen natural landscape in background  cinematic atmosphere,highly detailed, sharp focus, intricate design, 3d, unreal engine, octane render, CG best quality, highres, photorealistic, dramatic lighting, artstation, concept art, cinematic, epic Steven Spielberg movie still, sharp focus, smoke, sparks, art by pascal blanche and greg rutkowski and repin, trending on artstation, hyperrealism painting, matte painting, 4k resolution",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Line art",
        "prompt": "line art drawing {prompt} . professional, sleek, modern, minimalist, graphic, line art, vector graphics",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, blurry, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, mutated, realism, realistic, impressionism, expressionism, oil, acrylic",
    },
    {
    "name": "Anime",
    "prompt": "anime artwork {prompt} . anime style, key visual, vibrant, studio anime,  highly detailed",
    "negative_prompt": "photo, deformed, black and white, realism, disfigured, low contrast"
  },
  {
    "name": "Cinematic",
    "prompt": "cinematic film still {prompt} . shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
    "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
  },
  {
    "name": "Comic Book",
    "prompt": "comic {prompt} . graphic illustration, comic art, graphic novel art, vibrant, highly detailed",
    "negative_prompt": "photograph, deformed, glitch, noisy, realistic, stock photo"
  },
  {
    "name": "Craft Clay",
    "prompt": "play-doh style {prompt} . sculpture, clay art, centered composition, Claymation",
    "negative_prompt": "sloppy, messy, grainy, highly detailed, ultra textured, photo"
  },
  {
    "name": "Digital Art",
    "prompt": "concept art {prompt} . digital artwork, illustrative, painterly, matte painting, highly detailed",
    "negative_prompt": "photo, photorealistic, realism, ugly"
  },
  {
    "name": "Enhance",
    "prompt": "breathtaking {prompt} . award-winning, professional, highly detailed",
    "negative_prompt": "ugly, deformed, noisy, blurry, distorted, grainy"
  },
  {
    "name": "Abstract",
    "prompt": "Abstract style {prompt} . Non-representational, colors and shapes, expression of feelings, imaginative, highly detailed",
    "negative_prompt": "realistic, photographic, figurative, concrete"
  },
  {
    "name": "Cubist",
    "prompt": "Cubist artwork {prompt} . Geometric shapes, abstract, innovative, revolutionary",
    "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
  },
  {
    "name": "Graffiti",
    "prompt": "Graffiti style {prompt} . Street art, vibrant, urban, detailed, tag, mural",
    "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
  },
  {
    "name": "Hyperrealism",
    "prompt": "Hyperrealistic art {prompt} . Extremely high-resolution details, photographic, realism pushed to extreme, fine texture, incredibly lifelike",
    "negative_prompt": "simplified, abstract, unrealistic, impressionistic, low resolution"
  },
  {
    "name": "Impressionist",
    "prompt": "Impressionist painting {prompt} . Loose brushwork, vibrant color, light and shadow play, captures feeling over form",
    "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
  },
  {
    "name": "Renaissance",
    "prompt": "Renaissance style {prompt} . Realistic, perspective, light and shadow, religious or mythological themes, highly detailed",
    "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, modernist, minimalist, abstract"
  },
  {
    "name": "GTA",
    "prompt": "GTA-style artwork {prompt} . Satirical, exaggerated, pop art style, vibrant colors, iconic characters, action-packed",
    "negative_prompt": "realistic, black and white, low contrast, impressionist, cubist, noisy, blurry, deformed"
  },
  {
    "name": "Super Mario",
    "prompt": "Super Mario style {prompt} . Vibrant, cute, cartoony, fantasy, playful, reminiscent of Super Mario series",
    "negative_prompt": "realistic, modern, horror, dystopian, violent"
  },
  {
    "name": "Minecraft",
    "prompt": "Minecraft style {prompt} . Blocky, pixelated, vibrant colors, recognizable characters and objects, game assets",
    "negative_prompt": "smooth, realistic, detailed, photorealistic, noise, blurry, deformed"
  },
  {
    "name": "Pokémon",
    "prompt": "Pokémon style {prompt} . Vibrant, cute, anime, fantasy, reminiscent of Pokémon series",
    "negative_prompt": "realistic, modern, horror, dystopian, violent"
  },
  {
    "name": "Retro Arcade",
    "prompt": "Retro arcade style {prompt} . 8-bit, pixelated, vibrant, classic video game, old school gaming, reminiscent of 80s and 90s arcade games",
    "negative_prompt": "modern, ultra-high resolution, photorealistic, 3D"
  },
  {
    "name": "Retro Game",
    "prompt": "Retro game art {prompt} . 16-bit, vibrant colors, pixelated, nostalgic, charming, fun",
    "negative_prompt": "realistic, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
  },
  {
    "name": "RPG Fantasy Game",
    "prompt": "Role-playing game (RPG) style fantasy {prompt} . Detailed, vibrant, immersive, reminiscent of high fantasy RPG games",
    "negative_prompt": "sci-fi, modern, urban, futuristic, low detailed"
  },
  {
    "name": "Strategy Game",
    "prompt": "Strategy game style {prompt} . Overhead view, detailed map, units, reminiscent of real-time strategy video games",
    "negative_prompt": "first-person view, modern, photorealistic"
  },
  {
    "name": "Street Fighter",
    "prompt": "Street Fighter style {prompt} . Vibrant, dynamic, arcade, 2D fighting game, highly detailed, reminiscent of Street Fighter series",
    "negative_prompt": "3D, realistic, modern, photorealistic, turn-based strategy"
  },
  {
    "name": "Legend of Zelda",
    "prompt": "Legend of Zelda style {prompt} . Vibrant, fantasy, detailed, epic, heroic, reminiscent of The Legend of Zelda series",
    "negative_prompt": "sci-fi, modern, realistic, horror"
  },
]

styles = {k["name"]: (k["prompt"], k["negative_prompt"]) for k in style_list}