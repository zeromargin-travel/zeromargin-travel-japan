import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

feedback_i18n = {
    'en': {
        'btn.reportError': '💬 Report Spot Error / Feedback',
        'btn.terms': '⚖️ Terms & Disclaimer',
        'modal.feedbackTitle': '💬 Feedback & Spot Error Report',
        'modal.feedbackSub': 'Notice an error in spot details, opening hours, or have a suggestion? Let us know!',
        'modal.spotNameLabel': 'Spot Name / City:',
        'modal.spotNamePlaceholder': 'e.g. Louvre Museum / Paris',
        'modal.detailsLabel': 'Correction Details / Message:',
        'modal.detailsPlaceholder': 'Describe the incorrect information or your feedback...',
        'modal.emailLabel': 'Your Email (Optional):',
        'modal.emailPlaceholder': 'your.email@example.com (if you want a reply)',
        'modal.sendBtn': '✉️ Send Feedback & Error Report',
        'modal.termsTitle': '⚖️ Terms of Use & Liability Disclaimer',
        'modal.termsBody': 'While 0 Margin Travel(EU) strives to provide accurate spot information, opening hours, and routes, we do not guarantee complete accuracy or timeliness. Please verify official venue channels prior to travel. The site administrator accepts no liability for any losses, damages, or inconvenience resulting from the use of this website. Use at your own discretion.'
    },
    'ja': {
        'btn.reportError': '💬 スポット誤り指摘・ご意見',
        'btn.terms': '⚖️ 利用規約・免責事項',
        'modal.feedbackTitle': '💬 ご意見・スポット情報の誤りを指摘',
        'modal.feedbackSub': 'スポット情報の誤り、営業時間の間違い、改善のご意見などをお気軽にお寄せください。',
        'modal.spotNameLabel': '対象のスポット名・都市名:',
        'modal.spotNamePlaceholder': '例: ルーブル美術館 / パリ',
        'modal.detailsLabel': '誤りの内容・ご意見:',
        'modal.detailsPlaceholder': '間違っている情報や修正案、ご意見をご記入ください...',
        'modal.emailLabel': 'ご連絡先メールアドレス（任意）:',
        'modal.emailPlaceholder': 'your.email@example.com （返信をご希望の場合）',
        'modal.sendBtn': '✉️ ご意見・誤り指摘を送信する',
        'modal.termsTitle': '⚖️ 利用規約・免責事項',
        'modal.termsBody': '当サイト「0 Margin Travel(EU)」で提供するスポット情報、営業時間、位置情報、ルート案内等の正確性については細心の注意を払っておりますが、その完全性や最新性を保証するものではありません。実際の訪問に際しては、事前に施設公式情報等をご確認ください。当サイトの利用によって生じた損害・トラブル・不利益等について、当管理者は一切の責任を負いかねます。あらかじめご了承の上、自己責任にてご利用ください。'
    },
    'nl': {
        'btn.reportError': '💬 Fout Melden / Feedback',
        'btn.terms': '⚖️ Voorwaarden & Disclaimer',
        'modal.feedbackTitle': '💬 Feedback & Fout Melden',
        'modal.feedbackSub': 'Foutje gezien in een plek of openingstijden? Laat het ons weten!',
        'modal.spotNameLabel': 'Naam van de plek / Stad:',
        'modal.spotNamePlaceholder': 'bijv. Rijksmuseum / Amsterdam',
        'modal.detailsLabel': 'Details van de fout / Bericht:',
        'modal.detailsPlaceholder': 'Beschrijf de onjuiste informatie of je suggestie...',
        'modal.emailLabel': 'Je e-mailadres (optioneel):',
        'modal.emailPlaceholder': 'jouw.email@example.com',
        'modal.sendBtn': '✉️ Feedback Versturen',
        'modal.termsTitle': '⚖️ Gebruiksvoorwaarden & Disclaimer',
        'modal.termsBody': 'Hoewel 0 Margin Travel(EU) streeft naar nauwkeurige informatie, garanderen wij geen volledige juistheid. Controleer altijd de officiële bronnen voor je bezoek. De beheerder is niet aansprakelijk voor schade of ongemak voortvloeiend uit het gebruik van deze website.'
    },
    'fr': {
        'btn.reportError': '💬 Signaler une Erreur / Avis',
        'btn.terms': '⚖️ Conditions & Avertissement',
        'modal.feedbackTitle': '💬 Retours & Signalement d\'Erreur',
        'modal.feedbackSub': 'Remarqué une erreur sur un lieu ou des horaires ? Dites-le nous !',
        'modal.spotNameLabel': 'Nom du lieu / Ville :',
        'modal.spotNamePlaceholder': 'ex. Musée du Louvre / Paris',
        'modal.detailsLabel': 'Détails de l\'erreur / Message :',
        'modal.detailsPlaceholder': 'Décrivez les informations incorrectes ou vos suggestions...',
        'modal.emailLabel': 'Votre e-mail (facultatif) :',
        'modal.emailPlaceholder': 'votre.email@example.com',
        'modal.sendBtn': '✉️ Envoyer votre Signalement',
        'modal.termsTitle': '⚖️ Conditions d\'Utilisation & Avertissement',
        'modal.termsBody': 'Bien que 0 Margin Travel(EU) s\'efforce de fournir des informations exactes, nous ne garantissons pas leur exhaustivité. Veuillez vérifier auprès des sites officiels avant votre visite. L\'administrateur décline toute responsabilité pour les dommages résultant de l\'utilisation de ce site.'
    },
    'de': {
        'btn.reportError': '💬 Fehler Melden / Feedback',
        'btn.terms': '⚖️ Bedingungen & Haftungsausschluss',
        'modal.feedbackTitle': '💬 Feedback & Fehler Melden',
        'modal.feedbackSub': 'Fehler bei einem Ort oder den Öffnungszeiten entdeckt? Teilen Sie es uns mit!',
        'modal.spotNameLabel': 'Name des Ortes / Stadt:',
        'modal.spotNamePlaceholder': 'z.B. Brandenburger Tor / Berlin',
        'modal.detailsLabel': 'Fehlerbeschreibung / Nachricht:',
        'modal.detailsPlaceholder': 'Beschreiben Sie die fehlerhaften Informationen...',
        'modal.emailLabel': 'Ihre E-Mail (optional):',
        'modal.emailPlaceholder': 'ihre.email@example.com',
        'modal.sendBtn': '✉️ Feedback Absenden',
        'modal.termsTitle': '⚖️ Nutzungsbedingungen & Haftungsausschluss',
        'modal.termsBody': 'Obwohl 0 Margin Travel(EU) um Genauigkeit bemüht ist, übernehmen wir keine Gewähr für die Vollständigkeit. Bitte prüfen Sie vor Ihrer Reise die offiziellen Angaben. Der Betreiber haftet nicht für Schäden, die aus der Nutzung dieser Website entstehen.'
    },
    'es': {
        'btn.reportError': '💬 Informar Error / Opinión',
        'btn.terms': '⚖️ Términos y Aviso Legal',
        'modal.feedbackTitle': '💬 Comentarios e Informe de Errores',
        'modal.feedbackSub': '¿Vio un error en los detalles o horarios de un lugar? ¡Avísanos!',
        'modal.spotNameLabel': 'Nombre del lugar / Ciudad:',
        'modal.spotNamePlaceholder': 'ej. Museo del Prado / Madrid',
        'modal.detailsLabel': 'Detalles del error / Mensaje:',
        'modal.detailsPlaceholder': 'Describa la información incorrecta o su sugerencia...',
        'modal.emailLabel': 'Su correo electrónico (opcional):',
        'modal.emailPlaceholder': 'su.email@example.com',
        'modal.sendBtn': '✉️ Enviar Comentario',
        'modal.termsTitle': '⚖️ Términos de Uso y Aviso Legal',
        'modal.termsBody': 'Aunque 0 Margin Travel(EU) se esfuerza por ofrecer información precisa, no garantizamos su total exactitud. Verifique los canales oficiales antes de su visita. El administrador no asume responsabilidad por pérdidas o inconvenientes derivados del uso de este sitio.'
    },
    'zh': {
        'btn.reportError': '💬 纠错与意见反馈',
        'btn.terms': '⚖️ 免责声明与使用条款',
        'modal.feedbackTitle': '💬 意见反馈与景点信息纠错',
        'modal.feedbackSub': '发现景点名称、营业时间有误或有改进建议？欢迎随时告知！',
        'modal.spotNameLabel': '涉及景点名称 / 城市:',
        'modal.spotNamePlaceholder': '例如: 卢浮宫 / 巴黎',
        'modal.detailsLabel': '纠错详情 / 建议内容:',
        'modal.detailsPlaceholder': '请详细描述错误信息或您的宝贵建议...',
        'modal.emailLabel': '您的联系邮箱（可选）:',
        'modal.emailPlaceholder': 'your.email@example.com',
        'modal.sendBtn': '✉️ 提交意见与纠错',
        'modal.termsTitle': '⚖️ 使用条款与免责声明',
        'modal.termsBody': '尽管0 Margin Travel(EU)力求提供准确的景点和路线信息，但不对其完整性或时效性作绝对保证。出行前请务必核实官方最新信息。对于因使用本网站而产生的任何损失或不便，本站管理者概不承担法律责任。请您自行斟酌使用。'
    }
}

sections = re.split(r'("(?:en|nl|ja|es|zh|fr|de)":\s*\{)', content)

new_content = sections[0]
for i in range(1, len(sections), 2):
    header = sections[i]
    body = sections[i+1]
    lang = header[1:3]
    if lang in feedback_i18n:
        for k, v in feedback_i18n[lang].items():
            pattern = rf'"{re.escape(k)}":\s*"[^"]*"'
            replacement = f'"{k}": "{v}"'
            if re.search(pattern, body):
                body = re.sub(pattern, replacement, body)
            else:
                body = f'\n        "{k}": "{v}",' + body
    new_content += header + body

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("🎉 Successfully added Feedback Form & Terms i18n keys across 7 languages!")
