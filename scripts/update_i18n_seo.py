import json
import re

with open('js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

updates = {
    'en': {
        'banner.text': '✨ 0 Margin Travel: Free Europe & Benelux AI Trip Planner & Multi-Stop Google Maps Navigation',
        'hero.badge': '✨ 100% Free • Zero Research Fatigue • AI Route Generator',
        'hero.title': 'Explore Europe & Benelux Smarter with Instant Google Maps Routes.',
        'hero.tagline': 'Handpicked ★4.5+ Spots • Interactive AI Planner',
        'planner.tape': 'Smart AI Route Builder'
    },
    'nl': {
        'banner.text': '✨ 0 Margin Travel: Gratis Europa & Benelux AI Reisplanner & Google Maps Navigatie',
        'hero.badge': '✨ 100% Gratis • Geen Onderzoek Nodig • AI Route Generator',
        'hero.title': 'Verken Europa & Benelux Slimmer met Directe Google Maps Routes.',
        'hero.tagline': 'Handgeselecteerde ★4.5+ Plekken • Interactieve AI Planner',
        'planner.tape': 'Slimme AI Route Bouwer'
    },
    'fr': {
        'banner.text': '✨ 0 Margin Travel : Planificateur de Voyage IA Europe & Benelux Gratuit & Navigation Google Maps',
        'hero.badge': '✨ 100% Gratuit • Zéro Fatigue de Recherche • Générateur de Parcours IA',
        'hero.title': 'Explorez l\'Europe & le Benelux Plus Intelligemment avec des Itinéraires Google Maps Instantanés.',
        'hero.tagline': 'Lieux Sélectionnés ★4.5+ • Planificateur IA Interactif',
        'planner.tape': 'Générateur de Parcours IA Intelligent'
    },
    'de': {
        'banner.text': '✨ 0 Margin Travel: Kostenloser Europa & Benelux KI-Reiseplaner & Google Maps Navigation',
        'hero.badge': '✨ 100% Kostenlos • Keine Recherche-Müdigkeit • KI-Routengenerator',
        'hero.title': 'Erkunde Europa & Benelux Smarter mit Sofortigen Google Maps Routen.',
        'hero.tagline': 'Handverlesene ★4.5+ Orte • Interaktiver KI-Planer',
        'planner.tape': 'Smarter KI-Routenplaner'
    },
    'es': {
        'banner.text': '✨ 0 Margin Travel: Planificador IA de Viajes a Europa y Benelux Gratis y Navegación Google Maps',
        'hero.badge': '✨ 100% Gratis • Cero Fatiga de Búsqueda • Generador de Rutas IA',
        'hero.title': 'Explora Europa y Benelux de Forma Más Inteligente con Rutas Instantáneas en Google Maps.',
        'hero.tagline': 'Lugares Seleccionados ★4.5+ • Planificador IA Interactivo',
        'planner.tape': 'Constructor Inteligente de Rutas IA'
    },
    'ja': {
        'banner.text': '✨ 0 Margin Travel: 完全無料・ヨーロッパ＆ベネルクスAI旅行プランナーとGoogleマップナビ',
        'hero.badge': '✨ 100%無料 • リサーチの手間ゼロ • AIルートジェネレーター',
        'hero.title': 'Googleマップのルートを即座に作成して、ヨーロッパとベネルクスをよりスマートに探索しよう。',
        'hero.tagline': '厳選された★4.5+のスポット • インタラクティブAIプランナー',
        'planner.tape': 'スマートAIルートビルダー'
    },
    'zh': {
        'banner.text': '✨ 0 Margin Travel: 完全免费・欧洲及比荷卢AI旅行规划器与谷歌地图导航',
        'hero.badge': '✨ 100%免费 • 零搜索疲劳 • AI路线生成器',
        'hero.title': '通过即时谷歌地图路线，更智能地探索欧洲及比荷卢。',
        'hero.tagline': '精选★4.5+景点 • 交互式AI规划器',
        'planner.tape': '智能AI路线生成器'
    }
}

parts = content.split('translations: {')
if len(parts) == 2:
    prefix = parts[0]
    json_part = parts[1]
    
    new_json_part = json_part
    for lang, trans_dict in updates.items():
        lang_split = new_json_part.split(f'"{lang}": {{')
        if len(lang_split) >= 2:
            inner_content = lang_split[1]
            
            for key, val in trans_dict.items():
                escaped_val = val.replace('"', '\\"')
                pattern = rf'("{key}":\s*")[^"]*(")'
                inner_content = re.sub(pattern, rf'\g<1>{escaped_val}\g<2>', inner_content, count=1)
                
            lang_split[1] = inner_content
            new_json_part = f'"{lang}": {{'.join(lang_split)
            
    with open('js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(prefix + 'translations: {' + new_json_part)
    print("i18n successfully updated!")
else:
    print("Could not find translations object")
