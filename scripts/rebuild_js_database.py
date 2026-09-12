import os
import json
import glob
import re
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))

print("🚀 Running Integrated End-to-End Build Pipeline (v3.0.0)...")

# 1. Fetch & verify all Wikipedia photos (optional via FETCH_WIKI=1)
if os.environ.get('FETCH_WIKI') == '1':
    fetcher_script = os.path.join(base_dir, 'auto_wikipedia_image_fetcher.py')
    if os.path.exists(fetcher_script):
        subprocess.run(['python3', fetcher_script], check=True)

# 2. Universal Multilingual Hybrid Name Standard (Pattern A)
hybrid_script = os.path.join(base_dir, 'unify_hybrid_names_pattern_a.py')
if os.path.exists(hybrid_script):
    subprocess.run(['python3', hybrid_script], check=True)

# 3. Category & Tag Compliance Audit
audit_script = os.path.join(base_dir, 'audit_and_fix_translations.py')
if os.path.exists(audit_script):
    subprocess.run(['python3', audit_script], check=True)

# 4. Build js/ai-travel-engine.js with 3-Layer Compliance Verification
city_files = sorted(glob.glob(os.path.join(base_dir, '..', 'data', 'cities', '*.json')))
print(f"\nReading {len(city_files)} city JSON files for js/ai-travel-engine.js...")

ENGLISH_STOPWORDS = {'the', 'and', 'of', 'in', 'to', 'for', 'with', 'on', 'at', 'by', 'from', 'featuring', 'housing', 'connecting', 'located', 'famous', 'stretching', 'dominated'}
SPANISH_STOPWORDS = {'el', 'la', 'los', 'las', 'un', 'una', 'y', 'de', 'en', 'con', 'por', 'para', 'del', 'famoso', 'ubicado'}
FRENCH_STOPWORDS = {'le', 'la', 'les', 'un', 'une', 'et', 'de', 'du', 'des', 'en', 'dans', 'sur', 'avec', 'pour', 'situé', 'célèbre'}
GERMAN_STOPWORDS = {'der', 'die', 'das', 'ein', 'eine', 'und', 'von', 'in', 'mit', 'für', 'auf', 'berühmt', 'gelegen'}
JAPANESE_HIRAGANA_KATAKANA = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]')

total_audited_spots = 0
untranslated_violations = []
missing_hybrid_name_violations = []

db = {}

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
    cname = city_name_map.get(fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, dict):
        spots = data.get('spots', [])
        if not cname:
            cname = data.get('cityName', fname.replace('.json', '').title())
    elif isinstance(data, list):
        spots = data
    else:
        spots = []
    
    if not cname:
        cname = fname.replace('.json', '').replace('_', ' ').title()

    db[cname] = spots
    print(f" -> Loaded {cname}: {len(spots)} spots")

    for s in spots:
        total_audited_spots += 1
        sid = s.get('id', 'unknown')

        # Layer 1: Check Japanese text leakage in foreign language fields
        # Western fields (EN, DE, FR, ES, NL) must NOT contain CJK characters
        for fkey in ['tip_en', 'tip_de', 'tip_fr', 'tip_es', 'tip_nl', 'desc_en', 'desc_de', 'desc_fr', 'desc_es', 'desc_nl']:
            val = s.get(fkey, '')
            if JAPANESE_HIRAGANA_KATAKANA.search(val):
                untranslated_violations.append((cname, sid, s.get('name', ''), fkey, f"Japanese/CJK leakage: '{val[:30]}'"))

        # Chinese fields (ZH) must NOT contain Japanese Kana (Hiragana/Katakana)
        JAPANESE_KANA_ONLY = re.compile(r'[\u3040-\u30ff]')
        for fkey in ['tip_zh', 'desc_zh']:
            val = s.get(fkey, '')
            if JAPANESE_KANA_ONLY.search(val):
                untranslated_violations.append((cname, sid, s.get('name', ''), fkey, f"Japanese Kana leakage in Chinese field: '{val[:30]}'"))

        # Layer 2: Check empty desc or tip fields
        for fkey in ['desc_ja', 'desc_en', 'desc_es', 'desc_zh', 'desc_fr', 'desc_de', 'desc_nl', 'tip_ja', 'tip_en', 'tip_es', 'tip_zh', 'tip_fr', 'tip_de', 'tip_nl']:
            val = s.get(fkey, '')
            if not val or len(val.strip()) == 0:
                untranslated_violations.append((cname, sid, s.get('name', ''), fkey, "Empty field string"))

        # Layer 3: Check Japanese validity in desc_ja
        desc_ja = s.get('desc_ja', '')
        if not JAPANESE_HIRAGANA_KATAKANA.search(desc_ja) and len(desc_ja) > 5:
            untranslated_violations.append((cname, sid, s.get('name', ''), 'desc_ja', f"Missing Japanese: '{desc_ja[:30]}'"))

        # Layer 4: Hybrid Name verification across all 7 languages
        for lang_key in ['name_en', 'name_ja', 'name_es', 'name_zh', 'name_fr', 'name_de', 'name_nl']:
            val = s.get(lang_key, '')
            if not val:
                missing_hybrid_name_violations.append((cname, sid, s.get('name', ''), lang_key))

