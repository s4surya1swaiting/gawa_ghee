from PIL import Image

src = 'docs/images/500gjar/500-gms-1.jpeg'
dest = 'assets/images/products/500g-Jar-Raw.webp'

try:
    with Image.open(src) as img:
        img.save(dest, "webp", quality=80)
        print("Successfully converted 500-gms-1.jpeg")
except Exception as e:
    print(f"Error: {e}")
