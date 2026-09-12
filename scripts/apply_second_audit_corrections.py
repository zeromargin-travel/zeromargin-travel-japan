#!/usr/bin/env python3
"""
Zero-Margin Travel App - Apply 2nd Audit Report Corrections (v28.0.0)
Applies verified 2025-2026 European price increases, closures, and translation fixes across 18 cities:
- p_16 (Centre Pompidou): Mark closed for renovation (2026-2030)
- m_46 (Neuschwanstein): Free -> €21 guided tour ticket required (free=False)
- c_1 (Cologne Cathedral): €12 tourist entry fee from July 1, 2026 / Tower €8
- b_10 (Humboldt Forum): Permanent free -> Exhibitions €9, Roof €3 (Courtyard Free)
- a_5 (Zaanse Schans): Fix mistranslation 温室 -> 緑色の伝統木造建築群
- 2025-2026 Ticket Price Updates (Paris, Amsterdam, Berlin, Hamburg, Cologne, Munich, Nuremberg, Brussels, Luxembourg, Toulouse)
"""

import os
import json
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

def apply_paris_fixes(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'p_16':
            print("  -> Updating p_16: Centre Pompidou multi-year renovation closure notice")
            s['desc_en'] = "Iconic high-tech cultural center designed by Renzo Piano & Richard Rogers. NOTE: Main Beaubourg building is CLOSED for major renovation (2026–2030)."
            s['desc_ja'] = "レンゾ・ピアノとリチャード・ロジャース設計のハイテク建築の金字塔。※現在、大規模改修工事のため本館全館が長期休館中（2026〜2030年再開予定）。"
            s['desc_fr'] = "Centre culturel emblématique d'architecture high-tech. REMARQUE : Le bâtiment principal est FERMÉ pour rénovation majeure (2026–2030)."
            s['desc_de'] = "Ikonisches Kulturzentrum für moderne Kunst. HINWEIS: Das Hauptgebäude ist wegen umfassender Sanierung geschossen (2026–2030)."
            
            s['tip_en'] = "🚧 The Beaubourg building is CLOSED for renovation until 2030! Temporary exhibitions are hosted at Grand Palais and partner venues under 'Centre Pompidou Constellation'."
            s['tip_ja'] = "🚧 本館ビルは2030年まで全面改修休館中です！グラン・パレや学外会場で開催される「ポンピドゥー・星座（Constellation）」サテライト企画展をご利用ください。"
            
            s['price'] = "Closed for Renovation (2026–2030)"
            s['price_en'] = "Closed for Renovation (2026–2030)"
            s['price_ja'] = "大規模改修に伴い長期休館中（2026〜2030年）"
            s['price_fr'] = "Fermé pour travaux (2026–2030)"
            s['price_de'] = "Wegen Sanierung geschlossen (2026–2030)"
            s['free'] = False

        elif sid == 'p_14':
            print("  -> Updating p_14: Louvre Museum 2026 pricing (€22-€32)")
            s['price'] = "Entry: €22–€32"
            s['price_en'] = "Entry: €22–€32 (Online Booking Required)"
            s['price_ja'] = "入場料: 22〜32ユーロ（要事前Web予約）"

        elif sid == 'p_1':
            print("  -> Updating p_1: Eiffel Tower 2026 pricing (€35.30 Top Lift)")
            s['price'] = "Top Lift: €35.30 / Stairs: €14.20"
            s['price_en'] = "Top Lift: €35.30 / Stairs: €14.20"
            s['price_ja'] = "最上階エレベーター: 35.30€ / 階段: 14.20€"

        elif sid == 'p_2':
            print("  -> Updating p_2: Arc de Triomphe 2026 pricing (€16)")
            s['price'] = "Rooftop: €16"
            s['price_en'] = "Rooftop Entry: €16"
            s['price_ja'] = "屋上入場料: 16ユーロ"

        elif sid == 'p_3':
            print("  -> Updating p_3: Sainte-Chapelle 2026 pricing (€16)")
            s['price'] = "Entry: €16"
            s['price_en'] = "Entry: €16 (Combo Conciergerie: €26)"
            s['price_ja'] = "入場料: 16ユーロ（コンシエルジュリー共通26€）"

        elif sid == 'p_13':
            print("  -> Updating p_13: Catacombs 2026 pricing (€31)")
            s['price'] = "Entry: €31"
            s['price_en'] = "Entry: €31 (Audio Guide Included)"
            s['price_ja'] = "入場料: 31ユーロ（オーディオガイド付き）"

def apply_amsterdam_fixes(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'a_1':
            print("  -> Updating a_1: Rijksmuseum (€25)")
            s['price'] = "Adult: €25"
            s['price_en'] = "Adult: €25 (Under 19 Free)"
            s['price_ja'] = "入場料: 25ユーロ（18歳未満無料）"

        elif sid == 'a_2':
            print("  -> Updating a_2: Van Gogh Museum (€25 online only)")
            s['price'] = "Adult: €25 (Online Only)"
            s['price_en'] = "Adult: €25 (Online Only)"
            s['price_ja'] = "入場料: 25ユーロ（完全オンライン予約制）"

        elif sid == 'a_3':
            print("  -> Updating a_3: Anne Frank House (€16.50)")
            s['price'] = "Adult: €16.50"
            s['price_en'] = "Adult: €16.50 (Online Only)"
            s['price_ja'] = "入場料: 16.50ユーロ（完全Web予約制）"

        elif sid == 'a_5':
            print("  -> Updating a_5: Zaanse Schans mistranslation fix & ticket precision")
            s['desc_ja'] = "アムステルダム近郊のザーン川沿いに立つ、18〜19世紀の風車や緑色の伝統木造建築群（Zaanse houten huizen）が保存された歴史地区。"
            s['price'] = "Grounds Free (Windmills & Museums Paid)"
            s['price_en'] = "Grounds Free (Windmills & Museums Paid)"
            s['price_ja'] = "風車村敷地無料（各風車・博物館単体券あり）"

        elif sid == 'a_8':
            print("  -> Updating a_8: Oude Kerk (€13.50)")
            s['price'] = "Adult: €13.50"
            s['price_en'] = "Adult: €13.50"
            s['price_ja'] = "入場料: 13.50ユーロ"

        elif sid == 'a_12':
            print("  -> Updating a_12: Rembrandt House (€23.50)")
            s['price'] = "Adult: €23.50"
            s['price_en'] = "Adult: €23.50"
            s['price_ja'] = "入場料: 23.50ユーロ"

        elif sid == 'a_13':
            print("  -> Updating a_13: NEMO Science Museum (€21.50)")
            s['price'] = "Entry: €21.50"
            s['price_en'] = "Entry: €21.50 (Ages 4+)"
            s['price_ja'] = "入場料: 21.50ユーロ（4歳以上）"

def apply_berlin_fixes(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'b_3':
            print("  -> Updating b_3: Museumsinsel Pass (€24)")
            s['price'] = "Day Ticket: €24"
            s['price_en'] = "Museumsinsel Day Pass: €24"
            s['price_ja'] = "共通一日券: 24ユーロ"

        elif sid in ['b_6', 'b_7', 'b_8']:
            print(f"  -> Updating {sid}: SMB Museum (€14)")
            s['price'] = "Entry: €14"
            s['price_en'] = "Entry: €14"
            s['price_ja'] = "入場料: 14ユーロ"

        elif sid == 'b_9':
            print("  -> Updating b_9: Berliner Dom (€15)")
            s['price'] = "Entry: €15"
            s['price_en'] = "Entry: €15 (Incl. Audioguide & Crypt)"
            s['price_ja'] = "拝観料: 15ユーロ（オーディオガイド・地下墓所込み）"

        elif sid == 'b_10':
            print("  -> Updating b_10: Humboldt Forum pricing (€9 exhibitions / €3 roof)")
            s['price'] = "Courtyard Free / Exhibitions: €9 / Roof: €3"
            s['price_en'] = "Courtyard Free / Exhibitions: €9 / Roof Terrace: €3"
            s['price_ja'] = "中庭無料 / 企画展9€ / 屋上テラス3€"

        elif sid == 'b_13':
            print("  -> Updating b_13: Mauermuseum Checkpoint Charlie (€18.50)")
            s['price'] = "Outdoor Free / Museum: €18.50"
            s['price_en'] = "Outdoor Free / Museum: €18.50"
            s['price_ja'] = "屋外無料（博物館入場: 18.50€）"

        elif sid == 'b_16':
            print("  -> Updating b_16: Fernsehturm TV Tower (€25.50+)")
            s['price'] = "Observation: €25.50+"
            s['price_en'] = "Observation Deck: €25.50+ (Dynamic Pricing)"
            s['price_ja'] = "展望台: 25.50€〜（変動料金制）"

def apply_munich_fixes(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'm_3':
            print("  -> Updating m_3: Munich Residenz combo (€15)")
            s['price'] = "Residenz Combo: €15"
            s['price_en'] = "Residenz & Treasury Combo: €15"
            s['price_ja'] = "レジデンツ・宝物館共通券: 15ユーロ"

        elif sid == 'm_5':
            print("  -> Updating m_5: Deutsches Museum Munich (€16)")
            s['price'] = "Entry: €16"
            s['price_en'] = "Entry: €16"
            s['price_ja'] = "入場料: 16ユーロ"

        elif sid == 'm_46':
            print("  -> Updating m_46: Neuschwanstein Castle guided tour requirement (€21)")
            s['free'] = False
            s['price'] = "Guided Tour: €21"
            s['price_en'] = "Guided Tour: €21 (Advance Online Booking Required)"
            s['price_ja'] = "城内入場: 21ユーロ（要事前Web予約）"
            s['tip_ja'] = "🏰 マリエン橋や城の敷地外観の散策は無料ですが、城内見学には21€の事前日時指定Web予約チケットが必須です！数週間前には完売するため早期確保を。"

def apply_cologne_fixes(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'c_1':
            print("  -> Updating c_1: Cologne Cathedral tourist entry fee (€12 from July 2026)")
            s['price'] = "Tourist Entry: €12 / Tower: €8 / Prayer Free"
            s['price_en'] = "Tourist Entry: €12 / Tower Climb: €8 (Prayer & Services Free)"
            s['price_ja'] = "聖堂観光12€（2026年7月〜）/ 塔8€ / 礼拝無料"
            s['tip_ja'] = "⛪ 2026年7月より観光客向けの内陣見学チケット（12€）が導入されます（礼拝・お祈りは無料）。高さ157mのツインタワーと533段の塔登り（8€）は圧巻です。"

        elif sid == 'c_9':
            print("  -> Updating c_9: Cologne Chocolate Museum (€17.50/€19)")
            s['price'] = "Entry: €17.50 (Weekday) / €19 (Weekend)"
            s['price_en'] = "Entry: €17.50 (Weekday) / €19 (Weekend)"
            s['price_ja'] = "入場料: 17.50€（平日）/ 19€（土日）"

def apply_hamburg_fixes(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'h_1':
            print("  -> Updating h_1: Miniatur Wunderland (€22)")
            s['price'] = "Adult: €22"
            s['price_en'] = "Adult: €22"
            s['price_ja'] = "入場料: 22ユーロ"

        elif sid == 'h_2':
            print("  -> Updating h_2: Elbphilharmonie Plaza (Free, online booking €2)")
            s['price'] = "Plaza Free (Online Reservation €2)"
            s['price_en'] = "Plaza Free (Online Time-Slot Booking €2)"
            s['price_ja'] = "プラザ入場無料（Web事前時間指定予約: 2€）"

def apply_nuremberg_fixes(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'nu_1':
            print("  -> Updating nu_1: Nuremberg Castle (€10)")
            s['price'] = "Castle & Tower Combo: €10"
            s['price_en'] = "Castle & Sinwell Tower Combo: €10"
            s['price_ja'] = "城館・ジンウェル塔共通券: 10ユーロ"

        elif sid == 'nu_12':
            print("  -> Updating nu_12: Nuremberg Doc Center (€7.50)")
            s['price'] = "Entry: €7.50"
            s['price_en'] = "Entry: €7.50"
            s['price_ja'] = "入場料: 7.50ユーロ"

def apply_other_fixes(data, fname):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'br_3':
            print("  -> Updating br_3: Atomium Brussels (€17)")
            s['price'] = "Adult: €17"
            s['price_en'] = "Adult: €17 (Includes Design Museum Brussels)"
            s['price_ja'] = "入場料: 17ユーロ（デザインミュージアム共通）"
        elif sid == 'l_6':
            print("  -> Updating l_6: MUDAM Luxembourg (€10)")
            s['price'] = "Adult: €10"
            s['price_en'] = "Adult: €10"
            s['price_ja'] = "入場料: 10ユーロ"
        elif sid == 'to_34':
            print("  -> Updating to_34: Cité de l'Espace Toulouse (€29-€32)")
            s['price'] = "Entry: €29–€32"
            s['price_en'] = "Entry: €29–€32"
            s['price_ja'] = "入場料: 29〜32ユーロ"

def run_all_updates():
    print("🚀 Applying 2nd Audit Report Corrections across all city JSON files...")
    city_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))
    for fpath in city_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        fname = os.path.basename(fpath)
        if fname == 'paris.json':
            apply_paris_fixes(data)
        elif fname == 'amsterdam.json':
            apply_amsterdam_fixes(data)
        elif fname == 'berlin.json':
            apply_berlin_fixes(data)
        elif fname == 'munich.json':
            apply_munich_fixes(data)
        elif fname == 'cologne.json':
            apply_cologne_fixes(data)
        elif fname == 'hamburg.json':
            apply_hamburg_fixes(data)
        elif fname == 'nuremberg.json':
            apply_nuremberg_fixes(data)
        else:
            apply_other_fixes(data, fname)
            
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  - Refined {fname}")

if __name__ == '__main__':
    run_all_updates()
