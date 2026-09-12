import json
import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

missing_keys_data = {
    "label.hotel": {
        "en": "🏨 Custom Return Hotel / Accommodation (Optional):",
        "ja": "🏨 帰還ホテル・滞在先（任意）:",
        "nl": "🏨 Hotel / Accommodatie (Optioneel):",
        "fr": "🏨 Hôtel / Hébergement (Optionnel) :",
        "de": "🏨 Hotel / Unterkunft (Optional):",
        "es": "🏨 Hotel / Alojamiento (Opcional):",
        "zh": "🏨 下榻酒店/住宿地点（可选）:"
    },
    "label.hotelSub": {
        "en": "If specified, Route A and Route B will automatically end at your hotel.",
        "ja": "入力すると、ルートA・ルートBの最終目的地が自動的にあなたのホテルになります。",
        "nl": "Indien ingevuld, eindigen Route A en B automatisch bij je hotel.",
        "fr": "Si spécifié, les Routes A et B se termineront automatiquement à votre hôtel.",
        "de": "Wenn angegeben, enden Route A und B automatisch an Ihrem Hotel.",
        "es": "Si se especifica, las Rutas A y B terminarán automáticamente en su hotel.",
        "zh": "若填写，路线A和路线B的终点将自动设为您的下榻酒店。"
    },
    "btn.generate": {
        "en": "🗺️ Generate Ready-to-Use Dual Google Maps Routes ↗",
        "ja": "🗺️ そのまま使えるGoogle MapsルートA＆Bを自動生成 ↗",
        "nl": "🗺️ Genereer Direct Te Gebruiken Google Maps Routen ↗",
        "fr": "🗺️ Générer les Itinéraires Google Maps Prêts à l'Emploi ↗",
        "de": "🗺️ Einsatzbereite Google Maps Routen Generieren ↗",
        "es": "🗺️ Generar Rutas Listas para Usar en Google Maps ↗",
        "zh": "🗺️ 自动生成包含路线A与B的Google Maps导航 ↗"
    },
    "mobile.planner": {
        "en": "Route Planner", "ja": "ルート作成", "nl": "Routeplanner", "fr": "Planificateur", "de": "Routenplaner", "es": "Planificador", "zh": "路线规划"
    },
    "mobile.top": {
        "en": "Top", "ja": "トップ", "nl": "Top", "fr": "Haut", "de": "Nach oben", "es": "Arriba", "zh": "回到顶部"
    },
    "planner.tape": {
        "en": "Interactive Route Planner", "ja": "インタラクティブ・ルートプランナー", "nl": "Interactieve Routeplanner", "fr": "Planificateur d'Itinéraire Interactif", "de": "Interaktiver Routenplaner", "es": "Planificador de Ruta Interactivo", "zh": "交互式路线规划器"
    }
}

sections = re.split(r'("(?:en|nl|ja|es|zh|fr|de)":\s*\{)', content)
new_content = sections[0]

for i in range(1, len(sections), 2):
    header = sections[i]
    body = sections[i+1]
    lang = header[1:3]
    for k, lang_dict in missing_keys_data.items():
        val = lang_dict.get(lang, lang_dict["en"])
        pattern = rf'"{re.escape(k)}":\s*"[^"]*"'
        replacement = f'"{k}": "{val}"'
        if re.search(pattern, body):
            body = re.sub(pattern, replacement, body)
        else:
            body = f'\n        "{k}": "{val}",' + body
    new_content += header + body

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("🎉 Successfully injected the 6 missing keys across all 7 languages into js/i18n.js!")
