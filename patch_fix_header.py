import glob
import re

html_files = glob.glob("*.html")

target_pattern = r'\s*<div class="ghee-pour" id="gheePour">.*?</div>\s*</div>'

for f in html_files:
    with open(f, "r") as file:
        content = file.read()
    
    new_content = re.sub(target_pattern, '', content, flags=re.DOTALL)
    
    with open(f, "w") as file:
        file.write(new_content)
    print(f"Fixed {f}")
