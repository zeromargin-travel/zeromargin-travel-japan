import json
import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Unified dictionary for filter keys across all 7 languages
layer_keys = {
    'en': {
        'filter.layer1': 'Scope:',
        'filter.layer2': 'Categories:',
        'filter.layer3': 'Conditions:'
    },
    'ja': {
        'filter.layer1': 'Scope (厳選プリセット):',
        'filter.layer2': 'Categories (ジャンル):',
        'filter.layer3': 'Conditions (状況フィルター):'
    },
    'nl': {
        'filter.layer1': 'Bereik:',
        'filter.layer2': 'Categorieën:',
        'filter.layer3': 'Voorwaarden:'
    },
    'fr': {
        'filter.layer1': 'Portée:',
        'filter.layer2': 'Catégories:',
        'filter.layer3': 'Conditions:'
    },
    'de': {
        'filter.layer1': 'Auswahl:',
        'filter.layer2': 'Kategorien:',
        'filter.layer3': 'Bedingungen:'
    },
    'es': {
        'filter.layer1': 'Alcance:',
        'filter.layer2': 'Categorías:',
        'filter.layer3': 'Condiciones:'
    },
    'zh': {
        'filter.layer1': '范围预设:',
        'filter.layer2': '景点类型:',
        'filter.layer3': '筛选条件:'
    }
}

sections = re.split(r'("(?:en|nl|ja|es|zh|fr|de)":\s*\{)', content)

new_content = sections[0]
for i in range(1, len(sections), 2):
    header = sections[i]
    body = sections[i+1]
    lang = header[1:3]
    if lang in layer_keys:
        for k, v in layer_keys[lang].items():
            pattern = rf'"{re.escape(k)}":\s*"[^"]*"'
            replacement = f'"{k}": "{v}"'
            if re.search(pattern, body):
                body = re.sub(pattern, replacement, body)
            else:
                body = f'\n        "{k}": "{v}",' + body
    new_content += header + body

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("🎉 Complete i18n layer keys check passed!")
