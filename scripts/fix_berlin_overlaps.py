import json

berlin_overlap_fixes = {
    "b_5": { # Neues Museum
        "tip_en": "📸 Photography is STRICTLY PROHIBITED inside the Octagonal Room—enjoy looking at the 3,300-year-old royal masterpiece with your own eyes!",
        "tip_ja": "📸 王妃の彫像が飾られた『八角形の間』の内部は写真・動画撮影が完全禁止！携帯をしまって古代の奇跡の造形美を静かに観賞しましょう。",
        "tip_es": "📸 ¡Está ESTRICTAMENTE PROHIBIDO fotografiar en la sala octogonal! Disfruta la vista en persona sin pantallas.",
        "tip_zh": "📸 展出陈列的“八面体主厅”内严禁任何形式的拍照录像！请放下手机用肉眼近距离打量这一古埃及美学奇迹。",
        "tip_fr": "📸 Les photos sont STRICTEMENT INTERDITES dans la salle octogonale abritant le chef-d'œuvre.",
        "tip_de": "📸 Fotografieren im achteckigen Raum ist STRENGSTENS VERBOTEN! Das Meisterwerk ohne Kamera genießen."
    },
    "b_5b": { # Alte Nationalgalerie
        "tip_en": "🖼️ Head to Room 3.06 to view iconic German masterpieces including 'The Monk by the Sea' and 'Abbey in the Oakwood'.",
        "tip_ja": "🖼️ 3.06展示室へ直行！19世紀ロマン派絵画の最高峰『海辺の修道士』と『オークの森の修道院』が並んで鑑賞できます。",
        "tip_es": "🖼️ Ve a la sala 3.06 para ver las dos pinturas icónicas del maestro del romanticismo.",
        "tip_zh": "🖼️ 直奔 3.06 展厅！亲眼观赏19世纪经典画作《海边的僧侣》与《橡树林中的修道院》。",
        "tip_fr": "🖼️ Rendez-vous dans la salle 3.06 pour admirer les tableaux mythiques du romantisme.",
        "tip_de": "🖼️ In den Raum 3.06 gehen, um die zwei Hauptwerke der deutschen Romantik zu sehen."
    },
    "b_6": { # Berliner Dom
        "tip_en": "📸 Climb the stairs up to the outer dome gallery for an open-air 360-degree view looking down over the Spree river and TV tower.",
        "tip_ja": "📸 階段を登ったドーム外周テラス（Domkuppel）へ！博物館島とテレビ塔を見下ろす360度オープンエアパノラマビューが楽しめます。",
        "tip_es": "📸 Sube las escaleras hasta el mirador exterior de la cúpula para una vista de 360° sobre la ciudad.",
        "tip_zh": "📸 攀登台阶直达穹顶外围回廊（Domkuppel）！360度无遮挡俯瞰施普雷河与远方高塔。",
        "tip_fr": "📸 Montez jusqu'à la galerie extérieure du dôme pour une vue panoramique sur la rivière.",
        "tip_de": "📸 Die Stufen zum Kuppelumgang aufsteigen für einen 360-Grad-Rundumblick auf die Spree."
    },
    "b_6b": { # Humboldt Forum
        "tip_en": "🎟️ Permanent exhibitions are 100% FREE! Take the elevator up to the Rooftop Terrace for views over the river and cathedral.",
        "tip_ja": "🎟️ 常設展は入場完全無料！エレベーターで屋上テラス（Rooftop Terrace）へ登ると大聖堂と街並みを見渡せます。",
        "tip_es": "🎟️ ¡Las colecciones permanentes son 100% GRATIS! Sube en ascensor a la terraza del tejado.",
        "tip_zh": "🎟️ 常设展完全免费！乘电梯登顶 Rooftop Terrace 屋顶露台可俯瞰大教堂与中心水岸。",
        "tip_fr": "🎟️ Les collections permanentes sont 100% GRATUITES ! Prenez l'ascenseur jusqu'au toit-terrasse.",
        "tip_de": "🎟️ Freier Eintritt zu den Dauerausstellungen! Mit dem Aufzug auf die Dachterrasse fahren."
    },
    "b_8": { # Gedenkstätte Berliner Mauer
        "tip_en": "📸 Visit the 5th-floor observation tower inside the Documentation Centre for a top-down view into the preserved border strip.",
        "tip_ja": "📸 通りの向かいにある施設5階の無料展望タワーへ！残された分断エリアの構造を真上からリアルに俯瞰できます。",
        "tip_es": "📸 Sube a la torre de observación en la 5ª planta para ver la zona fronteriza desde arriba.",
        "tip_zh": "📸 登上一路之隔的档案中心5楼免费展望塔！从高处直视完整保存的防护铁丝网与监视塔。",
        "tip_fr": "📸 Montez à la tour d'observation du 5e étage pour voir l'ancien secteur frontalier d'en haut.",
        "tip_de": "📸 Auf den Aussichtsturm im 5. Stock steigen, um den erhaltenen Grenzbereich von oben zu sehen."
    },
    "b_10": { # Holocaust-Mahnmal
        "tip_en": "🧥 Respectful behavior is strictly required (no running or jumping). Visit the free underground Ort der Information via the southeast stairs.",
        "tip_ja": "🧥 柱の上に乗る行為は厳禁！南東角の階段から地下の無料展示室（Ort der Information）へ入り、手紙や記録を静かに閲覧しましょう。",
        "tip_es": "🧥 ¡Está prohibido subirse a las estelas! Visita el centro subterráneo por la esquina sureste.",
        "tip_zh": "🧥 庄重提示：严禁攀爬跳跃！请从东南角阶梯下至地下免费展厅，静心阅读历史文献。",
        "tip_fr": "🧥 Interdiction de grimper sur les stèles ! Descendez au centre souterrain par l'escalier sud-est.",
        "tip_de": "🧥 Das Besteigen der Stelen ist untersagt! Das kostenlose unterirdische Ort der Information besuchen."
    },
    "b_12b": { # Gemäldegalerie
        "tip_en": "🖼️ Head to Room 18 to view 'Woman with a Pearl Necklace' and 'The Glass of Wine' in a quiet gallery setting.",
        "tip_ja": "🖼️ 第18展示室へ直行！現存数の少ない希少な17世紀オランダ絵画の傑作2点を静かに鑑賞できます。",
        "tip_es": "🖼️ Dirígete a la sala 18 para ver las dos obras maestras holandesas del siglo XVII.",
        "tip_zh": "🖼️ 直奔18号展厅！近距离独享极具代表性的17世纪荷兰画派传世珍品。",
        "tip_fr": "🖼️ Rendez-vous dans la salle 18 pour admirer deux chefs-d'œuvre rares du XVIIe siècle.",
        "tip_de": "🖼️ Direkt in Raum 18 gehen, um zwei seltene Meisterwerke des 17. Jahrhunderts zu sehen."
    },
    "b_13b": { # DHM
        "tip_en": "📸 Walk up the glass spiral staircase in the new wing for beautiful reflections of the surrounding historic courtyard.",
        "tip_ja": "📸 新館内部の透明な階段へ！光とガラスの幾何学構造が美しい人気の建築写真スポットです。",
        "tip_es": "📸 Sube por la escalera de caracol de cristal para tomar fotos de la arquitectura contemporánea.",
        "tip_zh": "📸 拾级而上攀登新馆通透楼梯！感受阳光打在几何幕墙上的视觉魅力。",
        "tip_fr": "📸 Montez l'escalier en colimaçon de verre pour admirer la rencontre des architectures.",
        "tip_de": "📸 Die gläserne Wendeltreppe im Neubau für tolle Architekturfotos nutzen."
    },
    "b_13d": { # Museum für Naturkunde
        "tip_en": "📸 Walk straight into the Main Hall to stand beneath the record-breaking giant sauropod dinosaur skeleton!",
        "tip_ja": "📸 入場してすぐの中央ホールへ！ギネス記録を誇る超巨大なブラキオサウルス骨格を見上げる光景は圧巻です。",
        "tip_es": "📸 ¡Entra a la Sala Principal para colocarte debajo del esqueleto de dinosaurio más alto del mundo!",
        "tip_zh": "📸 步入一楼中央大厅！站在创吉尼斯纪录的超巨型草食恐龙化石正下方仰望。",
        "tip_fr": "📸 Entrez dans la Grande Salle pour vous tenir sous le squelette de dinosaure géant !",
        "tip_de": "📸 Direkt in den Hauptsaal gehen und sich unter das gigantische Saurierskelett stellen!"
    },
    "b_13f": { # Computerspielemuseum
        "tip_en": "🎮 Play vintage classics like Nimrod, Pac-Man, Space Invaders, and Pong on authentic coin-op hardware!",
        "tip_ja": "🎮 1950年代の初期ハードや、パックマン、インベーダーの実機筐体を無料でプレイし放題！",
        "tip_es": "🎮 ¡Juega a clásicos como Pac-Man y Space Invaders en máquinas recreativas originales!",
        "tip_zh": "🎮 展厅内所有古董街机与复古主机均可免费无限次投币试玩！",
        "tip_fr": "🎮 Jouez gratuitement aux grands classiques sur les vraies bornes vintage !",
        "tip_de": "🎮 Klassiker an funktionierenden Original-Automaten ausprobieren!"
    },
    "b_13": { # Hackesche Höfe
        "tip_en": "📸 Walk straight into Hof 1 to admire the blue-and-white tiled walls, then stroll into neighboring Haus Schwarzenberg for raw street art!",
        "tip_ja": "📸 第1の中庭（Hof 1）の青と白のタイルの装飾壁画は撮影必至！すぐ隣の『Haus Schwarzenberg』の細道へ足を伸ばすとディープなストリートアート空間が広がります。",
        "tip_es": "📸 Entra en Hof 1 para ver los azulejos y luego descubre el pasaje callejero de al lado.",
        "tip_zh": "📸 走入1号中庭（Hof 1）拍摄蓝色瓷砖大楼！随后推开相邻的 Haus Schwarzenberg 小门，直达涂鸦文化长廊。",
        "tip_fr": "📸 Entrez dans la cour Hof 1 pour admirer les décorations, puis découvrez le passage street art d'à côté !",
        "tip_de": "📸 Im Hof 1 die Fassade fotografieren und nebenan das Haus Schwarzenberg mit Streetart erkunden."
    },
    "b_13k": { # Tempelhofer Feld
        "tip_en": "🚴 Rent a city bike or inline skates to ride at full speed down the open 2km asphalt runway without any traffic!",
        "tip_ja": "🚴 自転車やインラインスケートをレンタルして、障害物のない広大なアスファルトをフルスピードで駆け抜ける体験が最高に爽快！",
        "tip_es": "🚴 ¡Alquila una bicicleta o patines para recorrer la gran pista a toda velocidad sin coches!",
        "tip_zh": "🚴 租一辆城市自行车或直排轮滑鞋，在没有任何车辆干扰的柏油路面上全速飙车！",
        "tip_fr": "🚴 Louez un vélo ou des roller-skates pour filer à toute vitesse le long de la piste !",
        "tip_de": "🚴 Ein Fahrrad oder Inlineskates mieten und mit Vollgas die freie Piste entlangflitzen!"
    },
    "b_13l": { # KaDeWe
        "tip_en": "🍽️ Head straight to the 6th floor food hall to sit at the Austernbar for fresh oysters and a glass of Champagne!",
        "tip_ja": "🍽️ 6階（Feinschmeckeretage）の『オイスターバー（Austernbar）』へ直行！最高級生牡蠣と冷えたシャンパンをカウンターで味わうのが究極の贅沢。",
        "tip_es": "🍽️ ¡Sube a la 6ª planta y siéntate en la Austernbar a comer ostras frescas con champán!",
        "tip_zh": "🍽️ 建议直奔6楼大厅的 Austernbar 生蚝吧选座，现场享用现开顶级生蚝与冰镇香槟！",
        "tip_fr": "🍽️ Foncez au 6e étage pour vous installer à l'Austernbar et déguster des huîtres fraîches avec du champagne !",
        "tip_de": "🍽️ Direkt in den 6. Stock fahren und an der Austernbar frische Austern mit Champagner genießen!"
    }
}

fpath = "data/cities/berlin.json"
with open(fpath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for s in data['spots']:
    sid = s['id']
    if sid in berlin_overlap_fixes:
        up = berlin_overlap_fixes[sid]
        for k, v in up.items():
            s[k] = v
        s['tip'] = up.get('tip_en', s.get('tip', ''))
        count += 1

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Refined {count} spots in berlin.json for 0% description overlap")
