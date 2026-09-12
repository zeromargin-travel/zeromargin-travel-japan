import json
import glob
import os

# -------------------------------------------------------------
# Comprehensive Clean & Practical Tips Refinement for France
# (Paris, Nice, Lyon, Bordeaux, Strasbourg, Toulouse, Marseille)
# -------------------------------------------------------------

def refine_city(fname, updates):
    fpath = f"data/cities/{fname}"
    if not os.path.exists(fpath):
        print(f"⚠️ File {fpath} not found")
        return
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    cleared_count = 0

    for s in data['spots']:
        sid = s['id']
        if sid in updates:
            up = updates[sid]
            if up is None: # Clear tip (smart omit)
                for k in ['tip', 'tip_en', 'tip_ja', 'tip_es', 'tip_zh', 'tip_fr', 'tip_de']:
                    s[k] = ""
                cleared_count += 1
            else:
                for k, v in up.items():
                    s[k] = v
                s['tip'] = up.get('tip_en', s.get('tip', ''))
                updated_count += 1

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Refined {fname}: {updated_count} tips updated, {cleared_count} tips cleared (smart omit)")

# =============================================================
# 1. PARIS (55 spots) - Practical Tips Only
# =============================================================
paris_refinements = {
    "p_1": { # Tour Eiffel
        "tip_en": "🎟️ Book summit tickets online 60 days in advance! If sold out, walk up the stairs to 2nd floor for shorter lines, then buy the summit elevator ticket there.",
        "tip_ja": "🎟️ 最上階行チケットは60日前に公式サイトで即予約が鉄則！売り切れ時は2階まで階段（混雑大幅減）で登り、2階の専用窓口で最上階エレベーター券を購入する裏技が有効です。",
        "tip_es": "🎟️ ¡Reserva las entradas a la cumbre con 60 días de antelación! Si están agotadas, sube por las escaleras hasta el 2° piso y compra allí el ascensor a la cumbre.",
        "tip_zh": "🎟️ 登顶门票必须提前60天在官网秒杀！若售罄，可选择步行走楼梯至2层（排队极短），再在2层内部窗口现买登顶电梯票。",
        "tip_fr": "🎟️ Réservez vos billets pour le sommet 60 jours à l'avance ! Si c'est complet, montez à pied jusqu'au 2e étage et achetez la suite sur place.",
        "tip_de": "🎟️ Tickets für die Spitze 60 Tage im Voraus online buchen! Wenn ausverkauft, zu Fuß in den 2. Stock steigen und dort Aufzugticket kaufen."
    },
    "p_2": { # Louvre
        "tip_en": "🚪 Bypass the Pyramid queue by using the subterranean Porte des Lions or Carrousel du Louvre entrances. Free entry under 18 & EU residents under 26.",
        "tip_ja": "🚪 ガラスのピラミッド正面の大行列を避け、地下街『Porte des Lions』か『Carrousel du Louvre』入口から入るのが鉄則！金曜夜の夜間開館（21:45閉館）は比較的空いています。",
        "tip_es": "🚪 Evita la cola de la Pirámide entrando por el subterráneo de Porte des Lions o Carrousel du Louvre. Los viernes por la noche hay menos multitud.",
        "tip_zh": "🚪 切勿在玻璃金字塔地面排长队！走地下商城 Porte des Lions 或 Carrousel 入口秒进。每周五夜场（至21:45）人最少。",
        "tip_fr": "🚪 Évitez la file de la Pyramide en passant par l'accès Porte des Lions ou le Carrousel du Louvre. Nocturne le vendredi jusqu'à 21h45.",
        "tip_de": "🚪 Lange Schlangen an der Pyramide vermeiden: Nutzen Sie den Eingang Porte des Lions oder Carrousel du Louvre. Freitagabends ruhiger!"
    },
    "p_3": { # Musée d'Orsay
        "tip_en": "📸 Walk up to the 5th floor to take photos through the giant transparent station clock face overlooking Sacré-Cœur across the Seine.",
        "tip_ja": "📸 5階の印象派ギャラリー奥にある巨大大時計の裏側へ！ガラス文字盤越しにセーヌ川とサクレ・クール寺院が映り込む絶好の写真スポットです。",
        "tip_es": "📸 Ve a la 5ª planta para tomar fotos tras la esfera del gran reloj transparente de la estación con vistas a Sacré-Cœur.",
        "tip_zh": "📸 直奔5楼印象派展厅尽头！透过巨大的透明古董车站大钟表盘反光，可拍到对岸圣心大教堂与塞纳河绝美剪影。",
        "tip_fr": "📸 Montez au 5e étage pour vous photographier derrière la grande horloge transparente face à la Seine et Sacré-Cœur.",
        "tip_de": "📸 Im 5. Stock hinter dem riesigen transparenten Bahnhofsuhr-Zifferblatt fotografieren – mit Blick auf Sacré-Cœur!"
    },
    "p_4": { # Arc de Triomphe
        "tip_en": "🚶 Do NOT attempt to cross the busy roundabout above ground! Use the subterranean pedestrian tunnel on the north side of Champs-Élysées.",
        "tip_ja": "🚶 ラウンドアバウトの地上横断は極めて危険です！シャンゼリゼ通り北側（地下鉄入口付近）の地下歩道を使って安全に中央へ渡りましょう。夕暮れの屋上展望も最高です。",
        "tip_es": "🚶 ¡NO intentes cruzar la rotonda por superficie! Usa el túnel peatonal subterráneo en el lado norte de los Campos Elíseos.",
        "tip_zh": "🚶 切勿尝试横穿地面环岛车流！请务必走香榭丽舍大街北侧地下通道进入中央要塞。傍晚登上屋顶可看凯旋大道落日。",
        "tip_fr": "🚶 NE traversez PAS el rond-point à pied ! Empruntez el passage souterrain piéton au début des Champs-Élysées.",
        "tip_de": "🚶 Auf keinen Fall oberirdisch über den Kreisverkehr laufen! Nutzen Sie die Unterführung auf der Nordseite der Champs-Élysées."
    },
    "p_5": { # Sacré-Cœur
        "tip_en": "🎟️ Funicular railway up the hill accepts standard Navigo/Metro tickets. Beware of souvenir string sellers at the base of the stairs.",
        "tip_ja": "🎟️ 丘の上の聖堂へは地下鉄切符で乗れるケーブルカー（Funiculaire）が便利。階段下の押し売り（ミサンガ売り）には「Non」とはっきり断りスルーしましょう。",
        "tip_es": "🎟️ El funicular acepta billetes de metro comunes. Mantén tus pertenencias seguras frente a los vendedores en las escaleras.",
        "tip_zh": "🎟️ 登山缆车可使用普通地铁票。台阶下若遇到缠绑手绳索要钱财的人，无需理会 directly 绕行。",
        "tip_fr": "🎟️ Le funiculaire s'emprunte avec un simple ticket de métro. Ignorez les vendeurs à la sauvette au bas des marches.",
        "de": "🎟️ Die Standseilbahn fährt mit normalen Metro-Tickets. Am Fuß der Treppe Verkäufer ignoriert weitergehen."
    },
    "p_6": { # Cathédrale Notre-Dame
        "tip_en": "📸 Walk across Pont de l'Archevêché or Square Jean-XXIII behind the cathedral for the best restored Gothic facade view along the Seine.",
        "tip_ja": "📸 正面広場だけでなく、セーヌ川のアルシュヴェシェ橋や南側の公園から見上げるゴシック様式の飛翔壁（フライング・バットレス）の復元姿が圧巻です。",
        "tip_es": "📸 Camina por el Pont de l'Archevêché detrás de la catedral para admirar los arbotantes restaurados sobre el río.",
        "tip_zh": "📸 推荐走到大教堂后方的アルシュヴェシェ桥（Pont de l'Archevêché），远眺飞扶壁与大修后重现光彩的塔尖全景。",
        "tip_fr": "📸 Traversez le pont de l'Archevêché à l'arrière pour admirer les arcs-boutants restaurés au-dessus de la Seine.",
        "tip_de": "📸 Über die Brücke Pont de l'Archevêché auf der Rückseite spazieren für den besten Blick auf die restaurierten Strebepfeiler."
    },
    "p_7": { # Sainte-Chapelle
        "tip_en": "☀️ Visit on a sunny day between 11:00 AM and 2:00 PM when sunlight directly penetrates the 15-meter 13th-century stained glass windows upstairs.",
        "tip_ja": "☀️ 晴れた日の11:00〜14:00の見学がベスト！太陽光が直射し、2階礼拝堂の高さ15mの13世紀ステンドグラスが万華鏡のように光り輝きます（セキュリティ検査が厳しいため要予約）。",
        "tip_es": "☀️ Visítala en un día soleado entre las 11:00 y las 14:00 para ver la luz atravesar las vidrieras de 15 metros del siglo XIII.",
        "tip_zh": "☀️ 推荐择晴天午前11点至下午2点间入内！日光倾泻而下，2楼礼拜堂15米高古董彩绘玻璃化作耀眼星河（安检极严须提前预约）。",
        "tip_fr": "☀️ Visitez par temps ensoleillé entre 11h et 14h pour voir les vitraux du XIIIe siècle s'illuminer sous la lumière directe.",
        "tip_de": "☀️ Bei Sonnenschein zwischen 11:00 und 14:00 Uhr besuchen: Das Licht durch die 15m hohen Glasfenster ist magisch."
    },
    "p_8": { # Centre Pompidou
        "tip_en": " Escalator access to the top floor offers a sweeping rooftop view over Paris including Notre-Dame and Montmartre.",
        "tip_ja": " 館外の透明な蛇腹パイプ状エスカレーターで最上階へ上がると、エッフェル塔からサクレ・クールまで見渡せる穴場の屋上展望スペースがあります。",
        "tip_es": " Sube por las escaleras mecánicas tubulares transparentes hasta la última planta para disfrutar de una vista panorámica de París.",
        "tip_zh": " 沿着外墙透明玻璃管道透明电梯登顶！顶层露台是揽尽巴黎红瓦与远方埃菲尔铁塔的绝佳全景位。",
        "tip_fr": " Empruntez la chenille mécanique extérieure transparente jusqu'au toit pour un super panorama sur les toits de Paris.",
        "de": " Mit der transparenten Außen-Rolltreppe ins oberste Stockwerk fahren für den Ausblick über die Dächer von Paris."
    },
    "p_9": { # Jardin du Luxembourg
        "tip_en": " Pull up iconic green metal chairs ('Chaises du Luxembourg') around the central Medici Fountain for a relaxing afternoon read or picnic.",
        "tip_ja": " 園内あちこちに置いてある緑の鉄製チェアは移動自由！メディシスの噴水前や中央池の周りに運んで、テイクアウトしたパンでピクニックをするのがパリジャン流。",
        "tip_es": " Mueve las icónicas sillas verdes de metal cerca de la fuente Médicis para relajarte o almorzar al aire libre.",
        "tip_zh": " 园区内绿金金属椅子免费自由拎挪！挪一把到Medici水池旁树荫下，配上法棍面包享受正统巴黎式休假。",
        "tip_fr": " Déplacez librement les célèbres chaises vertes en métal autour de la fontaine Médicis pour une pause au soleil.",
        "de": " Die grünen Metallstühle frei am Medici-Brunnen aufstellen und das entspannte Pariser Parkleben genießen."
    },
    "p_10": { # Panthéon
        "tip_en": "🎟️ Buy the dome access option during summer months to climb 206 stairs for a rare high-altitude view of the Latin Quarter.",
        "tip_ja": "🎟️ 夏季限定のドーム登頂チケット（有料追加）で206段の階段を登ると、カルチェ・ラタンを見下ろす大パノラマを楽しめます。館内のフーコーのペンドラム実験も必見。",
        "tip_es": "🎟️ Compra el acceso a la cúpula en verano para subir 206 escalones y ver el Barrio Latino desde las alturas.",
        "tip_zh": "🎟️ 夏季登顶票（需加购）登206级阶梯可直达巨型穹顶最外围，鸟瞰整个拉丁区。大厅内的傅科摆装置亦极具魅力。",
        "tip_fr": "🎟️ En été, prenez le billet avec accès au dôme pour monter les 206 marches et admirer le Quartier Latin d'en haut.",
        "tip_de": "🎟️ Im Sommer die Aufstiegskarte für die Kuppel buchen: 206 Stufen für einen Panoramablick über das Quartier Latin."
    },
    "p_29": { # Marché des Enfants Rouges
        "tip_en": "🍽️ Head straight to Chez Alain Miam Miam for custom toasted sandwiches, or the authentic Moroccan stall for couscous on weekend lunches!",
        "tip_ja": "🍽️ 週末のランチは行列必至の名物巨大サンドイッチ店『Chez Alain Miam Miam』か、熱々のクスクスが味わえるモロッコ屋台に直行するのが地元流！",
        "tip_es": "🍽️ Ve directo a Chez Alain Miam Miam para sándwiches gigantes o al puesto marroquí para cuscús los fines de semana.",
        "tip_zh": "🍽️ 周末午餐推荐直奔 Chez Alain Miam Miam 尝尝现做巨大三明治，或前往摩洛哥档口品尝地道库斯库斯米饭！",
        "tip_fr": "🍽️ Foncez chez Alain Miam Miam pour ses sandwichs gargantuesques ou au traiteur marocain pour un couscous gourmand !",
        "de": "🍽️ Steuern Sie am Wochenende direkt Chez Alain Miam Miam für riesige Sandwiches oder den marokkanischen Stand an!"
    },
    "p_48": { # Cité des Sciences
        "tip_en": "🎟️ Reserve time slots for the Cité des Enfants interactive science zone online in advance. The Argonaut submarine tour is included!",
        "tip_ja": "🎟️ 体験型科学エリア『Cité des Enfants』の入場は公式サイトでの事前時間指定予約が必須！本物の潜水艦アルゴノート号内部見学もセットでどうぞ。",
        "tip_es": "🎟️ Reserva hora en línea para la Cité des Enfants. ¡La visita al submarino real Argonaute está incluida!",
        "tip_zh": "🎟️ 亲子互动区 Cité des Enfants 务必提前在官网预约场次！门票已包含实物退役潜艇阿尔戈号（Argonaute）内部参观。",
        "tip_fr": "🎟️ Réservez vos créneaux en ligne pour la Cité des Enfants. La visite du sous-marin Argonaute est incluse !",
        "de": "🎟️ Zeitfenster für die Cité des Enfants vorab online buchen. Die Besichtigung des echten U-Boots Argonaute ist inklusive!"
    }
}

