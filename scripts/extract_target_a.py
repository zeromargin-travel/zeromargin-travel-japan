import json
import re

classification_file = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/curation_report.md'
master_file = 'data/master_spots.json'

keep_tuples = []
with open(classification_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = re.search(r'\*\s*\*\*\[KEEP\]\*\*\s*-\s*(.+?):\s*(.+)', line)
        if match:
            city_str = match.group(1).strip().split(',')[0].strip().lower()
            name_str = match.group(2).strip().lower()
            keep_tuples.append((city_str, name_str))

with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

target_a_spots = []

for full_city, spots in master_data.items():
    city_short = full_city.split(',')[0].strip().lower()
    for spot in spots:
        spot_name = spot.get('name', '').lower()
        
        # Check if it's one of the 110 KEEP spots
        is_keep = False
        for (r_city, r_name) in keep_tuples:
            if r_city in city_short and r_name == spot_name:
                is_keep = True
                break
                
        if is_keep:
            target_a_spots.append({'city': full_city, 'spot': spot})
            continue
            
        # Check if it's terrible everywhere (max length < 40)
        langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']
        lengths = {lang: len(spot.get(f'desc_{lang}', '')) for lang in langs}
        if max(lengths.values()) < 40:
            target_a_spots.append({'city': full_city, 'spot': spot})

print(f"Total Target A spots found: {len(target_a_spots)}")

# Split into 5 chunks
import math
chunk_size = math.ceil(len(target_a_spots) / 5)

for i in range(5):
    chunk = target_a_spots[i*chunk_size : (i+1)*chunk_size]
    with open(f'data/target_a_chunk_{i+1}.json', 'w', encoding='utf-8') as f:
        json.dump(chunk, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(chunk)} spots to data/target_a_chunk_{i+1}.json")
