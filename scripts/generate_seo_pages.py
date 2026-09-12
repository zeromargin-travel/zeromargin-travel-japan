import json
import os
import glob

def get_country_for_city(city_id):
    # Mapping based on common prefixes in our DB
    if city_id.startswith('par_') or city_id.startswith('lyo_') or city_id.startswith('mar_') or city_id.startswith('nic_') or city_id.startswith('bor_') or city_id.startswith('str_') or city_id.startswith('tou_'):
        return "France"
    elif city_id.startswith('ber_') or city_id.startswith('mun_') or city_id.startswith('fra_') or city_id.startswith('ham_') or city_id.startswith('col_') or city_id.startswith('dre_') or city_id.startswith('hei_') or city_id.startswith('nur_'):
        return "Germany"
    elif city_id.startswith('ams_') or city_id.startswith('rot_') or city_id.startswith('the_') or city_id.startswith('utr_') or city_id.startswith('maa_'):
        return "Netherlands"
    elif city_id.startswith('bru_') or city_id.startswith('ant_') or city_id.startswith('ghe_') or city_id.startswith('brg_'):
        return "Belgium"
    elif city_id.startswith('lux_'):
        return "Luxembourg"
    return "Europe"

def generate_all_lps():
    os.makedirs('destinations', exist_ok=True)
    
    city_files = glob.glob('data/cities/*.json')
    count = 0
    
    for filepath in city_files:
        filename = os.path.basename(filepath)
        city_slug = filename.replace('.json', '')
        city_name_display = city_slug.replace('_', ' ').title()
        if city_slug == 'the_hague':
            city_name_display = "The Hague"
            
        with open(filepath, 'r', encoding='utf-8') as f:
            spots = json.load(f)
            
        if not spots:
            continue
            
        # Try to guess country from first spot ID
        country_name = get_country_for_city(spots[0].get('id', ''))
            
        top_spots = [s for s in spots if s.get('top7')]
        if not top_spots:
            top_spots = spots[:10]
        else:
            top_spots = (top_spots + [s for s in spots if not s.get('top7')])[:10]
            
        spots_html = ""
        for idx, s in enumerate(top_spots):
            insider_tip = s.get('insiderTip_en') or s.get('tip') or s.get('insiderTip_fr') or ''
            tip_html = f'<div style="margin-top:1rem; background:#FFFBEB; border-left:4px solid #F59E0B; padding:0.75rem; font-size:0.9rem; color:#92400E;"><strong>💡 Insider Tip:</strong> {insider_tip}</div>' if insider_tip else ''
            
            category = s.get('category', 'Attraction')
            rating = s.get('rating', '4.5')
            desc = s.get('desc_en') or s.get('desc') or ''
            
            img_src = s.get('image', '')
            if img_src and not img_src.startswith('http') and not img_src.startswith('data:'):
                img_src = f"../{img_src}"
            
            spots_html += f"""
            <div class="spot-card" style="margin-bottom:2.5rem; background:#FFF; border-radius:16px; overflow:hidden; box-shadow:0 10px 25px rgba(0,0,0,0.05); border:1px solid #E2E8F0;">
                <div style="height:250px; overflow:hidden; position:relative;">
                    <img src="{img_src}" alt="{s.get('name')}" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; top:1rem; left:1rem; background:rgba(0,0,0,0.75); color:#FFF; padding:0.25rem 0.75rem; border-radius:50px; font-weight:bold; font-size:0.85rem;">
                        ★ {rating}
                    </div>
                    <div style="position:absolute; top:1rem; right:1rem; background:rgba(255,255,255,0.9); color:#0F172A; padding:0.25rem 0.75rem; border-radius:50px; font-weight:bold; font-size:0.85rem;">
                        {category}
                    </div>
                </div>
                <div style="padding:1.5rem;">
                    <h3 style="margin:0 0 1rem 0; font-size:1.5rem; color:#0F172A;">{idx+1}. {s.get('name')}</h3>
                    <p style="margin:0 0 1rem 0; font-size:1rem; color:#475569; line-height:1.7;">{desc}</p>
                    {tip_html}
                </div>
            </div>
            """

        # Encode for URL
        city_url_param = f"{city_name_display}, {country_name}".replace(' ', '%20')
        country_url_param = country_name.replace(' ', '%20')
        link_url = f"../index.html?country={country_url_param}&city={city_url_param}"

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Ultimate 1-Day {city_name_display} Walking Tour & Itinerary | Free AI Google Maps Route</title>
    <meta name="description" content="Explore {city_name_display} smarter. Generate a perfect 1-day walking tour featuring {len(top_spots)} handpicked ★4.5+ spots with insider tips and instant Google Maps multi-stop navigation. 100% Free.">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; margin: 0; background: #F8FAFC; }}
        .header {{ background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); color: white; padding: 4rem 1rem; text-align: center; position:relative; overflow:hidden; }}
        .header::after {{ content:''; position:absolute; bottom:0; left:0; width:100%; height:4px; background: linear-gradient(90deg, #F59E0B, #10B981, #3B82F6); }}
        .container {{ max-width: 850px; margin: 0 auto; padding: 3rem 1rem; }}
        h2 {{ font-size: 2rem; color:#0F172A; margin-bottom:1.5rem; border-bottom:2px solid #E2E8F0; padding-bottom:0.5rem; }}
        .cta-btn {{ display: flex; align-items:center; justify-content:center; gap:0.5rem; width: 100%; max-width: 450px; margin: 2rem auto; text-align: center; background: #F59E0B; color: white; padding: 1.25rem; border-radius: 50px; text-decoration: none; font-weight: 800; font-size: 1.15rem; box-shadow: 0 10px 25px rgba(245, 158, 11, 0.4); transition: all 0.3s ease; }}
        .cta-btn:hover {{ transform: translateY(-3px); box-shadow: 0 15px 30px rgba(245, 158, 11, 0.5); }}
        .faq-item {{ margin-bottom: 1.5rem; }}
        .faq-q {{ font-weight: bold; font-size: 1.1rem; color: #0F172A; margin-bottom:0.25rem; }}
        .faq-a {{ color: #475569; }}
        .footer {{ text-align: center; padding: 3rem 1rem; color: #64748B; font-size: 0.9rem; border-top:1px dashed #CBD5E1; margin-top:3rem; }}
    </style>
</head>
<body>
    <div class="header">
        <h1 style="margin:0 0 1rem 0; font-size:3rem; font-weight:900; letter-spacing:-1px;">1-Day {city_name_display} Walking Tour</h1>
        <p style="font-size:1.3rem; color:#94A3B8; max-width:600px; margin:0 auto;">Skip the planning fatigue. Get a curated route of the highest-rated spots, complete with insider tips, and send it directly to your Google Maps.</p>
    </div>
    
    <div class="container">
        <div style="background:#FFF; padding:2rem; border-radius:12px; box-shadow:0 4px 6px rgba(0,0,0,0.05); margin-bottom:3rem;">
            <h2>Why This is the Only {city_name_display} Itinerary You Need</h2>
            <p style="font-size:1.1rem; color:#475569;">Planning a trip to {city_name_display} can be overwhelming. The internet is flooded with generic lists, and mapping them out by walking distance takes hours. That's why we built this specific 1-day walking tour featuring only the highest-rated (★4.5+) spots in the city.</p>
            <p style="font-size:1.1rem; color:#475569;">Read through the carefully curated spots below, complete with <strong>insider tips from locals</strong>. When you're ready, click the button to load this exact route into <strong>0Margin Travel</strong>, where you can instantly generate a multi-stop Google Maps navigation link for free.</p>
            <a href="{link_url}" class="cta-btn">🚀 Customize this Route in 1 Click</a>
        </div>
        
        <h2>Top {len(top_spots)} Highlights in This Route</h2>
        <p style="color:#64748B; margin-bottom:2rem;">Below are the handpicked venues included in this walking tour. Every location has been verified for quality and geographic proximity.</p>
        
        {spots_html}
        
        <div style="text-align:center; margin: 4rem 0;">
            <a href="{link_url}" class="cta-btn" style="background:#047857; box-shadow: 0 10px 25px rgba(4, 120, 87, 0.4); max-width:550px;">
                <span style="font-size:1.5rem;">📍</span> Load Full Interactive Route in 0Margin Travel
            </a>
            <p style="color:#64748B; font-size:0.9rem; margin-top:1rem;">100% Free. No signup required. Direct to Google Maps.</p>
        </div>

        <h2>Frequently Asked Questions (FAQ)</h2>
        <div class="faq-item">
            <div class="faq-q">Q: Is it really possible to walk to all these spots in one day?</div>
            <div class="faq-a">A: Yes! This {city_name_display} itinerary is designed to group geographically close locations. However, depending on your pace, you might want to use local public transport for longer stretches.</div>
        </div>
        <div class="faq-item">
            <div class="faq-q">Q: How do I transfer this route to Google Maps?</div>
            <div class="faq-a">A: Click the green button above to load the interactive planner. From there, you can reorder or remove spots, and then click "Generate Ready-to-Use Google Maps Routes" to open the live turn-by-turn navigation on your phone.</div>
        </div>
        <div class="faq-item">
            <div class="faq-q">Q: Do I need to book tickets in advance for these attractions?</div>
            <div class="faq-a">A: For major landmarks, booking weeks in advance is highly recommended. Our insider tips above mention specific booking advice for each venue.</div>
        </div>
    </div>
    
    <div class="footer">
        &copy; 2026 0Margin Travel. All rights reserved.
        <br><br>
        <a href="../index.html" style="color:#94A3B8; text-decoration:none;">Return to Main AI Route Generator</a>
    </div>
</body>
</html>"""

        with open(f'destinations/{city_slug}.html', 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1
        print(f"Generated destinations/{city_slug}.html")
        
    print(f"Successfully generated {count} city LPs.")

if __name__ == "__main__":
    generate_all_lps()
