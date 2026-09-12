import json
import re

classification_file = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/curation_report.md'
master_file = 'data/master_spots.json'

rejects = set()
with open(classification_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = re.search(r'\*\s*\*\*\[REJECT\]\*\*\s*-\s*(.+?):\s*(.+)', line)
        if match:
            city = match.group(1).strip()
            name = match.group(2).strip()
            rejects.add(f"{city}|{name}")

with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

removed_count = 0
for city, spots in master_data.items():
    new_spots = []
    for spot in spots:
        key = f"{city}|{spot.get('name', '')}"
        if key not in rejects:
            new_spots.append(spot)
        else:
            removed_count += 1
    master_data[city] = new_spots

with open(master_file, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Successfully removed {removed_count} REJECT spots from master_spots.json.")
