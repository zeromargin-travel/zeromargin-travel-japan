#!/usr/bin/env python3
"""
Zero-Margin Travel App - Complete Dutch 300 Spots Data Compiler (v33.0.0)
Populates 60 spots for Amsterdam, 60 for Rotterdam, 60 for The Hague, 60 for Utrecht, 60 for Maastricht.
"""

import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

def build_city_json(fname, city_name, country_name, city_ja, country_ja, spots_list):
    filepath = os.path.join(cities_dir, fname)
    data = {
        "city": city_name,
        "country": country_name,
        "city_ja": city_ja,
        "country_ja": country_ja,
        "spots": spots_list
    }
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"🎉 Created {fname} with {len(spots_list)} spots!")

print("Compiler script initialized...")
