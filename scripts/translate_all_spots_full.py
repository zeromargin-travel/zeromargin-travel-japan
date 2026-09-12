import json
import glob
import os

# Dictionary of spot name translations for key landmark spots across Western Europe
NAME_TRANSLATIONS = {
    # Paris
    "Eiffel Tower": {
        "en": "Eiffel Tower", "ja": "エッフェル塔", "es": "Torre Eiffel", "zh": "埃菲尔铁塔", "fr": "Tour Eiffel", "de": "Eiffelturm"
    },
    "Louvre Museum": {
        "en": "Louvre Museum", "ja": "ルーヴル美術館", "es": "Museo del Louvre", "zh": "卢浮宫博物馆", "fr": "Musée du Louvre", "de": "Louvre-Museum"
    },
    "Arc de Triomphe": {
        "en": "Arc de Triomphe", "ja": "エトワール凱旋門", "es": "Arco del Triunfo", "zh": "巴黎凯旋门", "fr": "Arc de Triomphe", "de": "Triumphbogen"
    },
    "Sainte-Chapelle": {
        "en": "Sainte-Chapelle", "ja": "サント・シャペル礼拝堂", "es": "Sainte-Chapelle", "zh": "圣礼拜堂", "fr": "Sainte-Chapelle", "de": "Sainte-Chapelle"
    },
    "Sacré-Cœur Basilica & Montmartre": {
        "en": "Sacré-Cœur Basilica & Montmartre", "ja": "サクレ・クール寺院＆モンマルトルの丘", "es": "Basílica del Sacré-Cœur y Montmartre", "zh": "圣心大教堂与蒙马特高地", "fr": "Basilique du Sacré-Cœur & Montmartre", "de": "Basilika Sacré-Cœur & Montmartre"
    },
    "Notre-Dame Cathedral": {
        "en": "Notre-Dame Cathedral", "ja": "ノートルダム大聖堂", "es": "Catedral de Notre-Dame", "zh": "巴黎圣母院", "fr": "Cathédrale Notre-Dame de Paris", "de": "Kathedrale Notre-Dame"
    },
    "Musée d'Orsay": {
        "en": "Musée d'Orsay", "ja": "オルセー美術館", "es": "Museo de Orsay", "zh": "奥赛博物馆", "fr": "Musée d'Orsay", "de": "Musée d'Orsay"
    },
    "Centre Pompidou": {
        "en": "Centre Pompidou", "ja": "ポンピドゥー・センター", "es": "Centro Pompidou", "zh": "蓬皮杜艺术中心", "fr": "Centre Pompidou", "de": "Centre Pompidou"
    },
    "Palace of Versailles": {
        "en": "Palace of Versailles", "ja": "ヴェルサイユ宮殿", "es": "Palacio de Versalles", "zh": "凡尔赛宫", "fr": "Château de Versailles", "de": "Schloss Versailles"
    },
    "Disneyland Paris": {
        "en": "Disneyland Paris", "ja": "ディズニーランド・パリ", "es": "Disneyland París", "zh": "巴黎迪士尼乐园", "fr": "Disneyland Paris", "de": "Disneyland Paris"
    },

    # Toulouse
    "Place du Capitole & Capitole de Toulouse": {
        "en": "Place du Capitole & Capitole de Toulouse", "ja": "キャピトル広場＆市庁舎", "es": "Plaza del Capitole y Capitolio de Toulouse", "zh": "市政厅广场与图卢兹市政厅", "fr": "Place du Capitole & Capitole de Toulouse", "de": "Place du Capitole & Capitole von Toulouse"
    },
    "Basilique Saint-Sernin": {
        "en": "Basilique Saint-Sernin", "ja": "サン・セルナン大聖堂", "es": "Basílica de San Sernín", "zh": "圣塞尔南大教堂", "fr": "Basilique Saint-Sernin", "de": "Basilika Saint-Sernin"
    },
    "Couvent des Jacobins": {
        "en": "Couvent des Jacobins", "ja": "ジャコバン修道院", "es": "Convento de los Jacobeos", "zh": "雅各宾修道院", "fr": "Couvent des Jacobins", "de": "Jakobinerkloster"
    },
    "Pont Neuf Toulouse": {
        "en": "Pont Neuf Toulouse", "ja": "ポン・ヌフ（トゥールーズ新橋）", "es": "Pont Neuf de Toulouse", "zh": "图卢兹新桥", "fr": "Pont Neuf de Toulouse", "de": "Pont Neuf Toulouse"
    },
    "Cathédrale Saint-Étienne de Toulouse": {
        "en": "Cathédrale Saint-Étienne de Toulouse", "ja": "サン・テティエンヌ大聖堂", "es": "Catedral de San Esteban de Toulouse", "zh": "图卢兹圣艾蒂安大教堂", "fr": "Cathédrale Saint-Étienne de Toulouse", "de": "Kathedrale Saint-Étienne von Toulouse"
    },
    "Hôtel d'Assézat": {
        "en": "Hôtel d'Assézat", "ja": "アセザ館（ルネサンス大邸宅）", "es": "Palacio d'Assézat", "zh": "阿塞扎大宅", "fr": "Hôtel d'Assézat", "de": "Hôtel d'Assézat"
    },
    "Chapelle des Carmélites": {
        "en": "Chapelle des Carmélites", "ja": "カルメル会礼拝堂", "es": "Capilla de las Carmelitas", "zh": "迦密会礼拜堂", "fr": "Chapelle des Carmélites", "de": "Karmeliterkapelle"
    },
    "Hôtel-Dieu Saint-Jacques": {
        "en": "Hôtel-Dieu Saint-Jacques", "ja": "オテル・デュー・サン・ジャック", "es": "Hôtel-Dieu Saint-Jacques", "zh": "圣雅克主教医院旧址", "fr": "Hôtel-Dieu Saint-Jacques", "de": "Hôtel-Dieu Saint-Jacques"
    },
    "Cité de Carcassonne": {
        "en": "Cité de Carcassonne", "ja": "カルカソンヌ城塞都市（世界遺産）", "es": "Ciudadela de Carcasona", "zh": "卡尔卡松城堡（世界遗产）", "fr": "Cité de Carcassonne", "de": "Cité von Carcassonne"
    },
    "Cité Épiscopale d'Albi & Cathédrale Sainte-Cécile": {
        "en": "Cité Épiscopale d'Albi & Cathédrale Sainte-Cécile", "ja": "アルビ司教都市＆サント・セシル大聖堂", "es": "Ciudad Episcopal de Albi y Catedral de Santa Cecilia", "zh": "阿尔比主教城与圣塞西尔大教堂", "fr": "Cité Épiscopale d'Albi & Cathédrale Sainte-Cécile", "de": "Bischofsstadt Albi & Kathedrale Sainte-Cécile"
    },
    "Cité de l'Espace": {
        "en": "Cité de l'Espace", "ja": "シテ・ド・レスパス（宇宙の街テーマパーク）", "es": "Cité de l'Espace", "zh": "太空城航天主题公园", "fr": "Cité de l'Espace", "de": "Cité de l'Espace"
    },
    "La Halle de la Machine": {
        "en": "La Halle de la Machine", "ja": "ラ・アル・ド・ラ・マシン（巨大機械怪獣パーク）", "es": "La Halle de la Machine", "zh": "机械大厅艺术园区", "fr": "La Halle de la Machine", "de": "La Halle de la Machine"
    },
    "Musée des Augustins": {
        "en": "Musée des Augustins", "ja": "オーギュスタン美術館", "es": "Museo de los Agustinos", "zh": "奥古斯丁博物馆", "fr": "Musée des Augustins", "de": "Musée des Augustins"
    },
    "Fondation Bemberg": {
        "en": "Fondation Bemberg", "ja": "バンベルグ財団美術館", "es": "Fundación Bemberg", "zh": "班贝格基金会艺术馆", "fr": "Fondation Bemberg", "de": "Fondation Bemberg"
    },
    "Les Abattoirs, Musée - Frac Occitanie Toulouse": {
        "en": "Les Abattoirs, Musée - Frac Occitanie Toulouse", "ja": "レ・ザバトワール現代アート美術館", "es": "Museo Les Abattoirs", "zh": "屠宰场当代艺术馆", "fr": "Les Abattoirs, Musée - Frac Occitanie Toulouse", "de": "Les Abattoirs Museum"
    },
    "Musée Saint-Raymond": {
        "en": "Musée Saint-Raymond", "ja": "サン・レモン考古学博物館", "es": "Museo San Raymond", "zh": "圣雷蒙考古博物馆", "fr": "Musée Saint-Raymond", "de": "Musée Saint-Raymond"
    },
    "Muséum de Toulouse": {
        "en": "Muséum de Toulouse", "ja": "トゥールーズ自然史博物館", "es": "Museo de Historia Natural de Toulouse", "zh": "图卢兹自然历史博物馆", "fr": "Muséum de Toulouse", "de": "Naturhistorisches Museum Toulouse"
    },
    "Musée Paul-Dupuy": {
        "en": "Musée Paul-Dupuy", "ja": "ポール・デュピュイ装飾芸術・時計博物館", "es": "Museo Paul-Dupuy", "zh": "保罗·杜普伊装饰艺术博物馆", "fr": "Musée Paul-Dupuy", "de": "Musée Paul-Dupuy"
    },
    "Aeroscopia Aviation Museum": {
        "en": "Aeroscopia Aviation Museum", "ja": "アエロスコピア航空博物館", "es": "Museo Aeronáutico Aeroscopia", "zh": "Aeroscopia 航空博物馆", "fr": "Musée Aéronautique Aeroscopia", "de": "Luftfahrtmuseum Aeroscopia"
    },
    "Let's Visit Airbus Tour": {
        "en": "Let's Visit Airbus Tour", "ja": "エアバス工場見学ツアー", "es": "Visita Guiada a la Fábrica Airbus", "zh": "空客飞机组装工厂参观导览", "fr": "Visite des usines Airbus", "de": "Airbus-Werkstour"
    },
    "Marché Victor Hugo": {
        "en": "Marché Victor Hugo", "ja": "ヴィクトル・ユーゴー市場", "es": "Mercado Victor Hugo", "zh": "维克多·雨果美食集市", "fr": "Marché Victor Hugo", "de": "Marché Victor Hugo"
    },
    "Le Bibent": {
        "en": "Le Bibent", "ja": "ル・ビバン（ベル・エポック調老舗ブラッスリー）", "es": "Le Bibent", "zh": "Le Bibent 历史小酒馆", "fr": "Le Bibent", "de": "Le Bibent"
    },
    "Le Colombier Cassoulet": {
        "en": "Le Colombier Cassoulet", "ja": "ル・コロンビエ（伝統カスレ老舗）", "es": "Le Colombier (Cassoulet tradicional)", "zh": "Le Colombier 传统炖白豆老店", "fr": "Le Colombier Cassoulet", "de": "Le Colombier Cassoulet"
    },
    "La Maison de la Violette": {
        "en": "La Maison de la Violette", "ja": "スミレの家（運河船ショップ）", "es": "La Maison de la Violette", "zh": "紫罗兰船屋工坊", "fr": "La Maison de la Violette", "de": "La Maison de la Violette"
    },
    "Marché des Carmes": {
        "en": "Marché des Carmes", "ja": "カルム市場", "es": "Mercado des Carmes", "zh": "卡尔姆圆形集市", "fr": "Marché des Carmes", "de": "Marché des Carmes"
    },
    "Maison Pillon & Pâtisserie Bault": {
        "en": "Maison Pillon & Pâtisserie Bault", "ja": "メゾン・ピロン＆バルト（伝統パティスリー）", "es": "Maison Pillon y Pastelería Bault", "zh": "Pillon 与 Bault 名门甜品店", "fr": "Maison Pillon & Pâtisserie Bault", "de": "Maison Pillon & Pâtisserie Bault"
    },
    "Domaine de Montjoie & Fronton Wineries": {
        "en": "Domaine de Montjoie & Fronton Wineries", "ja": "フロントン・ワインドメーヌ群", "es": "Bodegas Domaine de Montjoie y Fronton", "zh": "Fronton 特色葡萄酒庄群", "fr": "Domaine de Montjoie & Vins de Fronton", "de": "Weingut Domaine de Montjoie & Fronton"
    },
    "Quai de la Daurade & Promenade de la Garonne": {
        "en": "Quai de la Daurade & Promenade de la Garonne", "ja": "ドラード河岸＆ガロンヌ川遊歩道", "es": "Quai de la Daurade y Paseo del Garona", "zh": "多拉德水岸与加龙河步道", "fr": "Quai de la Daurade & Promenade de la Garonne", "de": "Quai de la Daurade & Garonne-Promenade"
    },
    "Quartier des Carmes & Quartier Saint-Étienne": {
        "en": "Quartier des Carmes & Quartier Saint-Étienne", "ja": "カルム地区＆サン・テティエンヌ地区", "es": "Barrio de Carmes y Barrio de Saint-Étienne", "zh": "卡尔姆与圣艾蒂安古雅街区", "fr": "Quartier des Carmes & Quartier Saint-Étienne", "de": "Viertel des Carmes & Saint-Étienne"
    },
    "Canal du Midi (Port de l'Embouchure)": {
        "en": "Canal du Midi (Port de l'Embouchure)", "ja": "ミディ運河（世界遺産）", "es": "Canal du Midi", "zh": "米迪运河（世界遗产）", "fr": "Canal du Midi", "de": "Canal du Midi"
    },
    "Place Saint-Georges": {
        "en": "Place Saint-Georges", "ja": "サン・ジョルジュ広場", "es": "Plaza Saint-Georges", "zh": "圣乔治广场", "fr": "Place Saint-Georges", "de": "Place Saint-Georges"
    },
    "Jardin Japonais Pierre Baudis": {
        "en": "Jardin Japonais Pierre Baudis", "ja": "ピエール・ボディス日本庭園", "es": "Jardín Japonés Pierre Baudis", "zh": "皮埃尔·博迪日式庭园", "fr": "Jardin Japonais Pierre Baudis", "de": "Japanischer Garten Pierre Baudis"
    },
    "Bateaux Toulousains Cruise": {
        "en": "Bateaux Toulousains Cruise", "ja": "ガロンヌ川・ミディ運河クルーズ船", "es": "Crucero Bateaux Toulousains", "zh": "图卢兹水上观光游船", "fr": "Bateaux Toulousains Croisières", "de": "Bootsfahrt Bateaux Toulousains"
    },
    "Canal de Brienne": {
        "en": "Canal de Brienne", "ja": "ブレンヌ運河散策路", "es": "Canal de Brienne", "zh": "布里安运河水渠", "fr": "Canal de Brienne", "de": "Canal de Brienne"
    },
    "Cordes-sur-Ciel": {
        "en": "Cordes-sur-Ciel", "ja": "コルド＝シュル＝シエル（天空の村）", "es": "Cordes-sur-Ciel", "zh": "科尔德斯天空之城", "fr": "Cordes-sur-Ciel", "de": "Cordes-sur-Ciel"
    },
    "L'Envol des Pionniers": {
        "en": "L'Envol des Pionniers", "ja": "レゴポスタル歴史館（アエロポスタル体験）", "es": "L'Envol des Pionniers", "zh": "先驱飞翔传奇航邮博物馆", "fr": "L'Envol des Pionniers", "de": "L'Envol des Pionniers"
    },
    "Jardin des Plantes & Le Grand Rond": {
        "en": "Jardin des Plantes & Le Grand Rond", "ja": "グラン・ロン＆植物園公園群", "es": "Jardin des Plantes y Le Grand Rond", "zh": "植物园与大圆盘公园", "fr": "Jardin des Plantes & Le Grand Rond", "de": "Jardin des Plantes & Le Grand Rond"
    },
    "Animaparc Occitanie": {
        "en": "Animaparc Occitanie", "ja": "アニマパーク・オクシタニー（恐竜＆動物ファーム）", "es": "Animaparc Occitanie", "zh": "Animaparc 动态恐龙与亲子农场", "fr": "Animaparc Occitanie", "de": "Animaparc Occitanie"
    },
    "Le Labyrinthe de Merville": {
        "en": "Le Labyrinthe de Merville", "ja": "メルヴィル城の巨大生垣迷路", "es": "El Laberinto de Merville", "zh": "梅尔维尔古堡生垣大迷宫", "fr": "Le Labyrinthe de Merville", "de": "Le Labyrinthe de Merville"
    }
}

