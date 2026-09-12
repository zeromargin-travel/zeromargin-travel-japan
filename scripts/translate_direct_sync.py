import os
import json
import glob
import time
import requests

def translate_str(text, target_lang):
    if not text or not text.strip() or target_lang == 'en':
        return text
    t_code = 'zh-CN' if target_lang == 'zh' else target_lang
    url = 'https://translate.googleapis.com/translate_a/single'
    params = {'client': 'gtx', 'sl': 'en', 'tl': t_code, 'dt': 't', 'q': text}
    headers = {'User-Agent': 'Mozilla/5.0'}
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, headers=headers, timeout=5)
            if r.status_code == 200:
                data = r.json()
                if data and data[0]:
                    chunks = [c[0] for c in data[0] if c and c[0]]
                    out = "".join(chunks).strip()
                    if out:
                        return out
        except Exception:
            pass
        time.sleep(0.1)
    return text

city_files = glob.glob('data/cities/*.json')
print(f"Translating {len(city_files)} city JSON files synchronously...")

langs = ['ja', 'es', 'zh', 'fr', 'de']

for fpath in sorted(city_files):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    spots = data.get('spots', [])
    for s in spots:
        base_desc = s.get('desc', '') or s.get('desc_en', '')
        base_name = s.get('name', '') or s.get('name_en', '')
        base_price = s.get('price', '') or s.get('price_en', '')
        base_tip = s.get('tip_en', '') or s.get('tip_ja', '') or "Best visited early morning to avoid crowds."

        s['desc_en'] = base_desc
        s['name_en'] = base_name
        s['price_en'] = base_price
        s['tip_en'] = base_tip

        for l in langs:
            s[f'desc_{l}'] = translate_str(base_desc, l)
            s[f'name_{l}'] = translate_str(base_name, l)
            s[f'price_{l}'] = translate_str(base_price, l)
            s[f'tip_{l}'] = translate_str(base_tip, l)

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved {fname}")

print("Sync Translation Complete!")
