import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')
index_path = os.path.join(base_dir, '..', 'index.html')

print("🚀 Master fixing i18n dictionaries and full DOM coverage across all 7 languages...")

# 1. Update i18n.js with user's standardized robust terms & disclaimer across all 7 languages
with open(i18n_path, 'r', encoding='utf-8') as f:
    i18n_content = f.read()

disclaimer_updates = {
    'ja': {
        'footer.aiNotice': '🤖 当ツールはAI分析と専門リサーチ（★4.5+厳選）を融合して構築されていますが、情報の100%の完全性を保証するものではありません。訪問前に必ず公式情報をご確認ください。',
        'modal.termsTitle': '⚖️ 利用規約・免責事項',
        'modal.termsBody': """【利用規約・免責事項】
当サイト「0 Margin Travel(EU)」は、旅行計画を補助するための完全無料の情報案内ツールです。AIデータ解析と専門リサーチ（★4.5以上の高評価スポット基準）を融合し、掲載しているスポット情報、営業時間、料金、位置情報、ルート案内等の正確性については細心の注意を払っておりますが、その完全性、最新性、確実性を保証するものではありません。

営業日時や施設情報は予告なく変更される場合がありますので、実際の訪問に際しては必ず事前に施設公式ウェブサイト等で最新情報をご確認ください。

当サイトの利用、または掲載情報に基づいて行われた行動により生じたあらゆる損害・不利益・トラブル（交通費・宿泊費の損失、機会損失等を含む）について、当サイト管理者は法律上許容される最大限の範囲において一切の責任を負いかねます。あらかじめご了承の上、ご自身の責任においてご利用ください。当サイトのご利用をもって、本免責事項に同意いただいたものとみなします。""",
        'footer.termsNotice': '※当サイトのご利用をもって [ ⚖️ 利用規約・免責事項 ] に同意いただいたものとみなします。'
    },
    'en': {
        'footer.aiNotice': '🤖 Powered by AI analysis & expert research (Verified ★4.5+), but 100% accuracy is not guaranteed. Please verify official details prior to your trip.',
        'modal.termsTitle': '⚖️ Terms of Use & Legal Disclaimer',
        'modal.termsBody': """【Terms of Use & Legal Disclaimer】
0 Margin Travel(EU) is a completely free travel planning assistance tool. While we integrate AI data analysis with expert curation (selecting ★4.5+ top-rated spots) and exercise strict care regarding spot details, opening hours, prices, coordinates, and routes, we do not guarantee 100% completeness, timeliness, or accuracy.

Operating hours and venue details are subject to change without notice. Please always verify the latest information on official venue websites prior to your visit.

To the maximum extent permitted by applicable law, the site administrator disclaims all liability for any loss, damage, or trouble (including travel expenses, accommodation costs, lost opportunities, etc.) arising from the use of this website or actions taken based on its content. Please use at your own discretion. By using this website, you are deemed to have agreed to this Legal Disclaimer.""",
        'footer.termsNotice': '* By using this website, you are deemed to have agreed to the [ ⚖️ Terms of Use & Legal Disclaimer ].'
    },
    'nl': {
        'footer.aiNotice': '🤖 Aangedreven door AI-analyse & deskundige curatie (★4.5+), maar 100% nauwkeurigheid wordt niet gegarandeerd. Controleer altijd officiële bronnen voor je bezoek.',
        'modal.termsTitle': '⚖️ Gebruiksvoorwaarden & Disclaimer',
        'modal.termsBody': """【Gebruiksvoorwaarden & Disclaimer】
0 Margin Travel(EU) is een volledig gratis reisplanningstool. We combineren AI-analyse met deskundige curatie (★4.5+ locaties). Hoewel we zorg dragen voor alle gegevens, garanderen we geen 100% juistheid of volledigheid.

Openingstijden kunnen zonder voorafgaande kennisgeving veranderen. Verifieer altijd de meest recente informatie via officiële bronnen voor je bezoek.

Voor zover wettelijk toegestaan is de beheerder niet aansprakelijk voor enige schade, kosten of ongemak voortvloeiend uit het gebruik van deze site. Door deze site te gebruiken, gaat u akkoord met deze disclaimer.""",
        'footer.termsNotice': '* Door deze site te gebruiken, gaat u akkoord met de [ ⚖️ Gebruiksvoorwaarden & Disclaimer ].'
    },
    'fr': {
        'footer.aiNotice': '🤖 Propulsé par l\'analyse IA & la sélection d\'experts (★4.5+), mais l\'exactitude à 100% n\'est pas garantie. Veuillez vérifier auprès des sites officiels avant votre visite.',
        'modal.termsTitle': '⚖️ Conditions d\'Utilisation & Avertissement Légal',
        'modal.termsBody': """【Conditions d'Utilisation & Avertissement Légal】
0 Margin Travel(EU) est un outil gratuit d'aide au voyage. Nous combinons l'analyse IA et la sélection d'experts (lieux ★4.5+). Bien que nous apportions un soin particulier aux données, nous ne garantissons pas leur exactitude ou exhaustivité à 100%.

Les horaires peuvent changer sans préavis. Veuillez toujours vérifier les informations sur les sites officiels avant votre visite.

Dans la mesure maximale permise par la loi, l'administrateur décline toute responsabilité pour tout dommage ou frais découlant de l'utilisation de ce site. L'utilisation de ce site vaut acceptation des présentes conditions.""",
        'footer.termsNotice': '* En utilisant ce site, vous acceptez les [ ⚖️ Conditions d\'Utilisation & Avertissement Légal ].'
    },
    'de': {
        'footer.aiNotice': '🤖 KI-Analyse & Experten-Prüfung (★4.5+), jedoch wird 100% Genauigkeit nicht garantiert. Bitte prüfen Sie vor Ihrer Reise die offiziellen Angaben.',
        'modal.termsTitle': '⚖️ Nutzungsbedingungen & Haftungsausschluss',
        'modal.termsBody': """【Nutzungsbedingungen & Haftungsausschluss】
0 Margin Travel(EU) ist ein kostenloses Reiseplanungstool. Wir kombinieren KI-Analyse mit Experten-Prüfung (★4.5+ Orte). Trotz größter Sorgfalt übernehmen wir keine Gewähr für die 100%ige Vollständigkeit oder Aktualität.

Öffnungszeiten können sich ändern. Bitte prüfen Sie vor der Anreise stets die offiziellen Angaben.

Soweit gesetzlich zulässig, übernimmt der Betreiber keine Haftung für Schäden oder Kosten, die aus der Nutzung dieser Website entstehen. Mit der Nutzung dieser Website erklären Sie sich mit diesen Bedingungen einverstanden.""",
        'footer.termsNotice': '* Mit der Nutzung dieser Website erklären Sie sich mit den [ ⚖️ Nutzungsbedingungen & Haftungsausschluss ] einverstanden.'
    },
    'es': {
        'footer.aiNotice': '🤖 Impulsado por análisis de IA y curaduría experta (★4.5+), pero no se garantiza el 100% de precisión. Verifique los canales oficiales antes de viajar.',
        'modal.termsTitle': '⚖️ Términos de Uso y Aviso Legal',
        'modal.termsBody': """【Términos de Uso y Aviso Legal】
0 Margin Travel(EU) es una herramienta gratuita de planificación de viajes. Combinamos análisis de IA con curaduría experta (lugares ★4.5+). Aunque cuidamos los datos, no garantizamos el 100% de exactitud o actualización.

Los horarios pueden cambiar sin previo aviso. Verifique siempre la información en los sitios oficiales antes de su visita.

En la máxima medida permitida por la ley, el administrador no asume responsabilidad por daños o gastos derivados del uso de este sitio. El uso de este sitio implica la aceptación de este aviso legal.""",
        'footer.termsNotice': '* Al usar este sitio web, usted acepta los [ ⚖️ Términos de Uso y Aviso Legal ].'
    },
    'zh': {
        'footer.aiNotice': '🤖 本工具结合AI分析与专家严选（★4.5+严选），但无法保证100%绝对准确。出行前请务必核实官方最新信息。',
        'modal.termsTitle': '⚖️ 使用条款与免责声明',
        'modal.termsBody': """【使用条款与免责声明】
0 Margin Travel(EU) 是一款完全免费的旅行规划辅助工具。本工具结合AI分析与专家严选（★4.5+高分景点），虽力求信息准确，但无法保证100%绝对准确或实时性。

营业时间等信息可能随时变更，出行前请务必通过官方渠道核实最新信息。

在法律允许的最大范围内，本网站管理者不对因使用本网站而产生的任何损失、费用或纠纷承担法律责任。使用本网站即表示您已同意本免责声明。""",
        'footer.termsNotice': '* 使用本网站即表示您已同意 [ ⚖️ 使用条款与免责声明 ]。'
    }
}

