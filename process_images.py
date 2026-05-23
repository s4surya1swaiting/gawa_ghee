import os
import glob
from rembg import remove
from PIL import Image
import sys

input_dir = 'docs/images'
output_dir = 'assets/images/products'

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define sku mapping matching the directory structure
# This matches the names used in HTML
sku_mapping = {
    '50gjar': '50g-Jar',
    '100gjar': '100g-Jar',
    '250gjar': '250g-Jar',
    '500gjar': '500g-Jar',
    '1kgjar': '1Kg-Jar',
    '1kgtin': '1Kg-Tin',
    '5kgjar': '5Kg-Jar',
    '5kgtin': '5Kg-Tin',
    '15kgtin': '15Kg-Tin'
}

# Find all jpegs
all_images = glob.glob(f"{input_dir}/**/*.jpeg", recursive=True)

print(f"Found {len(all_images)} images to process...")

for img_path in all_images:
    # get folder name
    parent_dir = os.path.basename(os.path.dirname(img_path))
    filename = os.path.basename(img_path)
    
    if parent_dir not in sku_mapping:
        continue
        
    sku_prefix = sku_mapping[parent_dir]
    
    # We want to name them nicely, e.g. 500g-Jar-1.png, 500g-Jar-2.png
    # The original filename usually has a number, e.g. 500-gms-3.jpeg or 5-Kg-2-Tin.jpeg
    # Let's just extract the digit.
    import re
    digits = re.findall(r'\d+', filename)
    # The last digit is usually the sequence number
    if digits:
        seq = digits[-1]
    else:
        seq = "0"
        
    out_name = f"{sku_prefix}-{seq}.png"
    out_path = os.path.join(output_dir, out_name)
    
    print(f"Processing {filename} -> {out_name}...")
    
    try:
        with open(img_path, 'rb') as i:
            with open(out_path, 'wb') as o:
                input_data = i.read()
                output_data = remove(input_data)
                o.write(output_data)
    except Exception as e:
        print(f"Failed to process {img_path}: {e}")

print("Done!")
