import json
import re

classification_file = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/curation_report.md'
master_file = 'data/master_spots.json'

reject_tuples = []
with open(classification_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = re.search(r'\*\s*\*\*\[REJECT\]\*\*\s*-\s*(.+?):\s*(.+)', line)
        if match:
            city_str = match.group(1).strip().split(',')[0].strip().lower()
            name_str = match.group(2).strip().lower()
            reject_tuples.append((city_str, name_str))

with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

removed_count = 0
for full_city, spots in master_data.items():
    city_short = full_city.split(',')[0].strip().lower()
    new_spots = []
    for spot in spots:
        spot_name = spot.get('name', '').lower()
        
        is_reject = False
        for (r_city, r_name) in reject_tuples:
            if r_city in city_short and r_name == spot_name:
                is_reject = True
                break
                
        if is_reject:
            removed_count += 1
        else:
            new_spots.append(spot)
            
    master_data[full_city] = new_spots

with open(master_file, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Successfully removed {removed_count} REJECT spots from master_spots.json.")
