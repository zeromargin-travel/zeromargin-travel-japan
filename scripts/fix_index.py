with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find index of line with Check the boxes for spots
start_idx = -1
end_idx = -1

for i, l in enumerate(lines):
    if 'Check the boxes for spots you definitely want to visit.' in l:
        start_idx = i
    if '<!-- Optional Custom Return Hotel Field -->' in l:
        end_idx = i

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx+2]
    new_lines.append('            <div id="candidateSpotsGrid" class="grid-3" style="display:grid !important; visibility:visible !important;"></div>\n')
    new_lines.append('          </div>\n\n          ')
    new_lines.extend(lines[end_idx:])
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully updated index.html structure!")
else:
    print(f"Error: start={start_idx}, end={end_idx}")
