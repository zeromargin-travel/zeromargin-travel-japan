import os
import json
import glob

city_files = sorted(glob.glob('data/cities/*.json'))
print(f"Refining tags & prices across {len(city_files)} city JSON files...")

# Pure cafe/dining keywords to exclude from shopping
cafe_terms = ['café', 'cafe', 'bistro', 'restaurant', 'bakery', 'tea room', 'bar', 'coffee', 'dining']

# Strictly outdoor keywords to EXCLUDE from rain
outdoor_terms = [
    'bridge', 'pont', 'brücke', 'brug', 'park', 'jardin', 'garden', 'square', 'plaza', 'place',
    'promenade', 'walk', 'quay', 'quai', 'canal', 'river', 'cruise', 'viewpoint', 'panorama',
    'cemetery', 'citi-zone', 'outdoor', 'fountain', 'monument', 'statue', 'boulevard', 'avenue'
]

for fpath in city_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    spots = data.get('spots', [])

    for s in spots:
        cat = (s.get('category') or '').lower()
        name = (s.get('name') or '').lower()
        name_en = (s.get('name_en') or '').lower()
        name_ja = (s.get('name_ja') or '').lower()
        desc = (s.get('desc') or '').lower()
        desc_en = (s.get('desc_en') or '').lower()
        desc_ja = (s.get('desc_ja') or '').lower()
        price = (s.get('price') or '').lower()
        price_ja = (s.get('price_ja') or '')

        text = f"{cat} {name} {name_en} {desc} {desc_en}"

        # -------------------------------------------------------------
        # 1. REFINED SHOPPING TAG
        # Exclude pure cafes/dining unless explicitly market/shopping/passage/department store
        # -------------------------------------------------------------
        is_pure_cafe = any(c in cat for c in ['café', 'cafe', 'bistro']) and not any(m in text for m in ['market', 'marché', 'passage', 'store', 'boutique', 'shopping'])
        
        shop_match = any(w in text for w in [
            'department store', 'lafayette', 'bon marché', 'passage', 'galerie', 'boutique',
            'flea market', 'fleamarket', 'marché', 'marche', 'viktualienmarkt', 'waterlooplein',
            'bazaar', 'bazar', 'bouquinistes', 'gourmet hall', 'ka-de-we', 'kadewe', 'shopping',
            'souvenir shop', 'chocolatier', 'fashion'
        ])

        is_shopping = shop_match and not is_pure_cafe

        # -------------------------------------------------------------
        # 2. REFINED RAIN TAG (Indoor / Covered Only)
        # Exclude bridges, parks, outdoor squares, open promenades, cemeteries, cruises
        # -------------------------------------------------------------
        is_outdoor = any(o in text for o in outdoor_terms) and not any(inc in text for inc in ['museum', 'basilica', 'cathedral', 'church', 'passage', 'galerie', 'covered', 'indoor'])

        indoor_match = any(w in text for w in [
            'museum', 'art gallery', 'basilica', 'cathedral', 'church', 'chapel', 'pantheon',
            'passage', 'galerie', 'arcade', 'department store', 'lafayette', 'bon marché',
            'opera', 'theatre', 'indoor', 'domed', 'mausoleum', 'aquarium', 'hall', 'cellar'
        ]) or ('museum' in cat)

        is_rain = indoor_match and not is_outdoor

        # -------------------------------------------------------------
        # 3. REFINED FREE TAG & HYBRID PRICE LOCALIZATION
        # -------------------------------------------------------------
        is_100_free = any(p in price for p in ['free', '無料', '0€', '€0', 'gratuit', 'gratis', 'kostenlos']) or \
                      any(k in text for k in ['public park', 'city square', 'promenade', 'free entry', 'bridge', 'viewpoint', 'free access'])

        # Check for hybrid spots (free grounds/park/courtyard, but paid tower/museum/ticket)
        has_paid_ticket = ('€' in price or 'ticket' in price or 'entry' in price or '入場' in price or '見学' in price) and not is_100_free
        has_free_grounds = any(k in text for k in ['park', 'garden', 'jardin', 'parc', 'square', 'plaza', 'place', 'courtyard', 'parvis', 'exterior', 'grounds', 'cathedral', 'basilica'])

        if is_100_free:
            is_free = True
            s['price_ja'] = "入場無料"
            s['price_en'] = "Free Entry"
            s['price'] = "Free Entry"
        elif has_paid_ticket and has_free_grounds:
            is_free = True
            # Format explicit hybrid pricing in Japanese and English
            # Extract numerical fee if available
            import re
            m = re.search(r'€\s*\d+([.,]\d+)?', price)
            euro_val = m.group(0) if m else "有料"

            if 'park' in text or 'garden' in text or 'jardin' in text or 'parc' in text:
                s['price_ja'] = f"庭園無料（館内: {euro_val}）"
                s['price_en'] = f"Free Gardens (Interior: {euro_val})"
            elif 'square' in text or 'plaza' in text or 'place' in text or 'courtyard' in text or 'parvis' in text:
                s['price_ja'] = f"広場・外観無料（有料区域: {euro_val}）"
                s['price_en'] = f"Free Plaza & Exterior (Inside: {euro_val})"
            else:
                s['price_ja'] = f"敷地無料（展望/館内: {euro_val}）"
                s['price_en'] = f"Free Grounds (Ticket: {euro_val})"
        else:
            is_free = False
            # Ensure price_ja has proper prefix
            if not price_ja or price_ja == price:
                import re
                m = re.search(r'€\s*\d+([.,]\d+)?', price)
                euro_val = m.group(0) if m else price
                s['price_ja'] = f"チケット: {euro_val}"
                s['price_en'] = f"Entry: {euro_val}"

        s['rain'] = bool(is_rain)
        s['shopping'] = bool(is_shopping)
        s['free'] = bool(is_free)

    data['spots'] = spots
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f" ✅ Refined {fname} ({len(spots)} spots)")

print("\n🎉 TAG & PRICE REFINEMENT FINISHED SUCCESSFULLY ACROSS ALL 13 CITIES!")
