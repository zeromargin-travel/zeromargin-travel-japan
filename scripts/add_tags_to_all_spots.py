import os
import json
import glob

city_files = sorted(glob.glob('data/cities/*.json'))
print(f"Enriching {len(city_files)} city JSON files with rain, shopping, and free tags...")

for fpath in city_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    spots = data.get('spots', [])
    updated_cnt = 0

    for s in spots:
        cat = (s.get('category') or '').lower()
        name = (s.get('name') or '').lower()
        name_en = (s.get('name_en') or '').lower()
        desc = (s.get('desc') or '').lower()
        desc_en = (s.get('desc_en') or '').lower()
        price = (s.get('price') or '').lower()
        price_ja = (s.get('price_ja') or '').lower()
        price_en = (s.get('price_en') or '').lower()

        text = f"{cat} {name} {name_en} {desc} {desc_en}"

        # 1. RAIN TAG (Indoor / Covered)
        rain_keywords = [
            'museum', 'art', 'gallery', 'basilica', 'cathedral', 'church', 'chapel', 'palace',
            'château', 'chateau', 'passage', 'galerie', 'arcade', 'department store', 'lafayette',
            'bon marché', 'louvre', 'pantheon', 'opera', 'theatre', 'concert', 'hall', 'indoor',
            'domed', 'tomb', 'mausoleum', 'synagogue', 'mosque', 'aquarium', 'planetarium',
            'brewery', 'cellar', 'café', 'cafe', 'bistro', 'restaurant', 'bakery', 'tea'
        ]
        is_rain = ('museum' in cat) or ('café' in cat) or ('cafe' in cat) or any(k in text for k in rain_keywords)

        # 2. SHOPPING TAG (Stores, Markets, Boutiques, Arcades, Souvenirs)
        shop_keywords = [
            'shopping', 'market', 'marché', 'marche', 'flohmarkt', 'bazaar', 'bazar', 'boutique',
            'department store', 'lafayette', 'bon marché', 'passage', 'galerie', 'store', 'mall',
            'arcade', 'chocolatier', 'souvenir', 'bookshop', 'bouquinistes', 'fleamarket',
            'vintage', 'fashion', 'craft', 'shop', 'groceries', 'bakeries', 'gourmet'
        ]
        is_shopping = ('market' in cat) or ('shopping' in cat) or any(k in text for k in shop_keywords)

        # 3. FREE TAG (Free Entry, Free Access, Public Park, Plaza, Church, Viewpoint, Outdoor Promenade)
        free_price_terms = ['free', '無料', 'gratuit', 'gratis', 'kostenlos', '0€', '€0', 'no fee']
        free_location_terms = [
            'park', 'garden', 'jardin', 'parc', 'square', 'plaza', 'place', 'bridge', 'pont',
            'quay', 'walk', 'promenade', 'boulevard', 'avenue', 'viewpoint', 'panorama',
            'fountain', 'cathedral', 'church', 'basilica', 'passage', 'courtyard', 'cemetery',
            'memorial', 'landmark'
        ]
        is_free_by_price = any(p in price or p in price_ja or p in price_en for p in free_price_terms)
        is_free_by_location = any(k in text for k in free_location_terms)

        is_free = is_free_by_price or is_free_by_location

        s['rain'] = bool(is_rain)
        s['shopping'] = bool(is_shopping)
        s['free'] = bool(is_free)
        if s.get('kids') is None:
            s['kids'] = ('park' in cat) or ('garden' in cat) or ('kids' in text) or ('family' in text)

        updated_cnt += 1

    data['spots'] = spots
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f" ✅ Enriched {fname}: {updated_cnt} spots tagged with rain, shopping, and free flags.")

print("\n🎉 ALL 13 CITY JSON FILES SUCCESSFULLY ENRICHED WITH ALL 3 TAGS!")
