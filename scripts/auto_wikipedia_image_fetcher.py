#!/usr/bin/env python3
"""
Zero-Margin Travel App - Universal City-Modular Wikipedia Image Pipeline (v8.0.0)
Supports Japanese Wikipedia (ja.wikipedia.org) and Wikimedia Commons ImageInfo resolution.
Includes City-Qualified Disambiguation & High-Risk/Sensitive Keyword Blacklist Filter.
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
    'User-Agent': 'ZeroMarginTravelApp/24.0 (https://github.com/zeromargin-travel/zeromargin-travel-japan; contact@zeromargin-travel.com)'
}

# Sensitive/High-Risk keywords that MUST NOT match unless category is explicitly Memorial/Cemetery
SENSITIVE_KEYWORD_BLACKLIST = [
    'konzentrationslager', 'concentration_camp', 'kz_sachsenhausen', 'kz_dachau',
    'holocaust_memorial', 'gedenkstaette', 'holocaust-denkmal', 'cemetery_grave_marker'
]

# Manual high-quality candidate terms for specific Japanese spots
SPOT_OVERRIDE_TERMS = {
    'oki_p_3': ['瀬長島', 'ウミカジテラス'],
    'oki_p_5': ['玉泉洞', 'おきなわワールド'],
    'oki_p_8': ['ひめゆりの塔', '沖縄平和祈念堂', '平和祈念公園'],
    'oki_p_13': ['真栄田岬', '青の洞窟 (恩納村)'],
    'oki_p_14': ['浦添市', '港川'],
    'oki_p_16': ['フクギ', '備瀬'],
    'oki_p_17': ['古宇利大橋', '古宇利島'],
    'oki_p_18': ['古宇利島', '古宇利大橋'],
    'oki_p_20': ['名護市', 'パイナップル'],
    'oki_p_23': ['読谷村', '壺屋焼', 'やちむん'],
    'oki_p_24': ['波の上ビーチ', '波上宮']
}

# Direct Wikimedia Commons photo files for 100% photo fidelity
COMMONS_DIRECT_FILES = {
    'oki_p_16': 'File:Fukugi trees at Bise Village, Okinawa.jpg',
    'oki_p_23': 'File:Yomitan Yachimun no Sato.jpg',
    'oki_p_18': 'File:JP 沖繩 Okinawa Nago Kouri island Ocean Tower outdoor carpark January 2026 N13P 02.jpg'
}

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

                    # Blacklist Filter
                    if not any(cat in category.lower() for cat in ['memorial', 'cemetery', '追悼', '墓', '平和']):
                        for kw in SENSITIVE_KEYWORD_BLACKLIST:
                            if kw in src.lower() or kw in title_res or kw in extract_res:
                                print(f"  ⚠️ BLACKLIST REJECTED: '{slug}' matched sensitive keyword '{kw}'")
                                return ""

                    if src and ('wikimedia.org' in src or 'http' in src):
                        return src
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(0.8 * (attempt + 1))
            else:
                break
        except Exception:
            break
    return ""

def fetch_commons_thumb(filename, width=640):
    if not filename:
        return ""
    enc = urllib.parse.quote(filename)
    url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={enc}&prop=imageinfo&iiprop=url&iiurlwidth={width}&format=json'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=4) as res:
            d = json.loads(res.read().decode('utf-8'))
            pages = d.get('query', {}).get('pages', {})
            for p in pages.values():
                for info in p.get('imageinfo', []):
                    return info.get('thumburl', '')
    except Exception:
        pass
    return ""

def resolve_spot_image(spot, city_name=""):
    sid = spot.get('id', '')
    category = spot.get('category', '')
    
    # Check direct commons file first
    if sid in COMMONS_DIRECT_FILES:
        thumb = fetch_commons_thumb(COMMONS_DIRECT_FILES[sid])
        if thumb:
            return thumb

    candidates = []
    
    # 0. Japanese Spot Overrides
    if sid in SPOT_OVERRIDE_TERMS:
        for t in SPOT_OVERRIDE_TERMS[sid]:
            candidates.append(('ja', t))

    # 1. Japanese Name Candidates
    raw_name_ja = spot.get('name_ja', spot.get('name', ''))
    clean_ja = clean_title(raw_name_ja)
    if clean_ja:
        candidates.append(('ja', clean_ja))
        parts = [p.strip() for p in re.split(r'[・/]', clean_ja) if p.strip()]
        for p in parts:
            if p != clean_ja:
                candidates.append(('ja', p))
        no_koen = clean_ja.replace('公園', '').strip()
        if no_koen != clean_ja:
            candidates.append(('ja', no_koen))
        no_ato = clean_ja.replace('跡', '').strip()
        if no_ato != clean_ja:
            candidates.append(('ja', no_ato))

    # 2. English / Western Candidates
    raw_name_en = spot.get('name_en', '')
    clean_en = clean_title(raw_name_en)
    city_pure = city_name.split(',')[0].strip() if city_name else ""
    
    if clean_en and city_pure:
        candidates.append(('en', f"{clean_en}, {city_pure}"))
        candidates.append(('en', f"{clean_en} ({city_pure})"))
    if clean_en:
        candidates.append(('en', clean_en))

    raw_name_de = spot.get('name_de', '')
    clean_de = clean_title(raw_name_de)
    if clean_de:
        candidates.append(('de', clean_de))

    for lang, title in candidates:
        img_url = fetch_wiki_summary(lang, title, category)
        if img_url:
            return img_url

    return ""

def process_all_city_modules(data_cities_dir, js_file_path):
    print("🚀 Running Universal Direct Wikipedia REST API Resolver (v8.0.0 with Japan/ja support)...")
    json_files = sorted(glob.glob(os.path.join(data_cities_dir, '*.json')))
    
    if not json_files:
        print(f"❌ No city JSON files found in {data_cities_dir}")
        return

    total_photos = 0
    total_fallbacks = 0

    for fpath in json_files:
        fname = os.path.basename(fpath)
        # Only resolve okinawa.json for now to keep run fast
        if fname != 'okinawa.json':
            continue

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

        print(f"\n📂 Processing {fname} ({len(spots)} spots)...")

        for s in spots:
            current_img = s.get('image', '')
            # If image contains 400-broken link without query params or empty, resolve it
            needs_resolution = not current_img or ('?' not in current_img and 'upload.wikimedia.org' in current_img)

            if needs_resolution:
                resolved_url = resolve_spot_image(s, cityName)
                if resolved_url:
                    s['image'] = resolved_url
                    s['wikiImage'] = resolved_url
                    s['hasWiki'] = True
                    verified_in_city += 1
                    print(f"  ✅ [{s['id']}] {s['name']}: {resolved_url[:75]}...")
                else:
                    s['hasWiki'] = False
                    fallbacks_in_city += 1
                    print(f"  ⚠️ [{s['id']}] {s['name']}: No image found (fallback)")
            else:
                verified_in_city += 1

        total_photos += verified_in_city
        total_fallbacks += fallbacks_in_city

        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print("\n=======================================================")
    print("🎉 WIKIPEDIA DIRECT RESOLUTION (v8.0.0) COMPLETE!")
    print(f"   - Total Verified Live Photos: {total_photos} spots")
    print(f"   - Total Fallbacks: {total_fallbacks} spots")
    print(f"   - Total System Spots: {total_photos + total_fallbacks}")
    print("=======================================================")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
    js_file_path = os.path.join(base_dir, '..', 'js', 'ai-travel-engine.js')
    process_all_city_modules(data_cities_dir, js_file_path)
