import json
import glob
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
city_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))

print("🚀 Starting Night Spots Scope annotation across all cities...")

total_spots = 0
night_spots_count = 0

for fpath in city_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    spots = data.get('spots', []) if isinstance(data, dict) else data
    
    for s in spots:
        total_spots += 1
        raw_cat = str(s.get('category', '')).strip().lower()
        name_text = (str(s.get('name', '')) + ' ' + str(s.get('name_ja', '')) + ' ' + str(s.get('name_en', ''))).lower()
        desc_text = (str(s.get('desc_ja', '')) + ' ' + str(s.get('desc_en', ''))).lower()
        full_text = name_text + ' ' + desc_text + ' ' + raw_cat

        # Check Night Spot qualifications
        is_night = (
            s.get('night') is True or
            'night' in raw_cat or
            any(k in full_text for k in [
                '夜景', 'バー', '居酒屋', 'ビアホール', '醸造所', 'パブ', 'キャバレー',
                'イルミネーション', 'ライトアップ', '夜間', 'ナイト', 'ディナー', '夕食',
                'エッフェル', '凱旋門', 'サクレクール', '運河クルーズ', 'クルーズ',
                'bar', 'pub', 'brewery', 'night', 'cabaret', 'jazz', 'dinner',
                'illuminat', 'sunset', '夕日', 'カジノ', 'casino'
            ])
        )

        s['is_night_spot'] = is_night
        if is_night:
            night_spots_count += 1
            if 'categories' in s and isinstance(s['categories'], list):
                if 'Night' not in s['categories']:
                    s['categories'].append('Night')

    if isinstance(data, dict):
        data['spots'] = spots
    else:
        data = spots

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print(f"🎉 Night Spots Scope annotation complete: {night_spots_count} / {total_spots} spots ({night_spots_count/total_spots*100:.1f}%) annotated as is_night_spot!")
