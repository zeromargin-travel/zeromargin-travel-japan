import json
import re
import subprocess

# Load original data
result = subprocess.run(['git', 'show', 'd6c8bc5:data/master_spots.json'], capture_output=True, cwd='/Users/jnabi1/Desktop/zeromargin-travel.github.io')
orig_by_id = {}
for city, spots in json.loads(result.stdout).items():
    for spot in spots:
        orig_by_id[spot['id']] = spot

# Load current data
with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

langs = ['ja', 'zh', 'fr', 'de', 'es', 'nl'] # Focus on non-EN
fields = ['desc', 'insiderTip', 'whyThisSpot']

lang_tag_pattern = re.compile(r'^\s*\[(EN|JA|ZH|FR|DE|ES|NL)\]', re.IGNORECASE)

def is_mostly_ascii(text):
    if not text: return False
    non_space = text.replace(' ', '')
    if not non_space: return False
    return sum(1 for c in non_space if ord(c) < 128) / len(non_space) > 0.85

def has_cjk(text):
    return any('\u3000' <= c <= '\u9fff' or '\uac00' <= c <= '\ud7a3' for c in text)

cleaned_count = 0

for city, spots in master_data.items():
    for spot in spots:
        orig_spot = orig_by_id.get(spot.get('id'), {})
        
        for lang in langs:
            for field in fields:
                curr_key = f"{field}_{lang}"
                orig_key = curr_key
                if field == 'insiderTip':
                    orig_key = f"tip_{lang}"
                    
                val = spot.get(curr_key, '')
                if not val:
                    continue
                
                is_bad = False
                
                # Check 1: Tag
                if lang_tag_pattern.match(val):
                    is_bad = True
                
                # Check 2: English in JA/ZH
                if lang in ['ja', 'zh'] and is_mostly_ascii(val) and not has_cjk(val):
                    is_bad = True
                    
                # Check 3: HTTP 500
                if 'HTTP Error' in val or '500 Internal' in val:
                    is_bad = True
                
                if is_bad:
                    # Revert to original if it exists and is not empty
                    orig_val = orig_spot.get(orig_key, '')
                    if orig_val:
                        spot[curr_key] = orig_val
                        cleaned_count += 1
                    else:
                        # For whyThisSpot or empty orig, just remove the key
                        del spot[curr_key]
                        cleaned_count += 1

with open('data/master_spots.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Cleaned/Reverted {cleaned_count} bad language fields.")
