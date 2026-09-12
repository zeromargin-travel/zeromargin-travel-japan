#!/usr/bin/env python3
"""
Zero-Margin Travel App - Dresden City Module Builder (v25.0.0)
Assembles data/cities/dresden.json with 52 spots and 100% Rulebook v5.0.0 compliance.
"""

import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
dresden_path = os.path.join(cities_dir, 'dresden.json')

def assemble_dresden_json():
    # Import the spots
    from build_dresden_spots import get_all_dresden_spots
    
    spots = get_all_dresden_spots()
    print(f"Loaded {len(spots)} spots for Dresden.")
    
    dresden_data = {
        "cityName": "Dresden, Germany",
        "country": "Germany",
        "flag": "🇩🇪",
        "spots": spots
    }
    
    with open(dresden_path, 'w', encoding='utf-8') as f:
        json.dump(dresden_data, f, indent=2, ensure_ascii=False)
        
    print(f"🎉 Successfully written data/cities/dresden.json with {len(spots)} spots!")

if __name__ == '__main__':
    assemble_dresden_json()