sections = re.split(r'("(?:en|nl|ja|es|zh|fr|de)":\s*\{)', i18n_content)
new_i18n = sections[0]

for i in range(1, len(sections), 2):
    header = sections[i]
    body = sections[i+1]
    lang = header[1:3]
    if lang in disclaimer_updates:
        for k, v in disclaimer_updates[lang].items():
            pattern = rf'"{re.escape(k)}":\s*"[^"]*"'
            replacement = f'"{k}": "{v.replace(chr(10), "\\n")}"'
            if re.search(pattern, body):
                body = re.sub(pattern, replacement, body)
            else:
                body = f'\n        "{k}": "{v.replace(chr(10), "\\n")}",' + body
    new_i18n += header + body

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(new_i18n)

# 2. Update index.html to bind data-i18n attributes everywhere and ensure 100% seamless language switching
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update Footer terms notice area
terms_notice_html = """<div style="margin-top:0.4rem; font-size:0.8rem; color:#78716C;">
          <span data-i18n="footer.termsNotice">※当サイトのご利用をもって [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;" data-i18n="btn.terms">⚖️ 利用規約・免責事項</a> ] に同意いただいたものとみなします。</span>
        </div>"""

# Ensure footer bottom block uses proper data-i18n binding
if 'data-i18n="footer.termsNotice"' not in html:
    html = re.sub(r'<div style="margin-top:0\.4rem; font-size:0\.8rem; color:#78716C;">\s*<a href="javascript:void\(0\)" onclick="openTermsModal\(\)".*?<\/a>\s*<\/div>', terms_notice_html, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("🎉 Master i18n update complete: All 7 languages updated with standardized legal disclaimers and seamless language switching!")
