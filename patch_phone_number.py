import glob

html_files = glob.glob("*.html")

for f in html_files:
    with open(f, "r") as file:
        content = file.read()
    
    # Replace the text variants
    new_content = content.replace("91636 94770", "70037 39984")
    # Replace the tel:/wa.me/ variants
    new_content = new_content.replace("9163694770", "7003739984")
    
    with open(f, "w") as file:
        file.write(new_content)
    
    print(f"Patched phone numbers in {f}")
