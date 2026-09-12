import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
i18n_path = os.path.join(base_dir, '..', 'js', 'i18n.js')

with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

terms_notice_with_links = {
    'ja': '※当サイトのご利用をもって [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;">⚖️ 利用規約・免責事項</a> ] に同意いただいたものとみなします。',
    'en': '* By using this website, you are deemed to have agreed to the [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;">⚖️ Terms of Use & Legal Disclaimer</a> ].',
    'nl': '* Door deze site te gebruiken, gaat u akkoord met de [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;">⚖️ Gebruiksvoorwaarden & Disclaimer</a> ].',
    'fr': '* En utilisant ce site, vous acceptez les [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;">⚖️ Conditions d\'Utilisation & Avertissement Légal</a> ].',
    'de': '* Mit der Nutzung dieser Website erklären Sie sich mit den [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;">⚖️ Nutzungsbedingungen & Haftungsausschluss</a> ] einverstanden.',
    'es': '* Al usar este sitio web, usted acepta los [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;">⚖️ Términos de Uso y Aviso Legal</a> ].',
    'zh': '* 使用本网站即表示您已同意 [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;">⚖️ 使用条款与免责声明</a> ]。'
}

sections = re.split(r'("(?:en|nl|ja|es|zh|fr|de)":\s*\{)', content)
new_content = sections[0]

for i in range(1, len(sections), 2):
    header = sections[i]
    body = sections[i+1]
    lang = header[1:3]
    if lang in terms_notice_with_links:
        val = terms_notice_with_links[lang]
        pattern = r'"footer\.termsNotice":\s*"[^"]*"'
        replacement = f'"footer.termsNotice": "{val}"'
        if re.search(pattern, body):
            body = re.sub(pattern, replacement, body)
        else:
            body = f'\n        "footer.termsNotice": "{val}",' + body
    new_content += header + body

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("🎉 Successfully embedded html links in footer.termsNotice across all 7 languages!")
