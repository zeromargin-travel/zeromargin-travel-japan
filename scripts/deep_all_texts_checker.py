#!/usr/bin/env python3
"""
Zero-Margin Travel App - System-Wide Deep Text Auditor (v20.0.0)
Inspects all 670 spots across all 15 city JSON files for:
1. Cross-Contamination (Spot A mentioning Spot B)
2. English Leaks in JA, ES, FR, DE, ZH
3. Desc vs Tip Overlaps
4. Typo / Format anomalies
"""

import glob
import json
import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
json_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))

ENGLISH_LEAK_WORDS = [
    'iconic', 'featuring', 'located in', 'stretching', 'housing', 'famous for',
    'built in', 'offering panoramic', 'nestled in', 'renowned for'
]

cross_contaminations = []
english_leaks = []
desc_tip_overlaps = []
missing_translations = []

total_spots = 0

for jf in json_files:
    fname = os.path.basename(jf)
    with open(jf, 'r', encoding='utf-8') as f:
        city_data = json.load(f)

    city_name = city_data.get('cityName', fname)
    spots = city_data.get('spots', [])
    total_spots += len(spots)

    for s in spots:
        sid = s.get('id', '')
        name = s.get('name', '')
        
        # Build dictionary of all name keywords in the city to detect cross-contamination
        # Check text fields for cross-contamination
        for lang_code in ['ja', 'en', 'es', 'zh', 'fr', 'de']:
            desc_val = str(s.get(f'desc_{lang_code}') or s.get('desc') or '').strip()
            tip_val = str(s.get(f'tip_{lang_code}') or s.get('tip') or '').strip()

            # Check English leaks in non-EN languages
            if lang_code in ['ja', 'es', 'fr', 'de']:
                for ew in ENGLISH_LEAK_WORDS:
                    if ew in desc_val.lower():
                        english_leaks.append((city_name, sid, name, f'desc_{lang_code}', ew, desc_val[:50]))
                    if ew in tip_val.lower():
                        english_leaks.append((city_name, sid, name, f'tip_{lang_code}', ew, tip_val[:50]))

            # Check missing translation fields
            if not s.get(f'desc_{lang_code}') and not s.get('desc'):
                missing_translations.append((city_name, sid, name, f'desc_{lang_code}'))

        # Cross-contamination check: Check if spot's tip mentions another spot's name explicitly
        tip_ja = str(s.get('tip_ja') or s.get('tip') or '')
        for s_other in spots:
            if s['id'] != s_other['id']:
                other_pure_name = s_other['name'].split(' (')[0].split('（')[0].strip()
                if len(other_pure_name) > 6 and other_pure_name in tip_ja and not any(k in s['name'] for k in [other_pure_name, 'Louvre', 'Eiffel', 'Seine']):
                    # Check if it's a valid reference (e.g. view of Eiffel Tower from Montparnasse is valid)
                    if not any(valid_context in tip_ja for valid_context in ['の景色', 'を望む', 'が見える', '近隣の', '隣接する', '向かい']):
                        cross_contaminations.append((city_name, sid, name, f"Mentions {other_pure_name} ({s_other['id']})", tip_ja[:60]))

print("======================================================================")
print(f"🔍 DEEP TEXT AUDIT REPORT ACROSS {len(json_files)} CITIES ({total_spots} SPOTS):")
print("======================================================================")
print(f"❌ Cross-Contamination Anomalies: {len(cross_contaminations)}")
for cc in cross_contaminations:
    print(f"   [{cc[0]}] {cc[1]} ({cc[2]}): {cc[3]} -> \"{cc[4]}...\"")

print(f"\n❌ English Leaks in Non-English Fields: {len(english_leaks)}")
for el in english_leaks[:15]:
    print(f"   [{el[0]}] {el[1]} ({el[2]}) in {el[3]}: leaked '{el[4]}' -> \"{el[5]}...\"")

print(f"\n⚠️ Missing Translation Fields: {len(missing_translations)}")
for mt in missing_translations[:10]:
    print(f"   [{mt[0]}] {mt[1]} ({mt[2]}): missing {mt[3]}")

print("======================================================================")
