#!/usr/bin/env python3
"""
Zero-Margin Travel App - Universal Smart Wikipedia Image Pipeline (v9.3.0)
Architecture Rules:
1. STRICT MATCHING ONLY: Never substitute a spot with its parent municipality (prevents fake castle/city photos).
2. LOGO & SVG FILTER: Reject icons, logos, flags, maps, coat-of-arms, diagrams, films, and stamps automatically.
3. ARTICLE PHOTO HARVEST: If the top Wikipedia image is a logo/SVG or missing, inspect images contained inside the article and resolve real photo thumbs from Wikimedia Commons.
4. COMMONS SEARCH FALLBACK: Search Wikimedia Commons for "{Spot} {City/Region}" with location qualification.
5. HONEST FALLBACK: If no authentic photo exists on Wikimedia, leave image empty so the app renders
   a clean, themed category SVG banner rather than a misleading photo.
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
    'User-Agent': 'ZeroMarginTravelApp/25.0 (https://github.com/zeromargin-travel/zeromargin-travel-japan; contact@zeromargin-travel.com)'
}

BAD_IMAGE_KEYWORDS = [
    '.svg', 'logo', 'icon', 'symbol', 'flag', 'seal', 'emblem', 'coat_of_arms',
    'map', 'locator', 'diagram', 'chart', 'drawing', 'stub', 'question', 'banner',
    'fossil', 'skull', 'painting', 'battle', 'cemetery_grave_marker', 'konzentrationslager',
    'yodore', 'film_still', 'movie_still'
]

def clean_title(raw_title):
    if not raw_title:
        return ""
    cleaned = raw_title
    while re.search(r'[\(\（][^\(\）\（\）]*[\)\）]', cleaned):
        cleaned = re.sub(r'[\(\（][^\(\）\（\）]*[\)\）]', '', cleaned).strip()
    return cleaned.strip()

def is_valid_photo_filename(title):
    if not title:
        return False
    t = title.lower()
    for bad in BAD_IMAGE_KEYWORDS:
        if bad in t:
            return False
    # Must have typical photo extensions
    return any(t.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp'])

def is_valid_photo_url(url, title=""):
    if not url:
        return False
    u = url.lower()
    t = (title or "").lower()
    for bad in BAD_IMAGE_KEYWORDS:
        if bad in u or bad in t:
            return False
    return ('wikimedia.org' in u or 'http' in u)

def fetch_wiki_summary_image(slug, lang='ja'):
    if not slug:
        return ""
    encoded_slug = urllib.parse.quote(slug.replace(' ', '_'))
    url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{encoded_slug}'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
            if res.status == 200:
                data = json.loads(res.read().decode('utf-8'))
                src = data.get('thumbnail', {}).get('source', '')
                title = data.get('title', '')
                if src and is_valid_photo_url(src, title):
                    return src
    except Exception:
        pass
    return ""

def fetch_wiki_article_photos(slug, lang='ja', width=800):
    """Harvest real photos listed inside a Wikipedia article if top image is a logo or missing."""
    if not slug:
        return ""
    encoded_slug = urllib.parse.quote(slug.replace(' ', '_'))
    url = f'https://{lang}.wikipedia.org/w/api.php?action=query&titles={encoded_slug}&prop=images&imlimit=50&format=json'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
            d = json.loads(res.read().decode('utf-8'))
            pages = d.get('query', {}).get('pages', {})
            candidate_files = []
            for p in pages.values():
                for img in p.get('images', []):
                    title = img.get('title', '')
                    clean_t = re.sub(r'^(ファイル|File):', '', title).strip()
                    if is_valid_photo_filename(clean_t):
                        candidate_files.append(clean_t)
            
            # Prioritize files containing spot keywords or scenic keywords
            candidate_files.sort(key=lambda x: (
                0 if any(k in x.lower() for k in ['aquarium', 'tank', 'main', 'hall', 'park', 'gate', 'beach', 'cliff']) else 1
            ))

            for cfile in candidate_files[:8]:
                enc_f = urllib.parse.quote('File:' + cfile)
                url_f = f'https://commons.wikimedia.org/w/api.php?action=query&titles={enc_f}&prop=imageinfo&iiprop=url&iiurlwidth={width}&format=json'
                req_f = urllib.request.Request(url_f, headers=HEADERS)
                with urllib.request.urlopen(req_f, context=ctx, timeout=3) as res_f:
                    df = json.loads(res_f.read().decode('utf-8'))
                    for pg in df.get('query', {}).get('pages', {}).values():
                        for info in pg.get('imageinfo', []):
                            thumb = info.get('thumburl')
                            if thumb and is_valid_photo_url(thumb, cfile):
                                return thumb
    except Exception:
        pass
    return ""

def search_wikimedia_commons_photos(query, width=800):
    """Search Wikimedia Commons directly for authentic spot photos."""
    if not query:
        return ""
    enc = urllib.parse.quote(query)
    url = f'https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={enc}&srnamespace=6&format=json'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=4) as res:
            if res.status == 200:
                d = json.loads(res.read().decode('utf-8'))
                results = d.get('query', {}).get('search', [])
                for r in results[:10]:
                    t = r.get('title', '')
                    clean_t = re.sub(r'^(ファイル|File):', '', t).strip()
                    if not is_valid_photo_filename(clean_t):
                        continue
                    enc_t = urllib.parse.quote(t)
                    url_t = f'https://commons.wikimedia.org/w/api.php?action=query&titles={enc_t}&prop=imageinfo&iiprop=url&iiurlwidth={width}&format=json'
                    req_t = urllib.request.Request(url_t, headers=HEADERS)
                    with urllib.request.urlopen(req_t, context=ctx, timeout=4) as res_t:
                        if res_t.status == 200:
                            d_t = json.loads(res_t.read().decode('utf-8'))
                            pages = d_t.get('query', {}).get('pages', {})
                            for p in pages.values():
                                for info in p.get('imageinfo', []):
                                    thumb = info.get('thumburl')
                                    if thumb and is_valid_photo_url(thumb, t):
                                        return thumb
    except Exception:
        pass
    return ""

def resolve_spot_image(spot, city_name=""):
    """
    Universal 4-Layer Smart Photo Resolution:
    1. Exact Wikipedia summary (validated photo)
    2. Article internal photo harvest (when summary is logo/diagram like Churaumi)
    3. English / Multilingual Wikipedia article
    4. Commons targeted search (requires spot name + regional context to avoid generic homonyms)
    5. Clean Honest Fallback (leave empty for category SVG)
    """
    raw_name_ja = spot.get('name_ja', spot.get('name', ''))
    clean_ja = clean_title(raw_name_ja)
    raw_name_en = spot.get('name_en', '')
    clean_en = clean_title(raw_name_en)

    spot_queries = []
    if clean_ja:
        spot_queries.append(clean_ja)
        parts = [p.strip() for p in re.split(r'[・/]', clean_ja) if p.strip()]
        for p in parts:
            if len(p) >= 3 and p != clean_ja:
                spot_queries.append(p)
        no_koen = clean_ja.replace('公園', '').strip()
        if len(no_koen) >= 3 and no_koen != clean_ja:
            spot_queries.append(no_koen)
        no_ato = clean_ja.replace('跡', '').strip()
        if len(no_ato) >= 3 and no_ato != clean_ja:
            spot_queries.append(no_ato)

    # 1. Try Japanese Wikipedia article summary
    for q in spot_queries:
        img = fetch_wiki_summary_image(q, lang='ja')
        if img:
            return img, f"ja.wiki_summary:{q}"

    # 2. Try Japanese Wikipedia article internal photos (harvest real photo if top is logo)
    for q in spot_queries:
        img = fetch_wiki_article_photos(q, lang='ja')
        if img:
            return img, f"ja.wiki_article_photo:{q}"

    # 3. Try English Wikipedia article summary & internal photos
    if clean_en:
        img = fetch_wiki_summary_image(clean_en, lang='en')
        if img:
            return img, f"en.wiki_summary:{clean_en}"
        img = fetch_wiki_article_photos(clean_en, lang='en')
        if img:
            return img, f"en.wiki_article_photo:{clean_en}"

    # 4. Try targeted Wikimedia Commons photo search (Must include Okinawa/City to avoid random cafes worldwide!)
    city_pure = city_name.split(',')[0].strip() if city_name else "Okinawa"
    commons_queries = []
    if clean_en:
        commons_queries.append(f"{clean_en} {city_pure}")
        commons_queries.append(f"{clean_en} Okinawa")
    if clean_ja:
        commons_queries.append(f"{clean_ja} {city_pure}")
        commons_queries.append(f"{clean_ja} 沖縄")

    for cq in commons_queries:
        img = search_wikimedia_commons_photos(cq)
        if img:
            return img, f"commons:{cq}"

    # 5. Honest fallback: return empty to let app render elegant SVG fallback
    return "", "no_authentic_photo"

def process_all_city_modules(data_cities_dir):
    print("🚀 Running Universal Smart Wikipedia Image Pipeline (v9.3.0)...")
    json_files = sorted(glob.glob(os.path.join(data_cities_dir, '*.json')))
    
    if not json_files:
        print(f"❌ No city JSON files found in {data_cities_dir}")
        return

    total_photos = 0
    total_fallbacks = 0

    for fpath in json_files:
        fname = os.path.basename(fpath)
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
            resolved_url, reason = resolve_spot_image(s, cityName)
            if resolved_url:
                s['image'] = resolved_url
                s['wikiImage'] = resolved_url
                s['hasWiki'] = True
                verified_in_city += 1
                print(f"  📸 [{s['id']}] {s['name']}: {reason} -> {resolved_url.split('/')[-1][:45]}")
            else:
                s['image'] = ""
                s['wikiImage'] = ""
                s['hasWiki'] = False
                fallbacks_in_city += 1
                print(f"  🏷️ [{s['id']}] {s['name']}: Honest Themed Fallback ({reason})")

        total_photos += verified_in_city
        total_fallbacks += fallbacks_in_city

        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print("\n=======================================================")
    print("🎉 UNIVERSAL IMAGE RESOLUTION COMPLETE!")
    print(f"   - Verified Authentic Photos: {total_photos} spots")
    print(f"   - Clean Themed Fallbacks: {total_fallbacks} spots")
    print(f"   - Total Spots Processed: {total_photos + total_fallbacks}")
    print("=======================================================")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
    process_all_city_modules(data_cities_dir)
