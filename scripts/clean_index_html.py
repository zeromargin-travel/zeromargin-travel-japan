import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<div id="candidateSpotsGrid".*?<!-- Optional Custom Return Hotel Field -->'
replacement = '<div id="candidateSpotsGrid" class="grid-3" style="display:grid !important; visibility:visible !important;"></div>\n          </div>\n\n          <!-- Optional Custom Return Hotel Field -->'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully cleaned static HTML cards in index.html!")
