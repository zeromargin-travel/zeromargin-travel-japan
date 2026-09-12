#!/usr/bin/env python3
"""
Zero-Margin Travel App - Master Database Sanitizer & Rebuilder
1. Cleans all 25 city JSON files in data/cities/
2. Strips all Japanese Kana/Hiragana leakage from non-JA language fields (en, zh, fr, de, es, nl)
3. Standardizes spot.name = clean native local name (without Japanese in parens)
4. Updates data/all_spots_database.json and js/ai-travel-engine.js
"""

import os
import glob
import json
import re
import unicodedata

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CITIES_DIR = os.path.join(BASE_DIR, '..', 'data', 'cities')
ALL_SPOTS_JSON = os.path.join(BASE_DIR, '..', 'data', 'all_spots_database.json')
JS_ENGINE_FILE = os.path.join(BASE_DIR, '..', 'js', 'ai-travel-engine.js')

JAPANESE_KANA_REGEX = re.compile(r'[\u3040-\u30ff]') # Hiragana & Katakana
JAPANESE_FULL_REGEX = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]')

CITY_NATIVE_LANG = {
    'paris.json': 'fr', 'bordeaux.json': 'fr', 'lyon.json': 'fr', 'marseille.json': 'fr',
    'nice.json': 'fr', 'strasbourg.json': 'fr', 'toulouse.json': 'fr',
    'berlin.json': 'de', 'cologne.json': 'de', 'dresden.json': 'de', 'frankfurt.json': 'de',
    'hamburg.json': 'de', 'heidelberg.json': 'de', 'munich.json': 'de', 'nuremberg.json': 'de',
    'amsterdam.json': 'nl', 'rotterdam.json': 'nl', 'the_hague.json': 'nl', 'utrecht.json': 'nl', 'maastricht.json': 'nl',
    'brussels.json': 'fr', 'bruges.json': 'nl', 'antwerp.json': 'nl', 'ghent.json': 'nl', 'luxembourg.json': 'fr'
}

def normalize_str(s):
    if not s:
        return ''
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[\s\-_,\.\'\"]', '', s).lower()
    return s

def is_near_identical(str1, str2):
    n1 = normalize_str(str1)
    n2 = normalize_str(str2)
    if not n1 or not n2:
        return True
    if n1 == n2:
        return True
    if n1 in n2 and len(n2) - len(n1) <= 4:
        return True
    if n2 in n1 and len(n1) - len(n2) <= 4:
        return True
    return False

def extract_outside_parens(val):
    if not val:
        return ''
    cleaned = re.sub(r'[\（\(].*?[\）\)]', '', val).strip()
    cleaned = cleaned.replace('（', '').replace('）', '').replace('(', '').replace(')', '').strip()
    return cleaned if cleaned else val.strip()

def extract_inside_parens(val):
    if not val:
        return ''
    m = re.search(r'[\（\(](.*?)[\）\)]', val)
    return m.group(1).strip() if m else ''

def clean_japanese_out(val):
    """Remove any parenthetical substring that contains Japanese Katakana/Hiragana."""
    if not val:
        return ''
    if not JAPANESE_KANA_REGEX.search(val):
        return val
    
    def sub_func(m):
        content = m.group(0)
        if JAPANESE_KANA_REGEX.search(content):
            return ''
        return content

    cleaned = re.sub(r'[\（\(].*?[\）\)]', sub_func, val).strip()
    if JAPANESE_KANA_REGEX.search(cleaned):
        cleaned = extract_outside_parens(cleaned)
        if JAPANESE_KANA_REGEX.search(cleaned):
            cleaned = re.sub(r'[\u3040-\u30ff]', '', cleaned).strip()
    return cleaned

def get_clean_local_name(spot, native_lang):
    raw_name = spot.get('name', '')
    outside_name = extract_outside_parens(raw_name)
    outside_name = clean_japanese_out(outside_name)

    native_key = f'name_{native_lang}'
    native_val = spot.get(native_key, '')
    if native_val:
        native_outside = extract_outside_parens(native_val)
        native_outside = clean_japanese_out(native_outside)
        if native_outside and not JAPANESE_KANA_REGEX.search(native_outside):
            if native_lang in ['fr', 'de', 'nl'] and re.search(r'[a-zA-ZÀ-ÿ]', native_outside):
                outside_name = native_outside

    name_en = spot.get('name_en', '')
    if name_en:
        en_outside = extract_outside_parens(name_en)
        en_outside = clean_japanese_out(en_outside)
        if en_outside and not outside_name:
            outside_name = en_outside

    return outside_name if outside_name else raw_name

