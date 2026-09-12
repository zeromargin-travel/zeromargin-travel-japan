#!/usr/bin/env python3
"""
Zero-Margin Travel App - Universal Hybrid Name Unification (Pattern A: Local Sign First)
1. Format: Local Native Name (Translation in Target Language)
2. Elimination: Omit parens entirely if translation is identical or near-identical to local native name.
3. Clean local native name base determined by city country.
"""

import glob
import json
import re
import unicodedata
import os

# City to native language map
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
    # NFKD normalize to strip accents
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    # Remove punctuation, spaces, quotes
    s = re.sub(r'[\s\-_,\.\'\"]', '', s).lower()
    return s

def is_near_identical(str1, str2):
    n1 = normalize_str(str1)
    n2 = normalize_str(str2)
    if not n1 or not n2:
        return True
    if n1 == n2:
        return True
    # If one is sub-string of the other with minor diff (<=4 chars)
    if n1 in n2 and len(n2) - len(n1) <= 4:
        return True
    if n2 in n1 and len(n1) - len(n2) <= 4:
        return True
    return False

def clean_name(val):
    if not val:
        return ''
    cleaned = re.sub(r'[\（\(].*?[\）\)]', '', val).strip()
    return cleaned if cleaned else val.strip()

def extract_parens(val):
    if not val:
        return ''
    m = re.search(r'[\（\(](.*?)[\）\)]', val)
    return m.group(1).strip() if m else ''

def extract_translation(val, base_name):
    if not val:
        return ''
    parens_val = extract_parens(val)
    outside_val = clean_name(val)
    
    if parens_val and outside_val:
        # Check which one is NOT the base_name
        if normalize_str(outside_val) == normalize_str(base_name):
            return parens_val
        elif normalize_str(parens_val) == normalize_str(base_name):
            return outside_val
        else:
            return parens_val
    elif outside_val and normalize_str(outside_val) != normalize_str(base_name):
        return outside_val
    return parens_val

def get_best_local_base(spot, native_lang):
    raw_name = spot.get('name', '')
    base_from_name = clean_name(raw_name)
    
    # Check native language key (e.g. name_fr, name_de)
    native_key = f'name_{native_lang}'
    native_val = spot.get(native_key, '')
    
    if native_val:
        p_val = extract_parens(native_val)
        o_val = clean_name(native_val)
        # If native key contains a native title inside parens or outside
        if native_lang in ['fr', 'de', 'nl']:
            # Prefer French/German/Dutch string if available
            if p_val and re.search(r'[a-zA-ZÀ-ÿ]', p_val) and not is_near_identical(p_val, base_from_name):
                # If p_val is Latin native title (e.g. "Tour Eiffel") while base_from_name was "Eiffel Tower"
                if "tower" in base_from_name.lower() or "square" in base_from_name.lower() or "castle" in base_from_name.lower():
                    return p_val
            if o_val and re.search(r'[a-zA-ZÀ-ÿ]', o_val):
                return o_val
    
    return base_from_name

def process_city_files(cities_dir):
    city_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))
    total_spots = 0
    total_eliminated = 0

    for filepath in city_files:
        fname = os.path.basename(filepath)
        native_lang = CITY_NATIVE_LANG.get(fname, 'en')
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            spots = data
        else:
            spots = data.get('spots', [])

        for s in spots:
            total_spots += 1
            local_base = get_best_local_base(s, native_lang)
            
            # Process 7 languages (including Dutch)
            langs = ['ja', 'en', 'es', 'zh', 'fr', 'de', 'nl']
            for lang in langs:
                key = f'name_{lang}'
                raw_val = s.get(key, '')
                trans = extract_translation(raw_val, local_base)
                
                # Rule 2: Check if trans is empty or near-identical to local_base
                if not trans or is_near_identical(local_base, trans):
                    s[key] = local_base
                    total_eliminated += 1
                else:
                    # Rule 1: Pattern A -> local_base (trans)
                    if lang == 'ja':
                        s[key] = f"{local_base}（{trans}）"
                    else:
                        s[key] = f"{local_base} ({trans})"

            # Sanitize Japanese Kana leakage in Chinese fields (desc_zh / tip_zh)
            JAPANESE_KANA_ONLY = re.compile(r'[\u3040-\u30ff]')
            for fkey in ['desc_zh', 'tip_zh']:
                val = s.get(fkey, '')
                if JAPANESE_KANA_ONLY.search(val):
                    s[fkey] = s.get(fkey.replace('_zh', '_en'), '')

            # Rule 3: Always set primary 'name' = name_ja
            s['name'] = s['name_ja']

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"🎉 Pattern A Unification Complete across {len(city_files)} cities and {total_spots} spots!")
    print(f"   - Redundant Parens Eliminated: {total_eliminated} instances")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
    process_city_files(cities_dir)
