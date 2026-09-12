import json
import re

def main():
    path = '/Users/jnabi1/Desktop/アプリ開発/旅行ツールアプリ版/js/ai-travel-engine.js'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate candidateSpotsDatabase
    m = re.search(r'const candidateSpotsDatabase = (\{.*?\n\};)', content, re.DOTALL)
    if not m:
        print("ERROR: candidateSpotsDatabase not found in ai-travel-engine.js")
        return

    db_str = m.group(1)[:-1] # strip trailing semicolon
    db = json.loads(db_str)

    def is_food_or_cafe(spot):
        cat = spot.get('category', '')
        desc = (spot.get('name_en', '') + ' ' + spot.get('name_ja', '') + ' ' + spot.get('desc_en', '') + ' ' + spot.get('desc_ja', '')).lower()
        if any(k in cat for k in ['Café', 'Bistro', 'Dining', 'Restaurant', 'Bakery']):
            return True
        if any(k in desc for k in ['カフェ', 'ビストロ', '老舗食堂', 'ベーカリー', 'ビアホール', '醸造所', 'パブ', 'bistro', 'brasserie', 'bakery', 'cafe', 'café', 'restaurant']):
            return True
        return False

    def is_cafe(spot):
        cat = spot.get('category', '')
        desc = (spot.get('name_en', '') + ' ' + spot.get('name_ja', '') + ' ' + spot.get('desc_en', '') + ' ' + spot.get('desc_ja', '')).lower()
        if 'bakery' in cat.lower() or 'ベーカリー' in desc or 'apple pie' in desc or 'ショコラ' in desc or 'パティスリー' in desc or 'patisserie' in desc:
            return True
        if 'café' in cat.lower() or 'カフェ' in desc or '喫茶' in desc or 'cafe' in desc:
            return True
        return False

    total_top7 = 0
    total_hidden = 0

    for city_name, spots in db.items():
        food_spots = [s for s in spots if is_food_or_cafe(s)]
        cafes = [s for s in food_spots if is_cafe(s)]
        restaurants = [s for s in food_spots if not is_cafe(s)]
        
        # If cafes or restaurants array is sparse, fallback to using food_spots
        if not cafes:
            cafes = food_spots[:1]
        if not restaurants:
            restaurants = food_spots[1:2] if len(food_spots) > 1 else food_spots[:1]

        sights = [s for s in spots if s not in food_spots]

        # Top7 Selection: 5 Sights + 1 Cafe + 1 Restaurant
        top7_sights = sights[:5]
        top7_cafe = cafes[:1]
        top7_rest = restaurants[:1] if restaurants[0:1] != top7_cafe else restaurants[1:2]

        top7_set = set()
        for s in top7_sights + top7_cafe + top7_rest:
            if s:
                top7_set.add(s['id'])

        # Guarantee exactly 7 top7 spots if len < 7
        if len(top7_set) < 7:
            for s in spots:
                if s['id'] not in top7_set:
                    top7_set.add(s['id'])
                    if len(top7_set) == 7:
                        break

        # HiddenGems Selection: 3 Hidden Sights + 1 Hidden Cafe + 1 Hidden Restaurant (excluding top7)
        remaining_sights = [s for s in sights if s['id'] not in top7_set]
        remaining_cafes = [s for s in cafes if s['id'] not in top7_set]
        remaining_rests = [s for s in restaurants if s['id'] not in top7_set]

        # Pick 3 hidden sights from mid-to-latter portion of remaining list (authentic off-the-beaten-path)
        hidden_sights = remaining_sights[len(remaining_sights)//4 : len(remaining_sights)//4 + 3]
        if len(hidden_sights) < 3:
            hidden_sights = remaining_sights[:3]

        hidden_cafe = remaining_cafes[:1] if remaining_cafes else remaining_sights[3:4]
        hidden_rest = remaining_rests[:1] if remaining_rests else remaining_sights[4:5]

        hidden_set = set()
        for s in hidden_sights + hidden_cafe + hidden_rest:
            if s and s['id'] not in top7_set:
                hidden_set.add(s['id'])

        # Ensure between 3 and 5 hidden gems
        if len(hidden_set) < 3:
            for s in spots:
                if s['id'] not in top7_set and s['id'] not in hidden_set:
                    hidden_set.add(s['id'])
                    if len(hidden_set) >= 3:
                        break

        # Apply flags to spots
        for s in spots:
            sp_id = s['id']
            s['top7'] = (sp_id in top7_set)
            s['hiddenGem'] = (sp_id in hidden_set)

        c_top = sum(1 for s in spots if s['top7'])
        c_hid = sum(1 for s in spots if s['hiddenGem'])
        total_top7 += c_top
        total_hidden += c_hid
        print(f"City '{city_name}': Top7={c_top}, HiddenGems={c_hid}, Total={len(spots)}")

    print(f"\nCompleted! Total Top7: {total_top7}, Total HiddenGems: {total_hidden}")

    # Re-serialize database back into content
    new_db_str = json.dumps(db, indent=2, ensure_ascii=False)
    new_content = content[:m.start(1)] + new_db_str + ';\n' + content[m.end(1):]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("Successfully updated js/ai-travel-engine.js with top7 and hiddenGem tags!")

if __name__ == '__main__':
    main()
