import json

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']
fields = ['desc', 'insiderTip', 'whyThisSpot']

total_spots = 0
short_desc_count = 0
combo_mention_count = 0
exact_duplicate_descs = 0

all_descs_en = set()

for city, spots in master_data.items():
    for spot in spots:
        total_spots += 1
        
        # Check English desc for brevity
        desc_en = spot.get('desc_en', '')
        if len(desc_en) < 40:
            short_desc_count += 1
            
        # Check for '&' or 'and' in desc_en which might indicate un-split text from the AI fail
        if '&' in desc_en or ' and ' in desc_en:
            combo_mention_count += 1
            
        if desc_en in all_descs_en:
            exact_duplicate_descs += 1
        else:
            all_descs_en.add(desc_en)

print(f"Total Spots: {total_spots}")
print(f"Spots with very short English desc (<40 chars): {short_desc_count}")
print(f"Spots with exact duplicate English desc: {exact_duplicate_descs}")
print(f"Spots mentioning '&' or 'and' in English desc: {combo_mention_count}")

# Print some examples of short descriptions
print("\nExamples of short descriptions:")
printed = 0
for city, spots in master_data.items():
    for spot in spots:
        desc = spot.get('desc_en', '')
        if len(desc) < 40:
            print(f"- {spot.get('name')}: {desc}")
            printed += 1
            if printed >= 5:
                break
    if printed >= 5:
        break
        
# Check the newly added Curry 36 to see what happened
print("\nChecking Curry 36:")
for city, spots in master_data.items():
    for spot in spots:
        if 'Curry 36' in spot.get('name', ''):
            print(f"Name: {spot.get('name')}")
            print(f"desc_en: {spot.get('desc_en')}")
            print(f"desc_ja: {spot.get('desc_ja')}")
