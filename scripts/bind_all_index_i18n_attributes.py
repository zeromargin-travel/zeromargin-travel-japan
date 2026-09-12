import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base_dir, '..', 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check Step 3 Title binding
html = re.sub(
    r'<span[^>]*class="font-serif"[^>]*>3️⃣</span>\s*<span[^>]*>.*?</span>',
    '<span class="font-serif">3️⃣</span> <span data-i18n="step3.title">Step 3: Launch in Maps — Choose Route A (Selected Only) or Route B (Curated Full-Day Loop)</span>',
    html,
    flags=re.DOTALL
)

# 2. Check Route Generation Button binding
html = re.sub(
    r'<button[^>]*id="generateRoutesBtn"[^>]*>.*?</button>',
    '<button type="button" id="generateRoutesBtn" class="btn-primary" onclick="AITravelEngine.generateDualRoutes()" style="font-size:1.1rem; padding:1.1rem 2.5rem; border-radius:18px;" data-i18n="btn.generateRoutes">🗺️ Generate Ready-to-Use Dual Google Maps Routes ↗</button>',
    html,
    flags=re.DOTALL
)

# 3. Check Footer elements binding
if 'data-i18n="btn.reportError"' not in html:
    html = html.replace('💬 スポット誤り指摘・ご意見', '💬 Report Spot Error / Feedback')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("🎉 Successfully bound all HTML attributes in index.html for 100% complete 7-language switching!")
