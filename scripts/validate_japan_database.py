#!/usr/bin/env python3
"""
zeromargin-travel-japan Database Compliance & Validation Script
Verifies spot data integrity, 0% overlap rule, coordinates, and categories.
"""
import os
import json
import glob
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

print("🌺 Validating zeromargin-travel-japan spot databases...")

city_files = glob.glob(os.path.join(cities_dir, 'okinawa.json'))
if not city_files:
    raise FileNotFoundError("okinawa.json not found in data/cities/")

total_spots = 0
violations = []

for cfile in city_files:
    fname = os.path.basename(cfile)
    with open(cfile, 'r', encoding='utf-8') as f:
        spots = json.load(f)
    
    print(f" -> Checking {fname}: {len(spots)} spots")
    spot_ids = set()

    for s in spots:
        total_spots += 1
        sid = s.get('id', 'unknown')
        name_ja = s.get('name_ja', '')
        desc_ja = s.get('desc_ja', '')
        tip_ja = s.get('tip_ja', '')

        # 1. Unique ID check
        if sid in spot_ids:
            violations.append((fname, sid, name_ja, "Duplicate ID"))
        spot_ids.add(sid)

        # 2. Required fields
        if not name_ja:
            violations.append((fname, sid, name_ja, "Missing name_ja"))
        if not desc_ja or len(desc_ja) < 10:
            violations.append((fname, sid, name_ja, "desc_ja is empty or too short"))
        if not tip_ja or len(tip_ja) < 10:
            violations.append((fname, sid, name_ja, "tip_ja is empty or too short"))

        # 3. 0% Overlap Rule: tip must not just copy desc
        desc_clean = re.sub(r'[\s、。！？!?,.]', '', desc_ja)
        tip_clean = re.sub(r'[\s、。！？!?,.💡]', '', tip_ja)
        if len(desc_clean) > 0 and (desc_clean in tip_clean or tip_clean in desc_clean):
            violations.append((fname, sid, name_ja, "0% Overlap Violation: tip duplicates desc"))

        # 4. Valid Coordinates
        lat = s.get('lat')
        lng = s.get('lng')
        if not (isinstance(lat, (int, float)) and 24.0 <= lat <= 30.0):
            violations.append((fname, sid, name_ja, f"Invalid latitude for Okinawa: {lat}"))
        if not (isinstance(lng, (int, float)) and 122.0 <= lng <= 132.0):
            violations.append((fname, sid, name_ja, f"Invalid longitude for Okinawa: {lng}"))

        # 5. LocationZone
        zone = s.get('locationZone')
        if zone not in ('city', 'suburban'):
            violations.append((fname, sid, name_ja, f"Invalid locationZone: {zone}"))

        # 6. Categorical Integrity Guard (Kids & Shopping must not over-flag non-shopping venues)
        if s.get('shopping') is True:
            cat = str(s.get('category', '')).lower()
            # Natural landmarks, capes, beaches, bridges must not be shopping
            if any(k in cat for k in ['nature', 'scenery', 'marine', 'park']) and not any(k in cat for k in ['shopping', 'market']):
                violations.append((fname, sid, name_ja, f"Categorical conflict: Natural venue flagged as shopping=True"))

if violations:
    print("\n❌ VALIDATION DEFECTS FOUND:")
    for v in violations:
        print(f"   [{v[0]}] {v[1]} ({v[2]}) -> {v[3]}")
    exit(1)
else:
    print(f"\n🛡️ 6-LAYER COMPLIANCE GUARD PASSED: All {total_spots} spots in Okinawa pass quality & integrity checks!")
