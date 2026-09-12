import json
import os
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

# Target counts definition
TARGET_COUNTS = {
    'paris.json': 58,       # 55 -> 58 (+3)
    'nice.json': 40,        # 36 -> 40 (+4)
    'lyon.json': 46,        # Maintain
    'strasbourg.json': 45,  # Maintain
    'marseille.json': 43,   # Maintain
    'bordeaux.json': 40,    # Maintain
    'toulouse.json': 39,    # Maintain
    'amsterdam.json': 60,   # Maintain
    'berlin.json': 75,      # Maintain
    'munich.json': 60,      # Maintain
    'brussels.json': 55,    # 60 -> 55
    'hamburg.json': 55,     # 61 -> 55
    'frankfurt.json': 50,   # 61 -> 50
    'cologne.json': 50,     # 56 -> 50
    'rotterdam.json': 48,   # 60 -> 48
    'dresden.json': 45,     # 52 -> 45
    'nuremberg.json': 45,   # 52 -> 45
    'antwerp.json': 45,     # 60 -> 45
    'the_hague.json': 45,   # 60 -> 45
    'bruges.json': 42,      # 60 -> 42
    'ghent.json': 42,       # 60 -> 42
    'luxembourg.json': 42,  # 60 -> 42
    'utrecht.json': 42,     # 60 -> 42
    'heidelberg.json': 42,  # 50 -> 42
    'maastricht.json': 40,  # 60 -> 40
}

