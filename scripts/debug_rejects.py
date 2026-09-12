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

existing_keys = set()
for city, spots in master_data.items():
    for spot in spots:
        existing_keys.add(f"{city}|{spot.get('name', '')}")

missing_rejects = []
for r in rejects:
    if r not in existing_keys:
        missing_rejects.append(r)

for m in missing_rejects:
    print(m)
print(f"Total missing: {len(missing_rejects)}")
