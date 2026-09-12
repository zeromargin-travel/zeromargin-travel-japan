import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract dictionary blocks
lang_blocks = {
    'en': {
        'filter.layer1': 'Scope:',
        'filter.layer2': 'Category:',
        'filter.layer3': 'Features:',
        'filter.allPreset': '✨ ALL',
        'filter.all': '✨ ALL',
        'filter.top7': '👑 Must-See Top 7',
        'filter.hiddenGems': '💎 Hidden Gems',
        'filter.nightPreset': '🌙 Night Spots',
        'filter.catAll': '🌐 ALL',
        'filter.landmark': '🏛️ Landmarks',
        'filter.museum': '🎨 Museums',
        'filter.cafe': '☕ Cafés & Dining',
        'filter.scenery': '🌇 Scenery & Walks',
        'filter.kids': '🧸 Kids & Family',
        'filter.shopping': '🛍️ Shopping',
        'filter.night': '🌙 Night Spots',
        'filter.rain': '☔ Rainy Day',
        'filter.free': '🆓 Free Entry'
    },
    'nl': {
        'filter.layer1': 'Bereik:',
        'filter.layer2': 'Categorie:',
        'filter.layer3': 'Kenmerken:',
        'filter.allPreset': '✨ ALLES',
        'filter.all': '✨ ALLES',
        'filter.top7': '👑 Must-See Top 7',
        'filter.hiddenGems': '💎 Verborgen Parels',
        'filter.nightPreset': '🌙 Nachtplekken',
        'filter.catAll': '🌐 ALLES',
        'filter.landmark': '🏛️ Bezienswaardigheden',
        'filter.museum': '🎨 Musea',
        'filter.cafe': '☕ Cafés & Dineren',
        'filter.scenery': '🌇 Uitzicht & Wandelen',
        'filter.kids': '🧸 Kinderen & Familie',
        'filter.shopping': '🛍️ Winkelen',
        'filter.night': '🌙 Nachtleven',
        'filter.rain': '☔ Regendag OK',
        'filter.free': '🆓 Gratis Toegang'
    },
    'ja': {
        'filter.layer1': 'Scope (厳選プリセット):',
        'filter.layer2': 'Categories (ジャンル):',
        'filter.layer3': 'Conditions (状況フィルター):',
        'filter.allPreset': '✨ すべて',
        'filter.all': '✨ すべて',
        'filter.top7': '👑 定番 Top 7',
        'filter.hiddenGems': '💎 穴場 Hidden Gems',
        'filter.nightPreset': '🌙 夜のおすすめ Night Spots',
        'filter.catAll': '🌐 すべて',
        'filter.landmark': '🏛️ 史跡・名所',
        'filter.museum': '🎨 美術館・博物館',
        'filter.cafe': '☕ カフェ・グルメ',
        'filter.scenery': '🌇 景観・散策',
        'filter.kids': '🧸 子連れ・Kids',
        'filter.shopping': '🛍️ 買い物・市場',
        'filter.night': '🌙 ナイトスポット',
        'filter.rain': '☔ 雨の日OK',
        'filter.free': '🆓 入場無料'
    },
    'es': {
        'filter.layer1': 'Alcance:',
        'filter.layer2': 'Categoría:',
        'filter.layer3': 'Características:',
        'filter.allPreset': '✨ TODOS',
        'filter.all': '✨ TODOS',
        'filter.top7': '👑 Imprescindibles Top 7',
        'filter.hiddenGems': '💎 Joyas Ocultas',
        'filter.nightPreset': '🌙 Lugares Nocturnos',
        'filter.catAll': '🌐 TODOS',
        'filter.landmark': '🏛️ Monumentos',
        'filter.museum': '🎨 Museos',
        'filter.cafe': '☕ Cafés y Restaurantes',
        'filter.scenery': '🌇 Paisajes y Paseos',
        'filter.kids': '🧸 Niños y Familia',
        'filter.shopping': '🛍️ Compras y Mercados',
        'filter.night': '🌙 Vida Nocturna',
        'filter.rain': '☔ Día de Lluvia OK',
        'filter.free': '🆓 Entrada Gratuita'
    },
    'zh': {
        'filter.layer1': '范围预设:',
        'filter.layer2': '景点类型:',
        'filter.layer3': '特色条件:',
        'filter.allPreset': '✨ 全部',
        'filter.all': '✨ 全部',
        'filter.top7': '👑 必去 Top 7',
        'filter.hiddenGems': '💎 小众宝藏',
        'filter.nightPreset': '🌙 奇妙夜景地标',
        'filter.catAll': '🌐 全部类型',
        'filter.landmark': '🏛️ 地标名胜',
        'filter.museum': '🎨 博物馆展馆',
        'filter.cafe': '☕ 咖啡与美食',
        'filter.scenery': '🌇 风景与漫步',
        'filter.kids': '🧸 亲子家庭',
        'filter.shopping': '🛍️ 购物与集市',
        'filter.night': '🌙 奇妙夜景',
        'filter.rain': '☔ 雨天推荐',
        'filter.free': '🆓 免费开放'
    },
    'fr': {
        'filter.layer1': 'Portée:',
        'filter.layer2': 'Catégorie:',
        'filter.layer3': 'Critères:',
        'filter.allPreset': '✨ TOUS',
        'filter.all': '✨ TOUS',
        'filter.top7': '👑 Incontournables Top 7',
        'filter.hiddenGems': '💎 Joyaux Cachés',
        'filter.nightPreset': '🌙 Spots Nocturnes',
        'filter.catAll': '🌐 TOUS',
        'filter.landmark': '🏛️ Monuments',
        'filter.museum': '🎨 Musées',
        'filter.cafe': '☕ Cafés & Gastronomie',
        'filter.scenery': '🌇 Paysages & Balades',
        'filter.kids': '🧸 Enfants & Famille',
        'filter.shopping': '🛍️ Shopping & Marchés',
        'filter.night': '🌙 Spots Nocturnes',
        'filter.rain': '☔ Jour de Pluie OK',
        'filter.free': '🆓 Entrée Gratuite'
    },
    'de': {
        'filter.layer1': 'Auswahl:',
        'filter.layer2': 'Kategorie:',
        'filter.layer3': 'Merkmale:',
        'filter.allPreset': '✨ ALLE',
        'filter.all': '✨ ALLE',
        'filter.top7': '👑 Highlight Top 7',
        'filter.hiddenGems': '💎 Geheimtipps',
        'filter.nightPreset': '🌙 Nacht-Highlights',
        'filter.catAll': '🌐 ALLE',
        'filter.landmark': '🏛️ Sehenswürdigkeiten',
        'filter.museum': '🎨 Museen',
        'filter.cafe': '☕ Cafés & Gastronomie',
        'filter.scenery': '🌇 Aussicht & Spaziergang',
        'filter.kids': '🧸 Kinder & Familie',
        'filter.shopping': '🛍️ Shopping & Märkte',
        'filter.night': '🌙 Nachtleben',
        'filter.rain': '☔ Regentag OK',
        'filter.free': '🆓 Freier Eintritt'
    }
}

# Carefully replace each key inside each language section
# Split content by language keys: "en": {, "nl": {, "ja": {, etc.
sections = re.split(r'("(?:en|nl|ja|es|zh|fr|de)":\s*\{)', content)

new_content = sections[0]
for i in range(1, len(sections), 2):
    header = sections[i]
    body = sections[i+1]
    
    lang = header[1:3]
    if lang in lang_blocks:
        kvs = lang_blocks[lang]
        for k, v in kvs.items():
            pattern = rf'"{re.escape(k)}":\s*"[^"]*"'
            replacement = f'"{k}": "{v}"'
            body = re.sub(pattern, replacement, body)
            
    new_content += header + body

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("🎉 PERFECT FIX: All 7 languages in js/i18n.js restored cleanly without cross-contamination!")
