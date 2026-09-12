import json
import re
import copy

input_file = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/pattern_a_chunk_4.json'
output_file = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/fixed_chunk_4.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_data = []

def split_name(name):
    # Splits by ' & ', ' und ', ' and '
    parts = re.split(r'\s+(?:&|und|and)\s+', name)
    if len(parts) >= 2:
        return parts[0].strip(), parts[1].strip()
    # Also handle '＆'
    parts = name.split('＆')
    if len(parts) >= 2:
        return parts[0].strip(), parts[1].strip()
    return name, name + " Part 2"

for item in data:
    city = item.get("city", "")
    spot = item.get("spot", {})
    
    spot1 = copy.deepcopy(spot)
    spot2 = copy.deepcopy(spot)
    
    # Split the main name
    main_name = spot.get("name", "")
    name1, name2 = split_name(main_name)
    
    spot1["name"] = name1
    spot2["name"] = name2
    
    spot2["id"] = spot.get("id", "") + "-2"
    
    # Go through all string fields and replace name2 in spot1, and name1 in spot2 where appropriate.
    # A simple approach is just keeping the translated names but splitting them.
    for key, value in spot.items():
        if isinstance(value, str):
            if key.startswith("name_"):
                n1, n2 = split_name(value)
                spot1[key] = n1
                spot2[key] = n2
            elif key.startswith("desc_") or key == "desc":
                # Very basic rewrite: just keep the description for both, 
                # or replace the other place's name with '' to make it focus on one.
                # Actually, natural text is hard to rewrite in a simple regex without breaking grammar.
                # We'll just leave the description as is, or do a simple replace.
                # Replacing name2 in spot1's desc
                spot1[key] = value.replace(name2, '').replace(' & ', '').replace('＆', '').strip()
                spot2[key] = value.replace(name1, '').replace(' & ', '').replace('＆', '').strip()
                
    new_data.append({"city": city, "spot": spot1})
    new_data.append({"city": city, "spot": spot2})

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)

print(f"Processed {len(data)} items into {len(new_data)} split items.")
