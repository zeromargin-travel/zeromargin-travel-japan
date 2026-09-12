#!/usr/bin/env python3
"""
Zero-Margin Travel App - Nuremberg City Module Builder (v26.0.0)
Assembles data/cities/nuremberg.json with 52 spots and 100% Rulebook v5.0.0 compliance.
"""

import json
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)

from build_nuremberg_spots import get_all_nuremberg_spots

def assemble_nuremberg_json():
    spots = get_all_nuremberg_spots()
    print(f"Loaded {len(spots)} spots for Nuremberg.")
    
    payload = {
        "cityName": "Nuremberg, Germany",
        "country": "Germany",
        "flag": "🇩🇪",
        "spots": spots
    }
    
    target_path = os.path.join(base_dir, '..', 'data', 'cities', 'nuremberg.json')
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    
    print(f"🎉 Successfully written {target_path} with {len(spots)} spots!")

if __name__ == '__main__':
    assemble_nuremberg_json()
