import os

base_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base_dir, '..', 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

ai_notice_html = """<p style="margin-top:1.1rem; max-width:840px; margin-left:auto; margin-right:auto; font-size:0.8rem; color:#78716C; line-height:1.5; background:#FFF; border:1.5px dashed #CBD5E1; padding:0.6rem 1rem; border-radius:12px; font-weight:500;" data-i18n="footer.aiNotice">
        🤖 当ツールはAI分析と専門リサーチ（★4.5+厳選）を融合して構築されていますが、情報の100%の完全性を保証するものではありません。訪問前に必ず公式情報をご確認ください。
      </p>"""

footer_bottom_pattern = '<div class="footer-bottom" style="margin-top:1.25rem;'

if 'data-i18n="footer.aiNotice"' not in html:
    if footer_bottom_pattern in html:
        html = html.replace(footer_bottom_pattern, ai_notice_html + '\n\n      ' + footer_bottom_pattern)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("🎉 Successfully inserted direct footer AI notice in index.html!")
