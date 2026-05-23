import glob
import re

html_files = glob.glob("*.html")

target_pattern = r'<div class="ghee-assistant" onclick="toggleAssistant\(\)">.*?</div>\s*</div>'

replacement = """<div class="header-call-action">
                    <a href="tel:+919163694770" class="pulse-call-btn">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
                            <path d="M6.62 10.79a15.15 15.15 0 006.59 6.59l2.2-2.2a1 1 0 011.11-.27c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.24.2 2.45.57 3.57a1 1 0 01-.27 1.11l-2.2 2.2z"/>
                        </svg>
                        <span>+91 91636 94770</span>
                    </a>
                </div>"""

for f in html_files:
    with open(f, "r") as file:
        content = file.read()
    
    # We use re.sub with re.DOTALL to match across newlines
    new_content = re.sub(target_pattern, replacement, content, flags=re.DOTALL)
    
    with open(f, "w") as file:
        file.write(new_content)
    print(f"Patched {f}")
