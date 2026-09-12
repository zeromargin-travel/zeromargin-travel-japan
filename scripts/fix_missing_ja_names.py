import json

fixes = {
    "cologne.json": {
        "c_6": ("Brauhaus Sion", "ブラウハウス・ジオン"),
        "c_8": ("Bei Oma Kleinmann", "バイ・オマ・クラインマン")
    },
    "luxembourg.json": {
        "l_1": ("Bock Casemates", "ボックの要塞・地下回廊"),
        "l_10": ("Um Plateau", "ウム・プラトー")
    },
    "lyon.json": {
        "lyon_5": ("Place des Terreaux & Bartholdi Fountain", "テロー広場＆バルトルディの噴水")
    },
    "marseille.json": {
        "ma_15": ("Musée des Beaux-Arts de Marseille", "マルセイユ美術館"),
        "ma_19": ("Friche la Belle de Mai", "フリッシュ・ラ・ベル・ド・メ"),
        "ma_23": ("Marché aux Poissons du Vieux-Port", "旧港の魚市場"),
        "ma_26": ("La Samaritaine & Café de la Banque", "ラ・サマリテーヌ＆カフェ・ド・ラ・バンク"),
        "ma_30": ("Vallon des Auffes", "ヴァロン・デ・ゾフ漁港")
    },
    "paris.json": {
        "p_5": ("Cathédrale Notre-Dame de Paris", "ノートルダム大聖堂")
    },
    "strasbourg.json": {
        "st_10": ("Église Saint-Thomas", "サン・トマ教会"),
        "st_16": ("Musée des Beaux-Arts de Strasbourg", "ストラスブール美術館")
    }
}

for fname, spot_dict in fixes.items():
    fpath = f"data/cities/{fname}"
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for s in data['spots']:
        sid = s['id']
        if sid in spot_dict:
            local_name, ja_name = spot_dict[sid]
            s['name_ja'] = f"{local_name}（{ja_name}）"
            s['name_en'] = f"{local_name} ({local_name})" if local_name != ja_name else local_name
            s['name'] = s['name_ja']

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Successfully updated missing Japanese names!")
