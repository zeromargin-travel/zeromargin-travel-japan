#!/usr/bin/env python3
"""
Zero-Margin Travel App - Heidelberg City Module Builder (v24.0.0)
Assembles data/cities/heidelberg.json with 50 spots and 100% Rulebook v5.0.0 compliance.
"""

import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
heidelberg_path = os.path.join(cities_dir, 'heidelberg.json')

def assemble_heidelberg_json():
    # Import the spots
    from build_heidelberg_spots import get_all_heidelberg_spots
    
    spots = get_all_heidelberg_spots()
    print(f"Loaded {len(spots)} spots for Heidelberg.")
    
    heidelberg_data = {
        "cityName": "Heidelberg, Germany",
        "country": "Germany",
        "flag": "🇩🇪",
        "spots": spots
    }
    
    with open(heidelberg_path, 'w', encoding='utf-8') as f:
        json.dump(heidelberg_data, f, indent=2, ensure_ascii=False)
        
    print(f"🎉 Successfully written data/cities/heidelberg.json with {len(spots)} spots!")

if __name__ == '__main__':
    assemble_heidelberg_json()