# Output Guard Report
print("\n" + "="*70)
if untranslated_violations or missing_hybrid_name_violations:
    print("⚠️ 5-LAYER COMPLIANCE GUARD NOTICE:")
    for v in untranslated_violations:
        print(f"   [{v[0]}] {v[1]} ({v[2]}) -> {v[3]}: \"{v[4]}...\"")
    for v in missing_hybrid_name_violations:
        print(f"   [{v[0]}] {v[1]} ({v[2]}) -> Missing {v[3]}")
    raise ValueError("Compliance Guard Failed: Defects present in database!")
else:
    print(f"🛡️ 5-Layer Compliance Guard PASSED: All {total_audited_spots} spots across {len(db)} cities pass Language Hygiene, Non-Empty, Category & Hybrid Name checks!")
print("="*70 + "\n")

# Write to js/ai-travel-engine.js
js_path = os.path.join(base_dir, '..', 'js', 'ai-travel-engine.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js_code = f.read()

# 1. Update candidateSpotsDatabase
db_marker = 'const candidateSpotsDatabase = '
func_marker = '\nfunction getCategoryIcon(cat)'

start_idx = js_code.find(db_marker)
func_idx = js_code.find(func_marker)

if start_idx != -1 and func_idx != -1:
    new_db_json = json.dumps(db, indent=2, ensure_ascii=False)
    js_code = js_code[:start_idx + len(db_marker)] + new_db_json + ';\n\n' + js_code[func_idx:]

# 2. Update countryCityMap dynamically in js/ai-travel-engine.js
new_country_map = {
    'France': [
        {'value': 'Paris, France', 'label': '🇫🇷 Paris'},
        {'value': 'Bordeaux, France', 'label': '🇫🇷 Bordeaux'},
        {'value': 'Lyon, France', 'label': '🇫🇷 Lyon'},
        {'value': 'Marseille, France', 'label': '🇫🇷 Marseille'},
        {'value': 'Nice, France', 'label': "🇫🇷 Nice & Côte d'Azur"},
        {'value': 'Strasbourg, France', 'label': '🇫🇷 Strasbourg'},
        {'value': 'Toulouse, France', 'label': '🇫🇷 Toulouse'}
    ],
    'Germany': [
        {'value': 'Berlin, Germany', 'label': '🇩🇪 Berlin'},
        {'value': 'Cologne, Germany', 'label': '🇩🇪 Cologne'},
        {'value': 'Dresden, Germany', 'label': '🇩🇪 Dresden'},
        {'value': 'Frankfurt, Germany', 'label': '🇩🇪 Frankfurt'},
        {'value': 'Hamburg, Germany', 'label': '🇩🇪 Hamburg'},
        {'value': 'Heidelberg, Germany', 'label': '🇩🇪 Heidelberg'},
        {'value': 'Munich, Germany', 'label': '🇩🇪 Munich'},
        {'value': 'Nuremberg, Germany', 'label': '🇩🇪 Nuremberg'}
    ],
    'Netherlands': [
        {'value': 'Amsterdam, Netherlands', 'label': '🇳🇱 Amsterdam'},
        {'value': 'Rotterdam, Netherlands', 'label': '🇳🇱 Rotterdam'},
        {'value': 'The Hague, Netherlands', 'label': '🇳🇱 The Hague'},
        {'value': 'Utrecht, Netherlands', 'label': '🇳🇱 Utrecht'},
        {'value': 'Maastricht, Netherlands', 'label': '🇳🇱 Maastricht'}
    ],
    'Belgium': [
        {'value': 'Brussels, Belgium', 'label': '🇧🇪 Brussels'},
        {'value': 'Bruges, Belgium', 'label': '🇧🇪 Bruges'},
        {'value': 'Antwerp, Belgium', 'label': '🇧🇪 Antwerp'},
        {'value': 'Ghent, Belgium', 'label': '🇧🇪 Ghent'}
    ],
    'Luxembourg': [
        {'value': 'Luxembourg City, Luxembourg', 'label': '🇱🇺 Luxembourg'}
    ]
}

map_marker = 'countryCityMap: '
on_country_marker = '\n  onCountryChange()'

m_start = js_code.rfind(map_marker)
m_end = js_code.find(on_country_marker, m_start if m_start != -1 else 0)

if m_start != -1 and m_end != -1:
    map_json = json.dumps(new_country_map, indent=4, ensure_ascii=False)
    js_code = js_code[:m_start + len(map_marker)] + map_json + ',\n' + js_code[m_end:]

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_code)
print(f"🎉 Successfully rebuilt {js_path} with 100% verified multilingual data and full countryCityMap across {len(db)} cities!")

# 5. Apply Top 7 & Hidden Gems Tagging
top7_script = os.path.join(base_dir, 'apply_top7_hiddengems_tags.py')
if os.path.exists(top7_script):
    print("\n🏷️ Applying Top 7 & Hidden Gems tagging across all cities...")
    subprocess.run(['python3', top7_script], check=True)

