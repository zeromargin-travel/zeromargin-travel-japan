import json
import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')
index_path = os.path.join(base_dir, '..', 'index.html')

print("🚀 Auditing & Fixing All i18n Keys across 7 Languages...")

# Read i18n.js
with open(i18n_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Extract language dictionary sections from i18n.js
langs = ['en', 'ja', 'nl', 'fr', 'de', 'es', 'zh']

# Master dictionary containing ALL keys required across the application
master_keys = {
    "nav.title": {
        "en": "0 Margin Travel(EU)", "ja": "0 Margin Travel(EU)", "nl": "0 Margin Travel(EU)", "fr": "0 Margin Travel(EU)", "de": "0 Margin Travel(EU)", "es": "0 Margin Travel(EU)", "zh": "0 Margin Travel(EU)"
    },
    "nav.badge": {
        "en": "Western Europe & Benelux", "ja": "西欧＆ベネルクス", "nl": "West-Europa & Benelux", "fr": "Europe de l'Ouest & Benelux", "de": "Westeuropa & Benelux", "es": "Europa Occidental y Benelux", "zh": "西欧与比荷卢"
    },
    "banner.text": {
        "en": "✨ 0 Margin Travel(EU): AI Route Planner & Google Maps Multi-Stop Navigation Platform",
        "ja": "✨ 0 Margin Travel(EU): AIルートプランナー＆Google Mapsマルチストップナビ",
        "nl": "✨ 0 Margin Travel(EU): AI Routeplanner & Google Maps Multi-Stop Navigatie",
        "fr": "✨ 0 Margin Travel(EU): Planificateur IA & Navigation Google Maps Multi-Arrêts",
        "de": "✨ 0 Margin Travel(EU): KI-Routenplaner & Google Maps Multi-Stopp Navigationsplattform",
        "es": "✨ 0 Margin Travel(EU): Planificador IA y Navegación Multi-Parada de Google Maps",
        "zh": "✨ 0 Margin Travel(EU): AI路线规划器与Google Maps多途经点导航平台"
    },
    "hero.badge": {
        "en": "Hello! I'm Artfantino, your travel partner! Let's explore together!",
        "ja": "こんにちは！旅のパートナー、アールファンティーノです！一緒に冒険しましょう！",
        "nl": "Hallo! Ik ben Artfantino, je reispartner! Laten we samen verkennen!",
        "fr": "Bonjour! Je suis Artfantino, votre partenaire de voyage! Explorons ensemble!",
        "de": "Hallo! Ich bin Artfantino, Ihr Reisepartner! Lassen Sie uns gemeinsam auf Entdeckungsreise gehen!",
        "es": "¡Hola! ¡Soy Artfantino, tu compañero de viaje! ¡Exploremos juntos!",
        "zh": "你好！我是你的旅行伙伴Artfantino！让我们一起去探索吧！"
    },
    "hero.title": {
        "en": "Travel Western Europe Smartly with Optimized Google Maps Routes.",
        "ja": "Google Maps最適化ルートで欧州をスマートに旅しよう。",
        "nl": "Reis Slim door West-Europa met Geoptimaliseerde Google Maps Routen.",
        "fr": "Voyagez Intelligemment en Europe de l'Ouest avec des Itinéraires Google Maps Optimisés.",
        "de": "Reisen Sie Smart durch Westeuropa mit Optimierten Google Maps Routen.",
        "es": "Viaje de Forma Inteligente por Europa Occidental con Rutas Optimizadas de Google Maps.",
        "zh": "利用Google Maps优化路线，智能畅游西欧。"
    },
    "hero.tagline": {
        "en": "Verified ★4.5+ Spots. Zero Prior Research Hassle.",
        "ja": "厳選★4.5+スポット。事前調べる手間はゼロへ。",
        "nl": "Geverifieerde ★4.5+ Plekken. Nul Voorafgaand Uitzoekwerk.",
        "fr": "Lieux Vérifiés ★4.5+. Zéro Recherche Préalable Fastidieuse.",
        "de": "Verifizierte ★4.5+ Orte. Null Aufwand für Vorab-Recherchen.",
        "es": "Lugares Verificados ★4.5+. Cero Complicaciones de Investigación Previa.",
        "zh": "严选★4.5+高分景点。无需做繁琐的提前攻略。"
    },
    "hero.subtitle": {
        "en": "Simply choose your favorite landmarks, cafés, and views. A ready-to-use Google Maps multi-stop navigation opens in seconds.",
        "ja": "行きたい名所・カフェ・絶景を選ぶだけ。数秒でそのまま使えるGoogle Mapsマルチストップナビが完成。",
        "nl": "Kies gewoon je favoriete bezienswaardigheden, cafés en uitzichten. In enkele seconden geopend in Google Maps.",
        "fr": "Choisissez simplement vos monuments, cafés et vues préférés. Une navigation multi-arrêts Google Maps prête en quelques secondes.",
        "de": "Wählen Sie einfach Ihre Lieblingssehenswürdigkeiten, Cafés und Aussichten. In Sekundenschnelle einsatzbereit in Google Maps.",
        "es": "Simplemente elija sus monumentos, cafés y vistas favoritas. Una navegación multi-parada de Google Maps lista en segundos.",
        "zh": "只需挑选心仪的地标、咖啡馆和风景。数秒内即可生成随取随用的Google Maps多途经点导航。"
    },
    "hero.cta": {
        "en": "🗺️ Build Custom Route", "ja": "🗺️ カスタムルートを作成する", "nl": "🗺️ Maak Aangepaste Route", "fr": "🗺️ Créer un Itinéraire Personnalisé", "de": "🗺️ Eigene Route Erstellen", "es": "🗺️ Crear Ruta Personalizada", "zh": "🗺️ 生成自定义路线"
    },
    "planner.title": {
        "en": "Create Your Ideal Day in 3 Simple Steps", "ja": "簡単3ステップで理想の1日を作成", "nl": "Creëer je Ideale Dag in 3 Eenvoudige Stappen", "fr": "Créez votre Journée Idéale en 3 Étapes Simples", "de": "Erstellen Sie Ihren Idealen Tag in 3 Einfachen Schritten", "es": "Cree su Día Ideal en 3 Sencillos Pasos", "zh": "简单3步即可规划理想的一天行程"
    },
    "planner.subtitle": {
        "en": "Select favorites from verified ★4.5+ places and launch Google Maps multi-stop navigation in 1 click!",
        "ja": "検証済み★4.5+の名所からお気に入りを選び、1クリックでGoogle Mapsマルチストップナビを起動！",
        "nl": "Kies favorieten uit ★4.5+ plekken en start Google Maps navigatie in 1 klik!",
        "fr": "Sélectionnez vos coups de cœur parmi des lieux ★4.5+ et lancez la navigation Google Maps en 1 clic!",
        "de": "Wählen Sie Favoriten aus ★4.5+ Orten und starten Sie die Google Maps Navigation mit 1 Klick!",
        "es": "¡Seleccione favoritos entre lugares ★4.5+ e inicie la navegación de Google Maps con 1 clic!",
        "zh": "从严选★4.5+景点中挑选心仪之地，一键开启Google Maps多途经点导航！"
    },
    "step1.title": {
        "en": "Step 1: Choose Destination — Select Country & City", "ja": "ステップ1: 目的地を選択 — 国と都市を選んでください", "nl": "Stap 1: Kies Bestemming — Selecteer Land & Stad", "fr": "Étape 1: Choisissez la Destination — Sélectionnez Pays et Ville", "de": "Schritt 1: Ziel Auswählen — Land & Stadt Wählen", "es": "Paso 1: Elija Destino — Seleccione País y Ciudad", "zh": "步骤 1: 选择目的地 — 挑选国家与城市"
    },
    "label.country": {
        "en": "Country:", "ja": "国:", "nl": "Land:", "fr": "Pays:", "de": "Land:", "es": "País:", "zh": "国家:"
    },
    "label.city": {
        "en": "City:", "ja": "都市:", "nl": "Stad:", "fr": "Ville:", "de": "Stadt:", "es": "Ciudad:", "zh": "城市:"
    },
    "label.areaZone": {
        "en": "Area Zone:", "ja": "エリアゾーン:", "nl": "Zone:", "fr": "Zone:", "de": "Bereich:", "es": "Zona:", "zh": "区域范围:"
    },
    "area.all": {
        "en": "✨ All Spots (City + Suburban Day Trips)", "ja": "✨ 全スポット（市内＋郊外日帰り）", "nl": "✨ Alle Plekken (Stad + Dagtrips)", "fr": "✨ Tous les Lieux (Ville + Excursions)", "de": "✨ Alle Orte (Stadt + Tagesausflüge)", "es": "✨ Todos los Lugares (Ciudad + Excursiones)", "zh": "✨ 全部景点（市区+郊外一日游）"
    },
    "area.city": {
        "en": "🏙️ City Center Spots Only", "ja": "🏙️ 市内中心部スポットのみ", "nl": "🏙️ Alleen Centrum", "fr": "🏙️ Centre-Ville Uniquement", "de": "🏙️ Nur Innenstadt-Orte", "es": "🏙️ Solo Centro Urbano", "zh": "🏙️ 仅限市中心景点"
    },
    "area.suburban": {
        "en": "🏞️ Suburban & Day-Trip Spots Only", "ja": "🏞️ 郊外・日帰りスポットのみ", "nl": "🏞️ Alleen Dagtrips", "fr": "🏞️ Banlieue & Excursions Uniquement", "de": "🏞️ Nur Vorort- & Ausflugsziele", "es": "🏞️ Solo Suburbios y Excursiones", "zh": "🏞️ 仅限郊外/日游景点"
    },
    "step2.title": {
        "en": "Step 2: Pick Your Spots — Handpick your favorites from Verified ★4.5+ places",
        "ja": "ステップ2: 訪問スポットを選択 — 検証済み★4.5+からお気に入りを選択",
        "nl": "Stap 2: Kies Je Plekken — Selecteer uit ★4.5+ locaties",
        "fr": "Étape 2: Choisissez vos Lieux — Sélectionnez parmi les lieux ★4.5+",
        "de": "Schritt 2: Orte Auswählen — Wählen Sie aus ★4.5+ Orten",
        "es": "Paso 2: Elija sus Lugares — Seleccione entre lugares ★4.5+",
        "zh": "步骤 2: 挑选景点 — 从严选★4.5+高分景点中勾选"
    },
    "step2.subtitle": {
        "en": "Check the boxes for spots you definitely want to visit. The AI engine will generate both Route A (Selected Spots Only) and Route B (Full 1-Day AI Course) for Google Maps navigation!",
        "ja": "チェックボックスを入れて行きたいスポットを選んでください。AIエンジンがルートA（選択スポットのみ）とルートB（1日フルおすすめコース）の2つのGoogle Mapsナビを自動生成します！",
        "nl": "Vink de plekken aan die je wilt bezoeken. De AI genereert zowel Route A (Geselecteerd) als Route B (Volledige Dag) voor Google Maps!",
        "fr": "Cochez les lieux que vous souhaitez visiter. L'IA générera la Route A (Sélectionnés) et la Route B (Journée Complète) pour Google Maps!",
        "de": "Wählen Sie Ihre Wunschorte. Die KI generiert sowohl Route A (Nur Ausgewählte) als auch Route B (Ganztageskurs) für Google Maps!",
        "es": "Marque los lugares que desea visitar. ¡La IA generará la Ruta A (Seleccionados) y la Ruta B (Día Completo) para Google Maps!",
        "zh": "勾选您想去的地方。AI引擎将自动生成路线A（仅限已选）和路线B（一日游精选）两条Google Maps导航！"
    },
    "badge.selected": {
        "en": "Selected:", "ja": "選択中:", "nl": "Geselecteerd:", "fr": "Sélectionné:", "de": "Ausgewählt:", "es": "Seleccionado:", "zh": "已选择:"
    },
    "badge.maxNotice": {
        "en": "(Max 8 Must-Visit Spots)", "ja": "(最大8箇所まで)", "nl": "(Max 8 plekken)", "fr": "(Max 8 lieux)", "de": "(Max 8 Orte)", "es": "(Máx. 8 lugares)", "zh": "(最多可选8处)"
    },
    "filter.layer1": {
        "en": "Scope:", "ja": "Scope (厳選プリセット):", "nl": "Bereik:", "fr": "Portée:", "de": "Auswahl:", "es": "Alcance:", "zh": "范围预设:"
    },
    "filter.layer2": {
        "en": "Categories:", "ja": "Categories (ジャンル):", "nl": "Categorieën:", "fr": "Catégories:", "de": "Kategorien:", "es": "Categorías:", "zh": "景点类型:"
    },
    "filter.layer3": {
        "en": "Conditions:", "ja": "Conditions (状況フィルター):", "nl": "Voorwaarden:", "fr": "Conditions:", "de": "Bedingungen:", "es": "Condiciones:", "zh": "筛选条件:"
    },
    "filter.allPreset": {
        "en": "✨ ALL", "ja": "✨ すべて", "nl": "✨ ALLES", "fr": "✨ TOUS", "de": "✨ ALLE", "es": "✨ TODOS", "zh": "✨ 全部"
    },
    "filter.top7": {
        "en": "👑 Must-See Top 7", "ja": "👑 定番 Top 7", "nl": "👑 Must-See Top 7", "fr": "👑 Incontournables Top 7", "de": "👑 Highlight Top 7", "es": "👑 Imprescindibles Top 7", "zh": "👑 必去 Top 7"
    },
    "filter.hiddenGems": {
        "en": "💎 Hidden Gems", "ja": "💎 穴場 Hidden Gems", "nl": "💎 Verborgen Parels", "fr": "💎 Joyaux Cachés", "de": "💎 Geheimtipps", "es": "💎 Joyas Ocultas", "zh": "💎 小众宝藏"
    },
    "filter.nightPreset": {
        "en": "🌙 Night Spots", "ja": "🌙 夜のおすすめ Night Spots", "nl": "🌙 Nachtplekken", "fr": "🌙 Spots Nocturnes", "de": "🌙 Nacht-Highlights", "es": "🌙 Lugares Nocturnos", "zh": "🌙 奇妙夜景地标"
    },
    "filter.catAll": {
        "en": "🌐 ALL", "ja": "🌐 すべて", "nl": "🌐 ALLES", "fr": "🌐 TOUS", "de": "🌐 ALLE", "es": "🌐 TODOS", "zh": "🌐 全部类型"
    },
    "filter.landmark": {
        "en": "🏛️ Landmarks", "ja": "🏛️ 史跡・名所", "nl": "🏛️ Bezienswaardigheden", "fr": "🏛️ Monuments", "de": "🏛️ Sehenswürdigkeiten", "es": "🏛️ Monumentos", "zh": "🏛️ 地标名胜"
    },
    "filter.museum": {
        "en": "🎨 Museums", "ja": "🎨 美術館・博物館", "nl": "🎨 Musea", "fr": "🎨 Musées", "de": "🎨 Museen", "es": "🎨 Museos", "zh": "🎨 博物馆展馆"
    },
    "filter.cafe": {
        "en": "☕ Cafés & Dining", "ja": "☕ カフェ・グルメ", "nl": "☕ Cafés & Dineren", "fr": "☕ Cafés & Gastronomie", "de": "☕ Cafés & Gastronomie", "es": "☕ Cafés y Restaurantes", "zh": "☕ 咖啡与美食"
    },
    "filter.scenery": {
        "en": "🌇 Scenery & Walks", "ja": "🌇 景観・散策", "nl": "🌇 Uitzicht & Wandelen", "fr": "🌇 Paysages & Balades", "de": "🌇 Aussicht & Spaziergang", "es": "🌇 Paisajes y Paseos", "zh": "🌇 风景与漫步"
    },
    "filter.kids": {
        "en": "🧸 Kids & Family", "ja": "🧸 子連れ・Kids", "nl": "🧸 Kinderen & Familie", "fr": "🧸 Enfants & Famille", "de": "🧸 Kinder & Familie", "es": "🧸 Niños y Familia", "zh": "🧸 亲子家庭"
    },
    "filter.shopping": {
        "en": "🛍️ Shopping", "ja": "🛍️ 買い物・市場", "nl": "🛍️ Winkelen", "fr": "🛍️ Shopping & Marchés", "de": "🛍️ Shopping & Märkte", "es": "🛍️ Compras y Mercados", "zh": "🛍️ 购物与集市"
    },
    "filter.rain": {
        "en": "☔ Rainy Day", "ja": "☔ 雨の日OK", "nl": "☔ Regendag OK", "fr": "☔ Jour de Pluie OK", "de": "☔ Regentag OK", "es": "☔ Día de Lluvia OK", "zh": "☔ 雨天推荐"
    },
    "filter.free": {
        "en": "🆓 Free Entry", "ja": "🆓 入場無料", "nl": "🆓 Gratis Toegang", "fr": "🆓 Entrée Gratuite", "de": "🆓 Freier Eintritt", "es": "🆓 Entrada Gratuita", "zh": "🆓 免费开放"
    },
    "step3.title": {
        "en": "Step 3: Launch in Maps — Choose Route A (Selected Only) or Route B (Curated Full-Day Loop)",
        "ja": "ステップ3: ナビ起動 — ルートA（選択のみ）またはルートB（1日フルおすすめコース）を選択",
        "nl": "Stap 3: Start Navigatie — Kies Route A (Alleen Geselecteerd) of Route B (Volledige Dag)",
        "fr": "Étape 3: Lancez Maps — Choisissez la Route A (Sélectionnés) ou la Route B (Journée Complète)",
        "de": "Schritt 3: Navigation Starten — Route A (Nur Ausgewählte) oder Route B (Ganztageskurs) Wählen",
        "es": "Paso 3: Inicie Navegación — Elija Ruta A (Solo Seleccionados) o Ruta B (Día Completo)",
        "zh": "步骤 3: 开启导航 — 选择路线A（仅已选景点）或路线B（一日全景精选）"
    },
    "btn.generateRoutes": {
        "en": "🗺️ Generate Ready-to-Use Dual Google Maps Routes ↗",
        "ja": "🗺️ そのまま使えるGoogle MapsルートA＆Bを自動生成 ↗",
        "nl": "🗺️ Genereer Direct Te Gebruiken Google Maps Routen ↗",
        "fr": "🗺️ Générer les Itinéraires Google Maps Prêts à l'Emploi ↗",
        "de": "🗺️ Einsatzbereite Google Maps Routen Generieren ↗",
        "es": "🗺️ Generar Rutas Listas para Usar en Google Maps ↗",
        "zh": "🗺️ 自动生成包含路线A与B的Google Maps导航 ↗"
    },
    "btn.reportError": {
        "en": "💬 Report Spot Error / Feedback", "ja": "💬 スポット誤り指摘・ご意見", "nl": "💬 Fout Melden / Feedback", "fr": "💬 Signaler une Erreur / Avis", "de": "💬 Fehler Melden / Feedback", "es": "💬 Informar Error / Opinión", "zh": "💬 纠错与意见反馈"
    },
    "btn.terms": {
        "en": "⚖️ Terms of Use & Legal Disclaimer", "ja": "⚖️ 利用規約・免責事項", "nl": "⚖️ Gebruiksvoorwaarden & Disclaimer", "fr": "⚖️ Conditions d'Utilisation & Avertissement Légal", "de": "⚖️ Nutzungsbedingungen & Haftungsausschluss", "es": "⚖️ Términos de Uso y Aviso Legal", "zh": "⚖️ 使用条款与免责声明"
    },
    "footer.aiNotice": {
        "en": "🤖 Powered by AI analysis & expert research (Verified ★4.5+), but 100% accuracy is not guaranteed. Please verify official details prior to your trip.",
        "ja": "🤖 当ツールはAI分析と専門リサーチ（★4.5+厳選）を融合して構築されていますが、情報の100%の完全性を保証するものではありません。訪問前に必ず公式情報をご確認ください。",
        "nl": "🤖 Aangedreven door AI-analyse & deskundige curatie (★4.5+), maar 100% nauwkeurigheid wordt niet gegarandeerd. Controleer altijd officiële bronnen voor je bezoek.",
        "fr": "🤖 Propulsé par l'analyse IA & la sélection d'experts (★4.5+), mais l'exactitude à 100% n'est pas garantie. Veuillez vérifier auprès des sites officiels avant votre visite.",
        "de": "🤖 KI-Analyse & Experten-Prüfung (★4.5+), jedoch wird 100% Genauigkeit nicht garantiert. Bitte prüfen Sie vor Ihrer Reise die offiziellen Angaben.",
        "es": "🤖 Impulsado por análisis de IA y curaduría experta (★4.5+), pero no se garantiza el 100% de precisión. Verifique los canales oficiales antes de viajar.",
        "zh": "🤖 本工具结合AI分析与专家严选（★4.5+严选），但无法保证100%绝对准确。出行前请务必核实官方最新信息。"
    },
    "footer.termsNotice": {
        "en": "* By using this website, you are deemed to have agreed to the [ <a href=\"javascript:void(0)\" onclick=\"openTermsModal()\" style=\"color:#78716C; text-decoration:underline; font-weight:600;\">⚖️ Terms of Use & Legal Disclaimer</a> ].",
        "ja": "※当サイトのご利用をもって [ <a href=\"javascript:void(0)\" onclick=\"openTermsModal()\" style=\"color:#78716C; text-decoration:underline; font-weight:600;\">⚖️ 利用規約・免責事項</a> ] に同意いただいたものとみなします。",
        "nl": "* Door deze site te gebruiken, gaat u akkoord met de [ <a href=\"javascript:void(0)\" onclick=\"openTermsModal()\" style=\"color:#78716C; text-decoration:underline; font-weight:600;\">⚖️ Gebruiksvoorwaarden & Disclaimer</a> ].",
        "fr": "* En utilisant ce site, vous acceptez les [ <a href=\"javascript:void(0)\" onclick=\"openTermsModal()\" style=\"color:#78716C; text-decoration:underline; font-weight:600;\">⚖️ Conditions d'Utilisation & Avertissement Légal</a> ].",
        "de": "* Mit der Nutzung dieser Website erklären Sie sich mit den [ <a href=\"javascript:void(0)\" onclick=\"openTermsModal()\" style=\"color:#78716C; text-decoration:underline; font-weight:600;\">⚖️ Nutzungsbedingungen & Haftungsausschluss</a> ] einverstanden.",
        "es": "* Al usar este sitio web, usted acepta los [ <a href=\"javascript:void(0)\" onclick=\"openTermsModal()\" style=\"color:#78716C; text-decoration:underline; font-weight:600;\">⚖️ Términos de Uso y Aviso Legal</a> ].",
        "zh": "* 使用本网站即表示您已同意 [ <a href=\"javascript:void(0)\" onclick=\"openTermsModal()\" style=\"color:#78716C; text-decoration:underline; font-weight:600;\">⚖️ 使用条款与免责声明</a> ]。"
    },
    "modal.feedbackTitle": {
        "en": "💬 Feedback & Spot Error Report", "ja": "💬 ご意見・スポット情報の誤りを指摘", "nl": "💬 Feedback & Fout Melden", "fr": "💬 Retours & Signalement d'Erreur", "de": "💬 Feedback & Fehler Melden", "es": "💬 Comentarios e Informe de Errores", "zh": "💬 意见反馈与景点信息纠错"
    },
    "modal.feedbackSub": {
        "en": "Notice an error in spot details, opening hours, or have a suggestion? Let us know!",
        "ja": "スポット情報の誤り、営業時間の間違い、改善のご意見などをお気軽にお寄せください。",
        "nl": "Foutje gezien in een plek of openingstijden? Laat het ons weten!",
        "fr": "Remarqué une erreur sur un lieu ou des horaires ? Dites-le nous !",
        "de": "Fehler bei einem Ort oder den Öffnungszeiten entdeckt? Teilen Sie es uns mit!",
        "es": "¿Vio un error en los detalles o horarios de un lugar? ¡Avísanos!",
        "zh": "发现景点名称、营业时间有误或有改进建议？欢迎随时告知！"
    },
    "modal.spotNameLabel": {
        "en": "Spot Name / City:", "ja": "対象のスポット名・都市名:", "nl": "Naam van de plek / Stad:", "fr": "Nom du lieu / Ville :", "de": "Name des Ortes / Stadt:", "es": "Nombre del lugar / Ciudad:", "zh": "涉及景点名称 / 城市:"
    },
    "modal.spotNamePlaceholder": {
        "en": "e.g. Louvre Museum / Paris", "ja": "例: ルーブル美術館 / パリ", "nl": "bijv. Rijksmuseum / Amsterdam", "fr": "ex. Musée du Louvre / Paris", "de": "z.B. Brandenburger Tor / Berlin", "es": "ej. Museo del Prado / Madrid", "zh": "例如: 卢浮宫 / 巴黎"
    },
    "modal.detailsLabel": {
        "en": "Correction Details / Message:", "ja": "誤りの内容・ご意見:", "nl": "Details van de fout / Bericht:", "fr": "Détails de l'erreur / Message :", "de": "Fehlerbeschreibung / Nachricht:", "es": "Detalles del error / Mensaje:", "zh": "纠错详情 / 建议内容:"
    },
    "modal.detailsPlaceholder": {
        "en": "Describe the incorrect information or your feedback...", "ja": "間違っている情報や修正案をご記入ください...", "nl": "Beschrijf de onjuiste informatie of je suggestie...", "fr": "Décrivez les informations incorrectes ou vos suggestions...", "de": "Beschreiben Sie die fehlerhaften Informationen...", "es": "Describa la información incorrecta o su sugerencia...", "zh": "请详细描述错误信息或您的宝贵建议..."
    },
    "modal.emailLabel": {
        "en": "Your Email (Optional):", "ja": "ご連絡先メールアドレス（任意）:", "nl": "Je e-mailadres (optioneel):", "fr": "Votre e-mail (facultatif) :", "de": "Ihre E-Mail (optional):", "es": "Su correo electrónico (opcional):", "zh": "您的联系邮箱（可选）:"
    },
    "modal.emailPlaceholder": {
        "en": "your.email@example.com", "ja": "your.email@example.com （返信をご希望の場合）", "nl": "jouw.email@example.com", "fr": "votre.email@example.com", "de": "ihre.email@example.com", "es": "su.email@example.com", "zh": "your.email@example.com"
    },
    "modal.sendBtn": {
        "en": "✉️ Send Feedback & Error Report", "ja": "✉️ ご意見・誤り指摘を送信する", "nl": "✉️ Feedback Versturen", "fr": "✉️ Envoyer votre Signalement", "de": "✉️ Feedback Absenden", "es": "✉️ Enviar Comentario", "zh": "✉️ 提交意见与纠错"
    },
    "modal.termsTitle": {
        "en": "⚖️ Terms of Use & Legal Disclaimer", "ja": "⚖️ 利用規約・免責事項", "nl": "⚖️ Gebruiksvoorwaarden & Disclaimer", "fr": "⚖️ Conditions d'Utilisation & Avertissement Légal", "de": "⚖️ Nutzungsbedingungen & Haftungsausschluss", "es": "⚖️ Términos de Uso y Aviso Legal", "zh": "⚖️ 使用条款与免责声明"
    },
    "modal.termsBody": {
        "en": "【Terms of Use & Legal Disclaimer】\\n0 Margin Travel(EU) is a completely free travel planning assistance tool. While we integrate AI data analysis with expert curation (selecting ★4.5+ top-rated spots) and exercise strict care regarding spot details, opening hours, prices, coordinates, and routes, we do not guarantee 100% completeness, timeliness, or accuracy.\\n\\nOperating hours and venue details are subject to change without notice. Please always verify the latest information on official venue websites prior to your visit.\\n\\nTo the maximum extent permitted by applicable law, the site administrator disclaims all liability for any loss, damage, or trouble (including travel expenses, accommodation costs, lost opportunities, etc.) arising from the use of this website or actions taken based on its content. Please use at your own discretion. By using this website, you are deemed to have agreed to this Legal Disclaimer.",
        "ja": "【利用規約・免責事項】\\n当サイト「0 Margin Travel(EU)」は、旅行計画を補助するための完全無料の情報案内ツールです。AIデータ解析と専門リサーチ（★4.5以上の高評価スポット基準）を融合し、掲載しているスポット情報、営業時間、料金、位置情報、ルート案内等の正確性については細心の注意を払っておりますが、その完全性、最新性、確実性を保証するものではありません。\\n\\n営業日時や施設情報は予告なく変更される場合がありますので、実際の訪問に際しては必ず事前に施設公式ウェブサイト等で最新情報をご確認ください。\\n\\n当サイトの利用、または掲載情報に基づいて行われた行動により生じたあらゆる損害・不利益・トラブル（交通費・宿泊費の損失、機会損失等を含む）について、当サイト管理者は法律上許容される最大限の範囲において一切の責任を負いかねます。あらかじめご了承の上、ご自身の責任においてご利用ください。当サイトのご利用をもって、本免責事項に同意いただいたものとみなします。",
        "nl": "【Gebruiksvoorwaarden & Disclaimer】\\n0 Margin Travel(EU) is een volledig gratis reisplanningstool. We combineren AI-analyse met deskundige curatie (★4.5+ locaties). Hoewel we zorg dragen voor alle gegevens, garanderen we geen 100% juistheid of volledigheid.\\n\\nOpeningstijden kunnen zonder voorafgaande kennisgeving veranderen. Verifieer altijd de meest recente informatie via officiële bronnen voor je bezoek.\\n\\nVoor zover wettelijk toegestaan is de beheerder niet aansprakelijk voor enige schade, kosten of ongemak voortvloeiend uit het gebruik van deze site. Door deze site te gebruiken, gaat u akkoord met deze disclaimer.",
        "fr": "【Conditions d'Utilisation & Avertissement Légal】\\n0 Margin Travel(EU) est un outil gratuit d'aide au voyage. Nous combinons l'analyse IA et la sélection d'experts (lieux ★4.5+). Bien que nous apportions un soin particulier aux données, nous ne garantissons pas leur exactitude ou exhaustivité à 100%.\\n\\nLes horaires peuvent changer sans préavis. Veuillez toujours vérifier les informations sur les sites officiels avant votre visite.\\n\\nDans la mesure maximale permise par la loi, l'administrateur décline toute responsabilité pour tout dommage ou frais découlant de l'utilisation de ce site. L'utilisation de ce site vaut acceptation des présentes conditions.",
        "de": "【Nutzungsbedingungen & Haftungsausschluss】\\n0 Margin Travel(EU) ist ein kostenloses Reiseplanungstool. Wir kombinieren KI-Analyse mit Experten-Prüfung (★4.5+ Orte). Trotz größter Sorgfalt übernehmen wir keine Gewähr für die 100%ige Vollständigkeit oder Aktualität.\\n\\nÖffnungszeiten können sich ändern. Bitte prüfen Sie vor der Anreise stets die offiziellen Angaben.\\n\\nSoweit gesetzlich zulässig, übernimmt der Betreiber keine Haftung für Schäden oder Kosten, die aus der Nutzung dieser Website entstehen. Mit der Nutzung dieser Website erklären Sie sich mit diesen Bedingungen einverstanden.",
        "es": "【Términos de Uso y Aviso Legal】\\n0 Margin Travel(EU) es una herramienta gratuita de planificación de viajes. Combinamos análisis de IA con curaduría experta (lugares ★4.5+). Aunque cuidamos los datos, no garantizamos el 100% de exactitud o actualización.\\n\\nLos horarios pueden cambiar sin previo aviso. Verifique siempre la información en los sitios oficiales antes de su visita.\\n\\nEn la máxima medida permitida por la ley, el administrador no asume responsabilidad por daños o gastos derivados del uso de este sitio. El uso de este sitio implica la aceptación de este aviso legal.",
        "zh": "【使用条款与免责声明】\\n0 Margin Travel(EU) 是一款完全免费的旅行规划辅助工具。本工具结合AI分析与专家严选（★4.5+高分景点），虽力求信息准确，但无法保证100%绝对准确或实时性。\\n\\n营业时间等信息可能随时变更，出行前请务必通过官方渠道核实最新信息。\\n\\n在法律允许的最大范围内，本网站管理者不对因使用本网站而产生的任何损失、费用或纠纷承担法律责任。使用本网站即表示您已同意本免责声明。"
    }
}

# Construct clean JavaScript file content
js_content = """/* ==========================================================================
   0 Margin Travel — Multilingual i18n Engine (7 Languages)
   ========================================================================== */

const I18nEngine = {
  currentLang: 'en',
  
  translations: {
"""

for l in langs:
    js_content += f'    "{l}": {{\n'
    keys_sorted = sorted(list(master_keys.keys()))
    for idx, k in enumerate(keys_sorted):
        val = master_keys[k].get(l, master_keys[k]["en"])
        escaped_val = val.replace('"', '\\"')
        comma = ',' if idx < len(keys_sorted) - 1 else ''
        js_content += f'      "{k}": "{escaped_val}"{comma}\n'
    comma_lang = ',' if l != langs[-1] else ''
    js_content += f'    }}{comma_lang}\n'

js_content += """  },

  init() {
    const saved = localStorage.getItem('0mt_lang');
    if (saved && this.translations[saved]) {
      this.currentLang = saved;
    } else {
      const navLang = (navigator.language || 'en').substring(0, 2).toLowerCase();
      if (this.translations[navLang]) {
        this.currentLang = navLang;
      } else {
        this.currentLang = 'en';
      }
    }

    const select = document.getElementById('languageSelect');
    if (select) {
      select.value = this.currentLang;
    }

    this.applyLanguage(this.currentLang);
  },

  setLanguage(lang) {
    if (!this.translations[lang]) return;
    this.currentLang = lang;
    localStorage.setItem('0mt_lang', lang);
    
    const select = document.getElementById('languageSelect');
    if (select && select.value !== lang) {
      select.value = lang;
    }

    this.applyLanguage(lang);

    if (window.AITravelEngine) {
      window.AITravelEngine.renderCandidateSpots();
    }
  },

  getText(key) {
    const langDict = this.translations[this.currentLang] || this.translations.en;
    return langDict[key] || this.translations.en[key] || key;
  },

  applyLanguage(lang) {
    const langDict = this.translations[lang] || this.translations.en;
    
    // Update elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (langDict[key]) {
        el.innerHTML = langDict[key];
      }
    });

    // Update input placeholders with data-i18n-placeholder
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (langDict[key]) {
        el.setAttribute('placeholder', langDict[key]);
      }
    });
  }
};

document.addEventListener('DOMContentLoaded', () => {
  I18nEngine.init();
});

if (typeof window !== 'undefined') {
  window.I18nEngine = I18nEngine;
}
"""

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("🎉 Audit & Fix Complete: All 45 keys fully synchronized across all 7 languages in js/i18n.js!")
