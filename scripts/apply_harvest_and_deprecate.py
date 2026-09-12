import json
import os

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Load harvested results
harvested = {}
for i in range(1, 9):
    path = f'data/harvest/result_{i}.json'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for item in json.load(f):
                harvested[item['id']] = item

applied_count = 0
deleted_ja_zh_count = 0

for city, spots in master_data.items():
    for spot in spots:
        spot_id = spot.get('id')
        
        # 1. Apply harvested English
        if spot_id in harvested:
            h_data = harvested[spot_id]
            if h_data.get('new_en_desc'):
                spot['desc_en'] = h_data['new_en_desc']
            if h_data.get('new_en_tip'):
                spot['insiderTip_en'] = h_data['new_en_tip']
            applied_count += 1
            
        # 2. Deprecate Asian languages (delete _ja and _zh keys)
        keys_to_delete = [k for k in spot.keys() if k.endswith('_ja') or k.endswith('_zh')]
        for k in keys_to_delete:
            del spot[k]
            deleted_ja_zh_count += 1

with open('data/master_spots.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Applied enriched English to {applied_count} spots.")
print(f"Deleted {deleted_ja_zh_count} JA/ZH fields to deprecate Asian languages.")
