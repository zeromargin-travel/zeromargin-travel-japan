#!/usr/bin/env python3
"""
Deep System-Wide Audit Script for Mismatched Tips & Generic Placeholders
Scan all 15 city JSON files (670 spots) for:
1. Mismatched/Swapped Tips (e.g. Louvre tip on Arc de Triomphe)
2. Generic Duplicate Placeholders ("早朝またはゴールデンアワーに...")
3. Text Overlaps between desc and tip
"""

import glob
import json
import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
json_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))

GENERIC_PLACEHOLDERS = [
    "素晴らしい写真を撮り",
    "混雑が少ない早朝またはゴールデンアワー",
    "早朝またはゴールデンアワー",
    "best time to visit is early morning",
    "take great photos"
]

mismatches = []
duplicates = []
overlaps = []

total_spots = 0

for jf in json_files:
    fname = os.path.basename(jf)
    with open(jf, 'r', encoding='utf-8') as f:
        data = json.load(f)

    city_name = data.get('cityName', fname)
    spots = data.get('spots', [])
    total_spots += len(spots)

    city_tips = {}

    for s in spots:
        sid = s.get('id', '')
        name = s.get('name', '')
        desc = s.get('desc_ja', '') or s.get('desc', '')
        tip = s.get('tip_ja', '') or s.get('tip', '')

        # 1. Check generic placeholder
        if any(p.lower() in tip.lower() for p in GENERIC_PLACEHOLDERS):
            duplicates.append((city_name, sid, name, "GENERIC_PLACEHOLDER", tip))

        # 2. Check mismatched tips (e.g. Arc de Triomphe having Louvre tip)
        if "Arc de Triomphe" in name and ("ルーブル" in tip or "ピラミッド" in tip or "Pyramid" in tip or "Louvre" in tip):
            mismatches.append((city_name, sid, name, "MISMATCHED_LOUVRE_TIP", tip))

        # 3. Check exact duplicates within city
        if tip and len(tip) > 15:
            if tip in city_tips:
                duplicates.append((city_name, sid, name, f"DUPLICATE_WITH_{city_tips[tip]}", tip))
            else:
                city_tips[tip] = sid

        # 4. Check overlap between desc and tip
        if desc and tip and len(desc) > 10:
            # Overlap check
            words_desc = set(re.findall(r'\w+', desc.lower()))
            words_tip = set(re.findall(r'\w+', tip.lower()))
            common = words_desc.intersection(words_tip)
            if len(common) > 10 and not any(k in tip for k in ['🎟️', '📸', '👕', '🍽️', '💡']):
                overlaps.append((city_name, sid, name, "TEXT_OVERLAP", desc, tip))

print("======================================================================")
print(f"📊 SYSTEM-WIDE AUDIT REPORT ACROSS {len(json_files)} CITIES ({total_spots} SPOTS):")
print("======================================================================")
print(f"❌ Mismatched/Swapped Tips Found: {len(mismatches)}")
for m in mismatches:
    print(f"   [{m[0]}] {m[1]} ({m[2]}): {m[3]} -> \"{m[4][:60]}...\"")

print(f"\n⚠️ Generic Duplicate Placeholders Found: {len(duplicates)}")
for d in duplicates[:15]:
    print(f"   [{d[0]}] {d[1]} ({d[2]}): {d[3]}")
if len(duplicates) > 15:
    print(f"   ... and {len(duplicates) - 15} more duplicates.")

print(f"\n⚠️ Desc vs Tip Text Overlaps Found: {len(overlaps)}")
for o in overlaps[:10]:
    print(f"   [{o[0]}] {o[1]} ({o[2]}): {o[3]}")
print("======================================================================")