# New Paris Spots
PARIS_NEW_SPOTS = [
    {
        "id": "p_56",
        "name": "Père Lachaise Cemetery",
        "name_ja": "Père Lachaise Cemetery（ペール・ラシェーズ墓地）",
        "name_en": "Père Lachaise Cemetery",
        "name_fr": "Cimetière du Père Lachaise",
        "name_de": "Friedhof Père Lachaise",
        "name_es": "Cementerio del Père Lachaise",
        "name_zh": "拉雪兹神父公墓",
        "name_nl": "Begraafplaats Père-Lachaise",
        "category": "Landmark",
        "lat": 48.8614,
        "lng": 2.3942,
        "desc_ja": "オスカー・ワイルド、ショパン、エディット・ピアフら世界の偉人が眠るパリ最大の広大な彫刻庭園墓地。樹木が立ち並ぶ静寂の小道はパリ屈指の歴史散策ルート。",
        "desc_en": "Paris's largest and most famous cemetery, where icons like Oscar Wilde, Chopin, and Edith Piaf are buried amid tree-lined cobbled avenues.",
        "desc_fr": "Le plus grand cimetière parisien où reposent Oscar Wilde, Chopin et Édith Piaf au cœur d'un magnifique parc paysager.",
        "desc_de": "Der größte Friedhof von Paris, auf dem berühmte Persönlichkeiten wie Oscar Wilde, Chopin und Edith Piaf in einer parkähnlichen Anlage ruhen.",
        "desc_es": "El cementerio más grande de París, donde descansan figuras legendarias como Oscar Wilde, Chopin y Edith Piaf entre pintorescos senderos.",
        "desc_zh": "巴黎最大的公墓，奥斯卡·王尔德、肖邦和艾迪特·皮雅芙等传奇人物长眠于这座风景如画的园林式墓园中。",
        "desc_nl": "De grootste en beroemdste begraafplaats van Parijs, waar iconen zoals Oscar Wilde, Chopin en Edith Piaf rusten in een sfeervol park.",
        "tip_ja": "メトロ2号線のPère Lachaise駅または3号線のGambetta駅から入場可能。人気のお墓の位置は入口の地図看板で確認するとスムーズです。",
        "tip_en": "Enter via Metro Père Lachaise (Line 2) or Gambetta (Line 3). Free maps showing famous grave locations are available at the main entrance.",
        "tip_fr": "Entrez par le métro Père Lachaise ou Gambetta. Un plan gratuit indiquant l'emplacement des sépultures célèbres est disponible à l'entrée.",
        "tip_de": "Zugang über U-Bahn Père Lachaise oder Gambetta. Kostenlose Pläne mit den Standorten berühmter Gräber gibt es am Haupteingang.",
        "tip_es": "Entra por el metro Père Lachaise o Gambetta. En la entrada principal hay mapas gratuitos con la ubicación de las tumbas famosas.",
        "tip_zh": "可从地铁2号线Père Lachaise站或3号线Gambetta站进入。主入口提供标有著名墓位免费地图。",
        "tip_nl": "Ingang via metro Père Lachaise of Gambetta. Gratis plattegronden met bekende graven zijn verkrijgbaar bij de hoofdingang."
    },
    {
        "id": "p_57",
        "name": "Shakespeare and Company",
        "name_ja": "Shakespeare and Company（シェイクスピア・アンド・カンパニー）",
        "name_en": "Shakespeare and Company",
        "name_fr": "Shakespeare and Company",
        "name_de": "Shakespeare and Company",
        "name_es": "Shakespeare and Company",
        "name_zh": "莎士比亚书店",
        "name_nl": "Shakespeare and Company",
        "category": "Scenery & Walk",
        "lat": 48.8525,
        "lng": 2.3471,
        "desc_ja": "ノートルダム大聖堂の対岸に立つ伝説的な英文学書店。ヘミングウェイやフィッツジェラルドら『失われた世代』の文豪が集った歴史ある文学の聖地。",
        "desc_en": "An iconic English-language bookstore facing Notre-Dame Cathedral, historically frequented by Ernest Hemingway, F. Scott Fitzgerald, and James Joyce.",
        "desc_fr": "Une librairie anglophone mythique face à Notre-Dame, haut lieu littéraire fréquenté jadis par Ernest Hemingway et James Joyce.",
        "desc_de": "Eine legendäre englischsprachige Buchhandlung gegenüber von Notre-Dame, die einst Treffpunkt von Ernest Hemingway und James Joyce war.",
        "desc_es": "Una legendaria librería de lengua inglesa frente a Notre-Dame, frecuentada históricamente por Ernest Hemingway y James Joyce.",
        "desc_zh": "位于巴黎圣母院对岸的传奇英文书店，曾是海明威、菲茨杰拉德和乔伊斯等文学巨匠的聚会之地。",
        "desc_nl": "Een iconische Engelstalige boekwinkel tegenover de Notre-Dame, ooit de ontmoetingsplek van Ernest Hemingway en James Joyce.",
        "tip_ja": "店内は撮影禁止のノスタルジックな空間。本を購入するとオリジナルの記念スタンプを押してもらえます。隣接するカフェも人気。",
        "tip_en": "No photos allowed inside. Books purchased here receive an exclusive official embossed stamp. Visit the adjacent café for organic coffee and baked goods.",
        "tip_fr": "Photos interdites à l'intérieur. Tout livre acheté est tamponné avec le sceau officiel de la librairie. Café bio très sympa juste à côté.",
        "tip_de": "Fotos im Innenbereich verboten. Gekaufte Bücher erhalten den offiziellen Buchhandlungsstempel. Nebenan gibt es ein schönes Bio-Café.",
        "tip_es": "No se permiten fotos dentro. Cada libro comprado se sella con el timbre oficial de la librería. El café contiguo sirve excelente café orgánico.",
        "tip_zh": "店内禁止拍照。购书可盖书店专属纪念章。隔壁的有机咖啡馆也是休息的好去处。",
        "tip_nl": "Fotograferen binnen niet toegestaan. Gekochte boeken krijgen een officieel Stempel. Het aangrenzende café serveert uitstekende biologische koffie."
    },
    {
        "id": "p_58",
        "name": "Bourse de Commerce",
        "name_ja": "Bourse de Commerce（ブルス・ドゥ・コメルス (ピノー・コレクション)）",
        "name_en": "Bourse de Commerce - Pinault Collection",
        "name_fr": "Bourse de Commerce - Collection Pinault",
        "name_de": "Bourse de Commerce - Sammlung Pinault",
        "name_es": "Bourse de Commerce - Colección Pinault",
        "name_zh": "皮诺私人美术馆（商会大厦）",
        "name_nl": "Bourse de Commerce - Pinault-collectie",
        "category": "Museum & Art",
        "lat": 48.8625,
        "lng": 2.3426,
        "desc_ja": "歴史的な円形穀物取引所を安藤忠雄氏の設計でコンクリートシリンダーと融合させた、フランソワ・ピノー氏の世界最高峰現代アート美術館。",
        "desc_en": "A historic circular grain exchange transformed by architect Tadao Ando into a world-class contemporary art museum housing the François Pinault Collection.",
        "desc_fr": "Ancienne bourse de commerce circulaire sublimée par l'architecte Tadao Ando pour abriter les chefs-d'œuvre d'art contemporain de la collection Pinault.",
        "desc_de": "Eine historische getreidebörse, die von Tadao Ando spektakulär restauriert wurde, um die hochkarätige zeitgenössische Kunstsammlung Pinault zu präsentieren.",
        "desc_es": "Antiguo edificio circular de la bolsa de comercio transformado por Tadao Ando para albergar la prestigiosa colección de arte contemporáneo de François Pinault.",
        "desc_zh": "由著名建筑师安藤忠雄重新设计的圆顶历史建筑，展出实业家弗朗索瓦·皮诺顶级现代艺术藏品。",
        "desc_nl": "Een historische ronde graanbeurs die door Tadao Ando is omgevormd tot een topmuseum voor hedendaagse kunst van de Pinault-collectie.",
        "tip_ja": "事前日時指定チケットの予約が必須。中央アトリウムのドーム壁画と現代建築のコントラストは必見です。",
        "tip_en": "Advance timed-entry tickets are required online. Don't miss the panoramic view of the glass rotunda ceiling from the upper walkway.",
        "tip_fr": "Réservation en ligne obligatoire avec créneau horaire. Admirez les fresques de la rotonde depuis la passerelle supérieure conçue par Tadao Ando.",
        "tip_de": "Zeitfenster-Tickets im Voraus online erforderlich. Vom oberen Laufsteg hat man einen fantastischen Blick auf das restaurierte Kuppelfresko.",
        "tip_es": "Se requiere reserva previa de entrada con hora. No te pierdas las vistas de la rotonda de cristal desde la pasarela superior de hormigón.",
        "tip_zh": "需提前在官网预约门票。切勿错过从上层走廊观赏穹顶历史壁画与混凝土圆柱的绝妙景象。",
        "tip_nl": "Vooraf online reserveren met tijdslot is verplicht. Geniet vanaf de bovenste omgang van het uitzicht op het glazen koepelfresco."
    }
]

