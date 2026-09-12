import json
import os

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']
fields = ['desc', 'insiderTip', 'whyThisSpot']

error_spots = []

for i in range(1, 11):
    file_path = f'data/target_b_written_{i}.json'
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for spot_obj in data:
        spot = spot_obj['spot']
        has_error = False
        
        for field in fields:
            for lang in langs:
                key = f"{field}_{lang}"
                val = spot.get(key, "")
                if not val or len(val) < 20:
                    has_error = True
                if lang in ['ja', 'zh'] and val == spot.get(f"{field}_en", "") and val != "":
                    has_error = True
                    
        if has_error:
            error_spots.append(spot_obj)

with open('data/target_b_errors.json', 'w', encoding='utf-8') as f:
    json.dump(error_spots, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(error_spots)} spots with errors.")
