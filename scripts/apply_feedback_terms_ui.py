import os

base_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base_dir, '..', 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add prominent feedback button to Step 2 Header
step2_target = '<div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; margin-bottom:1.25rem;">'
step2_replacement = """<div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; margin-bottom:1.25rem;">
              <div style="display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap;">
                <div style="font-size:1.15rem; font-weight:800; color:var(--primary-forest); display:flex; align-items:center; gap:0.5rem;" class="font-serif">
                  <img src="assets/mascot.png" alt="Mascot Guide" style="width:34px; height:34px; object-fit:contain; filter:drop-shadow(1px 1px 2px rgba(0,0,0,0.12));">
                  <span>2️⃣</span> <span data-i18n="step2.title">Step 2: Pick Your Spots — Handpick your favorites from Verified ★4.5+ places</span>
                </div>
                <!-- Prominent Feedback / Spot Error Button -->
                <button type="button" onclick="openFeedbackModal()" style="background:#FFF7ED; color:#C2410C; border:1.5px solid #292524; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.82rem; font-weight:800; box-shadow:2px 2px 0px #292524; cursor:pointer; transition:transform 0.15s ease;" data-i18n="btn.reportError">
                  💬 スポット誤り指摘・ご意見
                </button>
              </div>"""

if 'data-i18n="btn.reportError"' not in html:
    # Replace step 2 header block
    m = html.find(step2_target)
    if m != -1:
        # Find closing of step2 header div
        m_end = html.find('<p data-i18n="step2.subtitle"', m)
        old_header_block = html[m:m_end]
        
        new_header_block = """<div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; margin-bottom:1.25rem;">
              <div style="display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap;">
                <div style="font-size:1.15rem; font-weight:800; color:var(--primary-forest); display:flex; align-items:center; gap:0.5rem;" class="font-serif">
                  <img src="assets/mascot.png" alt="Mascot Guide" style="width:34px; height:34px; object-fit:contain; filter:drop-shadow(1px 1px 2px rgba(0,0,0,0.12));">
                  <span>2️⃣</span> <span data-i18n="step2.title">Step 2: Pick Your Spots — Handpick your favorites from Verified ★4.5+ places</span>
                </div>
                <button type="button" onclick="openFeedbackModal()" style="background:#FFF7ED; color:#C2410C; border:1.5px solid #292524; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.82rem; font-weight:800; box-shadow:2px 2px 0px #292524; cursor:pointer;" data-i18n="btn.reportError">
                  💬 スポット誤り指摘・ご意見
                </button>
              </div>

              <span id="spotsCounterBadge" style="font-size:0.88rem; font-weight:700; background:#E0F2FE; color:#0369A1; padding:0.35rem 0.85rem; border-radius:9999px; border:1.5px solid #0284C7;">
                Selected: <strong>0 / 8</strong> (Max 8 Must-Visit Spots)
              </span>
            </div>\n\n            """
        html = html[:m] + new_header_block + html[m_end:]

# 2. Update Footer with prominent feedback button + subtle terms link
footer_target = '<div class="footer-bottom" style="margin-top:1.5rem; border-top:1px dashed #EADEC9; padding-top:1rem;">'
footer_replacement = """<div style="margin-top:1rem; display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap;">
        <button type="button" onclick="openFeedbackModal()" style="background:#FFF7ED; color:#C2410C; border:1.5px solid #292524; padding:0.5rem 1.15rem; border-radius:999px; font-size:0.88rem; font-weight:800; box-shadow:2px 2px 0px #292524; cursor:pointer;" data-i18n="btn.reportError">
          💬 スポット誤り指摘・ご意見
        </button>
      </div>

      <div class="footer-bottom" style="margin-top:1.25rem; border-top:1px dashed #EADEC9; padding-top:1rem;">
        <div>© 2026 0 Margin EU Travel Platform. (Mobile & PC Edition)</div>
        <div style="margin-top:0.4rem; font-size:0.8rem; color:#78716C;">
          <a href="javascript:void(0)" onclick="openTermsModal()" style="color:#78716C; text-decoration:underline; font-weight:600;" data-i18n="btn.terms">
            ⚖️ 利用規約・免責事項
          </a>
        </div>
      </div>"""

if footer_target in html:
    html = html.replace(footer_target, footer_replacement)

