import os
import json
import glob
import time
import urllib.request
import urllib.parse
import ssl

ctx = ssl._create_unverified_context()

def translate_text(text, target_lang):
    if not text or not text.strip():
        return text
    if target_lang == 'en':
        return text
    try:
        url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=' + target_lang + '&dt=t&q=' + urllib.parse.quote(text)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx, timeout=8)
        data = json.loads(res.read().decode('utf-8'))
        translated_chunks = []
        if data and data[0]:
            for chunk in data[0]:
                if chunk and chunk[0]:
                    translated_chunks.append(chunk[0])
        result = "".join(translated_chunks)
        return result if result else text
    except Exception as e:
        print(f"Error translating '{text[:20]}...' to {target_lang}: {e}")
        return text

city_files = glob.glob('data/cities/*.json')
print(f"Found {len(city_files)} city JSON files.")

target_languages = ['ja', 'es', 'zh', 'fr', 'de']

total_spots = 0

for file_path in sorted(city_files):
    print(f"\nProcessing {os.path.basename(file_path)}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    spots = data.get('spots', [])
    city_name = data.get('cityName', '')

    for spot in spots:
        total_spots += 1
        spot_name = spot.get('name', '')
        spot_desc = spot.get('desc', '')
        spot_price = spot.get('price', '')
        spot_tip = spot.get('tip_en', '') or spot.get('tip_ja', '') or "Best visited during golden hour for fewer crowds."

        # Ensure base EN fields
        spot['name_en'] = spot.get('name_en') or spot_name
        spot['desc_en'] = spot.get('desc_en') or spot_desc
        spot['price_en'] = spot.get('price_en') or spot_price
        spot['tip_en'] = spot_tip

        # Check and translate into JA, ES, ZH, FR, DE
        for lang in target_languages:
            # 1. Translate Description if missing or equals English
            current_desc = spot.get(f'desc_{lang}', '')
            if not current_desc or current_desc == spot_desc or current_desc == spot.get('desc_en', ''):
                translated_desc = translate_text(spot_desc, lang)
                spot[f'desc_{lang}'] = translated_desc
                time.sleep(0.05)

            # 2. Translate Spot Name if missing or equals English
            current_name = spot.get(f'name_{lang}', '')
            if not current_name or current_name == spot_name:
                translated_name = translate_text(spot_name, lang)
                spot[f'name_{lang}'] = translated_name
                time.sleep(0.05)

            # 3. Translate Price if missing or equals English
            current_price = spot.get(f'price_{lang}', '')
            if not current_price or current_price == spot_price:
                translated_price = translate_text(spot_price, lang)
                spot[f'price_{lang}'] = translated_price
                time.sleep(0.05)

            # 4. Translate Tip if missing
            current_tip = spot.get(f'tip_{lang}', '')
            if not current_tip or (lang != 'ja' and current_tip == spot.get('tip_ja', '')):
                translated_tip = translate_text(spot['tip_en'], lang)
                spot[f'tip_{lang}'] = translated_tip
                time.sleep(0.05)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {os.path.basename(file_path)} ({len(spots)} spots)")

print(f"\nSuccessfully translated all {total_spots} spots across 13 cities!")
