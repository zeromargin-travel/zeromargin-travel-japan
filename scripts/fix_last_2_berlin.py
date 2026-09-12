import json

fpath = "data/cities/berlin.json"
with open(fpath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for s in data['spots']:
    if s['id'] == 'b_5b': # Alte Nationalgalerie
        s['tip_ja'] = "🖼️ 3.06展示室へ直行！カスパー・ダーヴィト・フリードリヒの名作『海辺の修道士』と『オークの森の修道院』が並んで鑑賞できます。"
        s['tip_en'] = "🖼️ Head straight to Room 3.06 to view Friedrich's masterworks 'The Monk by the Sea' and 'Abbey in the Oakwood'."
        s['tip'] = s['tip_en']
    elif s['id'] == 'b_13f': # Computerspielemuseum
        s['tip_ja'] = "🎮 1951年の最初期の対戦機Nimrodや、パックマン、インベーダーの実機筐体を無料で遊べます！"
        s['tip_en'] = "🎮 Play authentic classics like Nimrod, Pac-Man, Space Invaders, and Pong on genuine coin-op hardware!"
        s['tip'] = s['tip_en']

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Perfect! Fixed last 2 n-gram overlaps in Berlin.")
