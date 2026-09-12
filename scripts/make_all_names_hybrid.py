import json
import glob
import re

# Map city to local language
CITY_LOCAL_LANG = {
    'paris.json': 'fr',
    'bordeaux.json': 'fr',
    'lyon.json': 'fr',
    'marseille.json': 'fr',
    'nice.json': 'fr',
    'strasbourg.json': 'fr',
    'toulouse.json': 'fr',
    'berlin.json': 'de',
    'cologne.json': 'de',
    'munich.json': 'de',
    'amsterdam.json': 'nl',
    'brussels.json': 'fr',
    'luxembourg.json': 'fr'
}

def clean_base_name(text):
    if not text:
        return ""
    # Strip parentheses and contents if it contains ( or （
    # e.g. "Place des Terreaux & Bartholdi Fountain" -> "Place des Terreaux & Bartholdi Fountain"
    # "Brandenburger Tor（ブランデンブルク門）" -> "Brandenburger Tor"
    cleaned = re.sub(r'[\（\(].*?[\）\)]', '', text).strip()
    return cleaned if cleaned else text.strip()

def extract_translation(val):
    if not val:
        return ""
    # If val has parentheses, extract what's inside parentheses
    m = re.search(r'[\（\(](.*?)[\）\)]', val)
    if m:
        return m.group(1).strip()
    return val.strip()

city_files = sorted(glob.glob('data/cities/*.json'))
total_updated_spots = 0

for filepath in city_files:
    fname = filepath.split('/')[-1]
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list):
        spots = data
    else:
        spots = data.get('spots', [])
    updated_in_file = 0

    for s in spots:
        raw_name = s.get('name', '')
        raw_name_en = s.get('name_en', '')
        
        # Primary base local name
        local_base = clean_base_name(raw_name)
        if not local_base and raw_name_en:
            local_base = clean_base_name(raw_name_en)

        # Languages
        langs = ['en', 'ja', 'es', 'zh', 'fr', 'de']
        for lang in langs:
            key = f'name_{lang}'
            raw_val = s.get(key, '')
            trans_str = extract_translation(raw_val)
            if not trans_str:
                trans_str = extract_translation(raw_name)

            # If translation is same as local_base, keep clean local_base
            if not trans_str or trans_str.lower() == local_base.lower():
                s[key] = local_base
            else:
                # Format hybrid
                if lang == 'ja':
                    s[key] = f"{local_base}（{trans_str}）"
                else:
                    s[key] = f"{local_base} ({trans_str})"
        
        # Also ensure primary 'name' is name_ja
        s['name'] = s['name_ja']
        updated_in_file += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total_updated_spots += updated_in_file
    print(f"  - Refined {fname}: {updated_in_file} spots updated with universal 6-language hybrid names")

print(f"🎉 Successfully updated all {total_updated_spots} spots across {len(city_files)} cities!")
