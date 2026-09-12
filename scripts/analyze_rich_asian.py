import json

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']

def has_cjk(text):
    return any('\u3000' <= c <= '\u9fff' or '\uac00' <= c <= '\ud7a3' for c in text) if text else False

rich_asian_spots = []

for city, spots in master_data.items():
    for spot in spots:
        desc_en = spot.get('desc_en', '')
        desc_ja = spot.get('desc_ja', '')
        desc_zh = spot.get('desc_zh', '')
        
        len_en = len(desc_en)
        
        # Asian characters carry roughly 2-3 times more meaning per char than English.
        # If JA or ZH has MORE characters than EN, it means it has vastly more information.
        # Or even if it has > 60% of EN chars, it might be richer.
        # Let's flag any spot where JA or ZH is > 0.8 * EN length AND it is actually CJK.
        
        is_rich = False
        reason = []
        
        if len_en > 0:
            if has_cjk(desc_ja) and len(desc_ja) > len_en * 0.8:
                is_rich = True
                reason.append(f"JA is {len(desc_ja)} chars vs EN {len_en} chars")
            
            if has_cjk(desc_zh) and len(desc_zh) > len_en * 0.8:
                is_rich = True
                reason.append(f"ZH is {len(desc_zh)} chars vs EN {len_en} chars")
        else:
            if has_cjk(desc_ja) or has_cjk(desc_zh):
                is_rich = True
                reason.append("EN is missing but JA/ZH exists")
                
        if is_rich:
            rich_asian_spots.append({
                'id': spot.get('id'),
                'name': spot.get('name'),
                'en': desc_en[:50].replace('\n', ' '),
                'ja': desc_ja[:50].replace('\n', ' '),
                'zh': desc_zh[:50].replace('\n', ' '),
                'reason': " & ".join(reason)
            })

print(f"Spots where JA/ZH might contain richer info than EN: {len(rich_asian_spots)}")
for i, s in enumerate(rich_asian_spots[:10]):
    print(f"- {s['name']} | {s['reason']}")
    print(f"  EN: {s['en']}")
    if 'JA' in s['reason']: print(f"  JA: {s['ja']}")
    if 'ZH' in s['reason']: print(f"  ZH: {s['zh']}")
