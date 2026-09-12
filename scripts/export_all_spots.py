#!/usr/bin/env python3
"""
Zero-Margin Travel App - Consolidated Database Exporter
Consolidates all 18 city JSON files into a single master all_spots_database.json
"""

import os
import json
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
target_file = os.path.join(base_dir, '..', 'data', 'all_spots_database.json')

city_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))

master_db = {}
total_spots = 0

for fpath in city_files:
    fname = os.path.basename(fpath)
    city_key = fname.replace('.json', '')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, dict):
        city_name = data.get('cityName', city_key.title())
        spots = data.get('spots', [])
    elif isinstance(data, list):
        city_name = city_key.title()
        spots = data
    else:
        spots = []
        
    master_db[city_name] = spots
    total_spots += len(spots)
    print(f"Loaded {city_name}: {len(spots)} spots")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(master_db, f, indent=2, ensure_ascii=False)

print(f"\n🎉 Successfully exported consolidated database to {target_file}!")
print(f"Total Cities: {len(master_db)}, Total Spots: {total_spots}")
