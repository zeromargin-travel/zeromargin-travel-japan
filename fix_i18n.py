import re

with open('js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove 🗺️  from btn.generate and btn.generateRoutes
content = content.replace('"🗺️ ', '"')

# 2. Append step3 title text to route.title
# I will just find route.title and step3.title and do a manual replace for each language.

replacements = {
    "Custom AI Dual Routes": "Custom AI Dual Routes - Choose Route A (Selected Only) or Route B (Curated Full-Day Loop)",
    "AIカスタム2ルート案内": "AIカスタム2ルート案内 - ルートA（選択のみ）またはルートB（1日フルおすすめコース）を選択",
    "AI-Gegenereerde Dubbele Routes": "AI-Gegenereerde Dubbele Routes - Kies Route A of Route B",
    "Itinéraires IA Personnalisés": "Itinéraires IA Personnalisés - Choisissez la Route A ou la Route B",
    "KI-Generierte Zweifach-Routen": "KI-Generierte Zweifach-Routen - Route A oder Route B Wählen",
    "Rutas Duales Personalizadas con IA": "Rutas Duales Personalizadas con IA - Elija Ruta A o Ruta B",
    "AI自定义双路线指南": "AI自定义双路线指南 - 选择路线A或路线B"
}

for k, v in replacements.items():
    content = content.replace(f'"route.title": "{k}"', f'"route.title": "{v}"')

with open('js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(content)
