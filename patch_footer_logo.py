import glob

html_files = glob.glob("*.html")

target = '<h4 style="font-family: var(--font-heading); font-size: 1.5rem;">GAWA GHEE</h4>'
replacement = '<img src="assets/images/logo.png" alt="Gawa Ghee Logo" style="max-height: 40px; margin-bottom: 0.5rem; display: block;">'

for f in html_files:
    with open(f, "r") as file:
        content = file.read()
    
    if target in content:
        new_content = content.replace(target, replacement)
        with open(f, "w") as file:
            file.write(new_content)
        print(f"Patched footer logo in {f}")
    else:
        print(f"No match found in {f}")
