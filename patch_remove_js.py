import glob
import re

html_files = glob.glob("*.html")

# The script block looks like:
#        function toggleAssistant() {
#            ...
#        }

target_pattern = r'\s*function toggleAssistant\(\) \{[\s\S]*?\}\s*(?=</script>)'

for f in html_files:
    with open(f, "r") as file:
        content = file.read()
    
    new_content = re.sub(target_pattern, '', content)
    
    with open(f, "w") as file:
        file.write(new_content)
    print(f"Cleaned JS from {f}")