# =============================================================
# 2. MARSEILLE (43 spots) - Overlap Fix & Practical Tips Only
# =============================================================
marseille_refinements = {
    "ma_22": { # Le Miramar
        "tip_en": "🎟️ Reserve weeks in advance for a window table! Prepared strictly according to the 1980 Marseille Bouillabaisse Charter (served in 2 courses).",
        "tip_ja": "🎟️ 窓際席は数週間前要予約！1980年に制定された『マルセイユ・ブイヤベース憲章』を厳格に守る本物の魚スープ＆地魚の2段コースを提供。",
        "tip_es": "🎟️ ¡Reserva con semanas de antelación! Cumple la Carta oficial de la Bouillabaisse de 1980 (servida en 2 tiempos).",
        "tip_zh": "🎟️ 预订窗边位必须提前数周！严格遵循1980年官方《马赛鱼汤宪章》标准分两道程序呈现。",
        "tip_fr": "🎟️ Réservez des semaines à l'avance ! Respecte à la lettre la Charte de la Bouillabaisse de 1980 (service en 2 temps).",
        "de": "🎟️ Wochen im Voraus reservieren! Zubereitung streng nach der offiziellen Bouillabaisse-Charta von 1980."
    },
    "ma_24": { # Marché de Noailles
        "tip_en": "🍽️ Buy fresh mint for homemade tea, Harissa spice paste, and hot honey Baklava at Saladin Épices du Monde stall.",
        "tip_ja": "🍽️ スパイス専門店『Saladin Épices du Monde』で本場のハリッサ唐辛子ペースト、フレッシュミント、甘いバクラヴァ（パイ菓子）をゲット！",
        "tip_es": "🍽️ Compra pasta de Harissa, menta fresca para té y Baklava recién elaborado en la tienda Saladin.",
        "tip_zh": "🍽️ 在 Saladin Épices 档口购买正宗北非 Harissa 辣酱、鲜切薄荷叶与蜜糖果仁酥（Baklava）。",
        "tip_fr": "🍽️ Achetez du véritable harissa, de la menthe fraîche et des baklavas dorés chez Saladin Épices du Monde.",
        "de": "🍽️ Frische Minze, Harissa-Paste und süßes Baklava beim Gewürzladen Saladin Épices kaufen."
    },
    "ma_25": { # Four des Navettes
        "tip_en": "🛍️ Buy boat-shaped orange blossom cookies baked in a 200-year-old stone oven—they stay fresh for months in sealed boxes!",
        "tip_ja": "🛍️ 200年以上使われている歴史的な石窯で焼き上げられる伝統菓子ナベット（硬めのクッキー）を袋買い！密閉缶で数ヶ月日持ちするためお土産に最高です。",
        "tip_es": "🛍️ Compra galletas Navettes en caja metálica horneadas en el horno de piedra bicentenario: ¡duran meses frescas!",
        "tip_zh": "🛍️ 购买以200年历史古石烤炉烘烤的船形橙花干饼Navettes！装于铁盒中可保持数月酥脆，为手信首选。",
        "tip_fr": "🛍️ Achetez les navettes en boîte métallique cuites dans le four bicentenaire : elles se conservent des mois !",
        "de": "🛍️ Die im 200 Jahre alten Steinofen gebackenen Navettes in der Blechdose kaufen – monatelang haltbar!"
    },
    "ma_26": { # La Samaritaine & Café de la Banque
        "tip_en": "🍽️ Order a chilled Pastis (anise liqueur) diluting it with cold water and ice cubes at 5:00 PM for authentic local aperitivo culture.",
        "tip_ja": "🍽️ 17:00からの食前酒（アペロ）タイムに、アニス風味の『パスティス（Pastis）』を水と氷で割って飲むのが地元マルセイユっ子の流儀！",
        "tip_es": "🍽️ Pide un Pastis frío diluido con agua y hielo a las 17:00 para vivir el aperitivo local tradicional.",
        "tip_zh": "🍽️ 傍晚5点 Aperitif 进场，点上一杯加冷水与冰块的茴香酒（Pastis），体验地道马赛闲适文化。",
        "tip_fr": "🍽️ Commandez un pastis bien frais allongé d'eau fraîche et de glaçons à l'heure de l'apéro !",
        "de": "🍽️ Um 17 Uhr einen kühlen Pastis mit kaltem Wasser und Eiswürfeln bestellen – echtes Marseiller Flair!"
    },
    "ma_27": { # Maison de la Boule & Savonneries
        "tip_en": "🛍️ Look for the official stamp '72% d'huile d'olive' on green cube soaps to ensure you are buying real authentic Savon de Marseille.",
        "tip_ja": "🛍️ 緑色の立方体石鹸に『72% d'huile d'olive（オリーブオイル72%）』の刻印があるか確認！無添加の本物マルセイユ石鹸を見分ける目印です。",
        "tip_es": "🛍️ Busca el sello oficial '72% d'huile d'olive' en los cubos de jabón verde para garantizar que es autentico.",
        "tip_zh": "🛍️ 认准绿色皂块上刻有的“72% d'huile d'olive”（72%橄榄油）官方印章，切勿买到添加化学香精的假皂。",
        "tip_fr": "🛍️ Vérifiez le tampon '72% d'huile d'olive' sur les cubes de savon vert pour garantir un véritable Savon de Marseille.",
        "de": "🛍️ Achten Sie auf den Stempel '72% d'huile d'olive' auf den grünen Seifenblöcken für echte Marseiller Seife."
    },
    "ma_28": { # L'Épuisette
        "tip_en": "🎟️ Book 1-2 months ahead for dinner at sunset; the panoramic sea view tables over the rocks are spectacular.",
        "tip_ja": "🎟️ 夕暮れ時のディナーは1〜2ヶ月前要予約！波が打ち寄せる岩の上のガラス越しに広がる地中海の落日絶景は感動的です。",
        "tip_es": "🎟️ Reserva con 1 o 2 meses de antelación para cenar al atardecer sobre las rocas con vistas al mar.",
        "tip_zh": "🎟️ 日落时段晚餐建议提前1-2个月预订！透过悬崖玻璃窗直面地中海浪花与余晖十分唯美。",
        "tip_fr": "🎟️ Réservez 1 à 2 mois à l'avance pour un dîner au coucher du soleil face aux vagues.",
        "de": "🎟️ 1 bis 2 Monate im Voraus reservieren für ein Abendessen zum Sonnenuntergang direkt über den Klippen."
    },
    "ma_31": { # Corniche John F. Kennedy
        "tip_en": "📸 Walk or rent a Vélo'v bike during golden hour to take photos on the 3km continuous concrete bench over the Mediterranean.",
        "tip_ja": "📸 夕暮れ時の黄金色に染まる時間帯に散策やサイクリング！海を見下ろす全長3kmの連続コンクリートベンチに座って記念撮影するのが定番。",
        "tip_es": "📸 Recorre el paseo en bici o a pie al atardecer para fotografiarte en el banco de 3 km sobre el mar.",
        "tip_zh": "📸 黄金落日时刻骑行或散步！在长达3公里的连贯水泥海滨长椅上定格地中海金光。",
        "tip_fr": "📸 Baladez-vous à vélo ou à pied au coucher du soleil pour vous prendre en photo sur el banc de 3 km face à la mer.",
        "de": "📸 Bei Sonnenuntergang mit dem Rad oder zu Fuß die Klippenstraße entlang und auf der 3km-Bank fotografieren."
    },
    "ma_35": { # Calanques National Park
        "tip_en": "👚 Bring sturdy hiking shoes & 2L water! Access by foot is closed during high fire risk summer days—check the official Calanques app before heading out.",
        "tip_ja": "👚 履き慣れたスニーカーと最低2Lの水分必携！夏場の強風・乾燥時は火災リスクで入山規制（通行止め）になるため、公式アプリ『Mes Calanques』で当日の開通状況を確認しましょう。",
        "tip_es": "👚 ¡Lleva calzado de senderismo y 2L de agua! El acceso a pie se cierra en días de alto riesgo de incendio en verano (consulta la app oficial).",
        "tip_zh": "👚 务必穿登山运动鞋并自带至少2L饮用水！夏季高火险风天陆路禁入，出发前请查阅官方APP“Mes Calanques”通告。",
        "tip_fr": "👚 Chaussures de rando et 2L d'eau obligatoires ! L'accès à pied est fermé les jours de grand vent en été (vérifiez l'appli officielle).",
        "de": "👚 Feste Wanderschuhe und 2L Wasser mitnehmen! Im Sommer bei Wind oft wegen Waldbrandgefahr gesperrt (App prüfen)."
    },
    "ma_38": { # Parc Borély
        "tip_en": "🧺 Rent a rowboat on the central lake or grab ice cream near Château Borély for a relaxing local picnic under shaded plane trees.",
        "tip_ja": "🧺 中央池でボートをレンタルするか、ボレリー城前のショップでアイスを買って樹齢百年のプラタナスの木陰で芝生ピクニックが最高。",
        "tip_es": "🧺 Alquila una barca de remos en el lago o toma un helado junto al castillo para un picnic bajo los árboles.",
        "tip_zh": "🧺 在中央湖泊租划小皮划艇，或在 Borély 城堡旁买份冰淇淋，在百年树荫草坪上享受闲适野餐。",
        "tip_fr": "🧺 Louez une barque sur le lac ou prenez une glace près du château pour un pique-nique sous les arbres.",
        "de": "🧺 Leihen Sie ein Ruderboot auf dem See oder genießen Sie ein Eis im Schatten der alten Platanen."
    },
    "ma_43": { # Parc de Figuerolles
        "tip_en": "🧺 Pack a picnic lunch and extra apples for kids to feed friendly goats at the educational farm (Free entry).",
        "tip_ja": "🧺 敷地内の無料ふれあい農場でヤギやポニーにあげるリンゴを持参するのが家族連れの裏技！芝生でお弁当ピクニックも可能。",
        "tip_es": "🧺 Lleva manzanas para que los niños den de comer a las cabras en la granja gratuita y disfruta del picnic.",
        "tip_zh": "🧺 带有切片苹果带小朋友去免费农场区投喂小羊，并在松林草坪野餐。",
        "tip_fr": "🧺 Apportez des pommes pour les chèvres de la ferme pédagogique gratuite et profitez des espaces pique-nique.",
        "de": "🧺 Äpfel für die Ziegen auf dem kostenlosen Bauernhof mitnehmen und auf der Wiese picknicken."
    }
}

# Run updates for Paris and Marseille
refine_city("paris.json", paris_refinements)
refine_city("marseille.json", marseille_refinements)

print("🎉 Complete France cities insider tips sanitization finished!")
