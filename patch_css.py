import re

css_file = 'css/style.css'

with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# We want to replace everything from .ghee-bottle { ... up to but not including .ghee-content {
start_str = '.ghee-bottle {'
end_str = '.ghee-content {'

start_idx = css.find(start_str)
end_idx = css.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_css_block = """.ghee-bottle {
  width: 50px;
  height: 70px;
  position: relative;
  transition: transform 0.4s ease;
}

.ghee-bottle.active {
  transform: scale(0.95);
}

.bottle-cap {
  width: 30px;
  height: 15px;
  background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
  border-radius: 5px 5px 0 0;
  margin: 0 auto;
  position: relative;
  transition: transform 0.4s ease;
}

.ghee-bottle.active .bottle-cap {
  transform: translateY(-2px);
}

.bottle-body {
  width: 40px;
  height: 50px;
  background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%);
  border-radius: 5px 5px 10px 10px;
  margin: 0 auto;
  position: relative;
  box-shadow: inset -5px -5px 10px rgba(0,0,0,0.2), 0 5px 15px rgba(0,0,0,0.3);
  overflow: hidden;
}

.bottle-body::before {
  content: '';
  position: absolute;
  top: 5px;
  left: 5px;
  width: 10px;
  height: 20px;
  background: rgba(255,255,255,0.4);
  border-radius: 50%;
  filter: blur(2px);
}

.bottle-label {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 0.6rem;
  font-weight: bold;
  color: var(--deep-burgundy);
  background: var(--cream-ivory);
  padding: 2px 4px;
  border-radius: 3px;
  white-space: nowrap;
}

.assistant-popup {
  position: absolute;
  top: 80px;
  right: 0;
  background: var(--white);
  border-radius: 12px;
  padding: 1rem;
  box-shadow: 0 10px 40px rgba(0,0,0,0.2);
  min-width: 200px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: all 0.3s ease;
  border: 2px solid var(--royal-gold);
}

.assistant-popup.active {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

/* Ghee Spoon Presentation */
.ghee-pour {
  position: absolute;
  top: 50%;
  left: -120px;
  transform: translateY(-50%) translateX(20px);
  width: 110px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.4s ease, transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), visibility 0.4s;
  z-index: 1002;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.ghee-pour.active {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(0);
}

.ghee-spoon {
  width: 100px;
  height: auto;
  filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2));
  transform: rotate(-10deg);
  margin-bottom: 5px;
}

"""
    new_content = css[:start_idx] + new_css_block + css[end_idx:]
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("style.css successfully patched.")
else:
    print("Could not find start or end markers in style.css.")
