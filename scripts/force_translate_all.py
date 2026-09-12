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
        res = urllib.request.urlopen(req, context=ctx, timeout=10)
        data = json.loads(res.read().decode('utf-8'))
        translated_chunks = []
        if data and data[0]:
            for chunk in data[0]:
                if chunk and chunk[0]:
                    translated_chunks.append(chunk[0])
        result = "".join(translated_chunks)
        return result if result else text
    except Exception as e:
        print(f"Error translating '{text[:20]}' to {target_lang}: {e}")
        return text

city_files = glob.glob('data/cities/*.json')
print(f"Found {len(city_files)} city JSON files.")

target_languages = ['ja', 'es', 'zh', 'fr', 'de']

for file_path in sorted(city_files):
    print(f"\nProcessing {os.path.basename(file_path)}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    spots = data.get('spots', [])

    for idx, spot in enumerate(spots):
        spot_name = spot.get('name', '')
        spot_desc = spot.get('desc', '') or spot.get('desc_en', '')
        spot_price = spot.get('price', '') or spot.get('price_en', '')

        # Unconditionally translate desc into JA, ES, ZH, FR, DE
        for lang in target_languages:
            cur_desc = spot.get(f'desc_{lang}', '')
            # If current description is English or missing
            if not cur_desc or cur_desc == spot_desc or cur_desc == spot.get('desc_en', '') or any(w in cur_desc.lower() for w in ['iconic', 'tower', 'offering', 'panoramic', 'cathedral', 'museum', 'palace', 'famed', 'century', 'park', 'fountain', 'mausoleum', 'sculpture']):
                trans_desc = translate_text(spot_desc, lang)
                spot[f'desc_{lang}'] = trans_desc
                time.sleep(0.02)

            cur_price = spot.get(f'price_{lang}', '')
            if not cur_price or cur_price == spot_price or any(w in cur_price for w in ['Tickets:', 'Entry:', 'Rooftop:', 'Self-tour:', 'Free access', 'Free entry', 'Mains:', 'Hot Choc:', 'Pastries:']):
                trans_price = translate_text(spot_price, lang)
                spot[f'price_{lang}'] = trans_price
                time.sleep(0.02)

            cur_name = spot.get(f'name_{lang}', '')
            if not cur_name or cur_name == spot_name:
                trans_name = translate_text(spot_name, lang)
                spot[f'name_{lang}'] = trans_name
                time.sleep(0.02)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Done {os.path.basename(file_path)} ({len(spots)} spots)")

print("\nFinished translating all city spots!")