def process_all_spots():
    city_files = sorted(glob.glob(os.path.join(CITIES_DIR, '*.json')))
    all_spots_dict = {}
    total_spots = 0

    city_name_map = {
        "amsterdam.json": "Amsterdam, Netherlands",
        "antwerp.json": "Antwerp, Belgium",
        "berlin.json": "Berlin, Germany",
        "bordeaux.json": "Bordeaux, France",
        "bruges.json": "Bruges, Belgium",
        "brussels.json": "Brussels, Belgium",
        "cologne.json": "Cologne, Germany",
        "dresden.json": "Dresden, Germany",
        "frankfurt.json": "Frankfurt, Germany",
        "ghent.json": "Ghent, Belgium",
        "hamburg.json": "Hamburg, Germany",
        "heidelberg.json": "Heidelberg, Germany",
        "luxembourg.json": "Luxembourg City, Luxembourg",
        "lyon.json": "Lyon, France",
        "marseille.json": "Marseille, France",
        "munich.json": "Munich, Germany",
        "nice.json": "Nice, France",
        "nuremberg.json": "Nuremberg, Germany",
        "paris.json": "Paris, France",
        "rotterdam.json": "Rotterdam, Netherlands",
        "strasbourg.json": "Strasbourg, France",
        "the_hague.json": "The Hague, Netherlands",
        "toulouse.json": "Toulouse, France",
        "utrecht.json": "Utrecht, Netherlands",
        "maastricht.json": "Maastricht, Netherlands"
    }

    for fpath in city_files:
        fname = os.path.basename(fpath)
        cname = city_name_map.get(fname, fname.replace('.json', '').title())
        native_lang = CITY_NATIVE_LANG.get(fname, 'en')

        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            spots = data.get('spots', [])
        else:
            spots = data

        cleaned_spots = []
        for s in spots:
            total_spots += 1
            local_clean = get_clean_local_name(s, native_lang)
            s['name_local'] = local_clean
            s['name'] = local_clean  # Primary name is clean native local name!

            # Process name_ja
            raw_ja = s.get('name_ja', '')
            ja_trans = extract_inside_parens(raw_ja) or extract_outside_parens(raw_ja)
            if not JAPANESE_FULL_REGEX.search(ja_trans):
                ja_trans = extract_inside_parens(s.get('name', ''))
            if ja_trans and not is_near_identical(local_clean, ja_trans) and JAPANESE_FULL_REGEX.search(ja_trans):
                s['name_ja'] = f"{local_clean}（{ja_trans}）"
            else:
                s['name_ja'] = raw_ja if JAPANESE_FULL_REGEX.search(raw_ja) else local_clean

            # Process non-JA languages (en, zh, fr, de, es, nl)
            for lang in ['en', 'zh', 'fr', 'de', 'es', 'nl']:
                key = f'name_{lang}'
                raw_val = s.get(key, '')
                raw_val = clean_japanese_out(raw_val)

                inside = extract_inside_parens(raw_val)
                outside = extract_outside_parens(raw_val)

                trans = inside if inside else (outside if not is_near_identical(local_clean, outside) else '')
                trans = clean_japanese_out(trans)

                if trans and not is_near_identical(local_clean, trans):
                    s[key] = f"{local_clean} ({trans})"
                else:
                    s[key] = local_clean

            # Sanitize desc_zh and tip_zh Japanese Kana leakage
            for fkey in ['desc_zh', 'tip_zh']:
                val = s.get(fkey, '')
                if JAPANESE_KANA_REGEX.search(val):
                    s[fkey] = s.get(fkey.replace('_zh', '_en'), '')

            cleaned_spots.append(s)

        if isinstance(data, dict):
            data['spots'] = cleaned_spots
        else:
            data = cleaned_spots

        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        all_spots_dict[cname] = cleaned_spots
        print(f"  ✓ Cleaned {cname}: {len(cleaned_spots)} spots")

    # Update data/all_spots_database.json
    with open(ALL_SPOTS_JSON, 'w', encoding='utf-8') as f:
        json.dump(all_spots_dict, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Updated {ALL_SPOTS_JSON}")

    # Rebuild js/ai-travel-engine.js
    with open(JS_ENGINE_FILE, 'r', encoding='utf-8') as f:
        js_code = f.read()

    db_marker = 'const candidateSpotsDatabase = '
    func_marker = '\nfunction getCategoryIcon(cat)'

    start_idx = js_code.find(db_marker)
    func_idx = js_code.find(func_marker)

    if start_idx != -1 and func_idx != -1:
        new_db_json = json.dumps(all_spots_dict, indent=2, ensure_ascii=False)
        js_code = js_code[:start_idx + len(db_marker)] + new_db_json + ';\n\n' + js_code[func_idx:]

    with open(JS_ENGINE_FILE, 'w', encoding='utf-8') as f:
        f.write(js_code)

    print(f"✓ Rebuilt {JS_ENGINE_FILE} with sanitized database!")
    print(f"🎉 Master Database Cleanup Complete across {total_spots} spots!")

if __name__ == '__main__':
    process_all_spots()