# New Nice Spots
NICE_NEW_SPOTS = [
    {
        "id": "nice_37",
        "name": "Promenade de la Croisette (Cannes)",
        "name_ja": "Promenade de la Croisette（プロムナード・デ・ラ・クロワゼット（カンヌ））",
        "name_en": "Promenade de la Croisette (Cannes)",
        "name_fr": "Promenade de la Croisette (Cannes)",
        "name_de": "Promenade de la Croisette (Cannes)",
        "name_es": "Promenade de la Croisette (Cannes)",
        "name_zh": "戛纳克鲁瓦塞特大道",
        "name_nl": "Promenade de la Croisette (Cannes)",
        "category": "Scenery & Walk",
        "lat": 43.5507,
        "lng": 7.0253,
        "desc_ja": "カンヌ国際映画祭の会場「パレ・デ・フェスティバル」から続くヤシの木の並木道。高級ホテルやプライベートビーチが連なるコートダジュールの象徴。",
        "desc_en": "The glamorous palm-lined boulevard of Cannes, home to the International Film Festival palace, luxury boutiques, and iconic Mediterranean beaches.",
        "desc_fr": "Le mythique boulevard bordé de palmiers à Cannes, célèbre pour son Palais des Festivals, ses hôtels de luxe et ses plages de sable.",
        "desc_de": "Die berühmte palmengesäumte Promenade in Cannes mit dem Festspielhaus, Luxushotels und exklusiven Sandstränden.",
        "desc_es": "El glamuroso bulevar junto al mar en Cannes, famoso por el Palacio del Festival de Cine, boutiques de lujo y playas icónicas.",
        "desc_zh": "戛纳标志性的棕榈大道，毗邻戛纳电影节主会场、奢华酒店与绵延的蔚蓝海岸沙滩。",
        "desc_nl": "De glamoureuze boulevard van Cannes met palmbomen, het Filmfestivalpaleis, luxe boetieks en zandstranden.",
        "tip_ja": "ニース中央駅からTER（快速列車）で約30分。パレ・デ・フェスティバル前のレッドカーペット階段で記念撮影が定番。",
        "tip_en": "Take the TER train from Nice Ville (30 mins). Photo op on the famous red carpet steps at the Palais des Festivals.",
        "tip_fr": "Accès direct en 30 min par le train TER depuis Nice Ville. Photo souvenir incontournable sur les marches du tapis rouge du Palais.",
        "tip_de": "In 30 Minuten mit dem TER-Zug von Nice Ville erreichbar. Machen Sie ein Foto auf der roten Teppichtreppe des Festspielhauses.",
        "tip_es": "En tren TER desde Nice Ville toma unos 30 minutos. Tómate una foto en la famosa escalera de la alfombra roja del Palacio.",
        "tip_zh": "从尼斯火车站乘坐TER列车约30分钟即达。红地毯阶梯是必打卡的拍照点。",
        "tip_nl": "In 30 minuten te bereiken met de TER-trein vanaf Nice Ville. Maak een foto op de bekende rode loper van het paleis."
    },
    {
        "id": "nice_38",
        "name": "Vieux Menton & Basilique Saint-Michel",
        "name_ja": "Vieux Menton（マントン旧市街＆サン・ミッシェル聖堂）",
        "name_en": "Vieux Menton & Saint-Michel Basilica",
        "name_fr": "Vieux Menton & Basilique Saint-Michel",
        "name_de": "Altstadt Menton & Basilika Saint-Michel",
        "name_es": "Viejo Menton y Basílica San Miguel",
        "name_zh": "芒通老城与圣米歇尔大教堂",
        "name_nl": "Oude stad Menton & Basiliek Saint-Michel",
        "category": "Landmark",
        "lat": 43.7753,
        "lng": 7.5069,
        "desc_ja": "イタリア国境に位置する「フレンチ・リヴィエラの真珠」。パステルカラーの建物を描く旧市街とバロック様式のサン・ミッシェル聖堂が織りなす絶景。",
        "desc_en": "The pearl of the French Riviera near the Italian border, renowned for its pastel-colored old town, lemon groves, and Baroque Saint-Michel Basilica.",
        "desc_fr": "La perle de la France nichée près de l'Italie, célèbre pour ses façades pastel, ses citrons et sa basilique baroque surplombant la mer.",
        "desc_de": "Die Perle der Côte d'Azur nahe der italienischen Grenze, bekannt für bunte Pastellhäuser, Zitronenhaine und die barocke Basilika.",
        "desc_es": "La perla de la Costa Azul junto a Italia, célebre por sus fachadas de tonos pastel, huertos de limones y la basílica barroca frente al mar.",
        "desc_zh": "靠近意大利边境的蔚蓝海岸珍珠，以马卡龙色系的复古建筑群、柠檬树与圣米歇尔巴洛克教堂闻名。",
        "desc_nl": "De parel van de Franse Rivièra nabij de Italiaanse grens, bekend om de pastelkleurige oude stad en barokke basiliek.",
        "tip_ja": "ニースからTERで35分。旧港（Vieux Port）の波止場から見上げる旧市街と聖堂の景色が最も美しい撮影スポットです。",
        "tip_en": "35 mins by train from Nice. The view of the town rising above the sea from the pier at the Old Port is unforgettable.",
        "tip_fr": "35 min en train TER depuis Nice. La meilleure vue panoramique sur les façades pastel se prend depuis la jetée du Vieux Port.",
        "tip_de": "35 Minuten mit dem Zug von Nice. Die schönste Aussicht auf die bunten Häuser hat man vom Pier des Alten Hafens.",
        "tip_es": "35 minutos en tren desde Niza. La vista panorámica de la ciudad desde el espigón del Puerto Viejo es espectacular.",
        "tip_zh": "从尼斯乘火车35分钟即可到达。从老港（Vieux Port）码头仰望老城是绝佳摄影角度。",
        "tip_nl": "35 minuten met de trein vanaf Nice. Het mooiste uitzicht op de stad en de zee heb je vanaf de pier van de Oude Haven."
    },
    {
        "id": "nice_39",
        "name": "Villa Santo Sospir & Cap Ferrat",
        "name_ja": "Villa Santo Sospir（ヴィラ・サント・ソスピル＆キャップ・フェラ）",
        "name_en": "Villa Santo Sospir & Cap Ferrat",
        "name_fr": "Villa Santo Sospir & Cap Ferrat",
        "name_de": "Villa Santo Sospir & Cap Ferrat",
        "name_es": "Villa Santo Sospir y Cap Ferrat",
        "name_zh": "尚·高克多壁画别墅与费拉角",
        "name_nl": "Villa Santo Sospir & Cap Ferrat",
        "category": "Landmark",
        "lat": 43.6872,
        "lng": 7.3276,
        "desc_ja": "芸術家ジャン・コクトーが壁や天上にフレスコ画を描いた「タトゥーされた家」。サン・ジャン・キャップ・フェラ半島の絶景に位置する芸術の隠れ家。",
        "desc_en": "The 'tattooed villa' decorated with stunning frescoes painted by Jean Cocteau, set on the prestigious Saint-Jean-Cap-Ferrat peninsula.",
        "desc_fr": "La « villa tatouée » recouverte de fresques mythologiques réalisées par Jean Cocteau sur la très exclusive presqu'île de Cap Ferrat.",
        "desc_de": "Die „tätowierte Villa“, deren Wände von Jean Cocteau mit faszinierenden Fresken bemalt wurden, gelegen auf der Halbinsel Cap Ferrat.",
        "desc_es": "La 'villa tatuada' decorada con frescos mitológicos por Jean Cocteau, situada en la distinguida península de Cap Ferrat.",
        "desc_zh": "诗人兼艺术家让·谷克多亲自在墙面与天花板创作神话壁画的“纹身别墅”，坐落于费拉角半岛。",
        "desc_nl": "De 'getatoeëerde villa' voorzien van prachtige fresco's door Jean Cocteau op het schiereiland Saint-Jean-Cap-Ferrat.",
        "tip_ja": "エフルシ・ド・ロスチャイルド庭園から徒歩またはバスで周遊可能。地中海を望む沿岸遊歩道（Sentier du Littoral）の散策もおすすめ。",
        "tip_en": "Combine with a visit to Villa Ephrussi. Take a scenic hike along the Cap Ferrat coastal path (Sentier du Littoral).",
        "tip_fr": "À combiner avec la Villa Ephrussi. Profitez-en pour faire la promenade du sentier du littoral autour du Cap Ferrat.",
        "tip_de": "Lässt sich hervorragend mit der Villa Ephrussi kombinieren. Wandern Sie auf dem Küstenweg (Sentier du Littoral).",
        "tip_es": "Combínala con la visita a la Villa Ephrussi. Recorre el sendero litoral para disfrutar de impresionantes calas.",
        "tip_zh": "建议与罗斯柴尔德花园别墅一并游览，并可沿着费拉角海岸步道漫步。",
        "tip_nl": "Goed te combineren met Villa Ephrussi. Wandelen langs het kustpad is een echte aanrader."
    },
    {
        "id": "nice_40",
        "name": "Larvotto Beach & Promenade (Monaco)",
        "name_ja": "Larvotto Beach Monaco（ラルヴォット・ビーチ＆プロムナード（モナコ））",
        "name_en": "Larvotto Beach & Promenade (Monaco)",
        "name_fr": "Plage du Larvotto (Monaco)",
        "name_de": "Larvotto Strand (Monaco)",
        "name_es": "Playa de Larvotto (Mónaco)",
        "name_zh": "摩纳哥拉沃托海滩",
        "name_nl": "Larvotto Strand (Monaco)",
        "category": "Scenery & Walk",
        "lat": 43.7468,
        "lng": 7.4332,
        "desc_ja": "モナコ公国唯一のパブリックビーチ＆近代的なシーサイドプロムナード。建築家レンゾ・ピアノ氏設計の複合施設が並ぶ洗練されたリゾートエリア。",
        "desc_en": "Monaco's premier public beach complex designed by architect Renzo Piano, featuring stylish seaside promenades, restaurants, and crystal-clear waters.",
        "desc_fr": "La grande plage publique de Monaco réaménagée par l'architecte Renzo Piano, avec une promenade moderne bordée de restaurants branchés.",
        "desc_de": "Monacos öffentlicher Hauptstrand, gestaltet von Renzo Piano, mit moderner Seepromenade und stilvollen Meeresrestaurants.",
        "desc_es": "La principal playa pública de Mónaco rediseñada por Renzo Piano, con un paseo marítimo repleto de acogedores restaurantes.",
        "desc_zh": "由建筑师伦佐·皮亚诺重新设计的摩纳哥著名公共海滩与现代海滨长廊，拥有清澈海水与顶级餐厅。",
        "desc_nl": "Het vernieuwde openbare strand van Monaco, ontworpen door Renzo Piano met een moderne promenade en trendy restaurants.",
        "tip_ja": "モンテカルロ・カジノから徒歩10分。透明度の高い海で遊泳やカフェでのひとときを楽しめます。",
        "tip_en": "A short 10-minute walk down from Monte-Carlo Casino. Clean public amenities, shaded pergolas, and fine seaside dining.",
        "tip_fr": "Situé à 10 min à pied sous le Casino de Monte-Carlo. Zone de baignade très propre avec parasols et cafés en bord de mer.",
        "tip_de": "Nur 10 Gehminuten unterhalb des Casinos von Monte-Carlo. Sehr sauberes Wasser und schöne Strandcafés.",
        "tip_es": "A solo 10 minutos a pie desde el Casino de Montecarlo. Zona de baño limpia y ambiente relajante con cafeterías.",
        "tip_zh": "从蒙特卡洛赌场下行步行10分钟即可到达。拥有洁净的游泳区域与舒适的沿海露座。",
        "tip_nl": "Slechts 10 minuten lopen vanaf het Casino van Monte-Carlo. Helder zwemwater en gezellige terrassen aan zee."
    }
]

