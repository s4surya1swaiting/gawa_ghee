import re

file_path = "products.html"

with open(file_path, "r") as file:
    content = file.read()

# Replace <h3>Gawa Ghee — 50g Jar</h3> with <h3><b>50g Jar</b></h3>
new_content = re.sub(r'<h3>Gawa Ghee — (.*?)</h3>', r'<h3><b>\1</b></h3>', content)

with open(file_path, "w") as file:
    file.write(new_content)
    
print("Cleaned up product names in products.html")
