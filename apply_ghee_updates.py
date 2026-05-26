import os
import re
import glob
from PIL import Image

# Define directory paths
updated_dir = 'docs/images/updated'
output_dir = 'assets/images/products'

os.makedirs(output_dir, exist_ok=True)

# Mapping from source folder names to SKU prefix in HTML
folder_to_sku = {
    '50 Grams (Jar)': '50g-Jar',
    '100 Grams (Jar)': '100g-Jar',
    '250 Grams (Jar)': '250g-Jar',
    '500 Grams (Jar)': '500g-Jar',
    '1 Kg (Jar)': '1Kg-Jar',
    '1 Kg (Tin)': '1Kg-Tin',
    '5 Kgs (Jar)': '5Kg-Jar',
    '5 Kgs (Tin)': '5Kg-Tin',
    '15 Kgs (Tin)': '15Kg-Tin'
}

# Try to import rembg for background removal, with a fallback if not installed
try:
    from rembg import remove
    REMBG_AVAILABLE = True
    print("rembg is available. Background removal enabled.")
except ImportError:
    REMBG_AVAILABLE = False
    print("rembg is not installed. Converting directly to WebP.")

def process_image(src_path, dest_path):
    try:
        if REMBG_AVAILABLE:
            with open(src_path, 'rb') as f:
                input_data = f.read()
            output_data = remove(input_data)
            # Save bytes as Image
            from io import BytesIO
            img = Image.open(BytesIO(output_data))
        else:
            img = Image.open(src_path)
            
        img.save(dest_path, 'webp', quality=85)
        print(f"Success: {src_path} -> {dest_path}")
        return True
    except Exception as e:
        print(f"Error processing {src_path} -> {dest_path}: {e}")
        return False

# Find all subdirectories in updated_dir
subdirs = glob.glob(os.path.join(updated_dir, '*'))

for subdir in subdirs:
    folder_name = os.path.basename(subdir)
    if folder_name not in folder_to_sku:
        print(f"Skipping folder: {folder_name} (not in SKU mapping)")
        continue
        
    sku_prefix = folder_to_sku[folder_name]
    mockups_path = os.path.join(subdir, 'Final_Mockups')
    
    if not os.path.exists(mockups_path):
        print(f"Warning: Mockups directory does not exist for {folder_name}: {mockups_path}")
        continue
        
    jpegs = glob.glob(os.path.join(mockups_path, '*.jpeg')) + glob.glob(os.path.join(mockups_path, '*.jpg'))
    print(f"\nProcessing {len(jpegs)} images in {folder_name}...")
    
    for jpeg in jpegs:
        filename = os.path.basename(jpeg)
        
        # Check for the special filename
        if '202605211853' in filename:
            out_name = f"{sku_prefix}-202605211853.webp"
        else:
            # Extract sequence number from filename, e.g. 50-gms-1.jpeg -> 1
            digits = re.findall(r'\d+', filename)
            seq = digits[-1] if digits else "1"
            out_name = f"{sku_prefix}-{seq}.webp"
            
        dest_path = os.path.join(output_dir, out_name)
        process_image(jpeg, dest_path)

# Also generate the raw/lifestyle images used on the homepage
raw_homepage_images = [
    ('docs/images/updated/500 Grams (Jar)/Final_Mockups/500-gms-3.jpeg', 'assets/images/products/500g-Jar-Raw.webp'),
    ('docs/images/updated/1 Kg (Tin)/Final_Mockups/1-Kg-4-Tin.jpeg', 'assets/images/products/1Kg-Tin-Raw.webp'),
    ('docs/images/updated/15 Kgs (Tin)/Final_Mockups/15-Kg-2-Tin.jpeg', 'assets/images/products/15Kg-Tin-Raw.webp')
]

print("\nProcessing raw homepage preview images...")
for src, dest in raw_homepage_images:
    if os.path.exists(src):
        process_image(src, dest)
    else:
        print(f"Warning: Source file for homepage preview does not exist: {src}")

print("\nImage processing completed!")
