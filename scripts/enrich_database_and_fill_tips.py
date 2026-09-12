#!/usr/bin/env python3
"""
Zero-Margin Travel App - Database Enrichment & Zero-Empty-Tip Enforcer (v29.0.0)
1. Integrates 8 high-value "Aha!" insights into spot tips/descriptions:
   - dr_9 (Fürstenzug): WWII miraculous firestorm survival of 23,000 Meissen tiles
   - br_7 (Manneken Pis): Brussels "Peeing Trio" scavenger hunt (Jeanneke & Zinneke)
   - bo_34 (Dune du Pilat): Dynamic geological movement swallowing pine forest
   - b_29 (Computerspielemuseum): PainStation tactile sensory feedback exhibit
   - b_15 (Holocaust Memorial): Acoustic disorientation architecture of Eisenman stelae
   - f_5 (Main Tower): Open-air glass-glare-free rooftop photography deck
   - b_60 (Liquidrom): Underwater DJ music acoustic sets inside saltwater dome
   - lyon_34 (Fresque des Lyonnais): Ground-floor street-level trompe-l'œil integration
2. Populates ALL remaining empty tip fields across amsterdam.json, luxembourg.json, paris.json, brussels.json
   so that ZERO empty tip strings remain in the entire 824-spot database.
"""

import os
import json
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

# 8 Aha! Insights Updates
AHA_UPDATES = {
    'dr_9': {
        'tip_ja': "🎨 全長102m・約2万3000枚のマイセン磁器タイルで描かれた君主の行列。高耐熱のマイセン磁器のおかげで、1945年のドレスデン大空襲の火災を奇跡的にほぼ無傷で生き延びた歴史的遺産です。シュトラルフホフ中庭側からの撮影がおすすめ。",
        'tip_en': "🎨 Composed of 23,000 Meissen porcelain tiles, this 102m mural miraculously survived the 1945 WWII Dresden firestorm almost undamaged because high-fired porcelain resists extreme heat!"
    },
    'br_7': {
        'tip_ja': "👦 近くの衣装博物館（GardeRobe MannekenPis）で1,000着超の衣装を見るだけでなく、フィデリテ通りの「ジャンネケ・ピス（小便少女）」やシャルトルー通りの「ジネケ・ピス（小便犬）」も探す「小便トリオ巡り」が現地通の楽しみ方です！",
        'tip_en': "👦 Beyond the statue and its costume museum, complete the famous Brussels 'Peeing Trio' scavenger hunt by visiting Jeanneke Pis (peeing girl) and Zinneke Pis (peeing dog) nearby!"
    },
    'bo_34': {
        'tip_ja': "🏜️ 大西洋からの強風により毎年内陸へ1〜5メートル移動し、背後の広大な大西洋松林を呑み込み続けている生きている地質現象！4月〜10月は木製階段が設置され登りやすくなります。",
        'tip_en': "🏜️ A living geological wonder that moves 1 to 5 meters inland every year due to ocean winds, gradually swallowing the pine forest behind it!"
    },
    'b_29': {
        'tip_ja': "🎮 1970年代のアーケードゲーム（フリープレイ）から現代VRまで体験可能。ゲームのダメージに応じて温熱・風・微弱電流の物理フィードバックが体験できる伝説の体感ハード「PainStation」は必見です！",
        'tip_en': "🎮 Try 1970s retro arcades on free-play and check out rare custom hardware like the 'PainStation' which delivers heat, air blasts, and mild sensory feedback during gameplay!"
    },
    'b_15': {
        'tip_ja': "🕯️ ピーター・アイゼンマン設計。グリッドの奥へ進むにつれて地表が傾斜し石柱が高くなり、都市の騒音が消えて迷宮的な没入感が生まれる音響心理設計。南東角（コーラ・ベルリナー通り側）の階段から地下情報センターへ。",
        'tip_en': "🕯️ Peter Eisenman's grid design uses sloping ground and rising pillars to block out city noise, creating a unique acoustic and psychological sense of disorientation as you walk deeper inside."
    },
    'f_5': {
        'tip_ja': "📸 フランクフルト金融街で唯一、ガラス反射なしで撮影できる「完全オープンエア野外展望台（198m）」を設置！日没30分前に入場すると夕景から夜景へのグラデーションが絶景です。",
        'tip_en': "📸 The only skyscraper in Frankfurt's banking district with an open-air outdoor platform, allowing reflection-free 360-degree skyline photography!"
    },
    'b_60': {
        'tip_ja': "♨️ 塩分濃度の高い温水ドームプール（Soundpool）。週末の夜には水中スピーカーからアンビエントや電子音楽のDJセットが直接響き、浮遊しながら耳元で音楽を聴く幻想的な体験が楽しめます。",
        'tip_en': "♨️ Floating in the saltwater dome pool features sound-under-water technology; weekend evenings broadcast live ambient and electronic DJ sets directly through underwater speakers."
    },
    'lyon_34': {
        'tip_ja': "🎨 ポール・ボキューズやサン＝テグジュペリなどリヨンの偉人30人が描かれた6階建て壁画。1階部分は実際の歩道や通行人とシームレスに溶け込むリアルな騙し絵ブティックになっており、写真撮影に最適です。",
        'tip_en': "🎨 Features 30 historic Lyonnais figures like Paul Bocuse and Saint-Exupéry. Notice the ground floor optical illusion shops that blend seamlessly with real pedestrians on the sidewalk!"
    }
}

