import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

i18n_updates = {
    'en': {
        'filter.layer1': 'Layer 1: Scope',
        'filter.layer2': 'Layer 2: Categories',
        'filter.layer3': 'Layer 3: Conditions',
        'filter.allPreset': '✨ ALL',
        'filter.top7': '👑 Must-See Top 7',
        'filter.hiddenGems': '💎 Hidden Gems',
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
    'ja': {
        'filter.layer1': 'Scope (厳選プリセット):',
        'filter.layer2': 'Categories (ジャンル):',
        'filter.layer3': 'Conditions (状況フィルター):',
        'filter.allPreset': '✨ ALL',
        'filter.top7': '👑 定番 Must-See Top 7',
        'filter.hiddenGems': '💎 穴場 Hidden Gems',
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
    'nl': {
        'filter.layer1': 'Laag 1: Bereik',
        'filter.layer2': 'Laag 2: Categorieën',
        'filter.layer3': 'Laag 3: Voorwaarden',
        'filter.allPreset': '✨ ALLES',
        'filter.top7': '👑 Must-See Top 7',
        'filter.hiddenGems': '💎 Verborgen Parels',
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
    'fr': {
        'filter.layer1': 'Niveau 1: Portée',
        'filter.layer2': 'Niveau 2: Catégories',
        'filter.layer3': 'Niveau 3: Conditions',
        'filter.allPreset': '✨ TOUS',
        'filter.top7': '👑 Incontournables Top 7',
        'filter.hiddenGems': '💎 Joyaux Cachés',
        'filter.catAll': '🌐 TOUS',
        'filter.landmark': '🏛️ Monuments',
        'filter.museum': '🎨 Musées',
        'filter.cafe': '☕ Cafés & Gastronomie',
        'filter.scenery': '🌇 Paysages & Balades',
        'filter.kids': '🧸 Enfants & Famille',
        'filter.shopping': '🛍️ Shopping & Marchés',
        'filter.night': '🌙 Vie Nocturne',
        'filter.rain': '☔ Jour de Pluie OK',
        'filter.free': '🆓 Entrée Gratuite'
    },
    'de': {
        'filter.layer1': 'Ebene 1: Auswahl',
        'filter.layer2': 'Ebene 2: Kategorien',
        'filter.layer3': 'Ebene 3: Bedingungen',
        'filter.allPreset': '✨ ALLE',
        'filter.top7': '👑 Highlight Top 7',
        'filter.hiddenGems': '💎 Geheimtipps',
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
    },
    'es': {
        'filter.layer1': 'Nivel 1: Alcance',
        'filter.layer2': 'Nivel 2: Categorías',
        'filter.layer3': 'Nivel 3: Condiciones',
        'filter.allPreset': '✨ TODOS',
        'filter.top7': '👑 Imprescindibles Top 7',
        'filter.hiddenGems': '💎 Joyas Ocultas',
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
        'filter.layer1': '层级 1: 范围预设',
        'filter.layer2': '层级 2: 景点类型',
        'filter.layer3': '层级 3: 筛选条件',
        'filter.allPreset': '✨ 全部',
        'filter.top7': '👑 必去 Top 7',
        'filter.hiddenGems': '💎 小众宝藏',
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
    }
}

# Update dictionary blocks
for lang, kvs in i18n_updates.items():
    for k, v in kvs.items():
        pattern = rf'"{re.escape(k)}":\s*"[^"]*"'
        replacement = f'"{k}": "{v}"'
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
        else:
            # Insert after filter.presetGroup
            anchor = r'"filter\.presetGroup":\s*"[^"]*",?'
            content = re.sub(anchor, f'\\g<0>\n        "{k}": "{v}",', content, count=1)

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("🎉 Successfully updated js/i18n.js with complete 3-Layer Filter translations across 7 languages!")
