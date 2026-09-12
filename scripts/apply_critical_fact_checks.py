#!/usr/bin/env python3
"""
Zero-Margin Travel App - Apply Critical Fact-Checks to German Cities (v22.0.0)
Fixes:
1. f_19 Frankfurt Sachsenhausen: Replace Concentration Camp image with Frankfurt Sachsenhausen cider district image
2. b_13 Berlin Checkpoint Charlie: Remove banned fake soldier actors tip
3. b_59 Berlin SEA LIFE: Remove collapsed AquaDom from name and tip
4. b_4 Berlin Pergamonmuseum: Add main building renovation closure notice (Panorama hall open)
5. h_2 Hamburg Elbphilharmonie: Update Plaza ticket price to €3
6. m_52 Munich Kloster Andechs: Fix S8 train line
7. m_46 Munich Neuschwanstein: Fix King Ludwig II in desc_zh
8. m_5, m_6, m_7, m_8, m_15 Munich: Fix swapped tips
9. c_3, c_6, c_7, c_8, c_9 Cologne: Fix swapped tips & descriptions
"""

import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

# 1. Frankfurt fixes
f_path = os.path.join(cities_dir, 'frankfurt.json')
if os.path.exists(f_path):
    with open(f_path, 'r', encoding='utf-8') as f:
        fdata = json.load(f)
    for s in fdata['spots']:
        if s['id'] == 'f_19':
            s['image'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Frankfurt_Am_Main-Sachsenhausen-Schweizer_Strasse-Grosse_Rittergasse-Klappergasse-Bembel-20110904.jpg/330px-Frankfurt_Am_Main-Sachsenhausen-Schweizer_Strasse-Grosse_Rittergasse-Klappergasse-Bembel-20110904.jpg"
            s['wikiImage'] = s['image']
            s['tip_ja'] = "🎟️ 伝統の素焼き水差し（Bembel）で注がれるリンゴ酒（Apfelwein）と緑のソース（Grüne Soße）、ハントケース（Handkäs mit Musik）を味わうのが伝統の流儀。"
            s['tip_en'] = "🎟️ Order traditional Apfelwein served from an earthenware jug (Bembel) paired with Grüne Soße (green sauce) and Handkäs mit Musik cheese."
            s['tip'] = s['tip_en']
    with open(f_path, 'w', encoding='utf-8') as f:
        json.dump(fdata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Frankfurt f_19 Sachsenhausen image and tip!")

# 2. Berlin fixes
b_path = os.path.join(cities_dir, 'berlin.json')
if os.path.exists(b_path):
    with open(b_path, 'r', encoding='utf-8') as f:
        bdata = json.load(f)
    for s in bdata['spots']:
        # Checkpoint Charlie b_13
        if s['id'] == 'b_13':
            s['tip_ja'] = "📸 2019年に偽兵士アクターは市当局により全面禁止・追放されました。現在は地面に残る東西分割境界線、フランク・ティール作の巨大兵士肖像写真、壁博物館（Mauermuseum）の見学がメインです。"
            s['tip_en'] = "📸 Fake soldier actors were banned by city authorities in 2019. Focus on the cobblestone Cold War border line on the ground, Frank Thiel's giant portraits, and Mauermuseum."
            s['tip'] = s['tip_en']
        # AquaDom & SEA LIFE b_59
        elif s['id'] == 'b_59':
            s['name'] = "SEA LIFE Berlin（シーライフ・ベルリン（屋内水族館）"
            s['name_ja'] = "SEA LIFE Berlin（シーライフ・ベルリン（屋内水族館）"
            s['name_en'] = "SEA LIFE Berlin"
            s['desc_ja'] = "アレクサンダープラッツ近くの屋内水族館。熱帯ラグーンやサメ水槽、インタラクティブなタッチプールを楽しめる。"
            s['desc_en'] = "Indoor aquarium near Alexanderplatz featuring tropical shark tanks and interactive touch pools."
            s['tip_ja'] = "🎟️ 円筒形水槽アクアドームは2022年に崩壊・撤去されました。水族館本体（SEA LIFE）は営業中。混雑回避のため事前Webチケット予約がおすすめ。"
            s['tip_en'] = "🎟️ The AquaDom glass cylinder collapsed in 2022 and was removed. SEA LIFE aquarium itself is open; book online advance tickets to bypass lines."
            s['tip'] = s['tip_en']
        # Pergamonmuseum b_4
        elif s['id'] == 'b_4':
            s['tip_ja'] = "⚠️ ペルガモン博物館本館は大規模改修のため全館休館中（〜2027年以降）。360度パノラマ展示館『Pergamonmuseum. Das Panorama』のみ開館しています（事前Web予約必須）。"
            s['tip_en'] = "⚠️ Main Pergamon Museum building is closed for major renovation (until 2027+). Only the temporary 'Pergamonmuseum. Das Panorama' exhibition hall is open (timed web booking required)."
            s['tip'] = s['tip_en']
    with open(b_path, 'w', encoding='utf-8') as f:
        json.dump(bdata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Berlin Checkpoint Charlie, SEA LIFE AquaDom, and Pergamon Museum!")

# 3. Hamburg fixes
h_path = os.path.join(cities_dir, 'hamburg.json')
if os.path.exists(h_path):
    with open(h_path, 'r', encoding='utf-8') as f:
        hdata = json.load(f)
    for s in hdata['spots']:
        if s['id'] == 'h_2' or 'Elbphilharmonie' in s['name']:
            s['price_ja'] = "プラザ入場料: €3"
            s['price_en'] = "Plaza Admission: €3"
            s['price'] = "Plaza Admission: €3"
            s['tip_ja'] = "🎟️ 37m高のプラザ展望デッキ入場にはプラザチケット（€3）が必要です。82mの曲面エスカレーター『The Tube』を通るパノラマ体験は必見。"
            s['tip_en'] = "🎟️ Plaza viewing deck requires a €3 Plaza Ticket. Ride the 82m curved escalator 'The Tube' to the 37m high panoramic balcony."
            s['tip'] = s['tip_en']
    with open(h_path, 'w', encoding='utf-8') as f:
        json.dump(hdata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Hamburg Elbphilharmonie Plaza ticket pricing and tip!")

# 4. Munich fixes
m_path = os.path.join(cities_dir, 'munich.json')
if os.path.exists(m_path):
    with open(m_path, 'r', encoding='utf-8') as f:
        mdata = json.load(f)
    for s in mdata['spots']:
        # Kloster Andechs m_52
        if s['id'] == 'm_52':
            s['tip_ja'] = "🎟️ SバーンS8線（S8）の終点ヘルシャング（Herrsching）駅から聖なる丘まで徒歩約50分のハイキング。名物の修道院醸造ドッペルボック黒ビールとシュヴァインスハクセは必食！"
            s['tip_en'] = "🎟️ Take S-Bahn line S8 to the Herrsching terminus, then enjoy a scenic 50-minute hike up the Holy Mountain to sample famous monastic Doppelbock beer."
            s['tip'] = s['tip_en']
        # Neuschwanstein m_46
        elif s['id'] == 'm_46':
            s['desc_zh'] = "路德维希二世国王建造的梦幻城堡，迪士尼睡美人城堡的灵感来源。"
        # Deutsches Museum m_5
        elif s['id'] == 'm_5':
            s['tip_ja'] = "🎟️ 世界最大級の科学技術博物館。地下のリアル鉱山展示（Bergwerk）と高電圧放電実験ショーが必見。見学所要時間は最低3〜4時間必要です。"
            s['tip_en'] = "🎟️ World's largest science museum. Don't miss the underground mine exhibit and high-voltage electricity demonstrations. Allow at least 3–4 hours."
            s['tip'] = s['tip_en']
        # Alte Pinakothek m_6
        elif s['id'] == 'm_6':
            s['tip_ja'] = "🎟️ 毎週日曜日は入場料がわずか【1ユーロ】！デューラーの自画像やダ・ヴィンチの『カーネーションの聖母』などの傑作を鑑賞できます。"
            s['tip_en'] = "🎟️ Sunday admission is only €1! Features Dürer's Self-Portrait and Da Vinci's Madonna of the Carnation."
            s['tip'] = s['tip_en']
        # Neue Pinakothek m_7
        elif s['id'] == 'm_7':
            s['tip_ja'] = "⚠️ ノイエ・ピナコテーク本館は改修のため長期休館中（〜2029年予定）。ゴッホの『ひまわり』などの名作は隣のアルテ・ピナコテーク1階で特別展示されています。"
            s['tip_en'] = "⚠️ Main Neue Pinakothek building is closed for renovation until ~2029. Masterpieces like Van Gogh's Sunflowers are displayed on the 1st floor of Alte Pinakothek."
            s['tip'] = s['tip_en']
        # Pinakothek der Moderne m_8
        elif s['id'] == 'm_8':
            s['tip_ja'] = "🎟️ 現代美術・建築・デザイン・グラフィックの4館が1つになった大美術館。毎週日曜日は入場料【1ユーロ】でお得に入場できます。"
            s['tip_en'] = "🎟️ 4 museums in 1: art, architecture, design, and graphics. Sunday admission is only €1."
            s['tip'] = s['tip_en']
        # Augustiner-Keller m_15
        elif s['id'] == 'm_15':
            s['tip_ja'] = "🍺 1328年創業最古の醸造所。セルフサービスのビアガーデンエリアでは伝統的に自分の食べ物（パンやチーズ等）の持ち込みが自由です。"
            s['tip_en'] = "🍺 Munich's oldest brewery (1328). In the self-service beer garden area, bringing your own food (Brotzeit) is traditionally allowed!"
            s['tip'] = s['tip_en']
    with open(m_path, 'w', encoding='utf-8') as f:
        json.dump(mdata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Munich spots m_5, m_6, m_7, m_8, m_15, m_46, m_52!")

# 5. Cologne fixes
c_path = os.path.join(cities_dir, 'cologne.json')
if os.path.exists(c_path):
    with open(c_path, 'r', encoding='utf-8') as f:
        cdata = json.load(f)
    for s in cdata['spots']:
        # Altstadt c_3
        if s['id'] == 'c_3':
            s['desc_ja'] = "ケルン大聖堂南側に広がる歴史的な旧市街。ライン川沿いにカラフルな伝統家屋（Stapelhaus）と石畳の広場が続く。"
            s['desc_en'] = "Historic old town below Cologne Cathedral with colorful riverfront houses and cobblestone plazas."
            s['tip_ja'] = "📸 フィッシュマルクト（Fischmarkt）広場からカラフルな細長家屋と大聖マルティン教会の塔を背景に撮影するのがケルン一番のフォトロケーションです。"
            s['tip_en'] = "📸 The classic Cologne postcard view is captured at Fischmarkt plaza featuring colorful narrow houses with Groß St. Martin church in the background."
            s['tip'] = s['tip_en']
        # Groß St. Martin c_6
        elif s['id'] == 'c_6':
            s['desc_ja'] = "旧市街の象徴である12世紀ロマネスク様式の厳かな大教会。四角い大塔と四隅の小塔が特徴。"
            s['desc_en'] = "Imposing 12th-century Romanesque church dominating the Old Town skyline."
            s['tip_ja'] = "🎟️ 入堂は無料。地下の古代ローマ時代の建築遺構（ローマ時代の倉庫・浴場跡）見学は有料（€3）で必見です。"
            s['tip_en'] = "🎟️ Church entry is free. Don't miss the subterranean Roman architectural ruins in the basement (€3)."
            s['tip'] = s['tip_en']
        # Rheinauhafen c_7
        elif s['id'] == 'c_7':
            s['desc_ja'] = "ライン川沿いの再開発ウォーターフロント地区。クレーンを模した3棟の独創的懸造高層ビル『クレーンハウス（Kranhaus）』が立ち並ぶ。"
            s['desc_en'] = "Revitalized waterfront district famous for the 3 cantilevered Kranhaus (Crane House) towers."
            s['tip_ja'] = "📸 クレーンハウス（Kranhaus）を下から見上げるアングルや、対岸の夕景シルエットがモダン建築写真スポットとして絶品。"
            s['tip_en'] = "📸 Photograph the cantilevered Kranhaus towers from directly underneath or across the Rhine River at sunset."
            s['tip'] = s['tip_en']
        # KölnTriangle c_8
        elif s['id'] == 'c_8':
            s['desc_ja'] = "ライン川東岸に立つ103mのオフィスビル。屋上に全方位ガラス張りの360度パノラマ展望台を備える。"
            s['desc_en'] = "103m glass tower on the east bank of the Rhine offering 360° open-air rooftop views."
            s['tip_ja'] = "📸 大聖堂とホーエンツォレルン橋を同一構図に収める夕景・夜景撮影の最高地点（入場料€5）。"
            s['tip_en'] = "📸 Best vantage point to photograph Cologne Cathedral and the Hohenzollern Bridge together at sunset (€5)."
            s['tip'] = s['tip_en']
        # Schokoladenmuseum c_9
        elif s['id'] == 'c_9':
            s['desc_ja'] = "ライン川に浮かぶ船のような建築のチョコレート博物館。3mの金のチョコーレートファウンテンが名物。"
            s['desc_en'] = "Chocolate museum on the Rhine featuring a 3-meter golden chocolate fountain."
            s['tip_ja'] = "🍫 温かい液体チョコレートをウエハースに浸して無料で試食させてくれる巨大チョコレートファウンテンがハイライト！"
            s['tip_en'] = "🍫 Staff serve free dipped wafers directly from the 3-meter golden chocolate fountain!"
            s['tip'] = s['tip_en']
    with open(c_path, 'w', encoding='utf-8') as f:
        json.dump(cdata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Cologne spots c_3, c_6, c_7, c_8, c_9!")

print("🎉 Critical fact-checks successfully applied!")
