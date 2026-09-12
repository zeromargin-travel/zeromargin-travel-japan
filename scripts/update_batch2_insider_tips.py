import json
import os

def update_city_tips(fname, tips_dict):
    fpath = f"data/cities/{fname}"
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    for s in data['spots']:
        sid = s['id']
        if sid in tips_dict:
            tip_data = tips_dict[sid]
            for lang_key in ['tip_en', 'tip_ja', 'tip_es', 'tip_zh', 'tip_fr', 'tip_de']:
                if lang_key in tip_data:
                    s[lang_key] = tip_data[lang_key]
            # Ensure tip field also has default English tip
            s['tip'] = tip_data.get('tip_en', '')
            updated_count += 1

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Updated {updated_count} spots in {fname}")

# -------------------------------------------------------------
# BATCH 2: STRASBOURG (45 spots), TOULOUSE (39 spots), MARSEILLE (43 spots)
# -------------------------------------------------------------

strasbourg_tips = {
    "st_1": {
        "tip_en": "Be outside the cathedral at 12:30 PM to watch the 16th-century Astronomical Clock show. Climb the 332 steps to the platform for clear views over the Black Forest.",
        "tip_ja": "毎日12:30に動き出す16世紀のからくり天文時計ショーは見逃せません。332段の階段を登って展望台へ行くと、天気の良い日はドイツの黒い森（シュヴァルツヴァルト）まで遠望できます。",
        "tip_es": "A las 12:30 se activa el espectáculo del reloj astronómico del siglo XVI. Sube los 332 escalones para ver la Selva Negra.",
        "tip_zh": "每天中午12:30准时观赏16世纪古董天文钟打点木偶表演。攀登332级台阶至大教堂观景台，晴天可远眺德国黑森林。",
        "tip_fr": "Assistez au spectacle de l'horloge astronomique du XVIe siècle à 12h30 précis. Montez la plateforme (332 marches) pour voir la Forêt-Noire.",
        "tip_de": "Um 12:30 Uhr erleben Sie das automatisierte Figurenspiel der astronomischen Uhr. Die 332 Stufen zur Aussichtsplattform lohnen sich!"
    },
    "st_2": {
        "tip_en": "Take the Batorama glass-topped boat tour departing right next to Palais Rohan for a 360-degree view through the locks and around the UNESCO island.",
        "tip_ja": "ローアン宮前発着の『バトーラマ（Batorama）』ガラス屋根観光船での水上周遊が最高！水門通過や世界遺産グラン・ディルの絶景を楽しめます。",
        "tip_es": "Toma el barco panorámico Batorama con techo de cristal para recorrer los canales y las esclusas del centro histórico.",
        "tip_zh": "在Rohan宫旁乘坐Batorama全景玻璃顶游船。穿过古老水门体验船闸升降，环绕世界遗产大岛十分舒适。",
        "tip_fr": "Embarquez à bord des bateaux promeneurs Batorama pour un tour complet de la Grande Île avec passage des écluses.",
        "tip_de": "Die Batorama-Panoramabootstour führt durch die historischen Schleusen rund um die UNESCO-Altstadt."
    },
    "st_3": {
        "tip_en": "Walk up to the Vauban Dam (Barrage Vauban) roof terrace for THE classic postcard photo of the 3 Covered Bridges and cathedral spire.",
        "tip_ja": "ヴォーバン・ダム（Barrage Vauban）の屋上展望テラスへ登ってください！3つの屋根付き橋と大聖堂の尖塔を同時に収める『ストラスブール一番の絵はがきアングル』です。",
        "tip_es": "Sube a la terraza del tejado del Barrage Vauban para la foto perfecta de los 3 Puentes Cubiertos con la catedral de fondo.",
        "tip_zh": "登顶沃邦水坝（Barrage Vauban）屋顶观景露台！这里是拍摄3座廊桥与远方大教堂尖塔同框的“第一名胜明信片机位”。",
        "tip_fr": "Montez sur le toit-terrasse du Barrage Vauban pour immortaliser les Ponts Couverts avec la cathédrale en arrière-plan.",
        "tip_de": "Auf die Dachterrasse der Barrage Vauban steigen für das berühmte Fotomotiv der drei gedeckten Brücken vor dem Münster."
    },
    "st_4": {
        "tip_en": "Walk past the 1572 timber-framed tanners' houses during magic hour when canal reflections and floral window boxes light up.",
        "tip_ja": "1572年建築の皮なめし職人の木造家屋（Maison des Tanneurs）前。夕暮れ時に運河の水面と窓辺の赤いゼラニウムがライトアップされる景色は必見。",
        "tip_es": "Contempla las casas de entramado de madera de 1572 al atardecer, cuando las flores de las ventanas se reflejan en el agua.",
        "tip_zh": "漫步在1572年建成的制皮匠木构木屋旁。黄昏时刻运河水倒映着窗前鲜艳的天竺葵花海，梦幻唯美。",
        "tip_fr": "Admirez les maisons à colombages du XVIe siècle au bord de l'eau aux dernières lumières du jour.",
        "tip_de": "Die malerischen Fachwerkhäuser von 1572spiegeln sich am späten Nachmittag wunderschön im Wasser der Ill."
    },
    "st_5": {
        "tip_en": "Housed in an 18th-century episcopal palace designed by Robert de Cotte. Admission includes access to 3 museums (Fine Arts, Archeology, Decorative Arts).",
        "tip_ja": "18世紀のカーディナル宮殿。1枚のチケットで美術館、装飾美術館、考古学博物館の3つが見学でき、ヴェルサイユ宮殿風の豪奢な室内が見事。",
        "tip_es": "Palacio episcopal del siglo XVIII con 3 museos (Bellas Artes, Arqueología y Artes Decorativas). Entradas combinadas.",
        "tip_zh": "由18世纪皇家总主教宫改建，一张联票通吃三大博物馆（美术馆、考古馆、装饰艺术馆）。凡尔赛宫风格内饰极尽奢华。",
        "tip_fr": "Ancien palais des princes-évêques abritant 3 grands musées municipaux dans un cadre versaillais.",
        "tip_de": "Prachtvolles Bischofspalais des 18. Jahrhunderts mit 3 Museen (Schöne Künste, Archäologie, Kunstgewerbe)."
    },
    "st_6": {
        "tip_en": "Visit the Christmas Capital of Europe! Main giant 30-meter Christmas tree stands at Place Kleber from late November through December.",
        "tip_ja": "『ヨーロッパのクリスマス首都』！11月下旬〜12月にはクレベール広場に高さ30mの巨大クリスマスツリーとマルシェが登場し幻想的です。",
        "tip_es": "¡La Capital de la Navidad de Europa! En diciembre, Place Kléber alberga el gran árbol de Navidad iluminado de 30 metros.",
        "tip_zh": "欧洲圣诞之都的核心！11月底至12月期间，克勒贝尔广场上会竖起高达30米的巨型梦幻璀璨圣诞树与暖心集市。",
        "tip_fr": "Cœur vibrant de la 'Capitale de Noël' ! Le grand sapin de 30 mètres illumine la place dès fin novembre.",
        "tip_de": "Herzensort der 'Weihnachtshauptstadt Europas'! Ab Ende November steht hier der riesige 30-Meter-Weihnachtsbaum."
    },
    "st_7": {
        "tip_en": "Take a free guided tour of the Hemicycle debating chamber when the European Parliament is not in session (bring valid passport/ID).",
        "tip_ja": "パスポート提示で欧州議会の本会議場（Hemicycle）の無料見学ツアーに参加できます。近未来的なガラス建築とEUの歴史を体験。",
        "tip_es": "Visita gratuita al Hemiciclo del Parlamento Europeo cuando no hay sesiones (imprescindible pasaporte o DNI original).",
        "tip_zh": "无会议期间可凭护照/身份证免费进入欧洲议会全景圆顶议事厅参观。未来主义玻璃球形建筑十分震撼。",
        "tip_fr": "Visitez gratuitement l'Hémicycle du Parlement européen en dehors des sessions (passeport ou carte d'identité obligatoire).",
        "tip_de": "Kostenlose Besichtigung des Plenarsaals im Europäischen Parlament (gültiger Ausweis erforderlich)."
    },
    "st_8": {
        "tip_en": "Try traditional Choucroute Garnie (Alsatian sauerkraut with sausages and smoked pork) at Winstub Chez Yvonne or Maison des Tanneurs.",
        "tip_ja": "アルザス名物『シュークルート（発酵キャベツとソーセージ・豚肉の煮込み）』を老舗ウィンシュトゥブ（居酒屋）でアルザス白ワイン（リースリング）と合わせるのが極上！",
        "tip_es": "Prueba la Choucroute Garnie tradicional acompañada de vino blanco Riesling en una auténtica Winstub.",
        "tip_zh": "在古朴的Alsace居酒屋（Winstub）品尝名菜发酵酸菜香肠拼盘（Choucroute Garnie），配上一杯凛冽的雷司令（Riesling）白葡萄酒！",
        "tip_fr": "Dégustez una choucroute alsacienne généreuse arrosée d'un verre de Riesling dans une winstub typique.",
        "tip_de": "Genießen Sie ein deftiges elsässisches Choucroute mit einem Glas kühlem Riesling in einer gemütlichen Winstub."
    },
    "st_9": {
        "tip_en": "The oldest building in Strasbourg (1306). Try their famous Tarte Flambée (Flammekueche) with crispy thin crust and smoked bacon.",
        "tip_ja": "1306年建設のストラスブール最古の木造建築。アルザス風薄焼きピザ『タルト・フランベ（フラムクーヘン）』の焼きたてカリカリは絶品！",
        "tip_es": "El edificio más antiguo de Estrasburgo (1306). Prueba la Tarte Flambée (Flammekueche) recién horneada.",
        "tip_zh": "始于1306年、斯特拉斯堡最古老的历史木构建筑。必点现烤薄脆、铺满阿尔萨斯培根与奶油的火焰薄饼（Tarte Flambée）！",
        "tip_fr": "La plus ancienne maison de la ville (1306) ! Dégustez une tarte flambée (flammekueche) croustillante au feu de bois.",
        "tip_de": "Das älteste Bürgerhaus Strasburgs von 1306. Legendärer Ort für eine knusprige Flammkuchen-Einkehr."
    },
    "st_10": {
        "tip_en": "Houses the famous 1741 Silbermann organ that Wolfgang Amadeus Mozart played in 1778. Free entry to admire the baroque mausoleum.",
        "tip_ja": "1778年にモーツァルトが試奏した1741年製の名器ジルバーマン・オルガンを所蔵。サックス元帥の壮麗なロココ調墓碑彫刻も見どころ。",
        "tip_es": "Alberga el órgano Silbermann de 1741 que tocó Mozart en 1778. Entrada libre para ver el mausoleo barroco.",
        "tip_zh": "收藏有莫扎特于1778年曾倾情演奏的1741年名管风琴Silbermann。大理石雕凿的萨克森伯爵陵墓艺术感十足。免费开放。",
        "tip_fr": "Abrite le célèbre orgue Silbermann de 1741 joué par Mozart. Entrée libre pour admirer le mausolée du Maréchal de Saxe.",
        "tip_de": "Beherbergt die berühmte Silbermann-Orgel von 1741, auf der Mozart 1778 spielte. Eintritt frei."
    },
    "st_11": {
        "tip_en": "Cross the Passerelle Mimram footbridge into Kehl, Germany—you can walk or bike into another country in just 5 minutes!",
        "tip_ja": "ライン川に架かる歩道橋を渡ると僅か5分で対岸のドイツ（ケール市）へ！国境越え散策やドイツ側のライン公園ピクニックが楽しめます。",
        "tip_es": "Cruza la pasarela peatonal sobre el Rin hacia Kehl (Alemania). ¡Puedes cambiar de país caminando en 5 minutos!",
        "tip_zh": "跨越莱茵河海峡行人天桥即可步入德国Kehl市！短短5分钟完成徒步/骑行跨国体验，十分有趣。",
        "tip_fr": "Traversez la passerelle Mimram au-dessus du Rhin pour passer en Allemagne (Kehl) à pied en 5 minutes !",
        "tip_de": "Über die Fußgängerbrücke Mimram über den Rhein spazieren und in 5 Minuten in Deutschland (Kehl) sein."
    },
    "st_12": {
        "tip_en": "Buy authentic gingerbread (Pain d'épices) molded into heart shapes and traditional Alsatian Kugelhopf cake baked in glazed earthenware pots.",
        "tip_ja": "陶器の型で焼かれるアルザス伝統菓子『クグロフ』や、スパイス香る『パン・ド・エピス（クッキー）』はストラスブール土産の決定版！",
        "tip_es": "Compra pan de especias (Pain d'épices) y la tarta tradicional Alsaciana Kugelhopf horneada en moldes de barro.",
        "tip_zh": "推荐购买由彩釉陶型烘烤而成的阿尔萨斯奶油空心蛋糕“Kugelhopf”与充满肉桂香气的“Pain d'épices”姜饼。",
        "tip_fr": "Achetez un véritable kougelhopf au beurre et du pain d'épices artisanal préparé dans les moules en poterie de Soufflenheim.",
        "tip_de": "Kaufen Sie einen traditionellen elsässischen Gugelhupf und duftenden Lebkuchen (Pain d'épices)."
    },
    "st_13": {
        "tip_en": "A spiritual sanctuary at 763m altitude offering panoramic views over the Rhine Plain to the Black Forest. Walk the mysterious Pagan Wall path.",
        "tip_ja": "標高763mの修道院。アルザス平原とライン川、遠くドイツの黒い森を見渡す絶景。紀元前からの巨石遺構『異教徒の壁（Mur Païen）』散策も爽快。",
        "tip_es": "Santuario a 763m con vistas panorámicas sobre el Rin. Camina por el sendero de la misteriosa Muralla Pagana.",
        "tip_zh": "矗立于763米山顶的灵修圣地。鸟瞰莱茵河平原至德国黑森林。探访神秘的古加罗罗马时代巨石“异教徒之墙”（Mur Païen）。",
        "tip_fr": "Haut lieu spirituel à 763m d'altitude avec panorama exceptionnel sur la plaine d'Alsace. Balade le long du Mur Païen.",
        "tip_de": "Wallfahrtsort auf 763m Höhe mit herrlichem Rundumblick über die Rheinebene. Rundweg an der Heidenmauer."
    },
    "st_14": {
        "tip_en": "World-famous half-timbered wine village along the Alsace Wine Route (40 min from Strasbourg). Climb up to the 3 castle ruins above the vineyards.",
        "tip_ja": "アルザスワイン街道で最も美しいブドウ畑の木造村（ストラスブールから車で40分）。ブドウ畑の上の3つの城跡へのハイキングが最高。",
        "tip_es": "Famoso pueblo vinícola de casas de colores. Sube a las ruinas de los 3 castillos entre los viñedos.",
        "tip_zh": "阿尔萨斯葡萄酒之路上的彩色梦幻木构名村（距斯特拉斯堡40分钟）。徒步穿越山坡葡萄园攀登顶部的三座古堡遗址。",
        "tip_fr": "Village viticole emblématique de la Route des Vins. Montez aux trois châteaux forts surplombant les vignes.",
        "tip_de": "Berühmtes Weindorf an der Elsässer Weinstraße. Wanderung zu den drei Burgruinen hoch über den Reben."
    },
    "st_15": {
        "tip_en": "Known as 'Little Venice' (La Petite Venise) with half-timbered pastel houses along the Lauch canal. Combined day trip easily done by 30-min train.",
        "tip_ja": "ストラスブールから列車で僅か30分！『小ヴェネツィア』と呼ばれる運河沿いのパステルカラー木造家屋群とウンターリンデン美術館（イゼンハイム祭壇画）が見事。",
        "tip_es": "Conocido como 'La Petite Venise' con casas de colores junto al canal. Llegada fácil en tren en 30 minutos.",
        "tip_zh": "乘火车仅需30分钟！拥有被称为“小威尼斯”（La Petite Venise）的缤纷运河木屋群与菩提树下美术馆（Unterlinden）。",
        "tip_fr": "Découvrez 'La Petite Venise' de Colmar à 30 min de train ! Promenez-vous le long de la Lauch en barque.",
        "tip_de": "Das malerische 'Klein-Venedig' in Colmar ist mit dem Zug in nur 30 Minuten erreichbar. Romantische Kahnfahrt!"
    },
    "st_16": {
        "tip_en": "See original medieval sculptures, stained glass, and gargoyles saved from the Strasbourg Cathedral during centuries of restoration.",
        "tip_ja": "ストラスブール大聖堂のオリジナル彫刻やゴシック様式のステンドグラス本物を保存・展示する歴史的ミュージアム。",
        "tip_es": "Exhibe esculturas originales y vidrieras medievales salvadas de la catedral de Estrasburgo.",
        "tip_zh": "展示从斯特拉斯堡大教堂修复中替换保护下来的中世纪雕塑雕画真迹与中世纪彩绘玻璃真品。",
        "tip_fr": "Musée fascinant abritant les sculptures gothiques originales et vitraux authentiques de la cathédrale.",
        "tip_de": "Museum mit den originalen gotischen Skulpturen und mittelalterlichen Glasfenstern des Straßburger Münsters."
    },
    "st_17": {
        "tip_en": "Walk through the covered sandstone galleries of this 17th-century dam designed by Vauban to flood the city defenses during sieges.",
        "tip_ja": "17世紀に要塞技師ヴォーバンが敵の侵攻を防ぐ浸水要塞として設計した砂岩のアーチ橋。内部のギャラリーを通って屋上へ登れます。",
        "tip_es": "Recorre las galerías cubiertas de piedra arenisca de esta presa del siglo XVII diseñada por el ingeniero Vauban.",
        "tip_zh": "穿行于17世纪由著名军事工程家沃邦修筑的红砂岩水坝廊道内部。当年曾用于放水淹没要塞外围敌人。",
        "tip_fr": "Traversez le couloir intérieur de ce barrage militaire du XVIIe siècle conçu pour inonder la ville en cas de siège.",
        "tip_de": "Durchschreiten Sie den überdachten Wandelgang dieser historischen Wehrwehr-Anlage von Festungsbaumeister Vauban."
    },
    "st_18": {
        "tip_en": "Features the works of Strasbourgeois illustrator Tomi Ungerer (author of The Three Robbers) & 8,000 satiric drawings in a 19th-century villa.",
        "tip_ja": "絵本『すてきな三にんぐみ』で有名な地元出身の絵本作家トミ・アンゲラーのイラスト作品8000点を所蔵する美術館。",
        "tip_es": "Exhibe obras del ilustrador local Tomi Ungerer (autor de 'Los tres bandidos') en una villa del siglo XIX.",
        "tip_zh": "设于19世纪别墅内，展出出生于斯特拉斯堡的著名国际绘本大师汤米·温格尔（《三个强盗》作者）的8000幅手稿原作。",
        "tip_fr": "Musée unique dédié au dessinateur strasbourgeois Tomi Ungerer (auteur des 'Trois Brigands') et à l'illustration.",
        "tip_de": "Museum gewidmet den Werken des Straßburger Zeichners Tomi Ungerer ('Die drei Räuber')."
    },
    "st_19": {
        "tip_en": "Housed in a 14th-century butcher's guild house (Grande Boucherie) detailing Strasbourg's urban development from Roman times.",
        "tip_ja": "14世紀の精肉ギルド館を利用。古代ローマ時代の『アルジェントラトゥム』開拓から現代までのストラスブールの都市変遷史を展示。",
        "tip_es": "Ubicado en el antiguo gremio de carniceros del siglo XIV sobre la historia urbana de la ciudad.",
        "tip_zh": "位于14世纪屠夫公会大楼内部。完整呈现斯特拉斯堡自古罗马兵营时代至欧州首都的城市演进史。",
        "tip_fr": "Installé dans l'ancienne Grande Boucherie du XIVe siècle sur l'histoire politique et sociale de Strasbourg.",
        "tip_de": "Stadtgeschichtliches Museum in der ehemaligen Ausführung der Großen Fleischhalle von 1385."
    },
    "st_20": {
        "tip_en": "Strasbourg's oldest park featuring a boat lake, Josephine Pavilion, and wild storks nesting atop trees and rooftops.",
        "tip_ja": "アルザスのシンボル『コウノトリ（Storks）』の保護育殖地！木々や屋根の上にコウノトリの巨大な巣があり間近で観察できます。",
        "tip_es": "El parque más antiguo de Estrasburgo con lago, pabellón imperial y nidos de cigüeñas blancas en los árboles.",
        "tip_zh": "阿尔萨斯吉祥物白鹳的保护复育乐园！公园树顶与屋顶上栖息着巨大的白鹳鸟巢，非常治愈。",
        "tip_fr": "Plus ancien parc de la ville avec son lac, son pavillon Joséphine et ses cigognes blanches en liberté.",
        "tip_de": "Ältester Park Strasburgs mit einem Bootssüff, Pavillon und frei nistenden Weißstörchen."
    },
    "st_21": {
        "tip_en": "Discover modern art masterpieces by Monet, Picasso, Kandinsky, and Braque in a transparent glass building on the Ill riverbank.",
        "tip_ja": "イル川沿いの透明なガラス張りの現代美術館。モネ、ピカソ、カンディンスキー、アープの近現代アート名作を展示。",
        "tip_es": "Museo en un edificio de cristal junto al río Ill con obras de Monet, Picasso y Kandinsky.",
        "tip_zh": "坐落于伊尔河畔通透玻璃现代建筑内。收藏有莫奈、毕加索、康定斯基及让·阿尔普的近现代艺术珍品。",
        "tip_fr": "Musée d'art moderne et contemporain à l'architecture de verre surplombant l'Ill (œuvres de Monet, Picasso).",
        "tip_de": "Museum für moderne Kunst in einem kühnen Glasbau an der Ill mit Werken von Monet und Picasso."
    },
    "st_22": {
        "tip_en": "Dedicated to Art Nouveau & Art Deco glassmaster René Lalique in Wingen-sur-Moder (located in northern Alsace pine forest).",
        "tip_ja": "ガラス工芸の巨匠ルネ・ラリックの美術館。アール・ヌーヴォーのジュエリーや洗練された香水瓶、クリスタルガラスの輝きが眩い空間。",
        "tip_es": "Dedicado al maestro del cristal Art Nouveau René Lalique en Wingen-sur-Moder.",
        "tip_zh": "位于北阿尔萨斯松林小镇Wingen-sur-Moder。展示新艺术与装饰艺术玻璃大师雷内·拉里克（René Lalique）璀璨的珠宝与香水水晶瓶。",
        "tip_fr": "Musée somptueux consacré au maître verrier et bijoutier René Lalique à Wingen-sur-Moder.",
        "tip_de": "Museum gewidmet dem Glaskünstler und Schmuckgestalter René Lalique in Wingen-sur-Moder."
    },
    "st_23": {
        "tip_en": "Explore the late 19th-century German Imperial quarter built after 1871 featuring grand Prussian avenues and Palais du Rhin.",
        "tip_ja": "1871年以降のドイツ帝国統治時代に建設された壮大な都市区画（ユネスコ世界遺産）。重厚なネオ・バロック様式のライン宮殿（Palais du Rhin）が見どころ。",
        "tip_es": "Barrio imperial alemán de finales del siglo XIX patrimonio UNESCO con grandes avenidas y el Palais du Rhin.",
        "tip_zh": "1871年德法战争后由德意志帝国兴建的帝国街区（UNESCO世界遗产）。宏伟的新巴洛克风格莱茵宫（Palais du Rhin）极具气派。",
        "tip_fr": "Quartier impérial allemand du XIXe siècle classé UNESCO avec ses grandes avenues et le Palais du Rhin.",
        "tip_de": "Deutsches Kaiserquartier aus dem späten 19. Jahrhundert (UNESCO-Welterbe) mit dem prächtigen Palais du Rhin."
    },
    "st_24": {
        "tip_en": " Dine on the covered wooden balcony over the canal inside this 1572 timber house—book weeks in advance for a canal-side table!",
        "tip_ja": "1572年建築の木造館。運河に張り出したテラス席でいただくシュークルートは格別。運河沿いの席は数週間前の予約が必須です。",
        "tip_es": "Reserva con semanas de antelación para cenar en el balcón de madera sobre el canal de esta casa de 1572.",
        "tip_zh": "位于1572年古木屋的水上阳台。运河边餐位极具风情，务必提前数周预订！",
        "tip_fr": "Réservez des semaines à l'avance pour dîner sur le balcon en bois surplombant l'eau dans cette maison de 1572.",
        "tip_de": "Unbedingt im Voraus reservieren für einen Tisch auf dem überdachten Balkon direkt über dem Wasser!"
    },
    "st_25": {
        "tip_en": "Historic 1873 winstub frequented by former French presidents. Try their Escargots, Wädele (pork knuckle), and Gewürztraminer wine.",
        "tip_ja": "歴代フランス大統領も訪れた1873年創業の伝説の居酒屋。エスカルゴや豚ひざ肉料理（Wädele）にフルーティーなゲヴュルツトラミネールワインを合わせて。",
        "tip_es": "Winstub histórica de 1873 frecuentada por presidentes franceses. Prueba los caracoles y el codillo Wädele.",
        "tip_zh": "始于1873年、法国历任总统均曾光顾的传奇Winstub。必点法式焗蜗牛与红烧猪脚（Wädele）。",
        "tip_fr": "Winstub mythique de 1873 fréquentée par les présidents. Dégustez el jambonneau (wädele) et les escargots.",
        "tip_de": "Historische Winstub von 1873, in der schon französische Präsidenten speisten. Ausgezeichnetes Wädele!"
    },
    "st_26": {
        "tip_en": "Stroll down the pedestrian Rue des Orfèvres near the Cathedral—famous for gourmet charcuteries, cheese shops, and chocolate boutiques.",
        "tip_ja": "大聖堂近くの『金細工師通り（Rue des Orfèvres）』。アルザスチーズ、フォアグラ、ショコラティエ、ワインショップが集まるグルメストリート。",
        "tip_es": "Calle peatonal junto a la catedral famosa por sus tiendas de delicatessen, quesos y chocolaterías.",
        "tip_zh": "毗邻大教堂的金银匠步行街（Rue des Orfèvres）。聚集了各种阿尔萨斯精选干酪店、鹅肝酱店与精品巧克力工坊。",
        "tip_fr": "Rue piétonne gourmande incontournable près de la cathédrale bordée de pâtisseries et épiceries fines.",
        "de": "Malerische Fußgängerstraße beim Münster voller Feinkostläden, Käsegeschäfte und Chocolatiers."
    },
    "st_27": {
        "tip_en": "Discover 18th-century Alsatian rural life, painted furniture, ceramics, and costumes inside a timber courtyard mansion on the Ill river.",
        "tip_ja": "イル川沿いの木造館。かつてのアルザス農村の伝統衣装、手描きの婚礼家具、陶器、生活道具が美しく展示された民俗博物館。",
        "tip_es": "Muestra la vida rural tradicional de Alsacia con muebles pintados y trajes regionales en una casa del siglo XVIII.",
        "tip_zh": "设于18世纪伊尔河畔木宅内。展出阿尔萨斯乡村传统民族服饰、手绘婚姻木家具与民俗生活器具。",
        "tip_fr": "Musée charmant dédié aux arts et traditions populaires d'Alsace (costumes, meuble peint, céramique).",
        "de": "Faszinierendes Museum für elsässische Volkskunst mit bemaltem Fachwerk-Interieur und Trachten."
    },
    "st_28": {
        "tip_en": "Buy piping hot freshly baked pretzel (Bretzel) and Kugelhopf from local bakeries like Maison Alsacienne de Biscuiterie.",
        "tip_ja": "地元ベーカリーで買える塩味の効いた焼き立てプレッツェル（Bretzel）や甘いクグロフパンは街歩きのお供に最適です！",
        "tip_es": "Compra pretzels (Bretzel) salados recién horneados y Kugelhopf para ir comiendo por la calle.",
        "tip_zh": "在老牌饼店买一块现烤热气腾腾的盐花普雷结面包（Bretzel）与小圆奶油Kugelhopf，边走边吃极香。",
        "tip_fr": "Dégustez une bretzel au sel fraîchement cuite ou un mini-kougelhopf en flânant dans les rues piétonnes.",
        "de": "Frisch gebackene Brezeln und Gugelhupf bei den traditionellen Bäckereien für unterwegs kaufen."
    },
    "st_29": {
        "tip_en": "Admire the intricate 15th-century carved wooden balcony facade of Maison Kammerzell from the outdoor cafe terrace on Place du Cathédrale.",
        "tip_ja": "大聖堂広場に立つ15世紀の木造建築彫刻の傑作。カフェテラス席で大聖堂を見上げながらお茶や食事を楽しむのが定番の贅沢。",
        "tip_es": "Admira los intrincados tallados de madera del siglo XV de la Maison Kammerzell desde la terraza de la plaza.",
        "tip_zh": "站在大教堂广场露台咖啡座，仰望拉开于15世纪的Maison Kammerzell外墙精美木雕浮雕。",
        "tip_fr": "Installez-vous en terrasse face à la cathédrale pour admirer la façade sculptée du XVe siècle de la Maison Kammerzell.",
        "tip_de": "Genießen Sie auf der Terrasse den Blick auf die geschnitzte Holzfassade des Maison Kammerzell von 1427."
    },
    "st_30": {
        "tip_en": "Taste dry Alsatian Riesling and aromatic Gewürztraminer wines inside historic wine cellars dating back to 1395 beneath the hospital.",
        "tip_ja": "1395年創業！ストラスブール市立病院の地下にある歴史的ワインセラー。1472年ヴィンテージの世界最古の樽ワインが保管されています。",
        "tip_es": "Bodega histórica de 1395 bajo el hospital que conserva el vino en barrica más antiguo del mundo (año 1472).",
        "tip_zh": "始于1395年！位于医院地下的古老葡萄酒酒窖，保存着酿造于1472年（全球最古老橡木桶熟成葡萄酒）的传奇酒桶！",
        "tip_fr": "Cave à vin historique de 1395 située sous l'hôpital abritant le plus vieux vin du monde en tonneau (1472) !",
        "de": "Historischer Weinkeller von 1395 unter dem Spital mit dem ältesten Fasswein der Welt aus dem Jahr 1472!"
    },
    "st_31": {
        "tip_en": "Walk down this romantic cobblestone quay lined with half-timbered houses and willow trees along the Ill river.",
        "tip_ja": "イル川沿いのロマンチックな石畳の遊歩道。柳の木と木造家屋、水面に映る景色を眺めながらの夕方散策がおすすめ。",
        "tip_es": "Pasea por este romántico muelle empedrado bordeado de casas de madera y sauces a lo largo del río Ill.",
        "tip_zh": "沿伊尔河畔漫步于鹅卵石步道Quai Bateliers。垂柳依依、倒影涟涟，非常适合傍晚清静散步。",
        "tip_fr": "Flânez le long de ce quai pavé piétonnier bordé de magnifiques maisons à colombages et de saules pleureurs.",
        "de": "Romantisches Flussufer an der Ill mit Kopfsteinpflaster, Weidenbäumen und bunten Fachwerkhäusern."
    },
    "st_32": {
        "tip_en": "Explore the UNESCO World Heritage historic center entirely on foot—cars are banned on most bridges leading into the island.",
        "tip_ja": "旧市街全体がユネスコ世界遺産の島（Grande Île）。車両進入禁止の橋が多く、徒歩でのんびり散策するのが一番快適です。",
        "tip_es": "Explora el centro histórico UNESCO a pie; la mayoría de los puentes de acceso son peatonales.",
        "tip_zh": "整座老城岛屿均属于联合国教科文组织世界遗产。多数进入岛屿的桥梁均禁止汽车通行，最宜步行探秘。",
        "tip_fr": "Explorez à pied ce centre historique classé UNESCO entouré par les bras de la rivière Ill.",
        "de": "Erkunden Sie das gesamte UNESCO-Altstadtzentrum entspannt zu Fuß – weite Teile sind Fußgängerzone."
    },
    "st_33": {
        "tip_en": "Features tropical palm greenhouses and a quiet rose garden established in 1619 next to the University of Strasbourg.",
        "tip_ja": "1619年に創設されたフランスで2番目に古い植物園。ストラスブール大学敷地内にあり、巨木や温室が無料で楽しめます。",
        "tip_es": "Jardín botánico histórico de 1619 con grandes invernaderos tropicales e ingreso gratuito en el campus universitario.",
        "tip_zh": "始于1619年、全法第二古老的大学植物园。拥有庞大的热带巨型温室与玫瑰园，免费向公众开放。",
        "tip_fr": "Jardin botanique historique de 1619 abritant de grandes serres tropicales et des arbres remarquables en accès libre.",
        "de": "Historischer Botanischer Garten von 1619 auf dem Universitätsgelände mit tropischen Gewächshäusern (Eintritt frei)."
    },
    "st_34": {
        "tip_en": "Buy fresh local Munster cheese, Alsatian pretzels, and seasonal tartes Flambées from local producers inside the covered glass hall.",
        "tip_ja": "中央駅近くの屋内市場。名物のウォッシュチーズ『ミュンスター（Munster）』や地元産の新鮮な野菜・シャルキュトリーが買えます。",
        "tip_es": "Mercado cubierto donde comprar queso Munster tradicional, embutidos y productos frescos de Alsacia.",
        "tip_zh": "位于中央火车站附近的全天候室内集市。可购买到著名的阿尔萨斯洗泡洗干酪Munster及新鲜熟食。",
        "tip_fr": "Marché couvert gourmand pour acheter du fromage Munster AOP, des charcuteries alsaciennes et produits frais.",
        "de": "Überdachter Feinkostmarkt mit frischem Munster-Käse, elsässischer Wurst und regionalen Spezialitäten."
    },
    "st_35": {
        "tip_en": "The largest square in the Petite France district lined with outdoor cafes, street musicians, and floral timber houses.",
        "tip_ja": "プティット・フランスの中心広場。運河沿いのカフェテラス席でストリートミュージシャンの演奏を聴きながらコーヒーを。",
        "tip_es": "La plaza más animada de la Petite France repleta de terrazas de café, músicos callejeros y casas de entramado de madera.",
        "tip_zh": "Petite France 区域最热闹的核心广场。坐在运河畔露台咖啡座聆听街头琴师演奏，氛围极其浪漫。",
        "tip_fr": "La place la plus animée de la Petite France bordée de terrasses de café et de maisons à colombages fleurie.",
        "de": "Der schönste Platz in Petite France mit bunten Fachwerkhäusern, Straßencafés und Straßenmusikern."
    },
    "st_36": {
        "tip_en": "View the impressive modern architecture of the Council of Europe and the European Court of Human Rights from the canal banks.",
        "tip_ja": "イル川沿いに立つ欧州評議会や欧州人権裁判所のガラス張りの近未来建築群。運河の遊歩道からの散策や写真撮影がおすすめ。",
        "tip_es": "Arquitectura moderna del Consejo de Europa y el Tribunal Europeo de Derechos Humanos a lo largo del canal.",
        "tip_zh": "沿着运河漫步，观赏欧洲委员会与欧洲人权法院前卫现代的玻璃椭圆主体建筑物群。",
        "tip_fr": "Découvrez l'architecture contemporaine du Conseil de l'Europe et de la Cour européenne des droits de l'homme le long du canal.",
        "de": "Moderne Architektur des Europarates und des Europäischen Gerichtshofs für Menschenrechte am Kanalufer."
    },
    "st_37": {
        "tip_en": "Modern shopping mall built inside historical 19th-century military arsenal buildings near Place de l'Étoile.",
        "tip_ja": "19世紀の軍事兵器庫をリノベーションしたモダンなショッピングモール。ファッション、レストラン、映画館が完備。",
        "tip_es": "Centro comercial moderno construido dentro de los edificios de un antiguo arsenal militar del siglo XIX.",
        "tip_zh": "由19世纪军火库旧址改建而成的现代综合购物中心。集时尚品牌、餐饮与影院于一体。",
        "tip_fr": "Centre commercial moderne installé dans les bâtiments restaurés d'un ancien arsenal militaire du XIXe siècle.",
        "de": "Modernes Einkaufszentrum in den restaurierten Backsteinbauten eines ehemaligen Militärarsenals des 19. Jahrhunderts."
    },
    "st_38": {
        "tip_en": "Walk past the 14th-century Gothic tower (Tour du Bourreau) on Rue du Fossé-des-Tanneurs, part of Strasbourg's medieval wall defenses.",
        "tip_ja": "旧市街に残る14世紀のゴシック様式の石造タワー（処刑人の塔）。かつてのストラスブール中世城壁の歴史を物語るスポット。",
        "tip_es": "Torre de piedra gótica del siglo XIV que formaba parte de las murallas medievales defensivas de Estrasburgo.",
        "tip_zh": "位于老城旧墙处的14世纪哥特式石造防御塔楼（Tour du Bourreau）。保留着中世纪城墙遗风。",
        "tip_fr": "Tour gothique en pierre du XIVe siècle, vestige des anciennes fortifications médiévales de la ville.",
        "de": "Gotischer Turm aus dem 14. Jahrhundert, Teil der ehemaligen mittelalterlichen Stadtbefestigung."
    },
    "st_39": {
        "tip_en": "Discover 18th-century noble salons, crystal chandeliers, and French decorative art inside the former residence of Count de Gayot.",
        "tip_ja": "18世紀の貴族館を利用したインテリア博物館。クリスタルシャンデリアと貴族のサロン文化が保存されています。",
        "tip_es": "Exhibe salones nobles del siglo XVIII y artes decorativas en la antigua residencia del Conde de Gayot.",
        "tip_zh": "设于18世纪Gayot伯爵府邸内。呈现了18世纪贵族豪华沙龙文化、水晶吊灯与法国古典装饰艺术。",
        "tip_fr": "Magnifique hôtel particulier du XVIIIe siècle présentant des salons d'époque raffinés et des arts décoratifs.",
        "de": "Prachtvolles Stadtpalais des 18. Jahrhunderts mit historischen Salons und edlem Kunsthandwerk."
    },
    "st_40": {
        "tip_en": "Buy fresh produce, Alsatian cheeses, and local wines from regional farmers every Wednesday and Friday morning.",
        "tip_ja": "毎週水曜・金曜の朝に開催されるローカル農家マーケット。採れたてのアルザス産チーズやワイン、野菜が並び賑やかです。",
        "tip_es": "Mercado al aire libre los miércoles y viernes por la mañana con productores locales de queso y vino.",
        "tip_zh": "每周三、五早晨开放的本地农夫集市。可采买到新鲜阿尔萨ス农家自产干酪、水果与风味葡萄酒。",
        "tip_fr": "Marché de producteurs locaux les mercredis et vendredis matin : fromages frais, charcuterie et vins d'Alsace.",
        "de": "Beliebter Wochenmarkt mittwochs und freitags morgens mit frischen regionalen Produkten und Käse."
    },
    "st_41": {
        "tip_en": "View the massive red sandstone neo-Gothic church built during the German Imperial period (1897) at the tip of the Ill river junction.",
        "tip_ja": "イル川の合流点にそびえる赤砂岩のツインタワー大聖堂（1897年建造）。川面に映る教会堂の姿が美しいカメラアングル。",
        "tip_es": "Iglesia neogótica de piedra arenisca roja construida en 1897 en el punto donde se divide el río Ill.",
        "tip_zh": "建于1897年德国帝国时代的红砂岩双塔新哥特式大教堂。矗立于伊尔河两支流交汇处，倒影极美。",
        "tip_fr": "Église néo-gothique spectaculaire en grès rose bâtie en 1897 à la pointe de l'île Sainte-Madeleine.",
        "de": "Imposante neugotische Kirche aus rotem Sandstein von 1897 an der Spitze der Flussinsel."
    },
    "st_42": {
        "tip_en": "Housed in a modern glass building by architect Adrien Fainsilber displaying contemporary French and international sculpture installations.",
        "tip_ja": "ガラス張りの現代美術館内にある彫刻展示スペース。屋外テラスからは水辺と旧市街の景色が広がります。",
        "tip_es": "Exposiciones de escultura contemporánea en un edificio de cristal con vistas al río Ill.",
        "tip_zh": "位于现代美术馆内部的当代雕塑特展区。临河玻璃墙可饱览伊尔河风光与雕塑作品的交融。",
        "tip_fr": "Espace d'expositions de sculptures contemporaines au cœur du bâtiment transparent du MAMCS.",
        "de": "Skulpturensammlung im modernen Glasbau des Museums für moderne Kunst an der Ill."
    },
    "st_43": {
        "tip_en": "Walk across this scenic 19th-century iron bridge linking the Historic Island with the German Imperial Quarter (Neustadt).",
        "tip_ja": "グラン・ディル（旧市街）とノイシュタット（ドイツ街区）を結ぶ19世紀の鉄橋。大聖堂を遠望する撮影スポット。",
        "tip_es": "Puente de hierro del siglo XIX que une la Isla Histórica con el Barrio Imperial Alemán (Neustadt).",
        "tip_zh": "连接历史大岛与德国帝国区（Neustadt）的19世纪铸铁名桥。在桥上可拍到大教堂与运河交融的远景。",
        "tip_fr": "Pont en fer du XIXe siècle reliant la Grande Île au quartier de la Neustadt.",
        "de": "Historische Eisenbrücke des 19. Jahrhunderts zwischen der Altstadt und der Neustadt."
    },
    "st_44": {
        "tip_en": "Quiet pedestrian cobblestone street behind the Cathedral lined with artisan workshops, antiquarian bookstores, and tea salons.",
        "tip_ja": "大聖堂の裏手に佇む静かな石畳の小道。古書店や伝統工芸ショップ、落ち着いた紅茶サロンが集まる穴場ストリート。",
        "tip_es": "Callejuela peatonal tranquila detrás de la catedral con librerías de antiguo y salones de té.",
        "tip_zh": "位于大教堂后方幽静的鹅卵石小巷。聚集着古旧书店、精致手工艺工坊与下午茶沙龙。",
        "tip_fr": "Charmante ruelle pavée paisible derrière la cathédrale bordée de bouquinistes et salons de thé.",
        "de": "Ruhige Gasse hinter dem Münster mit Antiquariaten, Kunsthandwerkern und gemütlichen Teesalons."
    },
    "st_45": {
        "tip_en": "Housed in an 18th-century townhouse exploring Alsatian Jewish heritage, ritual objects, and historical documents since medieval times.",
        "tip_ja": "中世からのアルザス・ユダヤ社会の歴史、伝統工芸品、儀式器具を展示した歴史的ミュージアム。",
        "tip_es": "Museo en un palacete del siglo XVIII sobre la historia y cultura judía de Alsacia desde la Edad Media.",
        "tip_zh": "设于18世纪府邸内。展示自中世纪以来阿尔萨斯犹太社群的历史文化、礼仪器具与珍贵文献。",
        "tip_fr": "Musée présentant le patrimoine, la culture et l'histoire de la communauté juive d'Alsace depuis le Moyen Âge.",
        "de": "Museum zur Geschichte und Kultur der jüdischen Gemeinde im Elsass vom Mittelalter bis zur Gegenwart."
    }
}