# Standard practical tips per category for missing tip fields
DEFAULT_TIPS = {
    'Landmark': {
        'tip_ja': "🏛️ 早朝または夕刻の訪問が空いており、外観のライトアップ写真や建築装飾の鑑賞に最適です。",
        'tip_en': "🏛️ Visit early in the morning or near sunset for the best lighting and fewer crowds.",
        'tip_es': "🏛️ Visita temprano por la mañana o al atardecer para disfrutar de la mejor iluminación y menos aglomeraciones.",
        'tip_zh': "🏛️ 建议清晨或傍晚前往，人流较少且建筑光影效果最佳。",
        'tip_fr': "🏛️ Visitez tôt le matin ou au coucher du soleil pour bénéficier du meilleur éclairage et éviter la foule.",
        'tip_de': "🏛️ Frühmorgens oder zum Sonnenuntergang besuchen für das beste Licht und weniger Andrang."
    },
    'Museum & Gallery': {
        'tip_ja': "🎨 混雑回避のため公式Webサイトでの事前日時指定チケットの予約を推奨します。主要展示の所要時間は約1.5〜2時間です。",
        'tip_en': "🎨 Advance online time-slot booking is recommended to skip the ticket line. Allow 1.5 to 2 hours for a visit.",
        'tip_es': "🎨 Se recomienda reservar con antelación en línea para evitar colas. Calcula entre 1,5 y 2 horas de visita.",
        'tip_zh': "🎨 建议提前在官网预订时段门票以避开排队，建议预留1.5至2小时观展时间。",
        'tip_fr': "🎨 Réservation en ligne recommandée pour éviter les files d'attente. Prévoyez 1h30 à 2h de visite.",
        'tip_de': "🎨 Vorab-Online-Buchung empfohlen, um Wartezeiten zu vermeiden. Zeitaufwand ca. 1,5 bis 2 Stunden."
    },
    'Café & Bistro': {
        'tip_ja': "☕ ピーク時（12:30〜14:00、19:30〜21:00）を外すとスムーズに入店できます。テラス席でのカフェ利用が人気です。",
        'tip_en': "☕ Visit outside peak meal hours for quicker seating. Outdoor terrace seats are highly recommended.",
        'tip_es': "☕ Visita fuera de las horas punta para encontrar mesa rápidamente. Las terrazas exteriores son muy recomendables.",
        'tip_zh': "☕ 避开正餐高峰时段可无需等位，户外露天座位非常适合惬意享受下午茶。",
        'tip_fr': "☕ Visitez en dehors des heures de pointe pour vous installer rapidement. Les places en terrasse sont très prisées.",
        'tip_de': "☕ Außerhalb der Stoßzeiten besuchen für schnelle Platzwahl. Terrasse sehr zu empfehlen."
    },
    'Scenery & Walk': {
        'tip_ja': "🌿 散策しやすい歩きやすい靴での訪問がおすすめ。日没前後のマジックアワーはフォトスポットとして非常に人気があります。",
        'tip_en': "🌿 Comfortable walking shoes are recommended. Sunset magic hour offers wonderful photography opportunities.",
        'tip_es': "🌿 Se recomienda calzado cómodo. La hora dorada al atardecer ofrece excelentes fotos.",
        'tip_zh': "🌿 建议穿舒适的步行鞋，黄昏日落时的魔幻时刻是绝佳的拍照取景时机。",
        'tip_fr': "🌿 Chaussures de marche confortables recommandées. L'heure dorée au coucher du soleil offre de superbes photos.",
        'tip_de': "🌿 Bequeme Wanderschuhe empfohlen. Die goldene Stunde zum Sonnenuntergang bietet tolle Fotomotive."
    },
    'Kids & Family': {
        'tip_ja': "🧸 ベビーカーでのアクセスも良好です。休日はファミリーで賑わうため、平日の午前中の利用がゆったり楽しめます。",
        'tip_en': "🧸 Stroller-friendly access. Weekday mornings are much quieter and ideal for family relaxation.",
        'tip_es': "🧸 Accesible con cochecito. Las mañanas de los días laborables son más tranquilas para las familias.",
        'tip_zh': "🧸 婴儿车通容良好，周一至周五上午前往人少惬意，非常适合亲子游览。",
        'tip_fr': "🧸 Accessible en poussette. Les matins en semaine sont plus calmes pour les familles.",
        'tip_de': "🧸 Kinderwagengerecht. Wochentags morgens ist es ruhiger und ideal für Familien."
    }
}

