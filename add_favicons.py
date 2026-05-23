import glob
import os

html_files = glob.glob("*.html")

favicon_tags = """
    <!-- Favicon & Mobile Icons -->
    <link rel="icon" type="image/x-icon" href="assets/images/favicon/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="assets/images/favicon/apple-touch-icon.png">
    <meta name="theme-color" content="#FAF8F5">
</head>"""

for f in html_files:
    with open(f, "r") as file:
        content = file.read()
    
    # Check if we already added it to prevent duplication
    if "apple-touch-icon.png" not in content:
        # replace </head> with the new tags
        new_content = content.replace("</head>", favicon_tags)
        with open(f, "w") as file:
            file.write(new_content)
        print(f"Added favicons to {f}")
    else:
        print(f"Favicons already exist in {f}")
