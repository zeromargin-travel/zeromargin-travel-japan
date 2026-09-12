import json
import os

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']

for i in range(1, 11):
    file_path = f'data/target_b_written_{i}.json'
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for spot_obj in data:
        spot = spot_obj['spot']
        
        for lang in langs:
            # Fix insiderTip (might be 'tip_xx')
            if f'tip_{lang}' in spot and f'insiderTip_{lang}' not in spot:
                spot[f'insiderTip_{lang}'] = spot.pop(f'tip_{lang}')
            elif f'insiderTip_{lang}' not in spot:
                spot[f'insiderTip_{lang}'] = "" # Ensure key exists
                
            # Fix whyThisSpot (might be 'why_xx')
            if f'why_{lang}' in spot and f'whyThisSpot_{lang}' not in spot:
                spot[f'whyThisSpot_{lang}'] = spot.pop(f'why_{lang}')
            elif f'whyThisSpot_{lang}' not in spot:
                spot[f'whyThisSpot_{lang}'] = "" # Ensure key exists
                
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Fixed hallucinated keys in all chunks.")
