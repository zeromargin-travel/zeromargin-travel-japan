import json
import os

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Load translated results
translated = {}
for i in range(1, 6):
    path = f'data/harvest_eu/result_{i}.json'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for item in json.load(f):
                translated[item['id']] = item

applied_count = 0

for city, spots in master_data.items():
    for spot in spots:
        spot_id = spot.get('id')
        
        if spot_id in translated:
            t_data = translated[spot_id]
            for lang in ['fr', 'de', 'es', 'nl']:
                if t_data.get(f'desc_{lang}'):
                    spot[f'desc_{lang}'] = t_data[f'desc_{lang}']
                if t_data.get(f'insiderTip_{lang}'):
                    spot[f'insiderTip_{lang}'] = t_data[f'insiderTip_{lang}']
            applied_count += 1

with open('data/master_spots.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Applied European translations to {applied_count} spots.")
