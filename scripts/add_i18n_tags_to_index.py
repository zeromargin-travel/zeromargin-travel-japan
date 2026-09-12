import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    (
        '<span>0 Margin Travel(EU): AI Route Planner & Multi-Stop Google Maps Navigation.</span>',
        '<span data-i18n="banner.text">✨ 0 Margin Travel(EU): AI Route Planner & Multi-Stop Google Maps Navigation.</span>'
    ),
    (
        '<span style="font-size:0.95rem; font-weight:800; color:var(--primary-forest);">Hi! I\'m your Travel Buddy 🍓🐉 — Let\'s plan your route!</span>',
        '<span data-i18n="hero.badge" style="font-size:0.95rem; font-weight:800; color:var(--primary-forest);">Hi! I\'m your Travel Buddy 🍓🐉 — Let\'s plan your route!</span>'
    ),
    (
        '<h1 class="hero-title" style="font-size:2.8rem; margin-bottom:0.75rem;">\n        Explore Europe Smarter with Instant Google Maps Routes.\n      </h1>',
        '<h1 class="hero-title" data-i18n="hero.title" style="font-size:2.8rem; margin-bottom:0.75rem;">Explore Europe Smarter with Instant Google Maps Routes.</h1>'
    ),
    (
        '<p style="font-size:1.3rem; font-weight:800; color:var(--primary-forest); margin-top:0.4rem; margin-bottom:0.85rem; font-family:var(--font-serif);">\n        Curated ★4.5+ spots. Zero planning fatigue.\n      </p>',
        '<p data-i18n="hero.tagline" style="font-size:1.3rem; font-weight:800; color:var(--primary-forest); margin-top:0.4rem; margin-bottom:0.85rem; font-family:var(--font-serif);">Curated ★4.5+ spots. Zero planning fatigue.</p>'
    ),
    (
        '<p class="hero-subtitle" style="max-width:720px; margin:0 auto 1.5rem; font-size:1.05rem;">\n        Pick your must-visit landmarks, bistros, and gems — get ready-to-use multi-stop Google Maps navigation in seconds.\n      </p>',
        '<p class="hero-subtitle" data-i18n="hero.subtitle" style="max-width:720px; margin:0 auto 1.5rem; font-size:1.05rem;">Pick your must-visit landmarks, bistros, and gems — get ready-to-use multi-stop Google Maps navigation in seconds.</p>'
    ),
    (
        '<button class="btn btn-primary" onclick="document.getElementById(\'aiPlanDestination\').scrollIntoView({behavior:\'smooth\'})">\n          🗺️ Create Custom Travel Route\n        </button>',
        '<button class="btn btn-primary" data-i18n="hero.cta" onclick="document.getElementById(\'aiPlanDestination\').scrollIntoView({behavior:\'smooth\'})">🗺️ Create Custom Travel Route</button>'
    ),
    (
        '<span class="paper-tape">Interactive Route Planner</span>',
        '<span class="paper-tape" data-i18n="planner.tape">Interactive Route Planner</span>'
    ),
    (
        '<h2 style="font-size:2.2rem; margin-top:0.4rem; margin-bottom:0.5rem;" class="font-serif">\n            Build Your Custom Day in 3 Simple Steps\n          </h2>',
        '<h2 data-i18n="planner.title" style="font-size:2.2rem; margin-top:0.4rem; margin-bottom:0.5rem;" class="font-serif">Build Your Custom Day in 3 Simple Steps</h2>'
    ),
    (
        '<p style="font-size:0.95rem; color:var(--text-secondary);">\n            Handpick your favorites from ★4.5+ verified places and launch ready-to-use multi-stop Google Maps navigation in 1 click!\n          </p>',
        '<p data-i18n="planner.subtitle" style="font-size:0.95rem; color:var(--text-secondary);">Handpick your favorites from ★4.5+ verified places and launch ready-to-use multi-stop Google Maps navigation in 1 click!</p>'
    ),
    (
        '<span>1️⃣</span> <span>Step 1: Choose Destination — Select your country & city</span>',
        '<span>1️⃣</span> <span data-i18n="step1.title">Step 1: Choose Destination — Select your country & city</span>'
    ),
    (
        '<label class="form-label">Country:</label>',
        '<label class="form-label" data-i18n="label.country">Country:</label>'
    ),
    (
        '<label class="form-label">City:</label>',
        '<label class="form-label" data-i18n="label.city">City:</label>'
    ),
    (
        '<label class="form-label">Area Zone:</label>',
        '<label class="form-label" data-i18n="label.areaZone">Area Zone:</label>'
    ),
    (
        '<option value="ALL" selected>✨ All Spots (City + Suburban)</option>',
        '<option value="ALL" selected data-i18n="area.all">✨ All Spots (City + Suburban)</option>'
    ),
    (
        '<option value="city">🏙️ City Center Spots</option>',
        '<option value="city" data-i18n="area.city">🏙️ City Center Spots</option>'
    ),
    (
        '<option value="suburban">🏞️ Suburban & Day Trips</option>',
        '<option value="suburban" data-i18n="area.suburban">🏞️ Suburban & Day Trips</option>'
    ),
    (
        '<span>2️⃣</span> <span>Step 2: Pick Your Spots — Handpick your favorites from Verified ★4.5+ places</span>',
        '<span>2️⃣</span> <span data-i18n="step2.title">Step 2: Pick Your Spots — Handpick your favorites from Verified ★4.5+ places</span>'
    ),
    (
        '<p style="font-size:0.9rem; color:var(--text-secondary); margin-bottom:1.25rem;">\n              Check the boxes for spots you definitely want to visit. The AI engine will generate both <strong>Route A (Selected Spots Only)</strong> and <strong>Route B (Full 1-Day AI Course)</strong> for Google Maps navigation!\n            </p>',
        '<p data-i18n="step2.subtitle" style="font-size:0.9rem; color:var(--text-secondary); margin-bottom:1.25rem;">Check the boxes for spots you definitely want to visit. The AI engine will generate both Route A (Selected Spots Only) and Route B (Full 1-Day AI Course) for Google Maps navigation!</p>'
    ),
    (
        '<span>🏨 Return Hotel / Stay</span>',
        '<span data-i18n="label.hotel">🏨 Return Hotel / Stay</span>'
    ),
    (
        '<span style="font-size:0.72rem; font-weight:600; color:#64748B;">(Optional — Appended as final destination to Route A & B)</span>',
        '<span data-i18n="label.hotelSub" style="font-size:0.72rem; font-weight:600; color:#64748B;">(Optional — Appended as final destination to Route A & B)</span>'
    ),
    (
        '<input type="text" id="aiPlanHotelInput" placeholder="e.g. Ritz Paris or your hotel address (leave blank to skip)" style="width:100%; padding:0.6rem 0.85rem; border-radius:10px; border:1.5px solid #CBD5E1; font-size:0.9rem; background:#FFF; font-family:var(--font-sans);">',
        '<input type="text" id="aiPlanHotelInput" data-i18n-placeholder="placeholder.hotel" placeholder="e.g. Ritz Paris or your hotel address (leave blank to skip)" style="width:100%; padding:0.6rem 0.85rem; border-radius:10px; border:1.5px solid #CBD5E1; font-size:0.9rem; background:#FFF; font-family:var(--font-sans);">'
    ),
    (
        '<span>3️⃣</span> <span>Step 3: Launch in Maps — Choose Route A (Selected only) or Route B (Curated full-day loop)</span>',
        '<span>3️⃣</span> <span data-i18n="step3.title">Step 3: Launch in Maps — Choose Route A (Selected only) or Route B (Curated full-day loop)</span>'
    ),
    (
        '<button type="submit" class="btn btn-emerald" style="padding:1.1rem 2.75rem; font-size:1.2rem; border-radius:16px;">\n              🗺️ Generate Ready-to-Use Dual Google Maps Routes ↗\n            </button>',
        '<button type="submit" class="btn btn-emerald" data-i18n="btn.generate" style="padding:1.1rem 2.75rem; font-size:1.2rem; border-radius:16px;">🗺️ Generate Ready-to-Use Dual Google Maps Routes ↗</button>'
    ),
    (
        '<span>Route Planner</span>',
        '<span data-i18n="mobile.planner">Route Planner</span>'
    ),
    (
        '<span>Top</span>',
        '<span data-i18n="mobile.top">Top</span>'
    )
]

for target, replacement in replacements:
    if target in html:
        html = html.replace(target, replacement)
    else:
        print(f"Warning: target not found:\n{target[:60]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully added data-i18n tags to index.html!")
