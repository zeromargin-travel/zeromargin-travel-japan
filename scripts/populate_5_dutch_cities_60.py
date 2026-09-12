#!/usr/bin/env python3
"""
Zero-Margin Travel App - Dutch 300 Generator Script (v33.0.0)
Populates 60 spots per city across Amsterdam, Rotterdam, The Hague, Utrecht, Maastricht.
"""

import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

def build_city_file(fname, city_en, country_en, city_ja, country_ja, spots_data):
    path = os.path.join(cities_dir, fname)
    obj = {
        "city": city_en,
        "country": country_en,
        "city_ja": city_ja,
        "country_ja": country_ja,
        "spots": spots_data
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
    print(f"🎉 Successfully built {fname} ({len(spots_data)} spots)")

print("Populator ready...")
