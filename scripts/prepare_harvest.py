import json
import math
import os

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

def has_cjk(text):
    return any('\u3000' <= c <= '\u9fff' or '\uac00' <= c <= '\ud7a3' for c in text) if text else False

harvest_spots = []

for city, spots in master_data.items():
    for spot in spots:
        desc_en = spot.get('desc_en', '')
        desc_ja = spot.get('desc_ja', '')
        desc_zh = spot.get('desc_zh', '')
        len_en = len(desc_en)
        
        is_rich = False
        if len_en > 0:
            if has_cjk(desc_ja) and len(desc_ja) > len_en * 0.8: is_rich = True
            if has_cjk(desc_zh) and len(desc_zh) > len_en * 0.8: is_rich = True
        else:
            if has_cjk(desc_ja) or has_cjk(desc_zh): is_rich = True
            
        if is_rich:
            harvest_spots.append({
                'id': spot.get('id'),
                'city': city,
                'name': spot.get('name'),
                'en_desc': desc_en,
                'ja_desc': desc_ja,
                'zh_desc': desc_zh,
                'en_tip': spot.get('insiderTip_en', ''),
                'ja_tip': spot.get('insiderTip_ja', ''),
                'zh_tip': spot.get('insiderTip_zh', '')
            })

print(f"Total harvest spots: {len(harvest_spots)}")

chunk_size = math.ceil(len(harvest_spots) / 8) # 8 subagents
os.makedirs('data/harvest', exist_ok=True)

for i in range(8):
    chunk = harvest_spots[i*chunk_size:(i+1)*chunk_size]
    if not chunk: continue
    with open(f'data/harvest/chunk_{i+1}.json', 'w', encoding='utf-8') as f:
        json.dump(chunk, f, ensure_ascii=False, indent=2)
    print(f"Chunk {i+1}: {len(chunk)} spots")