toulouse_tips = {
    "to_1": {
        "tip_en": "Visit Place du Capitole at sunset when the red terracotta brick facades glow pink (hence Toulouse's nickname 'La Ville Rose').",
        "tip_ja": "日没時にキャピトール広場へ！夕日が赤煉瓦のファサードをピンク色に染め上げる瞬間が『バラ色の街（La Ville Rose）』の由来を体感できる最高のひとときです。",
        "tip_es": "Visita la Place du Capitole al atardecer cuando los ladrillos de terracota se iluminan de rosa.",
        "tip_zh": "推荐黄昏前往市政厅Capitole广场！余晖将红陶砖墙染成一片绮丽的粉红色，完美演绎“粉红之城（La Ville Rose）”的浪漫名号。",
        "tip_fr": "Admirez la Place du Capitole au coucher du soleil quand les briques de terre cuite prennent leur teinte rose caractéristique.",
        "tip_de": "Besuchen Sie den Place du Capitole bei Sonnenuntergang, wenn die Ziegel im berühmten rosa Licht erstrahlen."
    },
    "to_2": {
        "tip_en": "The largest Romanesque church in Europe! Step inside to view the 11th-century marble reliefs and the tomb of Saint Saturnin in the choir.",
        "tip_ja": "ヨーロッパ最大規模のロマネスク大聖堂！11世紀の彫刻や聖サトゥルニヌスの墓所がある内陣（有料）の見学価値が高く、サンティアゴ巡礼路の重要拠点です。",
        "tip_es": "La iglesia románica más grande de Europa. Entra para ver los relieves de mármol del siglo XI.",
        "tip_zh": "全欧洲规模最大的罗曼式大教堂！入内参观11世纪大理石大浮雕与圣萨图尔宁总主教陵墓。圣雅各朝圣之路重要节点。",
        "tip_fr": "La plus grande église romane d'Europe ! Admirez les reliefs en marbre du XIe siècle et le chœur sculpté.",
        "tip_de": "Größte romanische Kirche Europas! Der Innenraum mit den Marmorreliefs des 11. Jahrhunderts ist überwältigend."
    },
    "to_3": {
        "tip_en": "Stand beneath the famous 28-meter high 'Palm Tree' (Palmier) column—a single stone pillar branching out into 22 vaulted rib arches.",
        "tip_ja": "聖堂中央にある高さ28mの『ヤシの木（Palmier）』柱を真下から見上げてください！1本の石柱から22本の天井アーチが放射状に広がる奇跡のゴシック建築。",
        "tip_es": "Contempla la famosa columna 'Palmera' de 28 metros de altura de la que nacen 22 arcos góticos.",
        "tip_zh": "站在教堂内鼎鼎大名的28米高“棕榈树”（Palmier）石柱正下方仰望！单根石柱向上散射出22道哥特拱顶纹路，堪称建筑奇迹。",
        "tip_fr": "Admirez le célèbre 'Palmier' du Jacobins : une colonne unique de 28m soutenant 22 nervures de voûte !",
        "tip_de": "Staunen Sie unter der berühmten 28-Meter-Säule 'Palme des Jacobins', von der 22 Gewölberippen abzweigen."
    },
    "to_4": {
        "tip_en": "Housed in a 16th-century Renaissance mansion featuring a magnificent 26-meter tower courtyard. Free entrance to walk the courtyard.",
        "tip_ja": "16世紀のルネサンス富豪の館。高さ26mの塔と彫刻が並ぶ中庭は入場無料で自由に見学・撮影が可能です！",
        "tip_es": "Palacete renacentista del siglo XVI con un gran patio y torre de 26 metros. Acceso libre al patio.",
        "tip_zh": "建于16世纪的富商黄金时代文艺复兴府邸。拥有一座26米高的雕花塔楼与精致中庭，中庭区域免费开放观赏。",
        "tip_fr": "Magnifique hôtel particulier de la Renaissance avec sa cour intérieure et sa tour de 26 mètres en accès libre.",
        "tip_de": "Prachtvolles Renaissance-Stadtpalais des 16. Jahrhunderts. Der wunderschöne Innenhof mit dem 26m Turm ist frei zugänglich."
    },
    "to_5": {
        "tip_en": "Walk across Toulouse's oldest stone bridge (1632) for gorgeous views of the Hôtel-Dieu dome reflected in the Garonne river.",
        "tip_ja": "1632年完成のトゥールーズ最古の石橋。橋の上から眺めるガロンヌ川と、対岸のオテル・デュー（Hôtel-Dieu）のドーム屋根の景観が絵画のよう。",
        "tip_es": "El puente de piedra más antiguo de Toulouse (1632) con magníficas vistas del río Garona y la cúpula del Hôtel-Dieu.",
        "tip_zh": "建于1632年トゥールーズ最古老的石拱桥。站在桥上远眺加龙河及对岸Hôtel-Dieu圆顶构成的水天名画。",
        "tip_fr": "Le plus ancien pont de Toulouse (1632) offrant un panorama splendide sur la Garonne et el dôme de l'Hôtel-Dieu.",
        "tip_de": "Die älteste Steinbrücke der Stadt (1632) bietet fantastische Fotomotive der Garonne und des Hôtel-Dieu."
    },
    "to_6": {
        "tip_en": "Stroll down the riverbank promenade on Quai de la Daurade at dusk to join locals sipping wine and watching sunset over Pont Neuf.",
        "tip_ja": "夕暮れ時にドラード河岸プロムナードへ！地元の若者がワインを持ち寄ってポン・ヌフ橋に沈む夕日を眺めるローカルの憩いの場です。",
        "tip_es": "Pasea por el muelle al atardecer para unirte a los locales que disfrutan de la puesta de sol sobre el río.",
        "tip_zh": "傍晚漫步于Daurade河岸绿道！加入当地人的行列，坐在水岸草坪上小酌葡萄酒，观赏落日映照新桥（Pont Neuf）。",
        "tip_fr": "Rejoignez les toulousains sur les quais de la Daurade pour admirer el coucher du soleil sur la Garonne.",
        "tip_de": "Der Treffpunkt der Einheimischen am Flussufer der Daurade zum Sonnenuntergang über dem Pont Neuf."
    },
    "to_7": {
        "tip_en": "Visit the 18th-century Grand Salon inside Hôtel de Ville featuring vast historic oil paintings detailing Toulouse's history.",
        "tip_ja": "市庁舎（Capitole）の2階にある『Henri IVの間（Salle des Illustres）』は豪華絢爛なフレスコ画と金の装飾で埋め尽くされ、入場無料で見学できます！",
        "tip_es": "Visita la opulenta Salle des Illustres dentro del Ayuntamiento con enormes pinturas históricas (entrada libre).",
        "tip_zh": "步入Capitole市政厅二楼的名人厅（Salle des Illustres）！满满一整厅精美绝伦的壁画与金箔雕刻，完全免费对外开放！",
        "tip_fr": "Visitez gratuitement la somptueuse Salle des Illustres au premier étage du Capitole avec ses peintures monumentales.",
        "tip_de": "Besichtigen Sie kostenlos den prunkvollen Salle des Illustres im Capitole mit seinen riesigen Historiengemälden."
    },
    "to_8": {
        "tip_en": "UNESCO World Heritage canal shaded by centuries-old plane trees. Rent a bicycle to ride down the paved towpath towards Carcassonne.",
        "tip_ja": "ユネスコ世界遺産ミディ運河。プラタナスの木陰が続く平坦な運河沿いサイクリングロード（ポプラの並木道）でのサイクリングが爽快！",
        "tip_es": "Canal Patrimonio de la Humanidad UNESCO. Alquila una bicicleta para recorrer el camino a la sombra de los plátanos.",
        "tip_zh": "联合国教科文组织世界遗产。租一辆自行车沿着郁郁葱葱的法桐树荫运河水道骑行，一路风景如画。",
        "tip_fr": "Canal classé UNESCO ombragé par des platanes centenaires. Louez un vélo pour longer la voie verte aménagée.",
        "tip_de": "UNESCO-Welterbe-Kanal unter alten Platanen. Mieten Sie ein Fahrrad für eine Tour auf dem Treidelpfad."
    },
    "to_9": {
        "tip_en": "Toulouse's oldest cathedral showcasing a unique mix of 2 distinct Gothic architectures fused together with an off-center nave.",
        "tip_ja": "異なる2つの建築時期の聖堂が斜めに連結されたユニークな構造の大聖堂。内部の精巧なタペストリーやオルガンが見どころ。",
        "tip_es": "Catedral única que combina dos estilos góticos diferentes unidos en un ángulo asimétrico.",
        "tip_zh": "融合了两个不同建造时期哥特建筑风格的独特大教堂，中殿呈现神奇的非对称结构。内有珍贵织锦。",
        "tip_fr": "Cathédrale surprenante fusionnant deux architectures gothiques différentes dans un plan asymétrique.",
        "tip_de": "Faszinierende Kathedrale, die zwei verschiedene gotische Baustile in einem asymmetrischen Grundriss vereint."
    },
    "to_10": {
        "tip_en": "Housed in a 14th-century Augustinian convent featuring a peaceful Gothic cloister garden and a world-class collection of medieval gargoyles.",
        "tip_ja": "14世紀のアウグスティノ修道院を利用した美術館。ゴシック様式の美しい回廊庭園と、中世の石彫・ロマネスク様式の柱頭彫刻が見事。",
        "tip_es": "Museo en un convento del siglo XIV con un claustro gótico tranquilo y esculturas románicas.",
        "tip_zh": "设于14世纪奥古斯丁修道院内。拥有一座极佳的哥特拱廊花园与全法顶尖的中世纪石雕柱头珍藏。",
        "tip_fr": "Installé dans un ancien couvent du XIVe siècle doté d'un magnifique cloître gothique et de sculptures romanes.",
        "de": "Museum in einem ehemaligen Augustinerkloster des 14. Jahrhunderts mit einem wunderschönen gotischen Kreuzgang."
    },
    "to_11": {
        "tip_en": "View the iconic 18th-century dome of this former hospital from Pont Saint-Pierre, illuminated brightly over the Garonne river at night.",
        "tip_ja": "サン・ピエール橋からの夜景がロマンチック！ガロンヌ川に映る18世紀のオテル・デュー（旧病院）の巨大ドームライトアップが見事です。",
        "tip_es": "La gran cúpula del siglo XVIII iluminada sobre el río Garona tomada desde el puente Saint-Pierre es una postal nocturna.",
        "tip_zh": "位于圣彼得桥头的18世纪皇家总医院。夜幕降临，巨大的铜绿圆顶在加龙河倒影的衬托下璀璨夺目。",
        "tip_fr": "La cúpule illuminée du XVIIIe siècle se reflétant dans la Garonne depuis le Pont Saint-Pierre est féerique la nuit.",
        "de": "Die beleuchtete Kuppel aus dem 18. Jahrhundert spiegelt sich nachts wunderschön in der Garonne."
    },
    "to_12": {
        "tip_en": "Housed in the magnificent Renaissance Hôtel d'Assézat displaying a private collection of Impressionist masterpieces (Monet, Degas, Bonnard).",
        "tip_ja": "アセザ館（Hôtel d'Assézat）内部。モネ、ドガ、ボナール、カナレットなど、個人収集家ベンベルク氏の近世絵画の傑作コレクション。",
        "tip_es": "Ubicado en el palacio Hôtel d'Assézat con pinturas impresionistas de Monet, Degas y Bonnard.",
        "tip_zh": "位于Hôtel d'Assézat府邸内。私藏有莫奈、德加、博纳尔及卡纳莱托等大师的珍贵印象派与古典油画巨作。",
        "tip_fr": "Musée d'exception dans l'Hôtel d'Assézat abritant des chefs-d'œuvre de Monet, Degas et Tintoret.",
        "de": "Bemberg-Stiftung im Hôtel d'Assézat mit Meisterwerken von Monet, Degas und altmeisterlichen Gemälden."
    },
    "to_13": {
        "tip_en": "Modern and contemporary art museum housed in Toulouse's historic 1820 red-brick slaughterhouses near the river with giant outdoor installations.",
        "tip_ja": "1820年建設の旧精肉屠殺場（赤レンガ建築）を改装した現代美術館。ピカソの巨大舞台幕作品や屋外のグラフィティが見どころ。",
        "tip_es": "Museo de arte contemporáneo en el antiguo matadero de ladrillo rojo de 1820 con grandes instalaciones.",
        "tip_zh": "利用1820年历史红砖屠宰场改建的当代美术馆。拥有毕加索巨幅舞台幕布画及充满张力的户外装置。",
        "tip_fr": "Musée d'art moderne installé dans les anciens abattoirs en brique rouge de 1820 sur la rive gauche.",
        "de": "Museum für moderne Kunst im historischen Backstein-Schlachthof von 1820 mit Werken von Picasso."
    },
    "to_14": {
        "tip_en": "Located on Place Saint-Sernin featuring 1,000+ Roman marble statues, mosaics, and bust sculptures excavated in Southwestern France.",
        "tip_ja": "サン・セルナン大聖堂横。フランス南西部で発掘された古代ローマ時代のブロンズ像、大理石彫刻、モザイク画を集めた考古学博物館。",
        "tip_es": "Museo arqueológico junto a Saint-Sernin con más de 1.000 estatuas y mosaicos romanos.",
        "tip_zh": "位于Saint-Sernin大教堂旁。展出1000余件在法国西南地区发掘出的古罗马大理石雕像、胸像与精美地砖马赛克。",
        "tip_fr": "Musée d'archéologie antique présentant une collection exceptionnelle de scuptures et mosaïques romaines.",
        "de": "Archäologisches Museum beim Saint-Sernin mit über 1.000 römischen Marmorstatuen und Mosaiken."
    },
    "to_15": {
        "tip_en": "France's 2nd largest natural history museum featuring giant dinosaur skeletons, a botanical wall, and hands-on science labs for kids.",
        "tip_ja": "フランスで2番目に大きい自然史博物館！恐竜の全身化石標本や垂直壁面緑化庭園があり、ファミリーで楽しく学べる体験展示が豊富。",
        "tip_es": "El segundo museo de historia natural más grande de Francia con esqueletos de dinosaurios y laboratorios interactivos.",
        "tip_zh": "全法国第二大自然历史博物馆！内设巨型恐龙骨架化石、植物绿墙与极具趣味的亲子互动科学实验室。",
        "tip_fr": "Le 2e plus grand muséum d'histoire naturelle de France avec squelettes de dinosaures et serres superbes.",
        "de": "Zweitgrößtes Naturhistorisches Museum Frankreichs mit Dinosaurier-Skeletten und Mitmach-Laboren."
    },
    "to_16": {
        "tip_en": "Housed in a 17th-century Jesuit college displaying decorative arts, timepieces, clocks, and medieval gold artifacts.",
        "tip_ja": "17世紀の旧イエズス会学院。古代の時計コレクション、中世の金銀細工、伝統工芸品が歴史的建物内に並びます。",
        "tip_es": "Ubicado en un colegio jesuita del siglo XVII con colecciones de relojes antiguos y objetos de oro medievales.",
        "tip_zh": "设于17世纪耶稣会学院旧址内。陈列有珍贵的古董计时钟表珍藏、中世纪金银器与精细手工艺品。",
        "tip_fr": "Musée des arts précieux et de l'horlogerie installé dans un ancien collège jésuite du XVIIe siècle.",
        "de": "Museum für Kunsthandwerk und historische Uhren in einem Jesuitenkolleg des 17. Jahrhunderts."
    },
    "to_17": {
        "tip_en": "Walk inside actual legendary aircraft including 2 Concordes, the Super Guppy cargo plane, and the Airbus A380 near the airport!",
        "tip_ja": "エアバス工場の隣。音速旅客機コンコルド（2機）、大型輸送機スーパーグッピー、巨大旅客機A380の実機内部に入って見学できます！",
        "tip_es": "Camina dentro de aviones legendarios reales como 2 Concorde, el Super Guppy y el Airbus A380.",
        "tip_zh": "位于空中客车工厂旁！可直接登入2架传奇协和号（Concorde）超音速客机、超级彩虹鱼（Super Guppy）与A380实机机舱内参观！",
        "tip_fr": "Montez à bord d'avions légendaires : 2 Concorde, el Super Guppy et le géant Airbus A380 !",
        "de": "Gehen Sie an Bord historischer Flugzeuge: 2 originale Concorde, der Super Guppy und der Airbus A380."
    },
    "to_18": {
        "tip_en": "Book weeks in advance for a guided bus tour inside the massive Airbus assembly plant to view A350 passenger jets being built!",
        "tip_ja": "エアバス最新旅客機A350の最終組み立て工場の内部を見学できる人気ツアー。数ヶ月前からの事前予約が必須です！",
        "tip_es": "Reserva con semanas de antelación el tour por la fábrica de ensamblaje final del Airbus A350.",
        "tip_zh": "近距离观摩空中客车A350客机最终组装生产线的独家导览。门票必须提前数周在官网预订！",
        "tip_fr": "Réservez des semaines à l'avance pour visiter la chaîne d'assemblage finale de l'Airbus A350 !",
        "de": "Unbedingt Wochen im Voraus buchen: Führung durch die Montagehallen des Airbus A350."
    },
    "to_19": {
        "tip_en": "Toulouse's primary gourmet market! Head to the 1st floor rooftop restaurants at 12:00 PM for fresh duck confit, oysters, and local wines.",
        "tip_ja": "食の都トゥールーズの胃袋！2階にあるレストラン街で、地元産の鴨肉コンフィ、新鮮な生牡蠣、赤ワインのランチが絶品です（12時開店）。",
        "tip_es": "¡El mercado gourmet principal! Sube a la primera planta a las 12:00 para comer confit de pato fresco y ostras.",
        "tip_zh": "图卢兹第一美食大集市！中午12点直奔2楼露天市场餐厅区，享受新鲜鸭腿油脂包（Confit de canard）与鲜生蚝。",
        "tip_fr": "Le marché gourmand de référence ! Montez au 1er étage dès 12h pour déjeuner dans les bistros de marché.",
        "de": "Der Schlemmer-Markt von Toulouse! Im 1. Stock ab 12 Uhr frisches Enten-Confit und Meeresfrüchte genießen."
    },
    "to_20": {
        "tip_en": "Historic 1843 Neo-Baroque cafe on Place du Capitole with golden chandeliers and painted ceilings. Great spot for morning coffee & croissant.",
        "tip_ja": "キャピトール広場に面する1843年創業の高級カフェ。金箔の天井画を見上げながら味わうモーニングコーヒーとクロワッサンが優雅。",
        "tip_es": "Café neobarroco histórico de 1843 en Place du Capitole con techos pintados y lámparas de araña.",
        "tip_zh": "始于1843年、位于Capitole广场前的新巴洛克风华丽咖啡馆。在金箔彩绘天顶下享用早餐咖啡与羊角面包极具仪式感。",
        "tip_fr": "Café historique de 1843 sur la Place du Capitole avec ses plafonds dorés peints d'époque.",
        "de": "Historisches Neobarock-Café von 1843 am Place du Capitole mit prächtigen Deckenmalereien."
    },
    "to_21": {
        "tip_en": "The absolute temple for authentic Cassoulet (slow-cooked white bean stew with duck confit and Toulouse sausage) in an earthenware pot.",
        "tip_ja": "フランス南西部の郷土料理『カスレ（白インゲン豆と鴨肉、ソーセージの土鍋煮込み）』の名店！熱々の陶器鉢で提供される伝統の味。",
        "tip_es": "El templo del Cassoulet tradicional cocinado a fuego lento con judías blancas, confit de pato y salchicha.",
        "tip_zh": "品尝最正宗土锅慢炖“卡苏莱”（Cassoulet——鸭腿、图卢兹香肠与白油豆土锅炖菜）的终极名店！",
        "tip_fr": "Le temple du véritable Cassoulet toulousain mijoté au four dans sa cassole en terre cuite !",
        "de": "Das Mekka für ein authentisches Cassoulet (Bohneneintopf mit Enten-Confit und Toulouse-Wurst)."
    },
    "to_22": {
        "tip_en": "Located inside a converted barge moored on Canal du Midi selling violet liqueur, violet candies, and violet perfumes.",
        "tip_ja": "ミディ運河に浮かぶ赤い船上ショップ。『スミレの街トゥールーズ』名物のスミレのキャンディ、リキュール、香水、ジャムが揃います。",
        "tip_es": "Tienda en una barcaza en el Canal du Midi especializada en productos de violeta (caramelos, licor y perfumes).",
        "tip_zh": "停泊在米迪运河上的红色风情船上小店。售卖图卢兹特产紫罗兰软糖、紫罗兰利口酒、香水与果酱。",
        "tip_fr": "Boutique originale installée sur una péniche sur el Canal du Midi dédiée aux produits à la violette.",
        "de": "Origineller Laden auf einem Schiff am Canal du Midi mit Veilchen-Spezialitäten (Likör, Bonbons)."
    },
    "to_23": {
        "tip_en": "Covered neighborhood market surrounded by lively wine bars and tapas bistros in the charming Carmes district.",
        "tip_ja": "カルム地区の活気ある屋内市場。周りには地元客で賑わうワインバーやタパスビストロが集まり、夜のハシゴ酒に最適。",
        "tip_es": "Mercado cubierto rodeado de bares de vinos y tapas vibrantes en el barrio de Carmes.",
        "tip_zh": "位于卡尔姆（Carmes）街区的传统室内集市。周边围绕着无数烟火气十足的葡萄酒酒吧与小吃馆。",
        "tip_fr": "Marché couvert chaleureux entouré de petits bistros et bars à vins très animés à l'apéro.",
        "de": "Überdachter Markt im beliebten Carmes-Viertel, umgeben von gemütlichen Weinbars und Tapas-Bistros."
    },
    "to_24": {
        "tip_en": "Famous for 'Le Pavé du Capitole' pralines and delicate violet-flavored macarons handmade since 1816.",
        "tip_ja": "1816年創業の老舗洋菓子店。石畳を模したチョコ『Pavé du Capitole』やスミレ風影のマカロンがお土産に大人気。",
        "tip_es": "Pâtisserie famosa desde 1816 por sus chocolates 'Le Pavé du Capitole' y macarons de violeta.",
        "tip_zh": "始于1816年的名名甜品老铺。必买波尔多石头巧克力“Pavé du Capitole”与紫罗兰风味马卡龙。",
        "tip_fr": "Pâtisserie historique depuis 1816 célèbre pour le Pavé du Capitole et ses macarons à la violette.",
        "de": "Traditionelle Konditorei von 1816, bekannt für Schokoladen-Spezialitäten und Veilchen-Macarons."
    },
    "to_25": {
        "tip_en": "Visit the Fronton wine region (30 min north) famous for its unique dark, spicy Négrette grape wines.",
        "tip_ja": "トゥールーズ北部のフロントンワイン産地。この地域でしか栽培されない希少ブドウ品種『ネグレット（Négrette）』の黒スミレ香る赤ワインを試飲。",
        "tip_es": "Bodegas de la región de Fronton a 30 min al norte, famosas por su uva única Négrette.",
        "tip_zh": "探访图卢兹北部30分钟车程的Fronton红酒产区。品尝当地特有的黑色辛香葡萄品种Négrette酿造的佳酿。",
        "tip_fr": "Découvrez le vignoble de Fronton à 30 min de Toulouse et son cépage unique au monde : la Négrette.",
        "de": "Weingüter der Region Fronton, bekannt für die weltweit einzigartige Rebsorte Négrette."
    },
    "to_26": {
        "tip_en": "The prime spot for sunset watching over the Garonne river with Pont Neuf illuminated in the background.",
        "tip_ja": "ガロンヌ川沿いの芝生広場。ポン・ヌフ橋と対岸のオテル・デューが夕陽に染まる景色を眺めるトゥールーズ一番の夕暮れスポット。",
        "tip_es": "El lugar ideal para ver la puesta de sol sobre el río Garona con el Pont Neuf de fondo.",
        "tip_zh": "加龙河畔最著名的落日观景阶梯草坪。观赏夕阳斜照新桥与对面Hôtel-Dieu拱顶的最佳第一排视角。",
        "tip_fr": "Le spot préféré des toulousains pour regarder el coucher du soleil sur la Garonne.",
        "de": "Der beste Treffpunkt am Flussufer für fantastische Sonnenuntergänge über der Garonne."
    },
    "to_27": {
        "tip_en": "Wander the narrow cobblestone streets lined with red-brick Renaissance townhouses, antique shops, and hidden courtyards.",
        "tip_ja": "赤煉瓦のルネサンス調の館、アンティークショップ、隠れたカフェが点在するトレンディな旧市街カルム地区の散策。",
        "tip_es": "Barrio de calles estrechas con mansiones de ladrillo rojo, tiendas de antigüedades y patios escondidos.",
        "tip_zh": "漫步在由红砖古建筑、古董精品店与隐秘咖啡中庭构成的Carmes古老街区，氛围极其优雅浪漫。",
        "tip_fr": "Quartier historique aux ruelles pavées bordées d'hôtels particuliers en brique rose et de boutiques antiquaires.",
        "de": "Malerisches historisches Viertel mit engen Gassen, Backstein-Palais und gemütlichen Antiquariaten."
    },
    "to_28": {
        "tip_en": "The historic junction where the Canal du Midi, Canal de Brienne, and Garonne river meet marked by marble bas-reliefs.",
        "tip_ja": "ミディ運河、ブリエンヌ運河、ガロンヌ川が交差する歴史的な水上交通の要衝。大理石の彫刻レリーフが見事。",
        "tip_es": "La unión histórica del Canal du Midi, el Canal de Brienne y el río Garona con bajorrelieves de mármol.",
        "tip_zh": "米迪运河、布里埃纳运河与加龙河三大水域交汇的历史水运枢纽。墙面上雕刻有大理石浮雕水神像。",
        "tip_fr": "Le port d'embouchure historique où se rejoignent el Canal du Midi et el Canal de Brienne.",
        "de": "Historischer Knotenpunkt, an dem der Canal du Midi und der Canal de Brienne aufeinandertreffen."
    },
    "to_29": {
        "tip_en": "Charming tree-shaded square surrounded by open-air cafes, restaurants, and a historic fountain in the city center.",
        "tip_ja": "木陰が涼しいトゥールーズ中心部の噴水広場。テラス席でワインやコーヒーを味わいながら休むのに最適。",
        "tip_es": "Encantadora plaza sombreada por árboles rodeada de terrazas de cafeterías y una fuente histórica.",
        "tip_zh": "市中心被林荫环绕的喷泉小广场。四周分布着露天咖啡馆与西餐厅，适合午后歇息。",
        "tip_fr": "Jolie place ombragée au cœur de la ville bordée de terrasses de café très prisées aux beaux jours.",
        "de": "Ein schattiger kleiner Platz im Stadtzentrum, umgeben von gemütlichen Straßencafés."
    },
    "to_30": {
        "tip_en": "Authentic Japanese tea garden created inside Compans-Caffarelli park featuring a red bridge, koi pond, and Zen pavilion (Free entry!).",
        "tip_ja": "コンパン＝カファレリ公園内にある本格的な日本庭園（入場無料）！赤い太鼓橋、錦鯉の泳ぐ池、茶室があり静寂な癒やし空間。",
        "tip_es": "Auténtico jardín japonés con puente rojo, estanque con peces koi y pabellón zen (¡Entrada gratuita!).",
        "tip_zh": "设于Compans-Caffarelli公园内的正统日式庭园（完全免费开放）！拥有红色拱桥、锦鲤池与禅意茶室。",
        "tip_fr": "Authentique jardin japonais (gratuit !) au sein du parc avec son pont rouge, son étang à carpes koi et son pavillon de thé.",
        "de": "Authentischer japanischer Garten mit roter Brücke, Koi-Teich und Teehaus (Eintritt frei!)."
    },
    "to_31": {
        "tip_en": "Board a river cruise from Quai de la Daurade to pass through historic locks and under Pont Neuf bridge.",
        "tip_ja": "ドラード河岸から出航するリバークルーズ船。ガロンヌ川とミディ運河の水門を潜り抜けながらトゥールーズの街並みを鑑賞。",
        "tip_es": "Crucero fluvial desde el muelle de la Daurade navegando bajo el Pont Neuf y por las esclusas.",
        "tip_zh": "从Daurade码头登船的城市环游游船。穿过新桥（Pont Neuf）桥洞与历史水闸，欣赏水上倾城风光。",
        "tip_fr": "Embarquez pour una croisière fluviale commentée sur la Garonne et le Canal du Midi.",
        "tip_de": "Flusskreuzfahrt auf der Garonne und dem Canal du Midi mit Durchfahrt historischer Schleusen."
    },
    "to_32": {
        "tip_en": "Quiet 1.5km canal path shaded by giant plane trees connecting the Garonne river to the Port de l'Embouchure.",
        "tip_ja": "ガロンヌ川から続く長さ1.5kmの静かな運河。巨木のプラタナスが作るトンネルの下での散歩やサイクリングが快適。",
        "tip_es": "Tranquilo paseo de 1.5 km a la sombra de los plátanos que conecta el río con el canal.",
        "tip_zh": "连接加龙河的1.5公里幽静运河水道。巨大的法桐树冠交织成天然林荫隧道，散步骑行极佳。",
        "tip_fr": "Canal ombragé paisible de 1,5 km reliant la Garonne au Port de l'Embouchure.",
        "de": "Ruhiger 1,5 km langer Kanalweg unter alten Platanen vom Fluss bis zum Hafen."
    },
    "to_33": {
        "tip_en": "Breathtaking medieval hilltop village built on a mountain peak ('Village in the Clouds') 1 hour north of Toulouse.",
        "tip_ja": "トゥールーズから車/バスで1時間。『雲の上の村』と呼ばれる山頂の中世石造り要塞村。石畳の坂道と霧に浮かぶ全景が幻想的！",
        "tip_es": "Espectacular pueblo medieval en la cima de una montaña ('El pueblo en las nubes') a 1 hora al norte.",
        "tip_zh": "耸立于山顶之上的中世纪石雕小镇，被称为“云端上的小镇”（距图卢兹1小时）。晨雾弥漫时宛如天宫要塞。",
        "tip_fr": "Village médiéval perché spectaculaire ('Village dans les nuages') situé à 1h au nord de Toulouse.",
        "de": "Spektakuläres mittelalterliches Bergdorf ('Dorf in den Wolken') 1 Std. nördlich von Toulouse."
    },
    "to_34": {
        "tip_en": "Interactive space theme park featuring a real Ariane 5 rocket model (53m high), Mir space station module, and IMAX 3D planetarium!",
        "tip_ja": "実物大の高さ53mのアリアン5ロケットや宇宙ステーションミール、月面歩行体験がある巨大宇宙テーマパーク！宇宙ファン必見。",
        "tip_es": "Parque temático del espacio con el cohete Ariane 5 a tamaño real (53m), la estación Mir y planetario IMAX.",
        "tip_zh": "大型宇宙航天主题乐园！拥有一根53米高的真实比例阿丽亚娜5号（Ariane 5）火箭模型、和平号空间站舱段与IMAX 3D天文馆。",
        "tip_fr": "Parc d'aventure spatiale avec la fusée Ariane 5 grandeur nature (53m), la station Mir et le grand starium IMAX 3D.",
        "de": "Riesiger Weltraum-Themenpark mit einer 53m hohen Ariane-5-Rakete, der Raumstation Mir und IMAX-Kino."
    },
    "to_35": {
        "tip_en": "Ride the 12-meter tall mechanical Minotaur ('Le Minotaure') giant robot walking outdoors—a breathtaking experience for all ages!",
        "tip_ja": "高さ12mの巨大なメカミノタウロス（機械の牛）に乗って屋外を動く驚愕の体験！映画のような巨大機械モンスターの動きは必見です。",
        "tip_es": "Sube a bordo del Minotauro mecánico gigante de 12 metros de altura que camina al aire libre.",
        "tip_zh": "乘坐高达12米的巨型蒸汽朋克机械米诺陶洛斯（Minotaur）巨牛在户外行走！震撼视效令人心跳加速。",
        "tip_fr": "Montez à bord du géant Minotaure mécanique de 12m de haut qui se déplace en extérieur !",
        "de": "Fahren Sie auf dem 12 Meter hohen mechanischen Riesenumotaurus mit – ein spektakuläres Erlebnis!"
    },
    "to_36": {
        "tip_en": "Museum located on the historic runway where legendary French aviators Jean Mermoz and Antoine de Saint-Exupéry launched airmail flights to South America.",
        "tip_ja": "『星の王子さま』の著者サン＝テグジュペリらが南米へ郵便飛行（エアロポスタル）へと飛び立った歴史的滑走路跡地の航空博物館。",
        "tip_es": "Museo en la pista histórica donde Saint-Exupéry despegaba en los vuelos de correo aéreo.",
        "tip_zh": "位于历史传奇跑道旧址。这里曾是《小王子》作者圣埃克苏佩里等飞行先驱执飞跨大西洋邮政航班的起飞点。",
        "tip_fr": "Musée situé sur la piste historique d'où décollaient Saint-Exupéry et Mermoz pour l'Aéropostale.",
        "de": "Museum auf der historischen Startbahn, von der Saint-Exupéry zu seinen legendären Postflügen abhob."
    },
    "to_37": {
        "tip_en": "Beautiful English landscape park connected by an elevated footbridge to Le Grand Rond garden with historic statues and fountains.",
        "tip_ja": "歩道橋で繋がった植物園とル・グラン・ロン公園。緑豊かな大樹の下でのピクニックや子供用遊具が充実した市民の憩い場。",
        "tip_es": "Parque inglés conectado por una pasarela elevada con el jardín Le Grand Rond con estatuas y fuentes.",
        "tip_zh": "由高架行人天桥相连的英式植物园与Le Grand Rond公园。林荫漫布，拥有古典喷泉雕塑与亲子儿童设施。",
        "tip_fr": "Ensemble de jardins à l'anglaise reliés par une passerelle suspendue au-dessus des boulevards.",
        "de": "Wunderschöner englischer Garten, über eine Fußgängerbrücke mit dem Park Le Grand Rond verbunden."
    },
    "to_38": {
        "tip_en": "Family amusement park 30 min west featuring roller coasters, water splash rides, and a farm with 150+ friendly animals.",
        "tip_ja": "トゥールーズから30分のファミリーテーマパーク。ローラーコースター、ウォータースライダー、ふれあい動物園を完備。",
        "tip_es": "Parque de atracciones familiar a 30 min con montañas rusas, atracciones acuáticas y granja de animales.",
        "tip_zh": "距图卢兹30分钟的家庭游乐园。拥有云霄飞车、激流勇进水上设施与饲养有150多只亲人小动物的农场。",
        "tip_fr": "Parc d'attractions familial à 30 min de Toulouse avec montagnes russes, jeux d'eau et ferme pédagogique.",
        "de": "Familien-Freizeitpark 30 Min. westlich mit Achterbahnen, Wasserattraktionen und einem Streichelzoo."
    },
    "to_39": {
        "tip_en": "Explore Europe's largest boxwood maze (6 km of paths) inside the grounds of the 18th-century Château de Merville.",
        "tip_ja": "18世紀のメルヴィル城敷地内にある、ヨーロッパ最大のツゲの木迷路（全長6km）！暗号解読ゲームをしながら楽しめます。",
        "tip_es": "El laberinto de boj más grande de Europa (6 km de senderos) en el Château de Merville.",
        "tip_zh": "位于18世纪Merville城堡领地内、全欧洲最大的黄杨木树墙迷宫（全长6公里步道）！支持解谜互动过关。",
        "tip_fr": "Le plus grand labyrinthe de buis d'Europe (6 km de allées) au Château de Merville avec jeux de piste.",
        "de": "Größter Buchsbaum-Labyrinth Europas (6 km Wege) im Park des Château de Merville."
    }
}