# 3. Add Modals before </body>
modals_html = """
  <!-- Feedback / Spot Error Report Modal -->
  <div id="feedbackModal" class="modal-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.55); z-index:99999; backdrop-filter:blur(3px); align-items:center; justify-content:center; padding:1rem;">
    <div style="background:#FAF7F2; border:2.5px solid #292524; border-radius:20px; width:100%; max-width:520px; padding:1.5rem; box-shadow:5px 5px 0px #292524; position:relative; max-height:90vh; overflow-y:auto;">
      <button type="button" onclick="closeFeedbackModal()" style="position:absolute; top:1rem; right:1rem; background:none; border:none; font-size:1.4rem; cursor:pointer; font-weight:bold; color:#78716C;">✕</button>
      
      <div style="font-size:1.15rem; font-weight:800; color:#047857; margin-bottom:0.4rem;" data-i18n="modal.feedbackTitle">
        💬 ご意見・スポット情報の誤りを指摘
      </div>
      <p style="font-size:0.85rem; color:#57534E; margin-bottom:1rem; line-height:1.4;" data-i18n="modal.feedbackSub">
        スポット情報の誤り、営業時間の間違い、改善のご意見などをお気軽にお寄せください。
      </p>

      <form action="https://formsubmit.co/yamasaki_jun@hotmail.com" method="POST">
        <input type="hidden" name="_subject" value="0 Margin Travel: New Spot Error / Feedback Report">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">

        <div style="margin-bottom:0.85rem;">
          <label style="display:block; font-size:0.82rem; font-weight:800; color:#292524; margin-bottom:0.25rem;" data-i18n="modal.spotNameLabel">対象のスポット名・都市名:</label>
          <input type="text" name="spot_name" required style="width:100%; padding:0.55rem 0.75rem; border:1.5px solid #292524; border-radius:10px; font-size:0.88rem; background:#FFF;" data-i18n-ph="modal.spotNamePlaceholder" placeholder="例: ルーブル美術館 / パリ">
        </div>

        <div style="margin-bottom:0.85rem;">
          <label style="display:block; font-size:0.82rem; font-weight:800; color:#292524; margin-bottom:0.25rem;" data-i18n="modal.detailsLabel">誤りの内容・ご意見:</label>
          <textarea name="details" required rows="4" style="width:100%; padding:0.55rem 0.75rem; border:1.5px solid #292524; border-radius:10px; font-size:0.88rem; background:#FFF; resize:vertical;" data-i18n-ph="modal.detailsPlaceholder" placeholder="間違っている情報や修正案をご記入ください..."></textarea>
        </div>

        <div style="margin-bottom:1.1rem;">
          <label style="display:block; font-size:0.82rem; font-weight:800; color:#292524; margin-bottom:0.25rem;" data-i18n="modal.emailLabel">ご連絡先メールアドレス（任意）:</label>
          <input type="email" name="user_email" style="width:100%; padding:0.55rem 0.75rem; border:1.5px solid #292524; border-radius:10px; font-size:0.88rem; background:#FFF;" data-i18n-ph="modal.emailPlaceholder" placeholder="your.email@example.com （返信をご希望の場合）">
        </div>

        <button type="submit" style="width:100%; background:#047857; color:#FFF; border:2px solid #292524; padding:0.7rem; border-radius:12px; font-size:0.95rem; font-weight:800; cursor:pointer; box-shadow:3px 3px 0px #292524;" data-i18n="modal.sendBtn">
          ✉️ ご意見・誤り指摘を送信する
        </button>
      </form>
    </div>
  </div>

  <!-- Terms of Use & Liability Disclaimer Modal -->
  <div id="termsModal" class="modal-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.55); z-index:99999; backdrop-filter:blur(3px); align-items:center; justify-content:center; padding:1rem;">
    <div style="background:#FAF7F2; border:2.5px solid #292524; border-radius:20px; width:100%; max-width:540px; padding:1.5rem; box-shadow:5px 5px 0px #292524; position:relative; max-height:85vh; overflow-y:auto;">
      <button type="button" onclick="closeTermsModal()" style="position:absolute; top:1rem; right:1rem; background:none; border:none; font-size:1.4rem; cursor:pointer; font-weight:bold; color:#78716C;">✕</button>
      
      <div style="font-size:1.15rem; font-weight:800; color:#047857; margin-bottom:0.75rem; border-bottom:1.5px dashed #CBD5E1; padding-bottom:0.5rem;" data-i18n="modal.termsTitle">
        ⚖️ 利用規約・免責事項
      </div>
      
      <div style="font-size:0.88rem; color:#44403C; line-height:1.6; white-space:pre-wrap;" data-i18n="modal.termsBody">
        当サイト「0 Margin Travel(EU)」で提供するスポット情報、営業時間、位置情報、ルート案内等の正確性については細心の注意を払っておりますが、その完全性や最新性を保証するものではありません。
        実際の訪問に際しては、事前に施設公式情報等をご確認ください。当サイトの利用によって生じた損害・トラブル・不利益等について、当管理者は一切の責任を負いかねます。あらかじめご了承の上、自己責任にてご利用ください。
      </div>

      <div style="margin-top:1.25rem; text-align:right;">
        <button type="button" onclick="closeTermsModal()" style="background:#292524; color:#FFF; border:none; padding:0.45rem 1.25rem; border-radius:10px; font-size:0.85rem; font-weight:700; cursor:pointer;">
          OK
        </button>
      </div>
    </div>
  </div>

  <script>
    function openFeedbackModal() {
      const m = document.getElementById('feedbackModal');
      if (m) m.style.display = 'flex';
    }
    function closeFeedbackModal() {
      const m = document.getElementById('feedbackModal');
      if (m) m.style.display = 'none';
    }
    function openTermsModal() {
      const m = document.getElementById('termsModal');
      if (m) m.style.display = 'flex';
    }
    function closeTermsModal() {
      const m = document.getElementById('termsModal');
      if (m) m.style.display = 'none';
    }
  </script>
"""

if 'id="feedbackModal"' not in html:
    html = html.replace('</body>', modals_html + '\n</body>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("🎉 Successfully applied prominent Feedback button and subtle Terms link/modals in index.html!")
