import json
import re
import os

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

district_pattern = re.compile(r'^.{5,50} in (city|.{2,20}) district\.$', re.IGNORECASE)

target_c_spots = []

for city, spots in master_data.items():
    for spot in spots:
        if district_pattern.match(spot.get('desc_en', '')):
            # We need to give the subagent enough context (name, city) to write a new one
            target_c_spots.append({
                'id': spot.get('id'),
                'city': city,
                'name': spot.get('name')
            })

print(f"Extracted {len(target_c_spots)} template spots for Target C.")

os.makedirs('data/target_c', exist_ok=True)
chunk_1 = target_c_spots[:11]
chunk_2 = target_c_spots[11:]

with open('data/target_c/chunk_1.json', 'w', encoding='utf-8') as f:
    json.dump(chunk_1, f, ensure_ascii=False, indent=2)
with open('data/target_c/chunk_2.json', 'w', encoding='utf-8') as f:
    json.dump(chunk_2, f, ensure_ascii=False, indent=2)

print("Chunks created.")
