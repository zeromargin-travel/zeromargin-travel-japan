#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Programmatic SEO Landing Pages for Okinawa Model Courses
ZeroMargin Travel Japan
"""

import json
import os
import urllib.parse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(PROJECT_DIR, 'data', 'cities', 'okinawa.json')
OKINAWA_DIR = os.path.join(PROJECT_DIR, 'okinawa')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    ALL_SPOTS = json.load(f)

SPOTS_BY_ID = {s['id']: s for s in ALL_SPOTS}

COURSES = [
    {
        "slug": "rainy-day",
        "title": "沖縄 雨の日 ドライブコース＆屋内観光モデルコース | 0Margin Travel",
        "h1": "沖縄 雨の日のドライブ＆屋内観光モデルコース",
        "subtitle": "雨予報でも120%楽しめる！美ら海水族館・巨大鍾乳洞・市場・アイス作り体験を巡る最適周遊ルート",
        "meta_desc": "沖縄旅行が雨予報でも大丈夫！DMMかりゆし水族館、おきなわワールド、第一牧志公設市場、ブルーシール、美ら海水族館など雨天OKの屋内★4.5以上スポットを効率よく巡るGoogleマップ最適ドライブルート。完全無料・登録不要。",
        "keywords": "沖縄 雨の日 ドライブ, 沖縄 雨 観光モデルコース, 沖縄 雨天 スポット, 沖縄 雨 ドライブルート Googleマップ",
        "spot_ids": ["oki_p_51", "oki_p_5", "oki_p_6", "oki_p_54", "oki_p_15"],
        "tag": "☔ 雨の日・屋内満喫コース",
        "faqs": [
            ("沖縄で雨が降った時、レンタカー移動はどうすべき？", "沖縄はスコールや局地的な大雨が多いため、立体駐車場や屋根付き施設を中心に回るのが鉄則です。本コースは那覇南部から北部まで雨に濡れにくいスポットを地理順に並べています。"),
            ("美ら海水族館は雨の日でも混雑しますか？", "雨の日は観光客が水族館に集中します。午前中の早い時間帯（9:00前後）または夕方16:00以降の入館が比較的空いておりおすすめです。")
        ]
    },
    {
        "slug": "naha-halfday",
        "title": "那覇空港 到着日・最終日 半日観光ドライブコース | 0Margin Travel",
        "h1": "那覇空港 到着日・最終日の半日観光モデルコース",
        "subtitle": "フライト前後の3〜4時間で大満喫！ウミカジテラス・波上宮・国際通り・首里城を回る最適周遊ルート",
        "meta_desc": "那覇空港着の初日午後や、帰りのフライトまでの数時間で回れる那覇・南部半日観光ルート。ウミカジテラス、崖の上の波上宮、首里城、国際通りを移動ロスなく巡るGoogleマップナビ。完全無料・登録不要。",
        "keywords": "那覇空港 到着日 観光, 那覇 半日 モデルコース, 沖縄 最終日 ドライブ, 那覇 空港近く 観光ルート",
        "spot_ids": ["oki_p_3", "oki_p_4", "oki_p_1", "oki_p_48", "oki_p_2"],
        "tag": "✈️ 那覇空港発着・南部半日コース",
        "faqs": [
            ("那覇空港からウミカジテラスまでは車でどのくらい？", "渋滞がなければ車で約10〜15分です。飛行機の離着陸を目の前で眺めながらランチやカフェを楽しめるため、到着初日の最初の立ち寄り先に最適です。"),
            ("レンタカー返却前の給油と時間配分は？", "那覇空港周辺のレンタカー営業所は夕方混雑します。フライト出発時刻の2時間〜2時間半前には返却手続きに入れるよう逆算してルートを回るのが安心です。")
        ]
    },
    {
        "slug": "family-kids",
        "title": "沖縄 子連れ・ファミリー向け観光モデルコース | 0Margin Travel",
        "h1": "沖縄 子連れ・ファミリー向け周遊ドライブコース",
        "subtitle": "移動疲れゼロ＆子どもが大興奮！美ら海水族館・パイナップルパーク・動物園を巡る鉄板ルート",
        "meta_desc": "小さな子ども連れの沖縄旅行に最適！美ら海水族館、名護パイナップルパーク、ネオパークオキナワ、沖縄こどもの国など子どもが喜ぶ人気スポットを移動負担を最小化して巡るGoogleマップ周遊ルート。完全無料。",
        "keywords": "沖縄 子連れ モデルコース, 沖縄 ファミリー ドライブ, 沖縄 子連れ 観光ルート, 沖縄 子供 喜ぶ スポット",
        "spot_ids": ["oki_p_15", "oki_p_20", "oki_p_45", "oki_p_52", "oki_p_54"],
        "tag": "👨‍👩‍👧 子連れ・ファミリー鉄板コース",
        "faqs": [
            ("ベビーカーでの移動はしやすいですか？", "美ら海水族館、パイナップルパーク、ネオパークはいずれもバリアフリー設計でベビーカーでの観覧が快適です。無料貸出ベビーカーも充実しています。"),
            ("途中で子どもの機嫌が悪くなった時は？", "本ツールのルート画面で不要になったスポットの「✕」ボタンを押せば、即座に次の目的地への最適ナビに再計算されます。")
        ]
    },
    {
        "slug": "free-scenery",
        "title": "沖縄 入場無料スポットだけで巡る絶景ドライブコース | 0Margin Travel",
        "h1": "入場料0円！沖縄の無料絶景スポット巡りドライブコース",
        "subtitle": "チケット代ゼロで息をのむ絶景へ！古宇利大橋・海中道路・ニライカナイ橋を走る爽快縦断ルート",
        "meta_desc": "入場料無料（0円）の絶景スポットだけで沖縄本島を駆け抜けるコスパ最強ドライブコース。ニライカナイ橋、知念岬、海中道路、残波岬、古宇利大橋を網羅。1タップでGoogleマップ一括周遊ナビ。登録不要。",
        "keywords": "沖縄 無料 観光スポット, 沖縄 絶景 ドライブコース, 古宇利大橋 海中道路 ドライブ, 沖縄 コスパ 旅行 ルート",
        "spot_ids": ["oki_p_35", "oki_p_38", "oki_p_36", "oki_p_11", "oki_p_17"],
        "tag": "🆓 入場料0円！絶景ドライブ縦断",
        "faqs": [
            ("橋を渡るのにお金はかかりますか？", "古宇利大橋、海中道路、ニライカナイ橋はいずれも通行料金無料です。エメラルドグリーンの海上を爽快にドライブできます。"),
            ("一番きれいな海の景色を見る時間帯は？", "太陽が真上から差す11:00〜14:00が最も海が青く輝きます。古宇利大橋や海中道路はこの時間帯に通るのがベストです。")
        ]
    },
    {
        "slug": "ocean-cafe",
        "title": "沖縄 海が見える絶景カフェ＆おしゃれ街歩きドライブコース | 0Margin Travel",
        "h1": "沖縄 絶景オーシャンビューカフェ＆街歩きドライブコース",
        "subtitle": "青い海と波音に癒される！バンタカフェ・浜辺の茶屋・港川外国人住宅街を巡る大人のご褒美ルート",
        "meta_desc": "沖縄の美しい海を眺めながら過ごす至福のカフェドライブ。瀬長島ウミカジテラス、浜辺の茶屋、港川ステイツサイドタウン、星野リゾート バンタカフェ、花人逢を巡るGoogleマップ最適ナビ。完全無料。",
        "keywords": "沖縄 海カフェ ドライブ, 沖縄 絶景カフェ ルート, 沖縄 カフェ巡り モデルコース, バンタカフェ 浜辺の茶屋 ドライブ",
        "spot_ids": ["oki_p_3", "oki_p_26", "oki_p_14", "oki_p_57", "oki_p_28"],
        "tag": "☕ 絶景海カフェ＆おしゃれ街歩き",
        "faqs": [
            ("混雑しやすいカフェの予約は必要？", "浜辺の茶屋や花人逢は予約不可の先着順です。オープン直後かランチのピークを外した14:00〜16:00の訪問がスムーズです。"),
            ("夕日（サンセット）を見るならどのカフェ？", "読谷村の星野リゾート バンタカフェや北谷のTransit Cafeは西海岸に位置しており、水平線に沈む夕日の絶景スポットとして有名です。")
        ]
    },
    {
        "slug": "north-drive",
        "title": "沖縄 美ら海水族館＆古宇利島 王道北部絶景ドライブコース | 0Margin Travel",
        "h1": "沖縄北部 王道絶景ドライブモデルコース",
        "subtitle": "初めての沖縄旅行はこれを選べば間違いなし！万座毛・美ら海・フクギ並木・古宇利島・アメリカンビレッジ",
        "meta_desc": "沖縄本島北部の王道観光地を1日で効率よく巡る完全制覇ドライブルート。万座毛、美ら海水族館、備瀬のフクギ並木、古宇利大橋、ハートロック、アメリカンビレッジを網羅。Googleマップ即時ナビ。無料・登録不要。",
        "keywords": "沖縄 北部 ドライブコース, 美ら海水族館 古宇利島 ルート, 沖縄 王道 モデルコース, 沖縄 1日観光ドライブ",
        "spot_ids": ["oki_p_10", "oki_p_15", "oki_p_16", "oki_p_17", "oki_p_41", "oki_p_9"],
        "tag": "🌺 王道・美ら海＆古宇利島絶景コース",
        "faqs": [
            ("1日でこのスポット数を無理なく回れますか？", "那覇を朝8:00〜8:30に出発し、沖縄自動車道（高速道路）を利用すれば夕方にアメリカンビレッジで夕日とディナーを楽しむちょうど良いスケジュールになります。"),
            ("運転初心者でも走りやすい道ですか？", "国道58号線および高速道路が中心のため、道幅も広く非常に運転しやすいルートです。")
        ]
    }
]

def generate_page(c):
    spots_data = []
    for sid in c["spot_ids"]:
        if sid in SPOTS_BY_ID:
            spots_data.append(SPOTS_BY_ID[sid])

    spots_param = ",".join(c["spot_ids"])
    interactive_planner_url = f"./?city=Okinawa%2C%20Japan&spots={spots_param}"

    # Generate spots list HTML
    spot_cards_html = ""
    for idx, s in enumerate(spots_data):
        name = s.get("name_ja") or s.get("name")
        desc = s.get("desc_ja") or s.get("desc") or ""
        tip = s.get("insiderTip_ja") or s.get("tip_ja") or s.get("tip") or ""
        price = s.get("price_ja") or s.get("price") or ""
        cat = s.get("category") or "観光スポット"
        rating = s.get("rating") or "4.5"
        img = s.get("image") or ""
        if img and not img.startswith("http") and not img.startswith("data:"):
            img = f"../{img}"
        
        maps_query = urllib.parse.quote(f"{name} 沖縄")
        maps_single_url = f"https://www.google.com/maps/search/?api=1&query={maps_query}"

        tip_box = f"""
        <div style="background:#FFFBEB; border:1.5px solid #FCD34D; padding:0.6rem 0.85rem; border-radius:10px; font-size:0.83rem; color:#92400E; margin-top:0.75rem; line-height:1.45;">
            <strong style="color:#78350F;">💡 現地耳より情報!!:</strong> {tip}
        </div>
        """ if tip else ""

        img_box = f"""
        <div style="width:100%; height:200px; overflow:hidden; border-radius:12px; margin-bottom:0.75rem; background:#0F172A; position:relative;">
            <img src="{img}" alt="{name}" loading="lazy" style="width:100%; height:100%; object-fit:cover;">
            <span style="position:absolute; top:8px; right:8px; font-size:0.75rem; font-weight:800; background:rgba(15,23,42,0.85); color:#34D399; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid rgba(16,185,129,0.4);">★{rating}</span>
        </div>
        """ if img else ""

        spot_cards_html += f"""
        <div class="card" style="background:rgba(15, 23, 42, 0.9); border:1.5px solid rgba(255, 255, 255, 0.2); border-radius:18px; padding:1.25rem; margin-bottom:1.25rem; box-shadow:0 8px 20px rgba(0,0,0,0.4);">
            {img_box}
            <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:0.5rem; flex-wrap:wrap; margin-bottom:0.4rem;">
                <div style="display:flex; align-items:center; gap:0.5rem;">
                    <span style="background:#059669; color:#FFF; border-radius:50%; width:26px; height:26px; display:inline-flex; align-items:center; justify-content:center; font-weight:800; font-size:0.85rem;">{idx + 1}</span>
                    <h3 style="margin:0; font-size:1.25rem; color:#FFFFFF; font-weight:800;">{name}</h3>
                </div>
                <div style="display:flex; gap:0.4rem; align-items:center;">
                    <span style="font-size:0.75rem; font-weight:700; background:rgba(56,189,248,0.2); color:#38BDF8; padding:0.15rem 0.55rem; border-radius:6px; border:1px solid rgba(56,189,248,0.4);">{cat}</span>
                    <a href="{maps_single_url}" target="_blank" rel="noopener noreferrer" style="color:#38BDF8; font-size:0.8rem; font-weight:700; text-decoration:none; background:rgba(56,189,248,0.15); padding:0.2rem 0.55rem; border-radius:6px; border:1px solid rgba(56,189,248,0.3);">📍 Maps ↗</a>
                </div>
            </div>
            <p style="font-size:0.9rem; color:#CBD5E1; line-height:1.6; margin:0.4rem 0 0.5rem 0;">{desc}</p>
            <div style="font-size:0.8rem; color:#FCD34D; font-weight:700;">料金目安: {price}</div>
            {tip_box}
        </div>
        """

    # Other courses links
    other_courses_html = ""
    for oc in COURSES:
        if oc["slug"] != c["slug"]:
            other_courses_html += f"""
            <a href="{oc['slug']}.html" style="display:inline-block; background:rgba(30,41,59,0.9); color:#FCD34D; border:1px solid rgba(245,158,11,0.4); padding:0.5rem 0.9rem; border-radius:999px; text-decoration:none; font-size:0.85rem; font-weight:700; margin:0.25rem;">
                {oc['tag']} ➔
            </a>
            """

    # FAQ HTML
    faq_html = ""
    for q, a in c["faqs"]:
        faq_html += f"""
        <div style="background:rgba(30,41,59,0.8); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:1rem; margin-bottom:0.75rem;">
            <div style="font-weight:800; color:#FCD34D; font-size:0.95rem; margin-bottom:0.35rem;">Q. {q}</div>
            <div style="font-size:0.88rem; color:#CBD5E1; line-height:1.5;">{a}</div>
        </div>
        """

    # Schema JSON-LD
    schema_data = {
        "@context": "https://schema.org",
        "@type": "TouristTrip",
        "name": c["h1"],
        "description": c["meta_desc"],
        "touristType": ["Family", "Couples", "Solo Travelers"],
        "itinerary": {
            "@type": "ItemList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "item": {
                        "@type": "TouristAttraction",
                        "name": s.get("name_ja") or s.get("name"),
                        "description": s.get("desc_ja") or s.get("desc") or ""
                    }
                } for i, s in enumerate(spots_data)
            ]
        }
    }
    schema_json = json.dumps(schema_data, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-KHHYMRCMVD"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-KHHYMRCMVD');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  
  <title>{c['title']}</title>
  <meta name="description" content="{c['meta_desc']}">
  <meta name="keywords" content="{c['keywords']}">
  <link rel="canonical" href="https://japan.0margintravel.com/okinawa/{c['slug']}.html">
  <link rel="icon" type="image/png" href="../assets/mascot.png">

  <!-- Open Graph -->
  <meta property="og:site_name" content="0Margin Travel 🌺 沖縄">
  <meta property="og:title" content="{c['title']}">
  <meta property="og:description" content="{c['meta_desc']}">
  <meta property="og:image" content="https://japan.0margintravel.com/img/og-okinawa.jpg">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://japan.0margintravel.com/okinawa/{c['slug']}.html">

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{c['title']}">
  <meta name="twitter:description" content="{c['meta_desc']}">
  <meta name="twitter:image" content="https://japan.0margintravel.com/img/og-okinawa.jpg">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css?v=20261019_jp2">

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {schema_json}
  </script>
</head>
<body>

  <div class="slogan-banner">
    <span>✨</span>
    <span>0Margin Travel 🌺 沖縄: 完全無料・登録不要の観光ルート自動作成＆Googleマップナビ</span>
  </div>

  <!-- Navbar -->
  <header class="navbar">
    <div style="display:flex; justify-content:space-between; align-items:center; flex:1 1 100%; min-width:280px;">
      <a href="./" class="brand-container" style="text-decoration:none;">
        <img src="../assets/mascot.png" alt="0MT Mascot" class="brand-mascot-img" style="width:46px; height:46px; object-fit:contain;">
        <div>
          <span class="brand-title" style="white-space:nowrap;">0Margin Travel 🌺 沖縄</span>
        </div>
      </a>
      <a href="./" style="background:#059669; color:#FFF; text-decoration:none; padding:0.4rem 0.85rem; border-radius:8px; font-size:0.85rem; font-weight:800; border:1px solid #34D399;">
        🗺️ スポット自由選択へ ↗
      </a>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section" style="padding: 2.5rem 1rem 1.5rem 1rem; text-align:center;">
    <div class="container" style="max-width:860px; margin:0 auto;">
      
      <!-- Breadcrumb -->
      <nav style="font-size:0.82rem; color:#94A3B8; margin-bottom:1rem; text-align:left;">
        <a href="../" style="color:#94A3B8; text-decoration:underline;">0Margin Travel Japan</a> &gt; 
        <a href="./" style="color:#94A3B8; text-decoration:underline;">沖縄本島</a> &gt; 
        <span style="color:#FCD34D;">{c['tag']}</span>
      </nav>

      <div style="display:inline-block; background:rgba(245,158,11,0.2); color:#FCD34D; border:1px solid rgba(245,158,11,0.4); padding:0.35rem 0.85rem; border-radius:999px; font-size:0.85rem; font-weight:800; margin-bottom:0.75rem;">
        {c['tag']}
      </div>

      <h1 style="font-size:2.2rem; color:#FFFFFF; margin-bottom:0.75rem; font-family:var(--font-serif); line-height:1.3;">
        {c['h1']}
      </h1>

      <p style="font-size:1.05rem; color:#CBD5E1; line-height:1.6; margin-bottom:1.5rem;">
        {c['subtitle']}
      </p>

      <!-- MASTER CTA: Instant Route Launch -->
      <div style="background:linear-gradient(135deg, rgba(5,150,105,0.25), rgba(4,120,87,0.35)); border:2px solid #10B981; border-radius:20px; padding:1.5rem; margin-bottom:2rem; box-shadow:0 0 25px rgba(16,185,129,0.35);">
        <div style="font-size:1.15rem; font-weight:800; color:#34D399; margin-bottom:0.5rem;">
          ⚡ 面倒な入力ゼロ！1タップでこの周遊コースが完成します
        </div>
        <p style="font-size:0.9rem; color:#E2E8F0; margin-bottom:1rem;">
          下のボタンを押すと、この{len(spots_data)}スポットが自動セットされ、Googleマップの最適ドライブコース（ルートA・B）が即時起動します。
        </p>
        <a href="{interactive_planner_url}" class="btn btn-emerald" style="display:inline-flex; align-items:center; justify-content:center; gap:0.5rem; padding:1.1rem 2rem; font-size:1.15rem; font-weight:800; text-decoration:none; border-radius:14px; width:100%; max-width:540px; box-shadow:0 6px 20px rgba(16,185,129,0.5);">
          <span>🗺️ このルートをGoogleマップで起動する ↗</span>
        </a>
      </div>

    </div>
  </section>

  <!-- Spot Listing Section -->
  <main class="container" style="max-width:860px; margin:0 auto; padding:0 1rem 3rem 1rem;">
    
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem;">
      <h2 style="font-size:1.4rem; color:#FCD34D; font-weight:800; margin:0;">
        📍 経由する厳選{len(spots_data)}スポット（巡りやすい推奨順）
      </h2>
    </div>

    {spot_cards_html}

    <!-- Mid-Page CTA Button -->
    <div style="text-align:center; margin:2.5rem 0;">
      <a href="{interactive_planner_url}" class="btn btn-emerald" style="display:inline-flex; align-items:center; justify-content:center; gap:0.5rem; padding:1rem 1.8rem; font-size:1.1rem; font-weight:800; text-decoration:none; border-radius:14px; width:100%; max-width:500px; box-shadow:0 6px 20px rgba(16,185,129,0.4);">
        <span>🚗 Googleマップでこの周遊ルートを開く ↗</span>
      </a>
      <div style="margin-top:0.6rem; font-size:0.82rem; color:#94A3B8;">
        ※画面上でスポットの追加・順番入れ替え・削除も自由に行えます
      </div>
    </div>

    <!-- Frequently Asked Questions -->
    <section style="margin-top:3rem;">
      <h2 style="font-size:1.35rem; color:#FCD34D; font-weight:800; margin-bottom:1rem;">
        ❓ よくある質問・ドライブの注意点
      </h2>
      {faq_html}
    </section>

    <!-- Other Model Courses Section -->
    <section style="margin-top:3rem; padding:1.5rem; background:rgba(15,23,42,0.8); border:1.5px solid rgba(255,255,255,0.18); border-radius:18px;">
      <h2 style="font-size:1.2rem; color:#FFFFFF; font-weight:800; margin-bottom:0.75rem;">
        🌺 その他の沖縄テーマ別モデルコース
      </h2>
      <p style="font-size:0.85rem; color:#94A3B8; margin-bottom:1rem;">
        旅行の同行者や滞在時間、天候に合わせて最適なコースをお選びいただけます。
      </p>
      <div>
        {other_courses_html}
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer style="margin-top:4rem; padding: 2.5rem 1rem 5rem 1rem; color: var(--text-secondary); font-size: 0.85rem; border-top: 1px dashed rgba(255,255,255,0.15); background: var(--bg-dark); text-align:center;">
    <div style="max-width:1200px; margin:0 auto;">
      <div class="footer-brand" style="margin-bottom:0.5rem; font-size:1.3rem; font-weight:800; color:#FCD34D;">0Margin Travel 🌺 沖縄</div>
      <p class="footer-text" style="margin-bottom:1.25rem; color:#94A3B8;">
        沖縄・日本国内旅行 AI最適ルートプランナー ＆ Googleマップ周遊ナビ
      </p>
      <div style="display:flex; justify-content:center; gap: 1.25rem; margin-bottom: 1.25rem; flex-wrap:wrap;">
        <a href="./" style="color:#FCD34D; text-decoration:underline; font-weight:700;">🌺 沖縄トップ (スポット自由選択)</a>
        <a href="https://0margintravel.com/" target="_blank" rel="noopener noreferrer" style="color:#CBD5E1; text-decoration:underline;">🌍 ヨーロッパ27都市版 ↗</a>
      </div>
      <div class="footer-bottom" style="margin-top:1.25rem; border-top:1px dashed rgba(255,255,255,0.15); padding-top:1rem; color:#64748B;">
        <p>&copy; 2026 0Margin Travel 🌺 沖縄. All rights reserved.</p>
      </div>
    </div>
  </footer>

</body>
</html>
"""
    return html

def update_sitemap():
    sitemap_path = os.path.join(PROJECT_DIR, 'sitemap.xml')
    urls = [
        ("https://japan.0margintravel.com/", "0.9"),
        ("https://japan.0margintravel.com/okinawa/", "1.0")
    ]
    for c in COURSES:
        urls.append((f"https://japan.0margintravel.com/okinawa/{c['slug']}.html", "0.8"))

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for loc, priority in urls:
        xml_lines.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>2026-10-19</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>')
    xml_lines.append('</urlset>')

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_lines) + '\n')
    print(f"Updated {sitemap_path} with {len(urls)} URLs.")

def main():
    os.makedirs(OKINAWA_DIR, exist_ok=True)
    for c in COURSES:
        out_path = os.path.join(OKINAWA_DIR, f"{c['slug']}.html")
        html = generate_page(c)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {out_path}")

    update_sitemap()
    print("All SEO landing pages generated successfully!")

if __name__ == '__main__':
    main()
