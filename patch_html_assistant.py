import re

html_files = ['index.html', 'products.html', 'our-story.html', 'contact.html']

old_html = """                        <div class="ghee-drop">
                            <div class="ghee-content">
                                <div class="ghee-call-icon">📞</div>
                            </div>
                        </div>"""

new_html = """                        <img class="ghee-spoon" src="assets/images/products/spoonful_of_ghee.png" alt="Spoon of Ghee">"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_html in content:
        new_content = content.replace(old_html, new_html)
        # Also bump css version v=1.10 to v=1.11 to invalidate cache
        new_content = new_content.replace('css/style.css?v=1.10', 'css/style.css?v=1.11')
        new_content = new_content.replace('css/style.css?v=1.9', 'css/style.css?v=1.11')
        new_content = new_content.replace('css/style.css?v=1.8', 'css/style.css?v=1.11')
        new_content = new_content.replace('css/style.css?v=1.7', 'css/style.css?v=1.11')
        new_content = new_content.replace('css/style.css?v=1.6', 'css/style.css?v=1.11')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched {file}")
    else:
        print(f"Could not find old HTML in {file}")