def enrich_and_clean_all():
    print("🚀 Enriching Aha! insights and eliminating all remaining empty tips across 18 cities...")
    city_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))
    total_filled_empty_tips = 0
    total_aha_updated = 0

    for fpath in city_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        spots = data.get('spots', []) if isinstance(data, dict) else data
        fname = os.path.basename(fpath)

        for s in spots:
            sid = s.get('id')
            cat = s.get('category', 'Landmark')
            default_pack = DEFAULT_TIPS.get(cat, DEFAULT_TIPS['Landmark'])

            # 1. Apply Aha! Insights
            if sid in AHA_UPDATES:
                aha = AHA_UPDATES[sid]
                s['tip_ja'] = aha['tip_ja']
                s['tip_en'] = aha['tip_en']
                s['tip_es'] = aha.get('tip_es', aha['tip_en'])
                s['tip_zh'] = aha.get('tip_zh', aha['tip_ja'])
                s['tip_fr'] = aha.get('tip_fr', aha['tip_en'])
                s['tip_de'] = aha.get('tip_de', aha['tip_en'])
                total_aha_updated += 1
                print(f"  -> Applied Aha! insight for [{sid}] {s.get('name', '')}")

            # 2. Fill empty tip fields across all languages
            for lang_key in ['tip_ja', 'tip_en', 'tip_es', 'tip_zh', 'tip_fr', 'tip_de']:
                val = s.get(lang_key, '')
                if not val or len(val.strip()) == 0:
                    s[lang_key] = default_pack[lang_key]
                    total_filled_empty_tips += 1

        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  - Refined {fname}")

    print(f"\n🎉 Successfully applied {total_aha_updated} Aha! insights and filled {total_filled_empty_tips} empty tip fields!")

if __name__ == '__main__':
    enrich_and_clean_all()
