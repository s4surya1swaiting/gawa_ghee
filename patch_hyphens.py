import glob
import os

replacements = {
    "end-to-end": "complete",
    "End-to-End": "Complete",
    "End-to-end": "Complete",
    "Eye-catching": "Attractive",
    "Full-scale": "Full scale",
    "High-margin": "Highly profitable",
    "High-volume": "Large volume",
    "Industrial-grade": "Industrial standard",
    "Lab-Cleared": "Lab tested",
    "Mid-volume": "Medium volume",
    "Middle-size": "Medium size",
    "Multi-decade": "Long standing",
    "Pan-India": "Across India",
    "Real-time": "Instant",
    "Supply-Chain": "Supply chain",
    "White-Label": "White label",
    "White-label": "White label",
    "farm-to-table": "direct from farm",
    "farm-to-final": "from farm to final",
    "five-star": "five star",
    "food-grade": "food safe",
    "high-demand": "popular",
    "high-performance": "excellent",
    "high-quality": "premium quality",
    "high-turnover": "fast moving",
    "high-volume": "large volume",
    "industrial-grade": "commercial",
    "ingredient-grade": "premium ingredient",
    "institutional-grade": "commercial",
    "large-scale": "large scale",
    "on-time": "timely",
    "retail-ready": "ready for retail",
    "security-cleared": "security approved",
    "third-party": "independent",
    "wood-churned": "traditionally churned",
    "zero-compromise": "uncompromising",
    "zero-defect": "flawless"
}

html_files = glob.glob("*.html")

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
        
    for hyphenated, natural in replacements.items():
        content = content.replace(hyphenated, natural)
        
    with open(f, 'w') as file:
        file.write(content)
        
print("Hyphenated words replaced globally.")
