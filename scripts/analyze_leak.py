import json
import re

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']

leaked_spots = []
in_district_pattern = re.compile(r'^.+? in .*? district\.$', re.IGNORECASE)

for city, spots in master_data.items():
    for spot in spots:
        lengths = {lang: len(spot.get(f'desc_{lang}', '')) for lang in langs}
        max_len = max(lengths.values())
        desc_en = spot.get('desc_en', '')
        
        is_leaked = False
        reason = ""
        
        # Check if it was completely missed by previous logic (max_len between 40 and 80)
        if 40 <= max_len <= 80:
            is_leaked = True
            reason = f"Max length is {max_len} (between 40 and 80)"
            
        # Check if desc_en is just a generic "X in Y district"
        if in_district_pattern.match(desc_en):
            is_leaked = True
            reason = f"Generic template description: {desc_en}"
            
        if is_leaked:
            leaked_spots.append({
                'city': city,
                'name': spot.get('name'),
                'desc_en': desc_en,
                'max_len': max_len,
                'reason': reason
            })

print(f"Total spots caught by new leak detection: {len(leaked_spots)}")
print("\nSample of leaked spots:")
for i, s in enumerate(leaked_spots[:20]):
    print(f"- {s['name']} ({s['city']})")
    print(f"  Reason: {s['reason']}")
    print(f"  desc_en: {s['desc_en']}")
