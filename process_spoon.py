from rembg import remove
import sys

input_path = '/home/surya/.gemini/antigravity/brain/f86a86b7-3e1f-455b-9a0c-d1562be97f21/spoonful_of_ghee_raw_1779517499110.png'
output_path = '/home/surya/projects/gawa_ghee/assets/images/products/spoonful_of_ghee.png'

print(f"Processing {input_path}...")
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_data = i.read()
        output_data = remove(input_data)
        o.write(output_data)
print("Done!")
