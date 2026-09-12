#!/usr/bin/env python3
"""
Zero-Margin Travel App - Spot ID Sanitizer & Top7/HiddenGems Tag Generator
1. Fixes spot ID collisions across all 25 cities by assigning globally unique IDs (city_slug + original_id).
2. Assigns top7 (7 spots) and hiddenGem (3-5 spots) tags for every city.
3. Updates data/cities/*.json, data/all_spots_database.json, and js/ai-travel-engine.js.
"""

import os
import glob
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CITIES_DIR = os.path.join(BASE_DIR, '..', 'data', 'cities')
ALL_SPOTS_JSON = os.path.join(BASE_DIR, '..', 'data', 'all_spots_database.json')
JS_ENGINE_FILE = os.path.join(BASE_DIR, '..', 'js', 'ai-travel-engine.js')

CITY_SLUGS = {
    'amsterdam.json': 'ams',
    'antwerp.json': 'ant',
    'berlin.json': 'ber',
    'bordeaux.json': 'bod',
    'bruges.json': 'bru',
    'brussels.json': 'bru_c',
    'cologne.json': 'cgn',
    'dresden.json': 'drs',
    'frankfurt.json': 'fra',
    'ghent.json': 'gnt',
    'hamburg.json': 'ham',
    'heidelberg.json': 'hdb',
    'luxembourg.json': 'lux',
    'lyon.json': 'lyn',
    'marseille.json': 'mrs',
    'munich.json': 'muc',
    'nice.json': 'nce',
    'nuremberg.json': 'nue',
    'paris.json': 'par',
    'rotterdam.json': 'rtm',
    'strasbourg.json': 'sxb',
    'the_hague.json': 'hga',
    'toulouse.json': 'tls',
    'utrecht.json': 'utr',
    'maastricht.json': 'mst'
}

CITY_NAME_MAP = {
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

def is_food_or_cafe(spot):
    cat = spot.get('category', '')
    desc = (spot.get('name_en', '') + ' ' + spot.get('name_ja', '') + ' ' + spot.get('desc_en', '') + ' ' + spot.get('desc_ja', '')).lower()
    if any(k in cat for k in ['Café', 'Bistro', 'Dining', 'Restaurant', 'Bakery']):
        return True
    if any(k in desc for k in ['カフェ', 'ビストロ', '老舗食堂', 'ベーカリー', 'ビアホール', '醸造所', 'パブ', 'bistro', 'brasserie', 'bakery', 'cafe', 'café', 'restaurant']):
        return True
    return False

def is_cafe(spot):
    cat = spot.get('category', '')
    desc = (spot.get('name_en', '') + ' ' + spot.get('name_ja', '') + ' ' + spot.get('desc_en', '') + ' ' + spot.get('desc_ja', '')).lower()
    if 'bakery' in cat.lower() or 'ベーカリー' in desc or 'apple pie' in desc or 'ショコラ' in desc or 'パティスリー' in desc or 'patisserie' in desc:
        return True
    if 'café' in cat.lower() or 'カフェ' in desc or '喫茶' in desc or 'cafe' in desc:
        return True
    return False

def process_city_spots(fname, spots):
    slug = CITY_SLUGS.get(fname, fname.replace('.json', '')[:3])
    
    # 1. Unique IDs
    for idx, s in enumerate(spots):
        raw_id = s.get('id', f'sp_{idx+1}')
        if not raw_id.startswith(f"{slug}_"):
            s['id'] = f"{slug}_{raw_id}"
        else:
            s['id'] = raw_id

    # 2. Tag Selection
    food_spots = [s for s in spots if is_food_or_cafe(s)]
    cafes = [s for s in food_spots if is_cafe(s)]
    restaurants = [s for s in food_spots if not is_cafe(s)]

    if not cafes:
        cafes = food_spots[:1]
    if not restaurants:
        restaurants = food_spots[1:2] if len(food_spots) > 1 else food_spots[:1]

    sights = [s for s in spots if s not in food_spots]

    top7_sights = sights[:5]
    top7_cafe = cafes[:1]
    top7_rest = restaurants[:1] if restaurants[0:1] != top7_cafe else restaurants[1:2]

    top7_set = set()
    for s in top7_sights + top7_cafe + top7_rest:
        if s:
            top7_set.add(s['id'])

    if len(top7_set) < 7:
        for s in spots:
            if s['id'] not in top7_set:
                top7_set.add(s['id'])
                if len(top7_set) == 7:
                    break

    remaining_sights = [s for s in sights if s['id'] not in top7_set]
    remaining_cafes = [s for s in cafes if s['id'] not in top7_set]
    remaining_rests = [s for s in restaurants if s['id'] not in top7_set]

    hidden_sights = remaining_sights[len(remaining_sights)//4 : len(remaining_sights)//4 + 3]
    if len(hidden_sights) < 3:
        hidden_sights = remaining_sights[:3]

    hidden_cafe = remaining_cafes[:1] if remaining_cafes else remaining_sights[3:4]
    hidden_rest = remaining_rests[:1] if remaining_rests else remaining_sights[4:5]

    hidden_set = set()
    for s in hidden_sights + hidden_cafe + hidden_rest:
        if s and s['id'] not in top7_set:
            hidden_set.add(s['id'])

    if len(hidden_set) < 3:
        for s in spots:
            if s['id'] not in top7_set and s['id'] not in hidden_set:
                hidden_set.add(s['id'])
                if len(hidden_set) >= 3:
                    break

    for s in spots:
        sp_id = s['id']
        s['top7'] = (sp_id in top7_set)
        s['hiddenGem'] = (sp_id in hidden_set)

    return spots

def main():
    city_files = sorted(glob.glob(os.path.join(CITIES_DIR, '*.json')))
    all_spots_dict = {}
    total_spots = 0
    total_top7 = 0
    total_hidden = 0

    all_ids_check = set()
    duplicate_count = 0

    for fpath in city_files:
        fname = os.path.basename(fpath)
        cname = CITY_NAME_MAP.get(fname, fname.replace('.json', '').title())

        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            spots = data.get('spots', [])
        else:
            spots = data

        processed_spots = process_city_spots(fname, spots)

        for s in processed_spots:
            sid = s['id']
            if sid in all_ids_check:
                duplicate_count += 1
                print(f"WARNING: Duplicate ID found: {sid}")
            all_ids_check.add(sid)

        c_top7 = sum(1 for s in processed_spots if s.get('top7'))
        c_hid = sum(1 for s in processed_spots if s.get('hiddenGem'))

        total_spots += len(processed_spots)
        total_top7 += c_top7
        total_hidden += c_hid

        if isinstance(data, dict):
            data['spots'] = processed_spots
        else:
            data = processed_spots

        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        all_spots_dict[cname] = processed_spots
        print(f"  ✓ Processed {cname}: {len(processed_spots)} spots (Top7={c_top7}, HiddenGems={c_hid})")

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
    print(f"🎉 Complete! Total Spots: {total_spots}, Total Top7: {total_top7}, Total HiddenGems: {total_hidden}")
    print(f"   Duplicate IDs: {duplicate_count}")

if __name__ == '__main__':
    main()
