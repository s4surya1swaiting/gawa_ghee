import os
import glob
from PIL import Image

def convert_to_webp(src, dest):
    try:
        with Image.open(src) as img:
            img.save(dest, "webp", quality=80)
            return True
    except Exception as e:
        print(f"Error converting {src}: {e}")
        return False

# 1. Convert specific raw product images for homepage
os.makedirs('assets/images/products', exist_ok=True)

raw_images = [
    ('docs/images/500gjar/500-gms-3.jpeg', 'assets/images/products/500g-Jar-Raw.webp'),
    ('docs/images/1kgtin/1-Kg-4-Tin.jpeg', 'assets/images/products/1Kg-Tin-Raw.webp'),
    ('docs/images/15kgtin/15-Kg-2-Tin.jpeg', 'assets/images/products/15Kg-Tin-Raw.webp')
]

for src, dest in raw_images:
    print(f"Converting raw homepage image: {src} -> {dest}")
    convert_to_webp(src, dest)

# 2. Convert all existing images in assets/images/ to webp
all_images = glob.glob('assets/images/**/*.png', recursive=True) + \
             glob.glob('assets/images/**/*.jpeg', recursive=True) + \
             glob.glob('assets/images/**/*.jpg', recursive=True)

for img_path in all_images:
    base, ext = os.path.splitext(img_path)
    webp_path = base + '.webp'
    
    # Don't convert if webp already exists or if it's already a webp
    if ext.lower() == '.webp':
        continue
        
    print(f"Converting: {img_path} -> {webp_path}")
    if convert_to_webp(img_path, webp_path):
        # Optional: remove original to save space
        # os.remove(img_path)
        pass

print("WebP conversion completed.")
