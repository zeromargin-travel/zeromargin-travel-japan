import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

i18n_updates = {
    'en': {
        'filter.allPreset': '✨ ALL',
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
        'filter.rain': '☔ Rainy Day',
        'filter.free': '🆓 Free Entry'
    },
    'ja': {
        'filter.allPreset': '✨ ALL',
        'filter.top7': '👑 定番 Must-See Top 7',
        'filter.hiddenGems': '💎 穴場 Hidden Gems',
        'filter.nightPreset': '🌙 夜のおすすめ Night Spots',
        'filter.catAll': '🌐 すべて',
        'filter.landmark': '🏛️ 史跡・名所',
        'filter.museum': '🎨 美術館・博物館',
        'filter.cafe': '☕ カフェ・グルメ',
        'filter.scenery': '🌇 景観・散策',
        'filter.kids': '🧸 子連れ・Kids',
        'filter.shopping': '🛍️ 買い物・市場',
        'filter.rain': '☔ 雨の日OK',
        'filter.free': '🆓 入場無料'
    },
    'nl': {
        'filter.allPreset': '✨ ALLES',
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
        'filter.rain': '☔ Regendag OK',
        'filter.free': '🆓 Gratis Toegang'
    },
    'fr': {
        'filter.allPreset': '✨ TOUS',
        'filter.top7': '👑 Incontournables Top 7',
        'filter.hiddenGems': '💎 Joyaux Cachés',
        'filter.nightPreset': '🌙 Épisodes Nocturnes',
        'filter.catAll': '🌐 TOUS',
        'filter.landmark': '🏛️ Monuments',
        'filter.museum': '🎨 Musées',
        'filter.cafe': '☕ Cafés & Gastronomie',
        'filter.scenery': '🌇 Paysages & Balades',
        'filter.kids': '🧸 Enfants & Famille',
        'filter.shopping': '🛍️ Shopping & Marchés',
        'filter.rain': '☔ Jour de Pluie OK',
        'filter.free': '🆓 Entrée Gratuite'
    },
    'de': {
        'filter.allPreset': '✨ ALLE',
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
        'filter.rain': '☔ Regentag OK',
        'filter.free': '🆓 Freier Eintritt'
    },
    'es': {
        'filter.allPreset': '✨ TODOS',
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
        'filter.rain': '☔ Día de Lluvia OK',
        'filter.free': '🆓 Entrada Gratuita'
    },
    'zh': {
        'filter.allPreset': '✨ 全部',
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
        'filter.rain': '☔ 雨天推荐',
        'filter.free': '🆓 免费开放'
    }
}

for lang, kvs in i18n_updates.items():
    for k, v in kvs.items():
        pattern = rf'"{re.escape(k)}":\s*"[^"]*"'
        replacement = f'"{k}": "{v}"'
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
        else:
            anchor = r'"filter\.presetGroup":\s*"[^"]*",?'
            content = re.sub(anchor, f'\\g<0>\n        "{k}": "{v}",', content, count=1)

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("🎉 Updated i18n dictionary for Night Spots Scope expansion across 7 languages!")
