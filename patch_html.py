import os
import re

# Read products.html and index.html
html_files = ['products.html', 'index.html']
img_dir = 'assets/images/products'

# Collect available png images grouped by SKU
sku_images = {}
for file in os.listdir(img_dir):
    if file.endswith('.png'):
        # Extract SKU prefix
        parts = file.split('-')
        # e.g., 500g-Jar-1.png -> prefix 500g-Jar
        if len(parts) >= 3:
            sku = f"{parts[0]}-{parts[1]}"
            if sku not in sku_images:
                sku_images[sku] = []
            sku_images[sku].append(file)
            
# Sort the lists
for sku in sku_images:
    sku_images[sku] = sorted(sku_images[sku])

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace <div class="product-image"> ... </div>
    # with the new main image and the gallery
    
    # Find all product cards
    def replace_card(match):
        img_src = match.group(1) # e.g. assets/images/products/50g-Jar.jpeg
        alt_text = match.group(2)
        
        # Extract SKU from jpeg filename
        filename = os.path.basename(img_src)
        sku = filename.replace('.jpeg', '')
        
        # If we have processed PNGs for this SKU
        if sku in sku_images and len(sku_images[sku]) > 0:
            main_img_path = f"assets/images/products/{sku_images[sku][0]}"
            gallery_html = '\n                    <div class="product-gallery">\n'
            for idx, img in enumerate(sku_images[sku]):
                active_class = " active" if idx == 0 else ""
                gallery_html += f'                        <img src="assets/images/products/{img}" class="gallery-thumb{active_class}" alt="{alt_text} Variation {idx+1}">\n'
            gallery_html += '                    </div>'
            
            # Reconstruct the HTML
            res = f'<div class="product-image">\n                        <img src="{main_img_path}" alt="{alt_text}">\n                    </div>{gallery_html}'
            return res
        return match.group(0) # fallback
    
    # Regex to match the product image container
    # <div class="product-image">\n                        <img src="..." alt="...">\n                    </div>
    pattern = r'<div class="product-image">\s*<img src="([^"]+)" alt="([^"]+)">\s*</div>'
    
    new_content = re.sub(pattern, replace_card, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("HTML update complete!")
