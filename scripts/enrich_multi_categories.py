import json
import glob
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
city_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))

print("🚀 Starting Multi-Category Array Annotation across all cities...")

total_spots = 0
category_counts = {}

for fpath in city_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    spots = data.get('spots', []) if isinstance(data, dict) else data
    
    for s in spots:
        total_spots += 1
        raw_cat = str(s.get('category', '')).strip()
        name_text = (str(s.get('name', '')) + ' ' + str(s.get('name_ja', '')) + ' ' + str(s.get('name_en', ''))).lower()
        desc_text = (str(s.get('desc_ja', '')) + ' ' + str(s.get('desc_en', ''))).lower()
        full_text = name_text + ' ' + desc_text + ' ' + raw_cat.lower()

        cats = set()

        # Base category mapping
        if 'landmark' in raw_cat.lower():
            cats.add('Landmark')
        if 'museum' in raw_cat.lower() or 'gallery' in raw_cat.lower() or 'art' in raw_cat.lower():
            cats.add('Museum')
        if any(k in raw_cat.lower() for k in ['café', 'bistro', 'restaurant', 'dining', 'bakery']):
            cats.add('Café')
        if 'scenery' in raw_cat.lower() or 'walk' in raw_cat.lower():
            cats.add('Scenery')
        if 'kids' in raw_cat.lower() or s.get('kids') is True:
            cats.add('Kids')
        if 'shopping' in raw_cat.lower() or s.get('shopping') is True:
            cats.add('Shopping')

        # Keyword enrichment rules
        # Landmark
        if any(k in full_text for k in ['大聖堂', '教会', '城', '広場', '要塞', '宮殿', '門', '世界遺産', '遺跡', '塔', 'cathedral', 'church', 'castle', 'palace', 'square', 'tower', 'basilica']):
            cats.add('Landmark')

        # Museum
        if any(k in full_text for k in ['美術館', '博物館', '科学館', 'プラネタリウム', '画廊', '記念館', '展示', 'museum', 'gallery', 'exhibition']):
            cats.add('Museum')

        # Café & Dining
        if any(k in full_text for k in ['カフェ', 'ビストロ', 'レストラン', 'ベーカリー', 'パティスリー', '地ビール', '醸造所', 'ビアホール', 'パブ', 'バー', 'ショコラ', 'cafe', 'bistro', 'restaurant', 'bakery', 'patisserie', 'brewery', 'pub', 'bar']):
            cats.add('Café')

        # Scenery & Walk
        if any(k in full_text for k in ['公園', '庭園', 'プロムナード', '運河', '散策', '展望', '通り', '海岸', 'ビーチ', '動物園', '水族館', '遊歩道', 'park', 'garden', 'promenade', 'canal', 'beach', 'zoo', 'aquarium']):
            cats.add('Scenery')

        # Kids & Family
        if s.get('kids') is True or any(k in full_text for k in ['動物園', '水族館', 'レゴ', 'おもちゃ', '公園', 'テーマパーク', '遊園地', '子供', 'キッズ', 'ファミリー', 'ミッフィー', 'zoo', 'aquarium', 'planetarium', 'amusement', 'kids', 'family', 'toy']):
            cats.add('Kids')

        # Shopping
        if s.get('shopping') is True or any(k in full_text for k in ['ショッピング', 'デパート', '市場', 'マルシェ', '蚤の市', 'モール', 'アウトレット', 'アーケード', 'ブティック', '買い物', '買物', 'shopping', 'market', 'mall', 'outlet', 'bazaar', 'store', 'boutique']):
            cats.add('Shopping')

        # Night Spots
        if s.get('night') is True or any(k in full_text for k in ['夜景', 'バー', '居酒屋', 'ビアホール', '醸造所', 'パブ', 'キャバレー', 'イルミネーション', 'ライトアップ', '夜間', 'ナイト', 'bar', 'pub', 'brewery', 'night', 'cabaret', 'jazz', 'illuminat']):
            cats.add('Night')

        # Guarantee at least 1 category
        if not cats:
            cats.add('Landmark')

        cat_list = sorted(list(cats))
        s['categories'] = cat_list

        for c in cat_list:
            category_counts[c] = category_counts.get(c, 0) + 1

    if isinstance(data, dict):
        data['spots'] = spots
    else:
        data = spots

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print(f"🎉 Multi-Category Array annotation complete for {total_spots} spots across {len(city_files)} cities!")
print("\n=== Category Coverage Summary ===")
for c, cnt in sorted(category_counts.items(), key=lambda x: -x[1]):
    print(f"  {c:<15}: {cnt} spots ({cnt/total_spots*100:.1f}%)")
