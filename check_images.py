from PIL import Image
import glob

all_jpegs = glob.glob('docs/images/*/*.jpeg')

def is_checkerboard(img_path):
    try:
        with Image.open(img_path) as img:
            # check the top left 100x100 pixels
            region = img.crop((0, 0, 100, 100))
            colors = region.getcolors(maxcolors=256)
            if colors is None:
                return False # more than 256 colors, so it's a natural image
            
            # If the top left is perfectly composed of a few colors (e.g., grey and white), it's probably checkerboard
            if len(colors) < 10:
                return True
            return False
    except Exception as e:
        return True

valid_images = []
for j in all_jpegs:
    if not is_checkerboard(j):
        valid_images.append(j)

print("Valid images (no checkerboard at top-left):")
for v in valid_images:
    print(v)
