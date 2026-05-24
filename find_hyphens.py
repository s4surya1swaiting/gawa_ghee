import glob
import re
from bs4 import BeautifulSoup

html_files = glob.glob("*.html")

all_hyphenated = set()

for f in html_files:
    with open(f, 'r') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    text = soup.get_text()
    # Find hyphenated words
    words = re.findall(r'\b[a-zA-Z]+-[a-zA-Z]+\b', text)
    
    for w in words:
        all_hyphenated.add(w)

print("Hyphenated words found in content:")
for w in sorted(list(all_hyphenated)):
    print(w)
