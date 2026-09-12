import json
import math
import os

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Load harvested results to know which spots were updated
harvested_ids = set()
for i in range(1, 9):
    path = f'data/harvest/result_{i}.json'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for item in json.load(f):
                harvested_ids.add(item['id'])

to_translate = []
for city, spots in master_data.items():
    for spot in spots:
        if spot.get('id') in harvested_ids:
            to_translate.append(spot)

print(f"Total spots to translate to EU languages: {len(to_translate)}")

chunk_size = math.ceil(len(to_translate) / 5) # 5 subagents
os.makedirs('data/harvest_eu', exist_ok=True)

for i in range(5):
    chunk = to_translate[i*chunk_size:(i+1)*chunk_size]
    if not chunk: continue
    # Only keep the EN fields needed for translation to keep prompt small
    small_chunk = []
    for s in chunk:
        small_chunk.append({
            'id': s['id'],
            'city': city,
            'name': s.get('name'),
            'desc_en': s.get('desc_en'),
            'insiderTip_en': s.get('insiderTip_en')
        })
    with open(f'data/harvest_eu/chunk_{i+1}.json', 'w', encoding='utf-8') as f:
        json.dump(small_chunk, f, ensure_ascii=False, indent=2)
    print(f"Chunk {i+1}: {len(chunk)} spots")
