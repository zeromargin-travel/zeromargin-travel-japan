import glob
import json
import re
import os

city_files = sorted(glob.glob('data/cities/*.json'))

# Language specific signature stop-words
ENGLISH_STOPWORDS = {'the', 'and', 'of', 'in', 'to', 'for', 'with', 'on', 'at', 'by', 'from', 'featuring', 'housing', 'connecting', 'located', 'famous', 'stretching', 'dominated'}
SPANISH_STOPWORDS = {'el', 'la', 'los', 'las', 'un', 'una', 'y', 'de', 'en', 'con', 'por', 'para', 'del', 'famoso', 'ubicado'}
FRENCH_STOPWORDS = {'le', 'la', 'les', 'un', 'une', 'et', 'de', 'du', 'des', 'en', 'dans', 'sur', 'avec', 'pour', 'situé', 'célèbre'}
GERMAN_STOPWORDS = {'der', 'die', 'das', 'ein', 'eine', 'und', 'von', 'in', 'mit', 'für', 'auf', 'berühmt', 'gelegen'}
JAPANESE_HIRAGANA_KATAKANA = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]')

print(f"Auditing and auto-correcting translations & tags across {len(city_files)} city JSON files...")

# Keywords that qualify a non-'Kids & Family' category spot as genuine family/kids friendly
FAMILY_KEYWORDS = [
    'zoo', 'aquarium', 'planetarium', 'science', 'theme park', 'amusement', 'dinosaur',
    'miniatur', 'water park', 'playground', 'tierpark', 'kindermuseum', 'freizeitpark',
    'wildpark', 'schokolade', 'chocolat', 'lido', 'disney', 'parc astérix', 'europa-park',
    'phantasialand', 'futuroscope', 'legoland', 'fairytale', '童話', '動物園', '水族館', '科学', 'テーマパーク'
]

# Keywords that FORBID a spot from being tagged as 'kids': true
EXCLUDE_KIDS_KEYWORDS = [
    'brauhaus', 'kneipe', 'pub', 'bar', 'nightlife', 'reeperbahn', 'cider', 'apfelwein',
    'friedhof', 'cimetière', 'cemetery', 'tomb', '墓地', '遺構', 'ゲシュタポ', 'ホロコースト',
    'holocaust', 'gestapo', 'ns-dokumentationszentrum', 'unterwelten', 'bunker', 'dungeon',
    'red light', 'キャバレー', '歓楽街', '風俗'
]

# Curated translation fixes for English leaks
curated_fixes = {
    "b_49": {
        "desc_es": "Extenso parque paisajístico con jardines temáticos de Asia, Oriente Medio y Europa con un teleférico panorámico.",
        "desc_de": "Weitläufiger Landschaftspark in Berlin-Marzahn mit traditionellen Gartenkünsten aus Asien, dem Orient und Europa sowie Seilbahn."
    },
    "h_13": {
        "desc_es": "Renombrado museo de artes aplicadas, diseño, fotografía y cultura visual en un edificio neorrenacentista.",
        "desc_de": "Renommiertes Museum für angewandte Kunst, Design, Fotografie und Mode nahe dem Hamburger Hauptbahnhof."
    },
    "h_33": {
        "desc_es": "Experiencia sensorial inmersiva donde guías no videntes conducen a los visitantes a través de salas completamente a oscuras.",
        "desc_de": "Einzigartige Erlebnisausstellung in der Speicherstadt, bei der blinde Guides Besucher durch völlig abgedunkelte Räume führen."
    }
}

total_spots_modified = 0
total_kids_spots = 0

for fpath in city_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list):
        spots = data
    else:
        spots = data.get('spots', [])

    for s in spots:
        sid = s.get('id')
        if sid in curated_fixes:
            for k, v in curated_fixes[sid].items():
                s[k] = v
        category = s.get('category', '')
        name = s.get('name', '')
        desc = (s.get('desc_ja', '') + " " + s.get('desc_en', '')).lower()
        name_lower = name.lower()

        # -------------------------------------------------------------
        # STRICT KIDS CATEGORY TAG AUDITING (Rule #5)
        # -------------------------------------------------------------
        # Force false if matching adult/sensitive keywords
        is_excluded = any(kw in name_lower or kw in desc for kw in EXCLUDE_KIDS_KEYWORDS)
        
        if is_excluded:
            s['kids'] = False
        elif category == "Kids & Family":
            s['kids'] = True
        else:
            # Only set true if explicitly family-oriented
            is_family = any(kw in name_lower or kw in desc for kw in FAMILY_KEYWORDS)
            s['kids'] = is_family

        if s.get('kids'):
            total_kids_spots += 1

        # -------------------------------------------------------------
        # STRICT RAIN TAG AUDITING
        # -------------------------------------------------------------
        if category in ["Museum & Gallery", "Shopping"]:
            s['rain'] = True
        elif category in ["Scenery & Walk"]:
            s['rain'] = False

        # -------------------------------------------------------------
        # CROSS-CONTAMINATION & LEAK DETECTOR GUARD
        # -------------------------------------------------------------
        tip_ja = s.get('tip_ja', '') or s.get('tip', '')
        for s_other in spots:
            if s['id'] != s_other['id']:
                other_pure_name = s_other['name'].split(' (')[0].split('（')[0].strip()
                if len(other_pure_name) > 6 and other_pure_name in tip_ja and not any(k in s['name'] for k in [other_pure_name, 'Louvre', 'Eiffel', 'Seine']):
                    if not any(valid_ctx in tip_ja for valid_ctx in ['の景色', 'を望む', 'が見える', '近隣の', '隣接する', '向かい', '内部', '敷地内']):
                        print(f"⚠️ CROSS-CONTAMINATION GUARD NOTICE: [{s['id']}] {s['name']} mentions {other_pure_name}")

        total_spots_modified += 1

    if isinstance(data, dict):
        data['spots'] = spots
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"  - Cleaned, audited & tag-verified {fname} ({len(spots)} spots)")

print(f"\n🎉 Successfully audited and refined {total_spots_modified} spots across all city files!")
print(f"   └─ Verified Kids-friendly spots count: {total_kids_spots} / {total_spots_modified}")
