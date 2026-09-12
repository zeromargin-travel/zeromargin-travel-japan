import json
import os

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Load translated results
results = {}
for i in [1, 2]:
    path = f'data/target_c/result_{i}.json'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for item in json.load(f):
                results[item['id']] = item

applied_count = 0
fields = ['desc', 'insiderTip', 'whyThisSpot']
langs = ['en', 'fr', 'de', 'es', 'nl']

for city, spots in master_data.items():
    for spot in spots:
        spot_id = spot.get('id')
        
        if spot_id in results:
            r_data = results[spot_id]
            for field in fields:
                for lang in langs:
                    key = f"{field}_{lang}"
                    if r_data.get(key):
                        spot[key] = r_data[key]
            applied_count += 1

with open('data/master_spots.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Applied Target C rewrites to {applied_count} spots.")
