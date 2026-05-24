from PIL import Image
import os

os.makedirs('assets/images/products', exist_ok=True)

# 1. 500g Jar - Crop top 15% to remove the baked-in Photoshop grid at the top
with Image.open('docs/images/500gjar/500-gms-3.jpeg') as img:
    width, height = img.size
    top_crop = int(height * 0.15)
    cropped_img = img.crop((0, top_crop, width, height))
    cropped_img.save('assets/images/products/500g-Jar-Raw.webp', 'webp', quality=85)
    print("Cropped and saved 500g-Jar-Raw.webp")

# 2. 1Kg Tin
with Image.open('docs/images/1kgtin/1-Kg-4-Tin.jpeg') as img:
    img.save('assets/images/products/1Kg-Tin-Raw.webp', 'webp', quality=85)
    print("Saved 1Kg-Tin-Raw.webp")

# 3. 15Kg Tin
with Image.open('docs/images/15kgtin/15-Kg-2-Tin.jpeg') as img:
    img.save('assets/images/products/15Kg-Tin-Raw.webp', 'webp', quality=85)
    print("Saved 15Kg-Tin-Raw.webp")
