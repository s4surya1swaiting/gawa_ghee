import glob
import os

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Replace png and jpeg with webp
    # This assumes we want to change ALL image references in HTML to webp.
    # We will ignore favicon.ico etc.
    content = content.replace('.png"', '.webp"')
    content = content.replace('.jpeg"', '.webp"')
    content = content.replace('.jpg"', '.webp"')
    
    # Specific homepage replacements for the real-background images requested by user
    if f == 'index.html':
        content = content.replace('retail & departmental stores.webp', '500g-Jar-Raw.webp')
        content = content.replace('wholesale & distributors.webp', '1Kg-Tin-Raw.webp')
        content = content.replace('F&B Industries.webp', '15Kg-Tin-Raw.webp')
        
    with open(f, 'w') as file:
        file.write(content)
        
    print(f"Patched HTML file: {f}")