marseille_tips = {
    "ma_1": {
        "tip_en": "Take the Petit Train tourist bus from Vieux-Port to the basilica. The 360-degree view over Marseille, the sea, and Frioul islands from 'La Bonne Mère' is breathtaking.",
        "tip_ja": "旧港（Vieux-Port）から観光プチトランに乗って標高149mの黄金の聖母像へ。テラスからのマルセイユ市街と地中海の360度パノラマは絶対の必見！",
        "tip_es": "Toma el tren turístico Petit Train desde el Vieux-Port. La vista panorámica de 360 grados sobre el mar y las islas es imbatible.",
        "tip_zh": "在老港（Vieux-Port）搭乘观光小火车直达山顶黄金圣母像。从大教堂观景台俯瞰马赛全城与蔚蓝海岸的360度全景极具冲击力！",
        "tip_fr": "Prenez el Petit Train depuis le Vieux-Port. La vue à 360° sur la ville, la mer et les îles du Frioul depuis la 'Bonne Mère' est époustouflante.",
        "tip_de": "Fahren Sie mit dem Petit Train vom Vieux-Port hoch zur 'Bonne Mère'. Der 360-Grad-Blick über Marseille und das Meer ist fantastisch."
    },
    "ma_2": {
        "tip_en": "Stand under the giant mirror canopy ('Ombrière') designed by Norman Foster to capture fun upside-down reflected photos of the harbor crowd.",
        "tip_ja": "ノーマン・フォスター設計の巨大な鏡の屋根『Ombrière』の真下へ！天井のステンレス鏡面に映り込む逆さまの群衆や港の不思議な写真を撮るのが人気。",
        "tip_es": "Pónte debajo de la gran marquesina de espejo 'Ombrière' de Norman Foster para tomar divertidas fotos reflejadas.",
        "tip_zh": "站在诺曼·福斯特设计的大型镜面天棚（Ombrière）正下方！拍摄反射在天花板反射镜面上上下颠倒的趣味人群照片。",
        "tip_fr": "Placez-vous sous l'Ombrière miroir géante de Norman Foster sur el Vieux-Port pour des photos au reflet inversé originales.",
        "tip_de": "Stellen Sie sich unter das riesige Spiegel-Dach 'Ombrière' von Norman Foster für verblüffende Fotos mit Spiegelbild."
    },
    "ma_3": {
        "tip_en": "Striking 19th-century Neo-Byzantine cathedral built with alternating green-and-white marble stripes overlooking the sea.",
        "tip_ja": "緑と白のストライプ模様の大理石が美しい、地中海を見下ろす19世紀のネオ・ビザンティン様式の大聖堂。内部のモザイク画も必見。",
        "tip_es": "Catedral neobizantina del siglo XIX con franjas de mármol verde y blanco junto al mar.",
        "tip_zh": "面向大海的19世纪新拜占庭式大教堂，由绿白相间的大理石条纹砌成。内部金色马赛克画极尽辉煌。",
        "tip_fr": "Cathédrale romano-byzantine spectaculaire aux rayures marbrées surplombant la mer et le nouveau quartier de la Joliette.",
        "de": "Imposante neobyzantinische Kathedrale mit grün-weiß gestreiften Marmorfassaden direkt über dem Meer."
    },
    "ma_4": {
        "tip_en": "Walk across the high footbridge connecting Fort Saint-Jean directly to the MuCEM museum for free panoramic walks over the harbor entry.",
        "tip_ja": "17世紀の要塞。要塞とMuCEM博物館を結ぶ空中のハイウェイ歩道橋からの旧港の眺めは無料で見学・歩行が可能です！",
        "tip_es": "Cruza la pasarela elevada que conecta el fuerte con el museo MuCEM gratis con vistas al puerto.",
        "tip_zh": "跨越悬空连接古要塞与MuCEM博物馆的空中高架步道。可免费漫步要塞庭院，观赏老港出海口全景。",
        "tip_fr": "Traversez la passerelle suspendue reliant le fort au MuCEM. Accès libre aux jardins et chemins de ronde du fort.",
        "de": "Spazieren Sie über die kühne Fußgängerbrücke vom Fort zum MuCEM für fantastische Blicke auf die Hafeneinfahrt."
    },
    "ma_5": {
        "tip_en": "Star-shaped 17th-century fortress guarding the south entrance of the Vieux-Port. Offers panoramic views of Fort Saint-Jean opposite.",
        "tip_ja": "旧港の南口を守る星型要塞。対岸のフォール・サン・ジャン要塞と出入りする船の風景を眺める素晴らしい展望スポット。",
        "tip_es": "Fortaleza en estrella del siglo XVII que protege la entrada sur del Vieux-Port con vistas al Fort Saint-Jean.",
        "tip_zh": "守卫着老港南侧出海口的17世纪星形古要塞。与对岸的Fort Saint-Jean遥相呼应，景色震撼。",
        "tip_fr": "Citadelle du XVIIe siècle gardant la passe du Vieux-Port. Panorama superbe sur le fort Saint-Jean en face.",
        "de": "Sternförmige Festung aus dem 17. Jahrhundert, die die südliche Hafeneinfahrt bewacht."
    },
    "ma_6": {
        "tip_en": "Monumental 19th-century palace featuring a massive waterfall fountain, colonnades, and houses the Beaux-Arts and Natural History museums.",
        "tip_ja": "19世紀建設の壮大な宮殿。中央の柱廊から流れ落ちる大噴水滝の躍動感が圧巻。左右の建物には美術館と自然史博物館が入っています。",
        "tip_es": "Palacio monumental del siglo XIX con una gran cascada y colonnadas. Alberga el Museo de Bellas Artes.",
        "tip_zh": "19世纪建造的宏伟宫殿！中央半圆雕花拱廊下奔流而下的巨型阶梯瀑布大喷泉极具视觉冲击力。",
        "tip_fr": "Château d'eau monumental du XIXe siècle aux magnifiques colonnades et cascades d'eau impressionnantes.",
        "de": "Monumentales Palais des 19. Jahrhunderts mit einer riesigen Kaskaden-Fontäne und prachtvollen Kolonnaden."
    },
    "ma_7": {
        "tip_en": "Le Corbusier's famous 1952 'Cité Radieuse' brutalist concrete housing block. Visit the rooftop terrace, hotel bar, and paddling pool for free!",
        "tip_ja": "ル・コルビュジエ設計のモダニズム巨編『ユニテ・ダビタシオン』。最上階の屋上庭園（浅いプールと彫刻）へは無料で登れます！",
        "tip_es": "El famoso edificio 'Cité Radieuse' de Le Corbusier (1952). La terraza de la azotea es de acceso libre.",
        "tip_zh": "现代建筑大师勒·柯布西耶于1952年设计的“马赛公寓（Cité Radieuse）”。顶层带有水池与幼儿园的屋顶花园免费开放！",
        "tip_fr": "Monument mythique de Le Corbusier (1952). Accès libre au toit-terrasse panoramique, son école et sa pataugeoire.",
        "de": "Le Corbusiers berühmte 'Cité Radieuse' von 1952. Die Dachterrasse mit Planschbecken ist frei zugänglich."
    },
    "ma_8": {
        "tip_en": "5th-century fortified abbey built over ancient Christian catacombs—one of France's oldest continuous places of worship.",
        "tip_ja": "5世紀のキリスト教地下カタコンベの上に建つ要塞修道院。薄暗い地下聖堂（クリプト）に残る古代の石棺群は非常に神秘的。",
        "tip_es": "Abadía fortificada del siglo V sobre catacumbas cristianas antiguas. Uno de los lugares de culto más antiguos de Francia.",
        "tip_zh": "建于5世纪古基督徒地下墓穴之上的堡垒修道院。深地下圣堂（Crypt）内保存着古老石棺，氛围庄严肃穆。",
        "tip_fr": "Abbaye fortifiée fondée au Ve siècle élevée sur des catacombes chrétiennes antiques (cryptes fascinantes).",
        "de": "Wehrabtei aus dem 5. Jahrhundert über antiken christlichen Katakomben. Eine der ältesten Kirchen Frankreichs."
    },
    "ma_9": {
        "tip_en": "Home stadium of Olympique de Marseille (OM) with a futuristic undulating white roof. Guided stadium tours leave daily.",
        "tip_ja": "サッカー名門『オリンピック・マルセイユ（OM）』のホーム！波打つ巨大な白屋根が特徴的。ロッカールームやピッチ脇を回るスタジアムツアーも人気。",
        "tip_es": "Estadio del Olympique de Marseille con una cubierta blanca ondulada futurista. Tours guiados por los vestuarios.",
        "tip_zh": "法甲豪门马赛队（OM）的波浪形未来主义白屋顶主场！提供走进球员更衣室与场边的看台导览ツアー。",
        "tip_fr": "Stade mythique de l'Olympique de Marseille (OM) à la toiture ondulée impressionnante. Visite des coulisses et du vestiaire.",
        "de": "Heimatstadion des Olympique de Marseille (OM) mit geschwungenem Dach. Stadionführungen täglich."
    },
    "ma_10": {
        "tip_en": "The 16th-century island fortress made famous by Alexandre Dumas's novel 'The Count of Monte Cristo'. Take the 20-minute boat from Vieux-Port.",
        "tip_ja": "デュマの小説『モンテ・クリスト伯（巌窟王）』の舞台となった16世紀の孤島要塞。旧港から船で20分、ダンテスの脱獄牢獄を体験！",
        "tip_es": "Fortaleza insular del siglo XVI famosa por la novela 'El conde de Montecristo'. Barco de 20 min desde el Vieux-Port.",
        "tip_zh": "大仲马名著《基度山伯爵》中囚禁主人公埃德蒙·唐泰斯的16世纪孤岛要塞！在老港搭乘20分钟快艇即可抵达登岛探秘牢房。",
        "tip_fr": "Forteresse insulaire du XVIe siècle immortalisée par Alexandre Dumas dans 'Le Comte de Monte-Cristo'. Traversée en bateau 20 min.",
        "tip_de": "Inselfestung aus dem 16. Jahrhundert, bekannt aus 'Der Graf von Monte Christo'. 20 Min. Überfahrt vom Vieux-Port."
    },
    "ma_11": {
        "tip_en": "19th-century château surrounded by a park dedicated to French novelist Marcel Pagnol ('My Mother's Castle') with film exhibits.",
        "tip_ja": "作家マルセル・パニョルの自伝小説『母の城』の舞台となった19世紀の城館。シネマ博物館と緑豊かな公園が広がります。",
        "tip_es": "Castillo del siglo XIX dedicado al escritor Marcel Pagnol ('El castillo de mi madre') con exposiciones de cine.",
        "tip_zh": "法国著名作家马塞尔·帕尼奥尔自传小说《我母亲的城堡》原型古堡。内设电影博览馆与法式庭园。",
        "tip_fr": "Château du XIXe siècle au cœur d'un parc dédié à l'univers du cinéaste et écrivain Marcel Pagnol.",
        "de": "Schloss des 19. Jahrhunderts, gewidmet dem Schriftsteller Marcel Pagnol ('Das Schloss meiner Mutter')."
    },
    "ma_12": {
        "tip_en": "Architectural marvel surrounded by a black concrete lacy mesh. Take the footbridge over the sea to Fort Saint-Jean for free rooftop views!",
        "tip_ja": "黒い網目状コンクリートで覆われた先端建築。要塞へ伸びる海上の空中歩道橋と、地中海を見下ろす屋上テラスの散策は完全無料です！",
        "tip_es": "Proeza arquitectónica rodeada por una red de hormigón negro. La terraza de la azotea y las pasarelas son gratuitas.",
        "tip_zh": "被黑色镂空混凝土面罩包裹的当代建筑奇迹。通往古要塞的海上步道与俯瞰地中海的屋顶露台完全免费开放散步！",
        "tip_fr": "Chef-d'œuvre d'architecture enveloppé d'une résille de béton noir. Accès libre au toit-terrasse et à la passerelle au-dessus de la mer.",
        "de": "Architektonisches Meisterwerk mit schwarzer Beton-Spitze. Freier Zugang zur Dachterrasse und den Stegen über dem Meer."
    },
    "ma_13": {
        "tip_en": "Exact replica of the flooded 30,000-year-old underwater Cosquer cave featuring prehistoric handprints and cave paintings of penguins & horses.",
        "tip_ja": "水没した3万年前の地中海海底洞窟『コスケール洞窟』の精巧な実物大レプリカ！探検カートに乗って古代のペンギンや手形の壁画を探索。",
        "tip_es": "Réplica exacta de la cueva submarina sumergida de 30.000 años de antigüedad con pinturas rupestres de pingüinos y manos.",
        "tip_zh": "1:1完美复刻沉没于地中海海底3万年之久的古克林崖画洞穴（Cosquer Cave）！坐上探险电瓶车观看远古企鹅与手印壁画。",
        "tip_fr": "Reconstitution spectaculaire à l'échelle 1 de la grotte préhistorique sous-marine avec ses peintures de pingouins et empreintes de mains.",
        "tip_de": "Spektakuläre 1:1-Nachbildung der 30.000 Jahre alten unter Wasser liegenden Cosquer-Höhle mit prähistorischen Höhlenmalereien."
    },
    "ma_14": {
        "tip_en": "Located inside the Bourse shopping center exploring 2,600 years of Marseille history with real ancient Greek shipwrecks.",
        "tip_ja": "ブルス・ショッピングセンター横。2600年前の古代ギリシャ都市『マッサリア』開拓史と、発掘された本物のギリシャ木造船体を展示。",
        "tip_es": "Ubicado junto al centro comercial Centre Bourse sobre los 2.600 años de historia de Marsella con barcos griegos reales.",
        "tip_zh": "位于商业中心内部。完整呈现马赛2600年前古希腊移民时代（Massalia）至现代的历史，展出古希腊木造沉船实物。",
        "tip_fr": "Découvrez les 2600 ans d'histoire de la plus ancienne ville de France avec ses épaves de navires grecs antiques.",
        "de": "Museum über die 2.600-jährige Geschichte der ältesten Stadt Frankreichs mit echten antiken griechischen Schiffswracks."
    },
    "ma_15": {
        "tip_en": "Housed in the right wing of Palais Longchamp featuring Old Master Italian and French paintings inside ornate 19th-century halls.",
        "tip_ja": "ロンシャン宮殿の右翼。16〜19世紀のイタリア・フランス古典絵画（ペルジーノ、フランクスなど）を豪華なホールで展示。",
        "tip_es": "Ubicado en el ala derecha del Palais Longchamp con pinturas italianas y francesas de los siglos XVI al XIX.",
        "tip_zh": "位于Longchamp宫殿右翼展馆内。在19世纪豪华殿堂内展出16至19世纪意大利与法兰西大师古典油画。",
        "tip_fr": "Installé dans l'aile droite du Palais Longchamp abritant des chefs-d'œuvre de la peinture italienne et française.",
        "de": "Im rechten Flügel des Palais Longchamp mit italienischen und französischen Gemälden des 16. bis 19. Jahrhunderts."
    },
    "ma_16": {
        "tip_en": "Housed in an 17th-century mansion near Rue de Rome featuring modern art by Picasso, Matisse, Ernst, and Surrealists.",
        "tip_ja": "17世紀の豪邸を利用した美術館。ピカソ、マティス、シュルレアリスム作品のコレクション。静かな中庭での休憩が心地よいです。",
        "tip_es": "Museo en un palacete del siglo XVII especializado en arte moderno con obras de Picasso, Matisse y Surrealistas.",
        "tip_zh": "设于17世纪豪宅内，专一收藏毕加索、马蒂斯与超现实主义大师作品。内庭环境清幽。",
        "tip_fr": "Musée d'art moderne installé dans un beau bâtiment du XVIIe siècle abritant des œuvres de Picasso et des Surréalistes.",
        "de": "Museum für moderne Kunst in einem Palais des 17. Jahrhunderts mit Werken von Picasso und den Surrealisten."
    },
    "ma_17": {
        "tip_en": "Reopened in 2023 near Bonneveine showcasing cutting-edge contemporary international sculpture, installations, and pop art.",
        "tip_ja": "2023年にリニューアルオープン！ボネヴェーヌ地区にある現代美術館。ウォーホルやジャン・ミシェル・バスキアのポップアート作品群。",
        "tip_es": "Reabierto en 2023 con destacadas colecciones de arte contemporáneo internacional y Pop Art.",
        "tip_zh": "于2023年全新升级重开。展出涵盖安迪·沃霍尔与巴斯奎特在内的大量国际前沿当代艺术与波普艺术创作。",
        "tip_fr": "Musée d'art contemporain récemment réouvert présentant des installations avant-gardistes et des œuvres Pop Art.",
        "de": "Museum für zeitgenössische Kunst mit herausragenden Werken der internationalen Gegenwartskunst und Pop Art."
    },
    "ma_18": {
        "tip_en": "Located in the left wing of Palais Longchamp showcasing 18th-century cabinet of curiosities, taxidermy animals, and fossils.",
        "tip_ja": "ロンシャン宮殿の左翼。18世紀の剥製、化石、魚類、驚異の部屋（ヴンダーカンマー）を保存した歴史的自然史博物館。",
        "tip_es": "Ubicado en el ala izquierda del Palais Longchamp con una colección histórica de fósiles y animales disecados.",
        "tip_zh": "位于Longchamp宫殿左翼。珍藏有18世纪古董标本、化石与复古“惊异之室”（Cabinet of curiosities）展示柜。",
        "tip_fr": "Installé dans l'aile gauche du Palais Longchamp : cabinet de curiosités du XVIIIe siècle et collections zoologiques.",
        "de": "Im linken Flügel des Palais Longchamp mit historischen Präparaten, Fossilien und einem Kuriositätenkabinett."
    },
    "ma_19": {
        "tip_en": "Trendy cultural center in a former tobacco factory featuring a huge rooftop terrace bar with sunset DJ sets and skatepark.",
        "tip_ja": "タバコ工場跡地をリノベした若者に大人気のオルタナティブ施設！広大な屋上テラス（Toit-terrasse）でのサンセットDJイベントは最高。",
        "tip_es": "Espacio cultural en una antigua fábrica de tabacos con una gran terraza en la azotea con sesiones de DJ al atardecer.",
        "tip_zh": "由旧卷烟厂改建的前卫文创艺术综合体！拥有庞大的屋顶露台（Toit-terrasse），傍晚的落日DJ音乐派对氛围绝佳。",
        "tip_fr": "Espace culturel branché dans una ancienne manufacture de tabac doté d'un immense toit-terrasse pour l'apéro-DJ du soir.",
        "de": "Kulturzentrum in einer ehemaligen Tabakfabrik mit einer riesigen Dachterrasse für DJ-Events zum Sonnenuntergang."
    },
    "ma_20": {
        "tip_en": "Housed inside Château Borély displaying 18th-century Neoclassical interiors, Marseille porcelain (Faïence), and vintage haute couture fashion.",
        "tip_ja": "ボレリー公園内のボレリー宮殿。18世紀の最高級マルセイユ焼き磁器（ファルアンス）とモード衣装のコレクション。",
        "tip_es": "Ubicado en el Château Borély con cerámicas tradicionales de Marsella del siglo XVIII y vestidos de alta costura.",
        "tip_zh": "设于Borély城堡内。展示18世纪波旁王朝时代精美绝伦的马赛彩釉瓷器（Faïence）与古董高级定制时装展。",
        "tip_fr": "Installé dans le Château Borély : céramiques d'art de Marseille du XVIIIe siècle et pièces de haute couture.",
        "de": "Im Château Borély mit historischen Marseiller Fayencen (Keramik) und edlen Mode-Kollektionen."
    },
    "ma_21": {
        "tip_en": "The legendary seafood restaurant in Vallon des Auffes! Order authentic multi-fish Bouillabaisse served in 2 courses with garlic rouille sauce.",
        "tip_ja": "小さな漁港ヴァロン・デ・オーフにある名門！ニンニク風味のルイユソースと何種類もの新鮮な地魚で作られる『本物のブイヤベース』の老舗！",
        "tip_es": "El legendario restaurante de marisco en Vallon des Auffes. Pide la auténtica sopa Bouillabaisse con salsa rouille.",
        "tip_zh": "坐落于静谧小渔港 Vallon des Auffes 的顶级海鲜名店！品尝由数种鲜活地中海地鱼与蒜泥蛋黄酱（Rouille）分两道呈现的正宗马赛鱼汤（Bouillabaisse）！",
        "tip_fr": "Restaurant emblématique du Vallon des Auffes ! Savourez la véritable bouillabaisse marseillaise servie dans les règles de l'art.",
        "de": "Das legendäre Fischrestaurant im Vallon des Auffes! Unbedingt die echte Marseiller Bouillabaisse probieren."
    },
    "ma_22": {
        "tip_en": "Located on the Vieux-Port serving traditional Bouillabaisse prepared according to the strict 1980 Marseille Bouillabaisse Charter.",
        "tip_ja": "旧港の目の前。1980年に制定された『マルセイユ・ブイヤベース憲章』を厳格に守る本物のブイヤベース専門店（要予約）。",
        "tip_es": "Ubicado en el Vieux-Port. Prepara la auténtica sopa Bouillabaisse respetando la Carta oficial de 1980.",
        "tip_zh": "位于老港正面。严格遵循1980年订立的官方《马赛鱼汤宪章》标准烹制地道地中海海鲜浓汤（需提前预订）。",
        "tip_fr": "Restaurant historique sur el Vieux-Port respectant à la lettre la Charte de la Bouillabaisse de Marseille.",
        "de": "Traditionsrestaurant am Vieux-Port, das die echte Bouillabaisse streng nach der offiziellen Charta zubereitet."
    },
    "ma_23": {
        "tip_en": "Operating every morning at the head of Vieux-Port. Watch fishermen sell fresh sea bream, octopus, and rockfish straight from their wooden boats.",
        "tip_ja": "旧港の頭部で毎朝開催される伝統の魚市！毎朝水揚げされたばかりの新鮮な真鯛、タコ、ブイヤベース用の地魚を漁師から直接買えます。",
        "tip_es": "Mercado de pescado diario en el Vieux-Port donde los pescadores venden sus capturas frescas directamente desde las barcas.",
        "tip_zh": "每天早晨在老港尽头开市的传统鱼市！看当地渔民直接从水上小船拉出刚打捞的鲜活海鲷、章鱼与海鲜。",
        "tip_fr": "Marché aux poissons quotidien sur el Vieux-Port. Les pêcheurs y vendent leurs poissons de roche frais du matin.",
        "de": "Täglicher Fischmarkt am Vieux-Port: Fischer verkaufen ihren fangfrischen Fisch direkt vom Boot."
    },
    "ma_24": {
        "tip_en": "Marseille's most vibrant North African & Mediterranean spices market. Buy fresh mint, couscous spices, harissa, and sweet baklava pastry.",
        "tip_ja": "マルセイユで最も賑やかなノアイユ地区のスパイス市場。フレッシュミント、北アフリカのハリッサ香辛料、甘いバクラヴァ菓子が手に入ります。",
        "tip_es": "Mercado multicultural de especias, menta fresca, dátiles y repostería árabe en el colorido barrio de Noailles.",
        "tip_zh": "马赛最火爆的北非与地中海多元香料大集市！可以买到极新鲜的薄荷叶、辣酱Harissa香料与甜美中东果仁蜜饼（Baklava）。",
        "tip_fr": "Marché populaire et haut en couleurs de Noailles : épices orientales, menthe fraîche, dattes et pâtisseries maghrébines.",
        "de": "Orient-Markt im bunten Noailles-Viertel mit frischer Minze, orientalischen Gewürzen und Baklava."
    },
    "ma_25": {
        "tip_en": "Marseille's oldest bakery since 1781 near Abbaye Saint-Victor. Buy traditional boat-shaped 'Navettes' orange blossom biscuits.",
        "tip_ja": "1781年創業！マルセイユ最古のパン屋。オレンジの花の水（オレンジフラワーウォーター）が香る小船型の焼き菓子『ナベット（Navettes）』が有名。",
        "tip_es": "La panadería más antigua de Marsella (1781) famosa por sus galletas en forma de barca 'Navettes' con agua de azahar.",
        "tip_zh": "始于1781年马赛最古老面包店！必买透着橙花水清香的传统船形硬面干饼“Navettes”。",
        "tip_fr": "La plus ancienne boulangerie de Marseille (1781) ! Dégustez les véritables navettes au parfum de fleur d'oranger cuites dans el four bicentenaire.",
        "de": "Marseilles älteste Bäckerei von 1781, bekannt für die traditionellen bootförmigen Orangenaspekt-Kekse 'Navettes'."
    },
    "ma_26": {
        "tip_en": "Historic Belle Époque cafes on the south side of the Vieux-Port. Perfect spot for morning espresso or Pastis anise liqueur aperitivo.",
        "tip_ja": "旧港の南側にある歴史的なベル・エポック調のカフェ。午後にアニス（ウイキョウ）風味のリキュール『パスティス（Pastis）』を水割りで飲むのがマルセイユ流！",
        "tip_es": "Cafés históricos de la Belle Époque frente al puerto. Pide un aperitivo de licor de anís Pastis con agua helada.",
        "tip_zh": "位于老港南侧的历史悠久的新艺术风咖啡馆。在午后点一杯马赛当地特有的茴香酒（Pastis）加冰水极具老马赛风情。",
        "tip_fr": "Cafés historiques emblématiques du Vieux-Port. Le lieu idéal pour boire un pastis à l'heure de l'apéro.",
        "de": "Historische Belle-Époque-Cafés am Vieux-Port. Perfekter Ort für den nachmittäglichen Pastis (Anislikör)."
    },
    "ma_27": {
        "tip_en": "Located in Le Panier exploring the history of Pétanque (boulle game). Buy genuine Savon de Marseille olive oil soap cut from big blocks.",
        "tip_ja": "ル・パニエ地区。地中海伝統の球技『ペタンク』の資料館兼、オリーブオイル72%使用の伝統『マルセイユ石鹸』の直売ショップ。",
        "tip_es": "Ubicado en Le Panier. Descubre el juego de la petanca y compra auténtico jabón verde de Marsella de aceite de oliva.",
        "tip_zh": "位于 Le Panier 街区。兼具滚球运动（Pétanque）博览与正宗72%橄榄油切块“马赛石碱”（Savon de Marseille）直营店。",
        "tip_fr": "Boutique-musée dédiée à la pétanque et à l'authentique Savon de Marseille au pur huile d'olive dans Le Panier.",
        "de": "Laden und Museum im Viertel Le Panier, gewidmet dem Pétanque-Spiel und der echten Marseiller Olivenöl-Seife."
    },
    "ma_28": {
        "tip_en": "Michelin-starred seafood restaurant perched directly over the sea rocks near Vallon des Auffes with panoramic bay windows.",
        "tip_ja": "ヴァロン・デ・オーフ近くの岩場の崖の上に張り出したミシュラン星付き高級海鮮レストラン。全面ガラス窓からの海景と洗練された魚料理。",
        "tip_es": "Restaurante de marisco con estrella Michelin encaramado sobre las rocas con ventanales sobre el mar.",
        "tip_zh": "矗立于 Vallon des Auffes 悬崖礁石之上的米其林星级海鮮餐厅。全景落地窗直面蔚蓝地中海波涛。",
        "tip_fr": "Restaurant gastronomique étoilé perché sur los rochers au-dessus de la mer avec baie vitrée panoramique.",
        "de": "Gourmet-Fischrestaurant mit Michelin-Stern, spektakulär auf den Klippen direkt über dem Meer gelegen."
    },
    "ma_29": {
        "tip_en": "Marseille's oldest quarter! Wander narrow Mediterranean alleys filled with pastel facades, street art murals, and artisan craft shops.",
        "tip_ja": "マルセイユ最古の旧市街地区！パステルカラーの壁、洗練されたウォールアート、可愛い雑貨店が迷路のような坂道に詰まっています。",
        "tip_es": "¡El barrio más antiguo de Marsella! Camina por sus callejuelas estrechas repletas de arte urbano y tiendas artesanales.",
        "tip_zh": "马赛最古老的老城区！游走在狭窄陡峭的粉彩巷弄间，两旁尽是潮流街头壁画与手工艺小店。",
        "tip_fr": "Le plus ancien quartier de Marseille ! Flânez dans ses ruelles piétonnes colorées bordées d'ateliers d'artistes.",
        "de": "Marseilles ältestes Viertel! Bummeln Sie durch die bunten Gassen mit Streetart und kleinen Kunsthandwerksläden."
    },
    "ma_30": {
        "tip_en": "Picturesque tiny traditional fishing cove hidden beneath a stone viaduct. Great spot for evening drinks and seafood at sunset.",
        "tip_ja": "アーチ状の石造アーチ橋の下に隠れた絵画のような小さな漁港。夕方に黄昏時の港を見下ろすレストランで海鮮を楽しむのが至福。",
        "tip_es": "Pintoresco puerto de pesca tradicional escondido bajo un viaducto de piedra. Ideal para cenar marisco al atardecer.",
        "tip_zh": "隐藏于拱形高架石桥下宛如油画般精致的避风小渔港。夕阳西下时在水岸边享用海鲜极为浪漫。",
        "tip_fr": "Petit port de pêche traditionnel pittoresque blotti sous un viaduc en pierre. Magique au coucher du soleil !",
        "de": "Malerischer kleiner Fischerhafen unter den Bögen einer Steinbrücke – ein wunderschöner Ort zum Sonnenuntergang."
    },
    "ma_31": {
        "tip_en": "Drive or walk along the coastal boulevard for dramatic views of the Mediterranean and Chateau d'If island. Spot the world's longest bench (3 km)!",
        "tip_ja": "地中海に沿って伸びる絶景ドライブコース。海岸沿いにはギネス記録にも載った『世界最長のコンクリートベンチ（全長3km）』が続いています！",
        "tip_es": "Paseo marítimo panorámico a lo largo de la costa con vistas a las islas. ¡Busca el banco de hormigón más largo del mundo (3 km)!",
        "tip_zh": "沿地中海延伸绝绝海景大道。海岸线旁修筑有被列入吉尼斯纪录的全长3公里的“世界最长水泥长椅”！",
        "tip_fr": "Avenue littorale panoramique face à la mer. Repérez el plus long banc du monde (3 km) qui longe el bord de côte !",
        "de": "Küstenstraße mit fantastischer Aussicht auf das Meer. Hier befindet sich die längste Sitzbank der Welt (3 km)!"
    },
    "ma_32": {
        "tip_en": "Marseille's bohemian alternative quarter famous for vibrant street art, vintage clothing stores, and bustling open-air terrace bars on the square.",
        "tip_ja": "ウォールアートとボヘミアン文化が爆発する若者の街。広場周辺にはアンティーク服店、カフェ、バーの屋外テラスが溢れています。",
        "tip_es": "Barrio bohemio famoso por sus murales de graffiti, tiendas vintage y terrazas de bares en la plaza.",
        "tip_zh": "马赛潮流波西米亚与街头涂鸦文化集聚区。中央广场周边满是复古古着店与人气极旺的露天酒馆。",
        "tip_fr": "Quartier alternatif et branché célèbre pour ses fresques de street art, ses friperies et ses nombreuses terrasses de café.",
        "de": "Trendiges alternatives Viertel, weltbekannt für farbenfrohe Streetart, Vintage-Läden und volle Straßencafés."
    },
    "ma_33": {
        "tip_en": "17th-century Baroque former almshouse featuring a pink stone dome designed by Pierre Puget. Now houses the African and Egyptian museums.",
        "tip_ja": "ピエール・ピュジェ設計の17世紀の旧救済院。ピンク色の石造ドームとバロック様式の回廊中庭が美しい文化複合施設（アフリカ・エジプト美術館内蔵）。",
        "tip_es": "Antiguo hospicio barroco del siglo XVII con una cúpula de piedra rosa y un claustro central arbolado.",
        "tip_zh": "17世纪粉色石头穹顶巴洛克古遗址。拥有一座优雅的三层拱廊中庭，内设非洲艺术与埃及考古博物馆。",
        "tip_fr": "Ancien hospice du XVIIe siècle à la remarquable chapelle ovale en pierre rose et aux galeries à arcades.",
        "de": "Ehemaliges Armenhaus des 17. Jahrhunderts mit einer spektakulären ovalen Kuppelkapelle aus rosa Stein."
    },
    "ma_34": {
        "tip_en": "Lively pedestrian cobblestone square near the Vieux-Port lined with olive trees, wine bars, and Italian bistros.",
        "tip_ja": "旧港近くのオリーブの木が植えられた石畳の歩行者広場。夜になるとライトアップされ、ワインバーやビストロのテラスで賑わいます。",
        "tip_es": "Animada plaza peatonal empedrada sombreada por olivos cerca del puerto repleta de bares de vinos.",
        "tip_zh": "位于老港附近、栽满橄榄树的石板路步行广场。夜晚华灯初上，周边葡萄酒酒吧与意式餐馆人声鼎沸。",
        "tip_fr": "Grande place piétonne pavée ombragée d'oliviers bordée de terrasses de restaurants très animées el soir.",
        "de": "Lebhafter Fußgängerplatz mit Olivenbäumen und vielen gemütlichen Restaurant-Terrassen nahe dem Hafen."
    },
    "ma_35": {
        "tip_en": "Spectacular limestone fjords plunging into crystal-clear turquoise waters. Take the boat from Vieux-Port or hike from Sugiton/Sormiou (bring plenty of water!).",
        "tip_ja": "垂直に切り立つ白い石灰岩の断崖とエメラルドグリーンの入江（カランク国立公園）！旧港からのボートクルーズか、スジトン/ソルミウからのハイキングが感動的です。",
        "tip_es": "Espectaculares acantilados de piedra caliza que caen al agua turquesa. Haz una excursión en barco desde el Vieux-Port o senderismo.",
        "tip_zh": "垂直切割入绝美绿松石色海水的白色石灰岩巨型峡湾（Calanques）！建议在老港预订游船，或徒步至Sugiton绝壁海湾！",
        "tip_fr": "Joyau naturel absolu ! Falaises de calcaire blanc plongeant dans des eaux turquoise. À découvrir en bateau depuis le Vieux-Port ou en randonnée.",
        "de": "Atemberaubende weiße Klippenschluchten im türkisblauen Meer. Per Boot ab Vieux-Port oder beim Wandern erkunden."
    },
    "ma_36": {
        "tip_en": "Take the 25-minute boat ferry from Vieux-Port to explore these rocky, car-free Mediterranean islands with turquoise swimming coves.",
        "tip_ja": "旧港から船で25分。車両禁止の岩山諸島。透明度抜群のシント・エステーヴ海灘での海水浴や野生植物散策が爽快。",
        "tip_es": "Toma el ferry de 25 minutos desde el puerto para explorar estas islas rocosas sin coches con calas de cristal.",
        "tip_zh": "从老港乘船25分钟直达无车岩石群岛。拥有一系列绝美水质的水晶泳湾与原生地中海植被。",
        "tip_fr": "Îles rocheuses sauvages sans voiture à 25 min de bateau du Vieux-Port. Superbes cales pour se baigner.",
        "de": "Autofreie Felseninseln 25 Min. mit dem Schiff vom Hafen entfernt. Kristallklare Buchen zum Schwimmen."
    },
    "ma_37": {
        "tip_en": "Tiny fishing port known as the 'End of the World' (Au bout du monde) at the edge of the Calanques. Fantastic spot for sunset grilled fish.",
        "tip_ja": "カランク国立公園の入口にある『世界の終わり（Les Goudes）』と呼ばれるローカルな小漁港。夕刻に波打ち際でいただく炭火焼き地魚が絶品。",
        "tip_es": "Pequeño puerto de pesca conocido como 'El fin del mundo' al borde de las Calanques. Pide pescado a la parrilla.",
        "tip_zh": "被称为“世界尽头”的岩石峭壁边缘小渔港。傍晚在极具原生态氛围的海边餐馆享用炭烤鲜鱼。",
        "tip_fr": "Petit port au bout du monde au départ des Calanques. Ambiance authentique et poissons grillés au bord de l'eau.",
        "de": "Kleine Fischerhafen-Siedlung am 'Ende der Welt' vor den Calanques. Perfekt für gegrillten Fisch am Meer."
    },
    "ma_38": {
        "tip_en": "Sprawling 17-hectare seaside park featuring Château Borély, a lake with rowboats, rose gardens, and free playground areas for kids.",
        "tip_ja": "地中海に面した17ヘクタールの広大な公園。ボレリー城、ボートの浮かぶ池、バラ園、広大な芝生があり市民のピクニックの聖地。",
        "tip_es": "Parque de 17 hectáreas junto al mar con el Château Borély, estanque con barcas y jardines botánicos.",
        "tip_zh": "紧邻大海的17公顷绿地海滨公园。拥有 Borély 古堡、天鹅湖与草坪，是马赛市民户外野餐的宝地。",
        "tip_fr": "Grand parc de 17 hectares face à la mer avec château, lac, roseraie et vastes pelouses pour s'allonger.",
        "de": "Riesiger 17-Hektar-Park am Meer mit Schloss Borély, einem See und wunderschönen Rosengärten."
    },
    "ma_39": {
        "tip_en": "Hop on the tourist road train at Vieux-Port for a scenic ride up the coastal Corniche to Notre-Dame de la Garde.",
        "tip_ja": "旧港から発着する観光プチトラン（観光小列車）。コーニッシュ海岸沿いの絶景ドライブを楽しみながら山頂の大聖堂へ直行できます。",
        "tip_es": "Sube al tren turístico en el Vieux-Port para un paseo panorámico por la costa hasta la basílica.",
        "tip_zh": "在老港搭乘观光小火车！沿着无敌海景 Corniche 大道一路爬升至山顶 Notre-Dame 大教堂，省力有趣。",
        "tip_fr": "Montez à bord du Petit Train sur el Vieux-Port pour una balade panoramique le long de la Corniche jusqu'à la Bonne Mère.",
        "de": "Fahrt mit dem Petit Train vom Vieux-Port die Küste entlang hoch zur Notre-Dame de la Garde."
    },
    "ma_40": {
        "tip_en": "Book a 3-hour or full-day boat cruise from Vieux-Port to explore the Calanques of Sormiou, Morgiou, and Sugiton from the sea.",
        "tip_ja": "旧港から出航するカランク周遊クルーズ船（3時間〜1日コース）。船上から断崖絶壁とエメラルドグリーンの海を間近で体感！",
        "tip_es": "Reserva un crucero en barco de 3 horas desde el puerto para ver los acantilados de las Calanques desde el agua.",
        "tip_zh": "在老港预约3小时或全天游船航线！从海上视角直接开进 Sormiou 与 Sugiton 峡湾深处，绝美惊艳。",
        "tip_fr": "Réservez une croisière en bateau de 3h depuis le Vieux-Port pour découvrir les fjord calanques depuis la mer.",
        "de": "Buchen Sie eine 3-stündige Bootstour ab dem Vieux-Port, um die spektakulären Calanques vom Wasser aus zu sehen."
    },
    "ma_41": {
        "tip_en": "Popular pebble and sand beach complex created for swimming, beach volleyball, windsurfing, and seaside skatepark.",
        "tip_ja": "マルセイユ最大の海水浴＆マリンスポーツビーチ！スケートパークやビーチバレー場、レストランが完備され夏場は大賑わい。",
        "tip_es": "Gran complejo de playas para nadar, windsurf y voleibol de playa con restaurantes junto al mar.",
        "tip_zh": "马赛规模最大的海滨游乐与游泳海滩！设有大型滑板场、沙滩排球场与海边海鲜景观餐厅。",
        "tip_fr": "Grande plage d'activités nautiques, baignade, skatepark et beach-volley très animée aux beaux jours.",
        "de": "Beliebter großer Strandkomplex zum Schwimmen, Windsurfen, Skatepark und Strandbar-Besuch."
    },
    "ma_42": {
        "tip_en": "Amusement park located in Ensues-la-Redonne featuring roller coasters, water rides, and western shows for kids.",
        "tip_ja": "マルセイユから車で25分。ローラーコースター、ウォータースライダー、ウエスタンショーがある子供向けアミューズメントパーク。",
        "tip_es": "Parque de atracciones para niños con montañas rusas y espectáculos del Oeste cerca de Marsella.",
        "tip_zh": "距马赛25分钟车程的亲子游乐园。拥有云霄飞车、水上激流与西部牛仔表演。",
        "tip_fr": "Parc d'attractions familial avec montagnes russes et spectacles de l'Ouest.",
        "de": "Familien-Freizeitpark mit Achterbahnen, Wasserbahnen und Showprogrammen."
    },
    "ma_43": {
        "tip_en": "Sprawling 130-hectare nature park near Martigues featuring farm animals, pony rides, zip-lines, and pine forest trails.",
        "tip_ja": "130ヘクタールの自然公園。ポニー乗馬体験、動物ふれあい広場、アスレチックがありファミリーのピクニックに最適。",
        "tip_es": "Gran parque natural de 130 hectáreas con animales de granja, paseos en pony y senderos en el pinar.",
        "tip_zh": "占地130公顷的自然生态公园。提供骑小矮马体验、小动物互动区与松林步道。",
        "tip_fr": "Grand domaine naturel de 130 hectares avec ferme pédagogique, balades à poney et accrobranche.",
        "de": "Großer Naturpark mit Lernbauernhof, Ponyreiten und Abenteuerpfaden im Pinienwald."
    }
}

# Run updates
update_city_tips("strasbourg.json", strasbourg_tips)
update_city_tips("toulouse.json", toulouse_tips)
update_city_tips("marseille.json", marseille_tips)

print("🎉 Finished Batch 2 Insider Tips update!")