print("🚀 Starting City Spot Count Optimization Process...")

for fname, target_count in TARGET_COUNTS.items():
    fpath = os.path.join(cities_dir, fname)
    if not os.path.exists(fpath):
        print(f"⚠️ File not found: {fname}")
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, dict):
        spots = data.get('spots', [])
    elif isinstance(data, list):
        spots = data
    else:
        spots = []

    old_count = len(spots)

    # Special logic for Paris
    if fname == 'paris.json':
        existing_ids = {s['id'] for s in spots}
        for s in PARIS_NEW_SPOTS:
            if s['id'] not in existing_ids:
                spots.append(s)
        print(f" -> {fname}: Expanded from {old_count} to {len(spots)} spots (Target: {target_count})")
    
    # Special logic for Nice
    elif fname == 'nice.json':
        existing_ids = {s['id'] for s in spots}
        for s in NICE_NEW_SPOTS:
            if s['id'] not in existing_ids:
                spots.append(s)
        print(f" -> {fname}: Expanded from {old_count} to {len(spots)} spots (Target: {target_count})")
    
    # Logic for pruning minor spots if count > target
    elif old_count > target_count:
        spots = spots[:target_count]
        print(f" -> {fname}: Pruned from {old_count} to {len(spots)} spots (Target: {target_count})")
    else:
        print(f" -> {fname}: Kept at {old_count} spots (Target: {target_count})")
    
    if isinstance(data, dict):
        data['spots'] = spots
        data['spotCount'] = len(spots)
    else:
        data = spots

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("\n🎉 City spot optimization completed successfully!")
