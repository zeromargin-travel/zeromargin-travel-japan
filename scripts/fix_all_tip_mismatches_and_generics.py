#!/usr/bin/env python3
"""
Zero-Margin Travel App - Universal Tip Alignment & Generic Placeholder Elimination Script (v19.0.0)
1. Fixes Arc de Triomphe (p_2) Louvre tip mismatch.
2. Replaces generic placeholder duplicate tips with authentic spot-specific secrets or clean empty tip handling (`tip: ""`).
"""

import glob
import json
import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
json_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))

GENERIC_PLACEHOLDERS = [
    "素晴らしい写真を撮り",
    "混雑が少ない早朝またはゴールデンアワー",
    "早朝またはゴールデンアワー",
    "best time to visit is early morning",
    "take great photos"
]

# Curated high-quality tips for specific spots
CURATED_TIPS = {
    # Paris Arc de Triomphe
    "p_2": {
        "tip_ja": "🎟️ 地下通路からアプローチ（地上交通の横断は厳禁）！夕暮れ30分前に屋上展望台へ登り、シャンゼリゼ通りと放射状に広がる12大通りの絶景、そして点灯するエッフェル塔を撮影するのが最高の裏技です。",
        "tip_en": "🎟️ Access via the underground pedestrian tunnel (never attempt to cross the chaotic roundabout above ground)! Climb to the rooftop 30 minutes before sunset for breathtaking 360° views down the 12 radiating avenues and the sparkling Eiffel Tower.",
        "tip_es": "🎟️ Accede a través del túnel subterráneo peatonal (¡nunca intentes cruzar la rotonda a pie!). Sube a la azotea 30 minutos antes del atardecer para disfrutar de las mejores vistas hacia las 12 avenidas y la Torre Eiffel iluminada.",
        "tip_zh": "🎟️ 必须走地下通道进入（绝对严禁穿行地面的环岛车道）！建议在日落前30分钟登顶，360度俯瞰12条放射状大干道以及华灯初上的埃菲尔铁塔。",
        "tip_fr": "🎟️ Accédez obligatoirement par le souterrain piéton (ne traversez jamais le rond-point au niveau de la rue) ! Montez sur le toit 30 minutes avant le coucher du soleil pour admirer les 12 avenues et la Tour Eiffel éclairée.",
        "tip_de": "🎟️ Zugang zwingend durch die Unterführung (niemals den Kreisverkehr oberirdisch überqueren)! Steigen Sie 30 Min. vor Sonnenuntergang auf die Aussichtsplattform für den besten Blick auf die 12 Alleen und den Eiffelturm.",
        "tip": "🎟️ Access via the underground pedestrian tunnel (never attempt to cross the chaotic roundabout above ground)! Climb to the rooftop 30 minutes before sunset for breathtaking 360° views down the 12 radiating avenues and the sparkling Eiffel Tower."
    },
    # Amsterdam Rijksmuseum
    "a_1": {
        "tip_ja": "🎟️ 公式サイトで『夜警（The Night Watch）』開館直後（9:00開館）または15:30以降の時間帯を事前予約するのが最も空いている狙い目です。",
        "tip_en": "🎟️ Book the 9:00 AM opening slot or post-3:30 PM slot online to view Rembrandt's 'The Night Watch' without heavy tour crowds.",
        "tip_es": "🎟️ Reserva el horario de las 9:00 h o después de las 15:30 h en línea para ver 'La ronda de noche' de Rembrandt sin aglomeraciones.",
        "tip_zh": "🎟️ 强烈建议在线预订早晨9:00首场或下午15:30以后的时段，可避开导游团近距离观赏伦勃朗《夜巡》。",
        "tip_fr": "🎟️ Réservez le créneau de 9h00 ou après 15h30 en ligne pour admirer 'La Ronde de nuit' de Rembrandt sans la foule.",
        "tip_de": "🎟️ Buchen Sie online das Zeitfenster um 9:00 Uhr oder nach 15:30 Uhr, um Rembrandts 'Nachtwache' ohne Reisegruppen zu sehen.",
        "tip": "🎟️ Book the 9:00 AM opening slot or post-3:30 PM slot online to view Rembrandt's 'The Night Watch' without heavy tour crowds."
    },
    # Amsterdam Van Gogh Museum
    "a_2": {
        "tip_ja": "🎟️ 完全事前オンライン日時指定制！現地での当日券販売は一切ないため、2〜4週間前のWEB予約が必須です。金曜夜の21:00夜間開館も穴場です。",
        "tip_en": "🎟️ Mandatory online booking weeks in advance (no tickets sold at the door)! Friday evening night openings (until 9 PM) feature DJ sessions and fewer crowds.",
        "tip_es": "🎟️ ¡Reserva obligatoria por internet semanas antes (no hay taquilla)! Las noches de los viernes (hasta las 21:00) cuentan con sesiones de DJ y menos gente.",
        "tip_zh": "🎟️ 门票全网必须提前数周在线预订（现场无售票处）！周五夜场开放至21:00，结合音乐会，人流大幅减少。",
        "tip_fr": "🎟️ Billet en ligne obligatoire des semaines à l'avance ! Les nocturnes du vendredi soir (jusqu'à 21h) proposent une ambiance musicale et moins de monde.",
        "tip_de": "🎟️ Verpflichtende Online-Buchung Wochen im Voraus! Freitagabends (bis 21:00 Uhr) gibt es Musik-Events und deutlich weniger Andrang.",
        "tip": "🎟️ Mandatory online booking weeks in advance (no tickets sold at the door)! Friday evening night openings (until 9 PM) feature DJ sessions and fewer crowds."
    },
    # Amsterdam Anne Frank House
    "a_3": {
        "tip_ja": "🎟️ 毎週火曜日の現地時間10:00に『6週間後の1週間分』のチケットが公式サイトで一括販売されます。アラームを設定して即確保が必須です。",
        "tip_en": "🎟️ Tickets are released every Tuesday at 10:00 AM CET for visits 6 weeks in advance. Set an alarm to secure your slot immediately upon release.",
        "tip_es": "🎟️ Las entradas se lanzan cada martes a las 10:00 h (CET) para visitas con 6 semanas de antelación. Pon una alarma para reservarla de inmediato.",
        "tip_zh": "🎟️ 门票于每周二欧洲时间10:00集中放票（抢购6周后的参观名额）。请务必提前设好闹钟抢票。",
        "tip_fr": "🎟️ Les billets sont mis en vente chaque mardi à 10h00 pour les visites 6 semaines plus tard. Mettez une alarme pour réserver dès l'ouverture.",
        "tip_de": "🎟️ Tickets werden jeden Dienstag um 10:00 Uhr MEZ für Besuche in 6 Wochen freigeschaltet. Stellen Sie einen Wecker zur Buchung!",
        "tip": "🎟️ Tickets are released every Tuesday at 10:00 AM CET for visits 6 weeks in advance. Set an alarm to secure your slot immediately upon release."
    }
}

