import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

robust_legal_data = {
    'ja': {
        'footer.aiNotice': '🤖 当ツールはAI分析と専門リサーチ（★4.5+厳選）を融合して構築されていますが、情報の100%の完全性を保証するものではありません。訪問前に必ず公式情報をご確認ください。',
        'modal.termsTitle': '⚖️ 利用規約・免責事項 (Legal Disclaimer & Terms)',
        'modal.termsBody': """【1. サービスの性質とAIコンテンツ・監査について】
当サイト「0 Margin Travel(EU)」は、最新のAIデータ解析と人の手によるリサーチ（★4.5以上の高評価スポット基準）を融合して開発された「無料の情報案内・ルート作成補助ツール」です。掲載情報の精度向上および監査には万全を期しておりますが、AIの性質および現地のリアルタイムな状況変化（店舗の移転、臨時休業、営業時間・料金の変更等）により、100%の完全性、正確性、最新性を保証するものではありません。

【2. 公式情報の事前確認義務と自己責任原則】
当サイトで提供されるスポット情報、位置情報、営業時間、交通ルート案内等は参考情報に過ぎません。利用者は、実際の訪問や行動に先立ち、必ず各施設・店舗・交通機関の公式ウェブサイトや最新の公式案内等をご自身で確認する義務を負うものとします。当サイトの利用、および掲載情報に基づいて行われた一切の行動は、利用者ご自身の自己責任において行われるものとします。

【3. 責任の最大免責（損害賠償義務の不発生）】
当サイトは完全無償で提供されるサービスであり、利用者が当サイトを利用したこと、または利用できなかったこと、掲載情報の誤り、遅延、欠落等に起因して被った一切の損害（交通費・宿泊キャンセル料・機会損失・損害賠償・身体的/精神的不利益・現地でのトラブル等を含むがこれらに限定されない）について、当サイトの提供者、開発者および管理者は、法律上許容される最大限の範囲において一切の法的責任および損害賠償義務を負いません。

【4. サービスの変更・中断・終了】
当サイトの掲載内容、機能、データベースは、利用者に予告することなく随時変更、追加、修正、または一時停止・終了される場合があります。

※当サイトをご利用いただくことで、本利用規約および免責事項のすべての条件に同意いただいたものとみなします。"""
    },
    'en': {
        'footer.aiNotice': '🤖 Powered by AI analysis & human curation (Verified ★4.5+), but 100% accuracy is not guaranteed. Please verify with official venue channels prior to your trip.',
        'modal.termsTitle': '⚖️ Terms of Use & Liability Disclaimer',
        'modal.termsBody': """【1. Nature of Service, AI Content & Curation】
0 Margin Travel(EU) is a free travel planning tool built by combining AI algorithms with human verification (selecting ★4.5+ top-rated spots). While rigorous audits are conducted, due to the dynamic nature of travel information (sudden closures, schedule changes, relocations) and AI characteristics, 100% completeness, accuracy, or real-time timeliness is NOT guaranteed.

【2. Duty of Pre-Visit Verification & Self-Responsibility】
All spot details, opening hours, coordinates, and route suggestions are provided solely as informative references. Users bear the sole obligation to verify details via official venue or transportation channels prior to actual travel. Any action taken based on the information provided on this site is performed entirely at the user's own risk and discretion.

【3. Maximum Disclaimer of Liability】
This website is provided free of charge. To the maximum extent permitted by applicable law, the site administrator, developers, and providers shall NOT be held liable for any direct, indirect, incidental, consequential, special, or punitive damages (including but not limited to travel costs, accommodation cancellation fees, lost opportunities, personal disputes, or inconvenience) arising out of or related to the use of, or inability to use, this service or reliance on any information presented.

【4. Modifications & Termination】
The contents, features, and database of this platform may be modified, updated, suspended, or terminated at any time without prior notice.

* By accessing and using this site, you acknowledge and agree to all terms and conditions set forth in this Legal Disclaimer."""
    },
    'nl': {
        'footer.aiNotice': '🤖 Aangedreven door AI-analyse & menselijke curatie (★4.5+), maar 100% nauwkeurigheid wordt niet gegarandeerd. Controleer altijd de officiële bronnen voor je bezoek.',
        'modal.termsTitle': '⚖️ Gebruiksvoorwaarden & Disclaimer',
        'modal.termsBody': """【1. Aard van de dienst & AI-inhoud】
0 Margin Travel(EU) is een gratis reisplanningstool die AI-analyse combineert met menselijke controle (★4.5+ locaties). Hoewel wij sturen op nauwkeurigheid, wordt 100% volledigheid of realtime juistheid niet gegarandeerd.

【2. Verplichting tot controle & Eigen verantwoordelijkheid】
Alle informatie is uitsluitend ter referentie. Gebruikers zijn verplicht om openingstijden en details vooraf via officiële kanalen te verifiëren. Elk gebruik vindt plaats op eigen risico.

【3. Maximale uitsluiting van aansprakelijkheid】
Voor zover wettelijk toegestaan, is de beheerder niet aansprakelijk voor enige directe of indirecte schade (zoals reiskosten, annuleringskosten of gemiste kansen) voortvloeiend uit het gebruik van deze gratis website.

* Door gebruik te maken van deze site gaat u akkoord met deze voorwaarden."""
    },
    'fr': {
        'footer.aiNotice': '🤖 Propulsé par l\'analyse IA & la sélection humaine (★4.5+), mais l\'exactitude à 100% n\'est pas garantie. Veuillez vérifier auprès des sites officiels avant votre visite.',
        'modal.termsTitle': '⚖️ Conditions d\'Utilisation & Avertissement Légal',
        'modal.termsBody': """【1. Nature du service & Contenu IA】
0 Margin Travel(EU) est un outil gratuit combinant analyse IA et vérification humaine (lieux ★4.5+). L'exactitude ou l'exhaustivité à 100% ne peut être garantie en raison des changements fréquents sur le terrain.

【2. Obligation de vérification préalable & Responsabilité】
Toutes les informations sont fournies à titre indicatif. L'utilisateur a l'obligation de vérifier les détails auprès des canaux officiels avant son déplacement. L'utilisation du site se fait sous sa propre responsabilité.

【3. Exonération maximale de responsabilité】
Dans la mesure maximale permise par la loi, l'administrateur décline toute responsabilité pour tout dommage direct ou indirect (frais de transport, annulations, pertes d'opportunité) découlant de l'utilisation de ce service gratuit.

* L'utilisation de ce site vaut acceptation pleine et entière des présentes conditions."""
    },
    'de': {
        'footer.aiNotice': '🤖 KI-Analyse & menschliche Prüfung (★4.5+), jedoch wird 100% Genauigkeit nicht garantiert. Bitte prüfen Sie vor Ihrer Reise die offiziellen Angaben.',
        'modal.termsTitle': '⚖️ Nutzungsbedingungen & Haftungsausschluss',
        'modal.termsBody': """【1. Natur des Dienstes & KI-Inhalte】
0 Margin Travel(EU) ist ein kostenloses Planungstool, das KI-Analysen mit menschlicher Kuratierung (★4.5+ Orte) kombiniert. Eine 100%ige Vollständigkeit oder Aktualität wird nicht garantiert.

【2. Prüfungspflicht & Eigenverantwortung】
Alle Angaben dienen lediglich als Orientierung. Nutzer sind verpflichtet, Details vor der Anreise über offizielle Kanäle zu überprüfen. Die Nutzung erfolgt auf eigene Gefahr.

【3. Maximaler Haftungsausschluss】
Soweit gesetzlich zulässig, übernimmt der Betreiber keinerlei Haftung für direkte oder indirekte Schäden (z. B. Reisekosten, Stornogebühren oder entgangene Chancen) aus der Nutzung dieser kostenlosen Website.

* Mit der Nutzung dieser Website erklären Sie sich mit diesen Bedingungen einverstanden."""
    },
    'es': {
        'footer.aiNotice': '🤖 Impulsado por análisis de IA y selección humana (★4.5+), pero no se garantiza el 100% de precisión. Verifique los canales oficiales antes de viajar.',
        'modal.termsTitle': '⚖️ Términos de Uso y Aviso Legal',
        'modal.termsBody': """【1. Naturaleza del servicio y Contenido de IA】
0 Margin Travel(EU) es una herramienta gratuita que combina análisis de IA con verificación humana (lugares ★4.5+). No se garantiza el 100% de exactitud o actualización en tiempo real.

【2. Obligación de verificación previa y Auto-responsabilidad】
Toda la información es meramente orientativa. El usuario tiene la obligación de verificar los detalles a través de canales oficiales antes de viajar. El uso del sitio es bajo su propio riesgo.

【3. Exención máxima de responsabilidad】
En la máxima medida permitida por la ley, el administrador no asumirá responsabilidad por daños directos o indirectos (gastos de viaje, cancelación, pérdidas de oportunidad) derivados del uso de este sitio gratuito.

* El uso de este sitio implica la aceptación total de estos términos."""
    },
    'zh': {
        'footer.aiNotice': '🤖 本工具结合AI分析与人工精心筛选（★4.5+严选），但无法保证100%绝对准确。出行前请务必核实官方最新信息。',
        'modal.termsTitle': '⚖️ 使用条款与法律免责声明',
        'modal.termsBody': """【1. 服务性质与AI生成说明】
0 Margin Travel(EU) 是一款结合最新AI算法分析与人工核实（★4.5+高分景点严选）的免费旅行规划辅助工具。尽管我们力求严谨，但受AI技术特性及当地实时动态（如临时闭馆、营业时间变动、搬迁等）影响，无法保证信息100%绝对准确、完整或实时更新。

【2. 出行前核实义务与自主责任原则】
本网站提供的所有景点、坐标、营业时间及路线规划仅供参考。用户在实际出行前，有义务通过景点或交通机构的官方渠道核实最新信息。基于本网站信息所做出的任何行为均由用户自行承担责任。

【3. 法律允许的最大限度免责声明】
本服务为完全免费提供。在法律允许的最大范围内，本网站管理者及开发人员不对因使用或无法使用本服务、或依赖本网站信息而产生的任何直接、间接、附带或衍生损失（包括但不限于交通费、退订损失、机会损失等）承担任何法律责任或赔偿义务。

* 使用本网站即表示您已阅读、理解并同意本免责声明的所有条款。"""
    }
}

sections = re.split(r'("(?:en|nl|ja|es|zh|fr|de)":\s*\{)', content)

new_content = sections[0]
for i in range(1, len(sections), 2):
    header = sections[i]
    body = sections[i+1]
    lang = header[1:3]
    if lang in robust_legal_data:
        for k, v in robust_legal_data[lang].items():
            pattern = rf'"{re.escape(k)}":\s*"[^"]*"'
            replacement = f'"{k}": "{v}"'
            if re.search(pattern, body):
                body = re.sub(pattern, replacement, body)
            else:
                body = f'\n        "{k}": "{v}",' + body
    new_content += header + body

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("🎉 Successfully injected robust legal disclaimers and footer AI notices across all 7 languages!")
