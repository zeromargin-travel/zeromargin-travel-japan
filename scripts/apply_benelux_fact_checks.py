#!/usr/bin/env python3
"""
Zero-Margin Travel App - Apply Benelux Fact-Checks & Coordinate Fixes (v22.1.0)
Fixes:
1. l_2 Chemin de la Corniche: Correct coordinates to Luxembourg (49.6105, 6.1338) and remove Brittany image
2. l_14 Gëlle Fra: Correct coordinates to Luxembourg (49.6094, 6.1296) and remove Puerto Rico image
3. l_15 Place d'Armes: Correct coordinates to Luxembourg (49.6112, 6.1294) and remove Montreal image
4. l_20 Müllerthal: Correct coordinates to Müllerthal (49.7719, 6.2872)
5. br_2 Royal Gallery of Saint-Hubert: Fix Japanese/Chinese name (Shopping Arcade, not Art Museum)
6. a_17 Moeders: Fix Chinese translation (Stamppot & Mains)
"""

import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

# 1. Luxembourg fixes
lux_path = os.path.join(cities_dir, 'luxembourg.json')
if os.path.exists(lux_path):
    with open(lux_path, 'r', encoding='utf-8') as f:
        ldata = json.load(f)
    for s in ldata['spots']:
        if s['id'] == 'l_2':
            s['lat'] = 49.6105
            s['lng'] = 6.1338
            s['image'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Chemin_de_la_Corniche_Luxembourg_01.jpg/330px-Chemin_de_la_Corniche_Luxembourg_01.jpg"
            s['wikiImage'] = s['image']
        elif s['id'] == 'l_14':
            s['lat'] = 49.6094
            s['lng'] = 6.1296
            s['image'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/G%C3%ABlle_Fra_Luxembourg.jpg/330px-G%C3%ABlle_Fra_Luxembourg.jpg"
            s['wikiImage'] = s['image']
        elif s['id'] == 'l_15':
            s['lat'] = 49.6112
            s['lng'] = 6.1294
            s['image'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Place_d_Armes_Luxembourg_01.jpg/330px-Place_d_Armes_Luxembourg_01.jpg"
            s['wikiImage'] = s['image']
        elif s['id'] == 'l_20':
            s['lat'] = 49.7719
            s['lng'] = 6.2872
    with open(lux_path, 'w', encoding='utf-8') as f:
        json.dump(ldata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Luxembourg coordinates for l_2, l_14, l_15, l_20!")

# 2. Brussels fixes
bru_path = os.path.join(cities_dir, 'brussels.json')
if os.path.exists(bru_path):
    with open(bru_path, 'r', encoding='utf-8') as f:
        bdata = json.load(f)
    for s in bdata['spots']:
        if s['id'] == 'br_2' or 'Saint-Hubert' in s['name']:
            s['name_ja'] = "Royal Gallery of Saint-Hubert（サンテュベール王立ギャラリー）"
            s['name_zh'] = "Royal Gallery of Saint-Hubert (圣于贝尔皇家长廊)"
            s['desc_ja'] = "1847年に完成したヨーロッパ最古級のガラス屋根付きショッピングアーケード。高級ショコラティエや歴史あるカフェが並ぶ。"
            s['desc_zh'] = "建成于1847年的欧洲最古老玻璃拱顶长廊街之一，汇聚顶级巧克力名店与历史悠久的咖啡馆。"
    with open(bru_path, 'w', encoding='utf-8') as f:
        json.dump(bdata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Brussels br_2 name and description!")

# 3. Amsterdam fixes
ams_path = os.path.join(cities_dir, 'amsterdam.json')
if os.path.exists(ams_path):
    with open(ams_path, 'r', encoding='utf-8') as f:
        adata = json.load(f)
    for s in adata['spots']:
        if s['id'] == 'a_17' or 'Moeders' in s['name']:
            s['desc_zh'] = "温馨的荷兰传统餐馆，供应正宗的传统混合土豆泥（Stamppot）、炖牛肉和家常炖菜。"
            s['price_zh'] = "主菜：17–24 欧元"
        elif s['id'] == 'a_20' or 'Brouwerij' in s['name']:
            s['price_zh'] = "啤酒品尝组合：12 欧元"
    with open(ams_path, 'w', encoding='utf-8') as f:
        json.dump(adata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Amsterdam a_17 and a_20 Chinese translations!")

print("🎉 Benelux critical fact-checks successfully applied!")
