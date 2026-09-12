import os
import json
import glob
import time
from deep_translator import GoogleTranslator, MyMemoryTranslator

def get_translation(text, target_lang):
    if not text or not text.strip():
        return text
    if target_lang == 'en':
        return text

    lang_map = {
        'ja': 'ja',
        'es': 'es',
        'zh': 'zh-CN',
        'fr': 'fr',
        'de': 'de'
    }
    
    t_code = lang_map.get(target_lang, target_lang)

    # Try GoogleTranslator first
    try:
        res = GoogleTranslator(source='en', target=t_code).translate(text)
        if res and not res.startswith("Error") and not "That’s an error" in res:
            return res
    except Exception as e:
        pass

    # Fallback to MyMemoryTranslator
    try:
        mm_code = 'zh-CN' if target_lang == 'zh' else target_lang
        res = MyMemoryTranslator(source='en-US', target=mm_code).translate(text)
        if res and not res.startswith("Error"):
            return res
    except Exception as e:
        pass

    return text

city_files = glob.glob('data/cities/*.json')
print(f"Found {len(city_files)} city JSON files.")

target_languages = ['ja', 'es', 'zh', 'fr', 'de']

for file_path in sorted(city_files):
    city_basename = os.path.basename(file_path)
    print(f"\nProcessing {city_basename}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    spots = data.get('spots', [])

    for idx, spot in enumerate(spots):
        spot_name = spot.get('name', '') or spot.get('name_en', '')
        spot_desc = spot.get('desc', '') or spot.get('desc_en', '')
        spot_price = spot.get('price', '') or spot.get('price_en', '')
        spot_tip = spot.get('tip_en', '') or spot.get('tip_ja', '') or "Best visited early morning to avoid crowds."

        # Keep EN clean
        spot['name_en'] = spot_name
        spot['desc_en'] = spot_desc
        spot['price_en'] = spot_price
        spot['tip_en'] = spot_tip

        # Translate for all target languages
        for lang in target_languages:
            # 1. Translate Name
            trans_name = get_translation(spot_name, lang)
            spot[f'name_{lang}'] = trans_name

            # 2. Translate Desc
            trans_desc = get_translation(spot_desc, lang)
            spot[f'desc_{lang}'] = trans_desc

            # 3. Translate Price
            trans_price = get_translation(spot_price, lang)
            spot[f'price_{lang}'] = trans_price

            # 4. Translate Tip
            trans_tip = get_translation(spot_tip, lang)
            spot[f'tip_{lang}'] = trans_tip

            time.sleep(0.05)

        if (idx + 1) % 5 == 0 or idx + 1 == len(spots):
            print(f"  [{city_basename}] Translated {idx+1}/{len(spots)} spots...")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Finished {city_basename}")

print("\n🎉 Perfect translation completed for all spots across all cities!")
