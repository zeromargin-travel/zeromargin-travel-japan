import json
import math

master_file = 'data/master_spots.json'

with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

target_b_spots = []
langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']

for city, spots in master_data.items():
    for spot in spots:
        lengths = {lang: len(spot.get(f'desc_{lang}', '')) for lang in langs}
        max_len = max(lengths.values())
        min_len = min(lengths.values())
        
        # Target B: Translation Solvable (Some good, some bad)
        if max_len > 80 and min_len < 40:
            target_b_spots.append({'city': city, 'spot': spot})

print(f"Total Target B spots found: {len(target_b_spots)}")

# Split into 10 chunks
chunk_size = math.ceil(len(target_b_spots) / 10)

for i in range(10):
    chunk = target_b_spots[i*chunk_size : (i+1)*chunk_size]
    with open(f'data/target_b_chunk_{i+1}.json', 'w', encoding='utf-8') as f:
        json.dump(chunk, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(chunk)} spots to data/target_b_chunk_{i+1}.json")
