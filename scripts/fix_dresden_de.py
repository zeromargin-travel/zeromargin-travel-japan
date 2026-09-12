#!/usr/bin/env python3
import json, os

dresden_path = "/Users/jnabi1/Desktop/アプリ開発/旅行ツールアプリ版/data/cities/dresden.json"
with open(dresden_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

spots = data.get('spots', [])
fixed_count = 0

for s in spots:
    desc_en = s.get('desc_en', s.get('desc_ja', ''))
    desc_de = s.get('desc_de', '')
    if not desc_de or len(desc_de.strip()) == 0:
        s['desc_de'] = desc_en if desc_en else s.get('desc_ja', '')
        fixed_count += 1
        print(f"Fixed desc_de in [{s.get('id')}] {s.get('name_en')}")

with open(dresden_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"🎉 Fixed {fixed_count} empty desc_de strings in dresden.json!")
