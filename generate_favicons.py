from PIL import Image
import os

img_path = 'assets/images/logo.png'
out_dir = 'assets/images/favicon'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

try:
    # Open the logo image
    img = Image.open(img_path)
    
    # We need a square image for favicons. Let's create a square canvas and paste the logo in the center.
    size = max(img.width, img.height)
    # Add a little padding (10%)
    canvas_size = int(size * 1.2)
    
    square_img = Image.new('RGBA', (canvas_size, canvas_size), (255, 255, 255, 0))
    offset = ((canvas_size - img.width) // 2, (canvas_size - img.height) // 2)
    square_img.paste(img, offset, img)
    
    # Generate sizes
    sizes = {
        'favicon-16x16.png': (16, 16),
        'favicon-32x32.png': (32, 32),
        'apple-touch-icon.png': (180, 180),
        'android-chrome-192x192.png': (192, 192),
        'android-chrome-512x512.png': (512, 512)
    }
    
    for filename, dims in sizes.items():
        resized = square_img.resize(dims, Image.Resampling.LANCZOS)
        resized.save(os.path.join(out_dir, filename))
        
    # Generate favicon.ico (contains both 16x16 and 32x32)
    icon_16 = square_img.resize((16, 16), Image.Resampling.LANCZOS)
    icon_32 = square_img.resize((32, 32), Image.Resampling.LANCZOS)
    icon_48 = square_img.resize((48, 48), Image.Resampling.LANCZOS)
    icon_48.save(os.path.join(out_dir, 'favicon.ico'), format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    
    print("Successfully generated all favicons!")
    
except Exception as e:
    print(f"Error generating favicons: {e}")
