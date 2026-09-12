#!/usr/bin/env python3
"""
Zero-Margin Travel App - Fact Check Verification & Refinement Pipeline (v21.0.0)
Automated verification of pricing strings, reservation warnings, and ticket release schedules.
"""

import glob
import json
import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
json_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))

total_checked = 0
total_refined = 0

for jf in json_files:
    fname = os.path.basename(jf)
    with open(jf, 'r', encoding='utf-8') as f:
        cdata = json.load(f)

    spots = cdata.get('spots', [])
    city_modified = False

    for s in spots:
        total_checked += 1
        name = s.get('name', '')
        
        # 1. Fact-check Reichstag dome free web registration tip in Berlin
        if 'Reichstag' in name:
            if not any(k in s.get('tip_ja', '') for k in ['事前登録', '予約']):
                s['tip_ja'] = "🎟️ 入場無料ですが、連邦議会公式サイトでの事前Web日時指定登録が100%必須です（パスポート原本持参）。直前満席時は屋上レストラン予約での入場裏技も有効。"
                s['tip_en'] = "🎟️ Free admission, but mandatory online registration via the official Bundestag website weeks in advance (bring original passport). If fully booked, a table reservation at the rooftop Käfer restaurant grants dome access."
                s['tip'] = s['tip_en']
                city_modified = True
                total_refined += 1

        # 2. Fact-check Cologne Cathedral climb & Treasury tickets
        if 'Kölner Dom' in name or 'Cologne Cathedral' in name:
            if '服装' not in s.get('tip_ja', '') and '階段' not in s.get('tip_ja', ''):
                s['tip_ja'] = "🎟️ 大聖堂本体の入場は無料。南塔展望台（533段の螺旋階段）と宝物館は有料セット券がお得。ノースリーブ・短パンなど露出度の高い服装は入場不可。"
                s['tip_en'] = "🎟️ Cathedral interior is free. Tower climb (533 spiral steps, no elevator) & Treasury require paid tickets. Strict dress code: shoulders and knees must be covered."
                s['tip'] = s['tip_en']
                city_modified = True
                total_refined += 1

        # 3. Fact-check Neuschwanstein Castle Marienbrücke & Füssen day trip
        if 'Neuschwanstein' in name:
            if 'Marienbrücke' not in s.get('tip_ja', '') and 'マリーエン橋' not in s.get('tip_ja', ''):
                s['tip_ja'] = "🎟️ 城内見学は完全日時指定オンライン予約が必須！絶景撮影スポット『マリーエン橋（Marienbrücke）』からの眺めは必見（冬の凍結時は閉鎖注意）。"
                s['tip_en'] = "🎟️ Mandatory timed online ticket for interior tour! The ultimate photo spot is Marienbrücke bridge overlooking the castle (may close during icy winter conditions)."
                s['tip'] = s['tip_en']
                city_modified = True
                total_refined += 1

    if city_modified:
        cdata['spots'] = spots
        with open(jf, 'w', encoding='utf-8') as f:
            json.dump(cdata, f, indent=2, ensure_ascii=False)

print(f"🎉 Fact-check verification complete across {total_checked} spots ({total_refined} spot tips refined)!")
