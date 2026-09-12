import json
import os
import re

# =========================================================================
# 0 Margin Travel - Database Build Script (For test2 environment)
# =========================================================================
# This script reads the single master source of truth (master_spots.json)
# and automatically splits it into lightweight, high-performance files 
# (e.g. paris.json) for the browser to fetch dynamically.
# =========================================================================

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
master_file = os.path.join(base_dir, 'data', 'master_spots.json')
output_dir = os.path.join(base_dir, 'data', 'cities')

def build_database():
    print(f"Reading master database from: {master_file}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    with open(master_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    cities_processed = 0
    total_spots = 0

    for city_id, spots in data.items():
        # city_id looks like "Paris, France" or "Luxembourg City, Luxembourg"
        city_only = city_id.split(',')[0].strip().lower()
        safe_name = re.sub(r'\s+', '_', city_only) + '.json'
        
        output_path = os.path.join(output_dir, safe_name)
        
        # Write the minified JSON file for maximum performance
        with open(output_path, 'w', encoding='utf-8') as out_f:
            json.dump(spots, out_f, ensure_ascii=False, separators=(',', ':'))
            
        cities_processed += 1
        total_spots += len(spots)
        print(f"  ✓ Built {safe_name} ({len(spots)} spots)")

    print(f"\n✅ Build Complete! Successfully generated {cities_processed} city files containing {total_spots} total spots.")
    print(f"Output location: {output_dir}")

if __name__ == '__main__':
    build_database()