total_fixed = 0

for jf in json_files:
    fname = os.path.basename(jf)
    with open(jf, 'r', encoding='utf-8') as f:
        city_data = json.load(f)

    spots = city_data.get('spots', [])
    city_modified = False

    for s in spots:
        sid = s.get('id', '')
        
        # 1. Apply specific curated tips if present
        if sid in CURATED_TIPS:
            for k, v in CURATED_TIPS[sid].items():
                s[k] = v
            city_modified = True
            total_fixed += 1
            continue

        # 2. Check if spot contains a generic placeholder tip
        tip_ja = s.get('tip_ja', '') or s.get('tip', '')
        if any(p.lower() in tip_ja.lower() for p in GENERIC_PLACEHOLDERS):
            # Clear generic tip across all language fields to let Smart Empty Tip Handling render clean UI
            s['tip_ja'] = ""
            s['tip_en'] = ""
            s['tip_es'] = ""
            s['tip_zh'] = ""
            s['tip_fr'] = ""
            s['tip_de'] = ""
            s['tip'] = ""
            city_modified = True
            total_fixed += 1

    if city_modified:
        city_data['spots'] = spots
        with open(jf, 'w', encoding='utf-8') as f:
            json.dump(city_data, f, indent=2, ensure_ascii=False)
        print(f"  - Cleaned & aligned tips in {fname}")

print(f"\n🎉 Successfully aligned and cleaned tips across {total_fixed} spots!")
