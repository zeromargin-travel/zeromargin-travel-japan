#!/usr/bin/env python3
"""
Zero-Margin Travel App - Universal City-Modular Wikipedia Image Pipeline (v7.0.0)
Includes City-Qualified Disambiguation & High-Risk/Sensitive Keyword Blacklist Filter
"""

import urllib.request
import json
import urllib.parse
import ssl
import time
import glob
import os
import re

ctx = ssl._create_unverified_context()
HEADERS = {
    'User-Agent': 'ZeroMarginTravelApp/23.0 (https://github.com/zeromargin-travel/zero-margin-travel-app; contact@zeromargin-travel.org)'
}

# Sensitive/High-Risk keywords that MUST NOT match unless category is explicitly Memorial/Cemetery
SENSITIVE_KEYWORD_BLACKLIST = [
    'konzentrationslager', 'concentration_camp', 'kz_sachsenhausen', 'kz_dachau',
    'holocaust_memorial', 'gedenkstaette', 'holocaust-denkmal', 'cemetery_grave_marker'
]

def clean_title(raw_title):
    if not raw_title:
        return ""
    cleaned = raw_title
    while re.search(r'[\(\（][^\(\）\（\）]*[\)\）]', cleaned):
        cleaned = re.sub(r'[\(\（][^\(\）\（\）]*[\)\）]', '', cleaned).strip()
    return cleaned.strip()

def fetch_wiki_summary(lang, slug, category=""):
    if not slug:
        return ""
    encoded_slug = urllib.parse.quote(slug.replace(' ', '_'))
    url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{encoded_slug}'
    
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=4) as res:
                if res.status == 200:
                    data = json.loads(res.read().decode('utf-8'))
                    src = data.get('thumbnail', {}).get('source', '')
                    title_res = data.get('title', '').lower()
                    extract_res = data.get('extract', '').lower()

                    # Blacklist Filter: Check if returned page contains sensitive keywords for non-memorial spots
                    if not any(cat in category.lower() for cat in ['memorial', 'cemetery', '追悼', '墓']):
                        for kw in SENSITIVE_KEYWORD_BLACKLIST:
                            if kw in src.lower() or kw in title_res or kw in extract_res:
                                print(f"  ⚠️ BLACKLIST REJECTED: '{slug}' matched sensitive keyword '{kw}'")
                                return ""

                    if src and ('upload.wikimedia.org' in src or 'http' in src):
                        return src
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(0.8 * (attempt + 1))
            else:
                break
        except Exception:
            break
    return ""

def resolve_spot_image(spot, city_name=""):
    candidates = []
    category = spot.get('category', '')
    
    # 1. City-Qualified Candidates (HIGHEST PRIORITY to prevent homonym collisions!)
    raw_name_de = spot.get('name_de', '')
    clean_de = clean_title(raw_name_de)
    
    city_pure = city_name.split(',')[0].strip() if city_name else ""
    
    if clean_de and city_pure:
        candidates.append(('de', f"{clean_de} ({city_pure})"))
        candidates.append(('en', f"{clean_de}, {city_pure}"))
    
    raw_name_en = spot.get('name_en', '')
    clean_en = clean_title(raw_name_en)
    if clean_en and city_pure:
        candidates.append(('en', f"{clean_en}, {city_pure}"))
        candidates.append(('en', f"{clean_en} ({city_pure})"))

    # 2. DE name bare
    if clean_de:
        candidates.append(('de', clean_de))
        candidates.append(('en', clean_de))
    
    # 3. EN name bare
    if clean_en:
        candidates.append(('en', clean_en))
        candidates.append(('de', clean_en))
    
    # 4. FR name bare
    clean_fr = clean_title(spot.get('name_fr', ''))
    if clean_fr:
        candidates.append(('fr', clean_fr))

    # 5. Fallback general clean name
    clean_gen = clean_title(spot.get('name', ''))
    if clean_gen:
        candidates.append(('de', clean_gen))
        candidates.append(('en', clean_gen))
        candidates.append(('fr', clean_gen))

    for lang, title in candidates:
        img_url = fetch_wiki_summary(lang, title, category)
        if img_url:
            return img_url

    return ""

def process_all_city_modules(data_cities_dir, js_file_path):
    print("🚀 Running Universal Direct Wikipedia REST API Resolver (v7.0.0 with City-Disambiguation & Blacklist)...")
    json_files = sorted(glob.glob(os.path.join(data_cities_dir, '*.json')))
    
    if not json_files:
        print(f"❌ No city JSON files found in {data_cities_dir}")
        return

    aggregated_db = {}
    total_photos = 0
    total_fallbacks = 0

    for fpath in json_files:
        fname = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            cityName = data.get('cityName', fname.replace('.json', ''))
            spots = data.get('spots', [])
        elif isinstance(data, list):
            cityName = fname.replace('.json', '').replace('_', ' ').title()
            spots = data
        else:
            spots = []
            cityName = fname
        verified_in_city = 0
        fallbacks_in_city = 0

        for s in spots:
            # Check existing image
            current_img = s.get('image', '')
            category = s.get('category', '')
            
            # Re-check existing image against blacklist
            rejected = False
            if current_img and not any(cat in category.lower() for cat in ['memorial', 'cemetery', '追悼', '墓']):
                for kw in SENSITIVE_KEYWORD_BLACKLIST:
                    if kw in current_img.lower():
                        rejected = True
                        print(f"  ⚠️ Existing image REJECTED for [{s['id']}] {s['name']}: contains '{kw}'")
                        s['image'] = ""
                        s['wikiImage'] = ""
                        break

            if not s.get('image') or rejected:
                resolved_url = resolve_spot_image(s, cityName)
                if resolved_url:
                    s['image'] = resolved_url
                    s['wikiImage'] = resolved_url
                    s['hasWiki'] = True
                    verified_in_city += 1
                else:
                    s['hasWiki'] = False
                    fallbacks_in_city += 1
            else:
                verified_in_city += 1

        total_photos += verified_in_city
        total_fallbacks += fallbacks_in_city

        # Save back city file
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print("\n=======================================================")
    print("🎉 WIKIPEDIA DIRECT RESOLUTION (v7.0.0) COMPLETE!")
    print(f"   - Total Verified Live Photos: {total_photos} spots")
    print(f"   - Total Fallbacks: {total_fallbacks} spots")
    print(f"   - Total System Spots: {total_photos + total_fallbacks}")
    print("=======================================================")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
    js_file_path = os.path.join(base_dir, '..', 'js', 'ai-travel-engine.js')
    process_all_city_modules(data_cities_dir, js_file_path)
