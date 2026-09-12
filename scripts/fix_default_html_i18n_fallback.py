import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base_dir, '..', 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hardcoded Japanese in footer elements with neutral English fallbacks + exact data-i18n attributes
html = html.replace(
    '💬 スポット誤り指摘・ご意見',
    '💬 Report Spot Error / Feedback'
)

html = html.replace(
    '🤖 当ツールはAI分析と専門リサーチ（★4.5+厳選）を融合して構築されていますが、情報の100%の完全性を保証するものではありません。訪問前に必ず公式情報をご確認ください。',
    '🤖 Powered by AI analysis & expert research (Verified ★4.5+), but 100% accuracy is not guaranteed. Please verify official details prior to your trip.'
)

html = html.replace(
    '※当サイトのご利用をもって [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;" data-i18n="btn.terms">⚖️ 利用規約・免責事項</a> ] に同意いただいたものとみなします。',
    '* By using this website, you are deemed to have agreed to the [ <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;" data-i18n="btn.terms">⚖️ Terms of Use & Legal Disclaimer</a> ].'
)

# Check DOM load inline script in index.html to guarantee I18nEngine.init() runs immediately
load_script_old = """window.addEventListener('load', function() {"""
load_script_new = """window.addEventListener('DOMContentLoaded', function() {
      if (window.I18nEngine) {
        window.I18nEngine.init();
      }
    });
    window.addEventListener('load', function() {"""

if 'window.I18nEngine.init();' not in html:
    html = html.replace(load_script_old, load_script_new)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("🎉 Fixed default HTML fallbacks to neutral English and added DOMContentLoaded I18nEngine.init() call!")