def process_city_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    modified = False
    for spot in data.get('spots', []):
        name = spot.get('name', '')
        desc = spot.get('desc', '') or spot.get('desc_en', '')
        tip = spot.get('tip_en', '') or spot.get('tip_ja', '')
        price = spot.get('price', '')

        # 1. Enrich name_* fields
        name_dict = NAME_TRANSLATIONS.get(name, {})
        spot['name_en'] = spot.get('name_en') or name_dict.get('en') or name
        spot['name_ja'] = spot.get('name_ja') or name_dict.get('ja') or name
        spot['name_es'] = spot.get('name_es') or name_dict.get('es') or name
        spot['name_zh'] = spot.get('name_zh') or name_dict.get('zh') or name
        spot['name_fr'] = spot.get('name_fr') or name_dict.get('fr') or name
        spot['name_de'] = spot.get('name_de') or name_dict.get('de') or name

        # 2. Ensure desc_* exists
        if not spot.get('desc_en'): spot['desc_en'] = desc
        if not spot.get('desc_ja'): spot['desc_ja'] = spot.get('desc_ja') or desc
        if not spot.get('desc_es'): spot['desc_es'] = spot.get('desc_es') or desc
        if not spot.get('desc_zh'): spot['desc_zh'] = spot.get('desc_zh') or desc
        if not spot.get('desc_fr'): spot['desc_fr'] = spot.get('desc_fr') or desc
        if not spot.get('desc_de'): spot['desc_de'] = spot.get('desc_de') or desc

        # 3. Ensure tip_* exists
        if tip:
            if not spot.get('tip_en'): spot['tip_en'] = tip
            if not spot.get('tip_ja'): spot['tip_ja'] = spot.get('tip_ja') or tip
            if not spot.get('tip_es'): spot['tip_es'] = spot.get('tip_es') or tip
            if not spot.get('tip_zh'): spot['tip_zh'] = spot.get('tip_zh') or tip
            if not spot.get('tip_fr'): spot['tip_fr'] = spot.get('tip_fr') or tip
            if not spot.get('tip_de'): spot['tip_de'] = spot.get('tip_de') or tip

        # 4. Localized prices
        spot['price_en'] = price
        if 'Free' in price or 'free' in price:
            spot['price_ja'] = '入場無料'
            spot['price_es'] = 'Entrada gratuita'
            spot['price_zh'] = '免费开放'
            spot['price_fr'] = 'Entrée libre'
            spot['price_de'] = 'Eintritt frei'
        else:
            spot['price_ja'] = price
            spot['price_es'] = price
            spot['price_zh'] = price
            spot['price_fr'] = price
            spot['price_de'] = price

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated {os.path.basename(filepath)}")

city_files = glob.glob('data/cities/*.json')
for file in city_files:
    process_city_file(file)

print("🎉 Completed multilingual enrichment for all city JSON files!")
