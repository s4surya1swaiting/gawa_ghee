from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

try:
    img = Image.open('assets/images/logo-1.png')
    # Convert to RGBA
    img = img.convert("RGBA")
    
    # Make white background transparent
    datas = img.getdata()
    newData = []
    for item in datas:
        # If it is white or very close to white, make it transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    
    img.putdata(newData)
    
    # Trim transparency
    bg = Image.new(img.mode, img.size, (255,255,255,0))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    # Resize to a reasonable max height for a logo (e.g., 200px)
    ratio = 200.0 / img.height
    new_size = (int(img.width * ratio), 200)
    img = img.resize(new_size, Image.Resampling.LANCZOS)
        
    img.save('assets/images/logo.png')
    print("Successfully processed logo.")
except Exception as e:
    print(f"Error: {e}")
