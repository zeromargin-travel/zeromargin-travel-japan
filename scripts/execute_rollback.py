import json
import subprocess
import os

# Load verdicts
with open('/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/scratch/all_verdicts.json') as f:
    verdicts = json.load(f)

# Load original data from git
result = subprocess.run(['git', 'show', 'd6c8bc5:data/master_spots.json'], capture_output=True, cwd='/Users/jnabi1/Desktop/zeromargin-travel.github.io')
orig_data_raw = json.loads(result.stdout)
orig_by_id = {}
for city, spots in orig_data_raw.items():
    for spot in spots:
        orig_by_id[spot['id']] = spot

# Load current data
with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']
fields = ['desc', 'insiderTip', 'whyThisSpot']

# Important: The original data had 'tip_xx', the current has 'insiderTip_xx'
# We must map 'tip_xx' from orig -> 'insiderTip_xx' in current when restoring

reverted_full = 0
reverted_mixed = 0
mixed_fields_reverted = 0

for city, spots in master_data.items():
    for spot in spots:
        spot_id = spot.get('id')
        
        # Find verdict for this spot
        v_item = next((v for v in verdicts if v['id'] == spot_id), None)
        if not v_item:
            continue
            
        orig_spot = orig_by_id.get(spot_id)
        if not orig_spot:
            continue
            
        verdict = v_item['verdict']
        
        if verdict in ['REVERT_ORIG', 'BOTH_BAD']:
            # Full revert of all text fields
            for f in fields:
                for lang in langs:
                    curr_key = f"{f}_{lang}"
                    
                    # Determine original key name
                    orig_key = curr_key
                    if f == 'insiderTip':
                        orig_key = f"tip_{lang}"
                        
                    # Copy from orig to curr (delete from curr if not in orig)
                    if orig_key in orig_spot:
                        spot[curr_key] = orig_spot[orig_key]
                    elif curr_key in spot:
                        del spot[curr_key]
            reverted_full += 1
            
        elif verdict == 'MIXED':
            # Revert only specific fields
            fields_to_revert = v_item.get('revert_fields', [])
            if fields_to_revert:
                for f_lang in fields_to_revert:
                    # e.g., 'desc_ja', 'tip_en'
                    f, lang = f_lang.split('_', 1)
                    
                    curr_key = f"{f}_{lang}"
                    if f == 'tip':
                        curr_key = f"insiderTip_{lang}"
                    
                    orig_key = f_lang
                    
                    if orig_key in orig_spot:
                        spot[curr_key] = orig_spot[orig_key]
                    elif curr_key in spot:
                        del spot[curr_key]
                        
                    mixed_fields_reverted += 1
                reverted_mixed += 1

# Save the reverted master_spots
with open('data/master_spots.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Full reversions (REVERT_ORIG/BOTH_BAD): {reverted_full} spots")
print(f"Partial reversions (MIXED): {reverted_mixed} spots ({mixed_fields_reverted} specific fields restored)")
