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
# BATCH 1: NICE (36 spots), LYON (46 spots), BORDEAUX (40 spots)
# -------------------------------------------------------------

nice_tips = {
    "nice_1": {
        "tip_en": "Walk up to the Bellanda Tower for the iconic curved photo of the Baie des Anges. Sunsets here are magical with the promenade lights turning on.",
        "tip_ja": "ベランダの塔展望台からは、天使の湾（プロムナード・デ・ザングレ）の完璧な美しい湾曲を眼下に撮影できます。街灯が灯る夕暮れ時が最もロマンチックです。",
        "tip_es": "Sube a la Torre Bellanda para tomar la foto icónica de la curva de la Bahía de los Ángeles al atardecer.",
        "tip_zh": "登上贝兰达塔（Bellanda Tower）观景台，可俯瞰天使湾最完美优雅弧线的标志性大片。傍晚华灯初上时最为浪漫。",
        "tip_fr": "Montez à la Tour Bellanda pour capturer la vue panoramique mythique sur la Baie des Anges au coucher du soleil.",
        "tip_de": "Erklimmen Sie den Bellanda-Turm für das perfekte Panoramabild der geschwungenen Engelsbucht bei Sonnenuntergang."
    },
    "nice_2": {
        "tip_en": "Elevator access is available near the Hotel Suisse if stairs are too steep. Don't miss the artificial waterfall on top cooled by sea breezes.",
        "tip_ja": "階段がキツい場合はスイスホテルの脇にある無料エレベーターが便利。頂上にある迫力満点の人工滝前は、夏の涼しい避暑スポットです。",
        "tip_es": "Usa el ascensor gratuito cerca del Hotel Suisse si no quieres subir escaleras. La cascada en la cima es muy fresca en verano.",
        "tip_zh": "如果不想爬台阶，Hotel Suisse旁设有免费电梯。城塞山顶拥有一座气势磅礴的流泻人工瀑布，夏日极为清凉。",
        "tip_fr": "Un ascenseur gratuit près de l'Hôtel Suisse permet d'éviter la montée à pied. La cascade au sommet est un havre de fraîcheur.",
        "tip_de": "Der kostenlose Aufzug nahe dem Hotel Suisse spart den steilen Aufstieg. Der künstliche Wasserfall oben bietet echte Abkühlung."
    },
    "nice_3": {
        "tip_en": "Buy piping hot Socca (chickpea pancake) directly from the iron pans at Chez René Socca, then eat it with cold rosé at the open tables.",
        "tip_ja": "名物『シェ・ルネ・ソッカ』の鉄板で焼き立ての熱々ソッカをテイクアウトし、通りの開放的なテラス席でキンキンに冷えたロゼワインと合わせるのが地元流！",
        "tip_es": "Pide socca caliente en Chez René Socca y disfrútala en las mesas al aire libre con una copa de vino rosado frío.",
        "tip_zh": "在Chez René Socca购买刚出大铁盘的热气腾腾 Socca（鹰嘴豆煎饼），在露天餐桌配上一杯冰镇普罗旺斯桃红葡萄酒最地道！",
        "tip_fr": "Dégustez la socca chaude sortie du four chez René Socca avec un verre de rosé frais en terrasse.",
        "tip_de": "Frische heiße Socca bei Chez René Socca bestellen und draußen mit einem kühlen Glas Rosé genießen."
    },
    "nice_4": {
        "tip_en": "Don't miss Chagall's stunning stained-glass windows in the concert hall depicting the Creation. The blue garden surrounding the museum is peaceful and free to enter.",
        "tip_ja": "コンサートホールの『創世記』を描いた青いステンドグラスは光が差し込む昼前が一番綺麗。美術館を取り囲むラベンダーの庭園散策は無料です。",
        "tip_es": "Las vidrieras azules de Chagall en la sala de conciertos se ven mejor a mediodía. El jardín exterior es gratuito.",
        "tip_zh": "音乐厅内以“创世纪”为主题的夏加尔蔚蓝彩绘玻璃窗在午前日光照耀下极为圣洁。外围薰衣草花园免费开放。",
        "tip_fr": "Les vitraux bleus de Chagall dans l'auditorium sont magnifiques sous la lumière du matin. Le jardin est en accès libre.",
        "tip_de": "Die blauen Chagall-Glasfenster im Konzertsaal leuchten am Vormittag am schönsten. Der Garten ist kostenlos zugänglich."
    },
    "nice_5": {
        "tip_en": "Houses Matisse's personal bronze sculptures and cutout paper art in a 17th-century Genoese villa. Combined ticket with nearby Roman ruins is available.",
        "tip_ja": "マティス晩年の切抜き絵（ペーパー・カットアウト）やブロンズ彫刻が見事。17世紀の赤いジェノヴァ風ヴィラと隣接するローマ遺跡公園の散策もセットでどうぞ。",
        "tip_es": "Colección de recortes de papel y esculturas de Matisse en una villa genovesa del siglo XVII. Billete combinado con ruinas romanas.",
        "tip_zh": "建于17世纪红墙热那亚别墅内，收藏马蒂斯晚年精妙的剪纸艺术与青铜雕塑。可购买包含旁边古罗马遗址的联票。",
        "tip_fr": "Superbe collection de gouaches découpées de Matisse dans une villa génoise rouge. Billet combiné avec les arènes de Cimiez.",
        "tip_de": "Matisse-Scherenschnitte in einer prächtigen roten Genueser Villa des 17. Jahrhunderts. Kombiticket mit den Römerruinen buchen."
    },
    "nice_6": {
        "tip_en": "Take the elevator to the rooftop terrace bar for panoramic 360-degree views of the Promenade des Anglais and Mediterranean Sea.",
        "tip_ja": "ネグレスコホテルの向かい。最上階のルーフトップバーからはプロムナード・デ・ザングレと地中海を360度見渡せる隠れた絶景スポットです。",
        "tip_es": "Sube a la terraza de la azotea para disfrutar de una vista de 360 grados de la Promenade des Anglais y el mar.",
        "tip_zh": "位于内格雷斯科酒店对面。乘电梯直达顶层露台酒吧，可360度俯瞰英国人散步大道与湛蓝蔚蓝海岸。",
        "tip_fr": "Prenez l'ascenseur jusqu'au toit-terrasse pour une vue panoramique à 360 degrés sur la Promenade des Anglais.",
        "tip_de": "Mit dem Aufzug auf die Dachterrasse fahren für einen spektakulären 360-Grad-Blick auf die Promenade und das Meer."
    },
    "nice_7": {
        "tip_en": "The largest Russian Orthodox Cathedral outside Russia. Respectful dress code (covered shoulders and knees) is strictly enforced at the entrance.",
        "tip_ja": "ロシア国外で最大規模のロシア正教会大聖堂。入場時は服装チェック（肩や膝の露出NG）が厳格に行われるため上着を持参しましょう。",
        "tip_es": "Catedral rusa ortodoxa fuera de Rusia más grande. Se exige código de vestimenta respetuoso (hombros y rodillas cubiertas).",
        "tip_zh": "俄罗斯境外规模最大的俄国正教大教堂。入口处严格检查着装（禁止露肩与短裤），请备好披肩或外套。",
        "tip_fr": "La plus grande cathédrale orthodoxe russe hors de Russie. Tenue correcte (épaules et genoux couverts) requise.",
        "tip_de": "Größte russisch-orthodoxe Kathedrale außerhalb Russlands. Angemessene Kleidung (Schultern und Knie bedeckt) ist Pflicht."
    },
    "nice_8": {
        "tip_en": "Buy fresh lavender honey, candied fruits, and socca seasoning from local growers. Closed on Mondays when it transforms into an antique flea market.",
        "tip_ja": "ラベンダー蜂蜜、ドライトマト、プロヴァンサルハーブの土産が充実。月曜日は花市・食料市がお休みになり、ヴィンテージの骨董市（蚤の市）に変わります。",
        "tip_es": "Compra miel de espliego y frutas escarchadas. Los lunes se convierte en un animado mercado de antigüedades.",
        "tip_zh": "可购买到普罗旺斯薰衣草蜂蜜、糖渍水果与特产香料。每周一农贸花市休市，转换为复古古董蚤之集市。",
        "tip_fr": "Achetez du miel de lavande et des fruits confits. Le lundi, le marché laisse place aux brocanteurs et antiquaires.",
        "tip_de": "Frischer Lavendelhonig und kandierte Früchte. Montags verwandelt sich der Markt in einen antiken Flohmarkt."
    },
    "nice_9": {
        "tip_en": "Walk past the fountain to the optical illusion trompe-l'œil facades painted on the yellow buildings on the north side of the square.",
        "tip_ja": "広場北側の黄色い建物群の窓や壁画には、精巧なだまし絵（トロンプ・ルイユ）が描かれています。噴水を背にじっくり観察してみてください。",
        "tip_es": "Observa los edificios amarillos del lado norte para descubrir los detallados frescos en trompe-l'œil pintados en las fachadas.",
        "tip_zh": "站在将领加里波第雕像旁仔细端详，广场北侧黄墙建筑物上的窗户与柱石大部分都是极其逼真的3D错视画（Trompe-l'œil）。",
        "tip_fr": "Admirez les façades des immeubles jaunes au nord de la place pour repérer les superbes fresques en trompe-l'œil.",
        "tip_de": "Betrachten Sie die gelben Gebäude an der Nordseite genau: Viele Fenster und Säulen sind faszinierende Trompe-l'œil-Malereien."
    },
    "nice_10": {
        "tip_en": "Take the #607 or #608 bus from Nice for just €2.10 along the lower corniche cliff road for stunning coastal views straight into Monaco.",
        "tip_ja": "ニースから僅か€2.10のバス（607/608系統）で断崖絶壁の海岸線を走りモナコへ行けます。進行方向右側の席に座るのが海の景色を楽しむコツ！",
        "tip_es": "Toma el autobús regional por poco más de 2€ a lo largo de la carretera costera para disfrutar de vistas espectaculares de Monaco.",
        "tip_zh": "从尼斯乘坐607/608路沿海断崖悬崖公交车仅需2.10欧即可直达摩纳哥！请选择车头右侧座椅以饱览无敌海景。",
        "tip_fr": "Prenez le bus littoral (ligne 607/608) pour un trajet panoramique spectaculaire le long de la mer jusqu'à Monaco pour seulement 2,10 €.",
        "tip_de": "Mit der Buslinie 607/608 für nur 2,10 € entlang der Klippenstraße nach Monaco fahren – unbedingt rechts sitzen!"
    },
    "nice_11": {
        "tip_en": "Wander the exotic botanical gardens on top of the medieval village for dramatic 400-meter vertical views over Cap Ferrat.",
        "tip_ja": "標高400mの断崖の頂上にあるサボテン熱帯庭園（Jardin Exotique）からの景色は南仏屈指！サン・ジャン・キャップ・フェラを一望できます。",
        "tip_es": "El jardín exótico en la cima del pueblo medieval ofrece una vista impresionante de 400 metros de altura sobre el mar.",
        "tip_zh": "位于悬崖小镇最顶端的异国仙人掌植物园（Jardin Exotique）拥有垂直高度400米的无敌视角，将费拉角尽收眼底。",
        "tip_fr": "Visitez le jardin exotique au sommet du village perché pour un panorama vertigineux à 400m au-dessus de la mer.",
        "tip_de": "Der exotische Garten auf dem Gipfel des Dorfes bietet einen spektakulären Blick aus 400 Metern Höhe über die Côte d'Azur."
    },
    "nice_12": {
        "tip_en": "Visit the 9 themed gardens (Spanish, Florentine, Japanese) and enjoy high tea on the terrace with views of both bays.",
        "tip_ja": "男爵夫人のピンクのヴィラと9つのテーマ庭園（スペイン、和風、ローズ）が見事。海を見下ろすテラス席でのアフタヌーンティーが至福です。",
        "tip_es": "Disfruta de los 9 jardines temáticos y tómate un té en la terraza con vistas a las bahías de Villefranche y Beaulieu.",
        "tip_zh": "罗斯柴尔德男爵夫人的粉色宫殿与9大主题花园（西班牙式、日式庭园）。在眺望双湾的露台享用下午茶极其优雅。",
        "tip_fr": "Flânez dans les 9 magnifiques jardins thématiques et prenez un thé sur la terrasse surplombant les deux baies.",
        "tip_de": "Erkunden Sie die 9 Themengärten und genießen Sie eine Tasse Tee auf der Terrasse mit Blick auf beide Meeresbuchten."
    },
    "nice_13": {
        "tip_en": "Stroll down the cobblestone Citadel paths to Plage des Marinières for one of the South of France's most picturesque swimming beaches.",
        "tip_ja": "カラフルな旧市街と城塞の小道を下ると美しいマリニエール海灘へ直結。プロバンスのカラフルな小船が浮かぶ絵画のような湾です。",
        "tip_es": "Pasea por las callejuelas del pueblo hacia la playa Plage des Marinières para disfrutar de un baño con vistas a la bahía.",
        "tip_zh": "漫步穿过悬崖小镇彩色巷弄直达マリニエール海滩（Plage des Marinières）。湾内停泊着色彩斑斓的南法木船，海景极绝。",
        "tip_fr": "Descendez les ruelles colorées vers la plage des Marinières pour une baignade dans l'une des plus belles baies de la côte.",
        "tip_de": "Durch die malerischen Gassen zur Plage des Marinières spazieren und in einer der schönsten Buchten der Riviera baden."
    },
    "nice_14": {
        "tip_en": "Hike the paved coastal path 'Promenade des Douaniers' around the rocky peninsula. High tide splash spots offer exhilarating sea views.",
        "tip_ja": "岩場の海岸線に沿って整備された絶景遊歩道『関税の道（Sentier du Littoral）』でのハイキングが爽快。透明度抜群のクリスタルブルーの海。",
        "tip_es": "Recorre el sendero costero pimentado alrededor de la península de Cap Ferrat para disfrutar de calas de agua cristalina.",
        "tip_zh": "沿着绕费拉角一圈修筑的海边绝壁小径（Sentier du Littoral）徒步。沿途可近距离接触清澈见底的玻璃海湾。",
        "tip_fr": "Empruntez le sentier douanier qui fait le tour de la presqu'île pour découvrir des criques sauvages aux eaux translucides.",
        "tip_de": "Der fantastische Küstenwanderweg rund um das Cap Ferrat bietet spektakuläre Ausblicke auf kristallklares Wasser."
    },
    "nice_15": {
        "tip_en": "Try the legendary Fenocchio ice cream on Place Rossetti right in front of the baroque cathedral—over 90 exotic flavors including lavender & thyme!",
        "tip_ja": "教会前のロセティ広場にある老舗アイス店『Fenocchio』は90種類以上のフレーバー！ラベンダー、ローズ、タイムなどプロヴァンス風味覚が楽しめます。",
        "tip_es": "Prueba los helados de Fenocchio frente a la catedral: ¡más de 90 sabores incluyendo lavanda, romero y tomillo!",
        "tip_zh": "教堂正前方Rossetti广场上的老字号冰淇淋店Fenocchio拥有超90种口味！推荐尝试薰衣草、百里香或玫瑰风味。",
        "tip_fr": "Dégustez une glace chez le glacier mythique Fenocchio sur la place Rossetti : plus de 90 parfums aux senteurs de Provence !",
        "tip_de": "Gegenüber der Kathedrale bei Fenocchio Eis essen: Über 90 Sorten, darunter Lavendel, Thymian und Rose."
    },
    "nice_16": {
        "tip_en": "Look out for traditional wooden Pointu fishing boats painted in bright blues and reds anchored on the quiet eastern quay.",
        "tip_ja": "港の東側に停泊する南仏伝統の木造漁船『ポワンチュ（Pointu）』のカラフルな船体が写真映え。賑やかな海岸通りより落ち着いて散策できます。",
        "tip_es": "Camina por el muelle este para fotografiar los barcos de pesca tradicionales de madera pintados de colores brillantes.",
        "tip_zh": "在老港东侧停泊码头近距离拍摄南法传统鲜艳彩绘木船“Pointu”。相比花果集市这里更为幽静宜人。",
        "tip_fr": "Admirez les barques traditionnelles en bois (pointus) peintes en couleurs vives amarrées le long des quais réaménagés.",
        "tip_de": "Am östlichen Kai liegen die traditionellen bunten Holzfischerboote (Pointus) – ein wunderschönes Fotomotiv."
    },
    "nice_17": {
        "tip_en": "Modern art gallery with a rooftop sculpture garden featuring panoramic city views. Entrance is included in the Nice Museum Pass.",
        "tip_ja": "4つのタワーが架け橋で繋がったモダン建築。最上階の屋上庭園からはニース市街と山々の素晴らしいビューが広がります。",
        "tip_es": "Galería de arte moderno con jardín de esculturas en la azotea y espectaculares vistas panorámicas de la ciudad.",
        "tip_zh": "由4座通透高塔与空中连廊构成的现代艺术馆。顶层雕塑露台可360度远眺尼斯市区与蔚蓝海岸。",
        "tip_fr": "Musée d'art contemporain doté d'un toit-terrasse arboré proposant un panorama sensationnel sur la ville.",
        "de": "Museum für moderne Kunst mit einem Skulpturengarten auf dem Dach und tollem Rundumblick über Nizza."
    },
    "nice_18": {
        "tip_en": "Features Impressionist and Belle Époque masterworks inside a 19th-century palace built for a Russian princess.",
        "tip_ja": "ロシアの親王妃のために建てられた19世紀の豪華な宮殿を利用した美術館。印象派やオルレアン派の美しいコレクション。",
        "tip_es": "Ubicado en un palacio del siglo XIX construido para una princesa rusa, con obras impresionistas y esculturas.",
        "tip_zh": "坐落于19世纪为俄国公主建造的豪华宫殿内，收藏有德加、莫奈与罗丹等巨匠的作品。",
        "tip_fr": "Installé dans un palais du XIXe siècle bâti pour une princesse russe, abritant de grands maîtres impressionnistes.",
        "de": "In einem prächtigen Palais des 19. Jahrhunderts für eine russische Prinzessin mit Werken des Impressionismus."
    },
    "nice_19": {
        "tip_en": "Surrounded by yellow Genoese facades with green shutters and arcades. Great spot for aperitivo at the outdoor cafes.",
        "tip_ja": "イタリア風の黄色の回廊建築に囲まれた広場。夕方にオープンエアのカフェで『アペリティーボ（食前酒）』を楽しむのに最高のアトモスフィア。",
        "tip_es": "Gran plaza rodeada de fachadas amarillas genovesas con arcos. Ideal para tomar un aperitivo al atardecer.",
        "tip_zh": "围绕着黄墙绿窗意式拱廊建筑的大广场。傍晚在露天咖啡馆喝上一杯Aperol Spritz食前酒极具南法情调。",
        "tip_fr": "Place majestueuse bordée d'immeubles jaunes à arcades de style piémontais. Parfait pour l'apéro en terrasse.",
        "tip_de": "Großzügiger Platz im piemontesischen Stil mit gelben Arcaden. Ideal für einen Aperitif am späten Nachmittag."
    },
    "nice_20": {
        "tip_en": "Expect queues at this legendary street food counter! Order Socca, Pissaladière (onion-anchovy tart), and Tourte blettes.",
        "tip_ja": "行列必至の名物屋台！ひよこ豆ペーストのソッカ、炒め玉ねぎとアンチョビのタルト『ピサラディエール』、フリットの持ち帰りが定番。",
        "tip_es": "¡Hay cola siempre! Pide Socca recién hecha, Pissaladière (tarta de cebolla y anchoas) y beignets de verduras.",
        "tip_zh": "火爆全城的传奇南法小吃摊！必点现炸Socca、洋葱安康鱼干薄饼（Pissaladière）与炸野菜。",
        "tip_fr": "Comptoir culte du Vieux-Nice ! File d'attente garantie pour goûter la socca, la pissaladière et les beignets de fleurs de courgette.",
        "tip_de": "Kult-Imbiss in der Altstadt! Schlange stehen lohnt sich für Socca, Pissaladière und frische Krapfen."
    },
    "nice_21": {
        "tip_en": "Stroll the interactive water mirror (Miroir d'eau) where 128 water jets spray mist in summer—bring towels if visiting with kids!",
        "tip_ja": "128基の噴水と霧が吹き出す『水鏡（Miroir d'eau）』は夏場のお子様や観光客の癒やしスポット。芝生エリアでピクニックも可能。",
        "tip_es": "Camina por el espejo de agua interactivo con 128 chorros de agua. Zona de juegos fantástica para niños.",
        "tip_zh": "由128座潜水喷泉构成的巨型水镜（Miroir d'eau）。夏日喷雾凉爽宜人，非常适合带小孩玩水与草坪野餐。",
        "tip_fr": "Traversez le miroir d'eau rafraîchissant doté de 128 jets de brume en été. Superbe parc paysager en cœur de ville.",
        "tip_de": "Der Wasserspiegel mit 128 Nebel- und Wasserstrahlen bietet im Sommer eine herrliche Erfrischung mitten in der Stadt."
    },
    "nice_22": {
        "tip_en": "Buy authentic AOP olive oil from local Provence groves inside bottles shaped like perfume flasks.",
        "tip_ja": "1868年創業のオリーブオイル老舗。香水瓶のようなガラス瓶に詰められたプロヴァンス産最高級AOPオリーブオイルはお土産に最高。",
        "tip_es": "Aceite de oliva galardonado producido localmente en recipientes elegantes como frascos de perfume.",
        "tip_zh": "始于1868年的香醇橄榄油百年老字号。装在如香水瓶般高雅玻璃瓶中的AOP特级初榨橄榄油是送礼佳品。",
        "tip_fr": "Maison fondée en 1868 proposant de grands crus d'huile d'olive de Provence présentés dans des flacons raffinés.",
        "tip_de": "Traditionsgeschäft seit 1868 mit erstklassigem provenzalischem Olivenöl in wunderschönen Flakons."
    },
    "nice_23": {
        "tip_en": "Discover candied clementines, violets, and chocolate-dipped orange peels handmade since 1820.",
        "tip_ja": "1820年創業。マティスも愛した老舗菓子店。プロヴァンス産の砂糖漬けフルーツ（クレマンティーヌやスミレの砂糖漬け）が名物。",
        "tip_es": "Frutas escarchadas artesanales, violetas confitadas y chocolates desde 1820. Un regalo gastronómico único.",
        "tip_zh": "1820年创办的糖渍水果名店。马蒂斯曾是其忠实拥趸。推荐购买糖渍小柑橘与薰衣草/紫罗兰糖膏。",
        "tip_fr": "Confiserie historique depuis 1820 célèbre pour ses fruits confits artisanaux, fleurs cristallisées et chocolats.",
        "tip_de": "Historische Konditorei seit 1820, berühmt für kandierte Früchte, kristallisierte Veilchen und Schokolade."
    },
    "nice_24": {
        "tip_en": "Historic 1860 opera house with opulent gold-and-velvet auditorium. Check the program for evening ballet or classical performances.",
        "tip_ja": "1860年建造の豪華なオペラ劇場。赤と金の豪華な天井フレスコ画（ボナロ作）を擁する劇場内部は、夜の公演鑑賞で体験できます。",
        "tip_es": "Ópera histórica de 1860 con una sala espectacular de terciopelo y pan de oro. Consulta su programación de ballet.",
        "tip_zh": "建于1860年的金碧辉煌剧院。内饰奢华的红绒与金箔天顶画，非常推荐在晚间预订一场芭蕾或交响乐。",
        "tip_fr": "Magnifique opéra du XIXe siècle au décor d'or et de velours rouge. Consultez la programmation pour une soirée concert ou ballet.",
        "tip_de": "Prachtvolles Opernhaus von 1860 mit samtrotem Interieur und Goldverzierungen. Abends Ballettaufführungen genießen."
    },
    "nice_25": {
        "tip_en": "Step inside a faithful recreation of an ancient 5th-century BC Greek noble villa built directly over the sea cliffs in Beaulieu.",
        "tip_ja": "ボーリューの海の上に建つ、古代ギリシャの貴族館を完璧に再現した美しいヴィラ。大理石の中庭とエメラルドの海景が見事です。",
        "tip_es": "Fascinante reconstrucción de una villa griega del siglo V a.C. construida junto al mar en Beaulieu-sur-Mer.",
        "tip_zh": "坐落于Beaulieu海边峭壁之上，完美重现公元前5世纪古希腊贵族奢华豪宅的艺术殿堂。大理石中庭美轮美奂。",
        "tip_fr": "Reconstitution unique et somptueuse d'un palais de la Grèce antique au bord de l'eau à Beaulieu-sur-Mer.",
        "tip_de": "Fasinierende und getreue Rekonstruktion einer antiken griechischen Adelsvilla direkt am Meeresufer in Beaulieu."
    },
    "nice_26": {
        "tip_en": "Dine inside an old chapel with stained glass windows at Le Saint Paul, offering cliffside terrace dining over the sea.",
        "tip_ja": "修道院をリノベーションしたホテルレストラン。崖の上のテラス席から海を眺めながらいただく地中海料理はロマンチックそのもの。",
        "tip_es": "Cena en una antigua capilla renovada con terraza sobre los acantilados marítimos cerca del puerto.",
        "tip_zh": "由修道院圣堂改建而成的精品海景餐厅。坐在绝壁露台一边观赏静谧的大海一边享受地中海美食。",
        "tip_fr": "Dînez dans le cadre d'un ancien séminaire doté d'une terrasse panoramique spectaculaire sur la mer.",
        "tip_de": "Dine in einem ehemaligen Klostergebäude mit einer atemberaubenden Terrasse direkt über dem Meer."
    },
    "nice_27": {
        "tip_en": "Take the scenic Train des Pignes steam train into the mountains for a rustic day trip to medieval Entrevaux.",
        "tip_ja": "ニースから山間部へと走る観光列車『プロヴァンス鉄道（Train des Pignes）』。城塞都市アントルヴォーへの日帰り旅に最適。",
        "tip_es": "Toma el pintoresco tren de montaña Train des Pignes para explorar los pueblos medievales del interior.",
        "tip_zh": "乘坐著名的普罗旺斯复古小火车载着你深入阿尔卑斯山区，探访中世纪巨石悬崖要塞Entrevaux。",
        "tip_fr": "Empruntez el mythique Train des Pignes pour une escapade bucolique à travers l'arrière-pays niçois jusqu'à Entrevaux.",
        "tip_de": "Mit dem historischen Train des Pignes durch das malerische Hinterland bis zum Mittelalterdorf Entrevaux fahren."
    },
    "nice_28": {
        "tip_en": "Stroll down the tree-lined pedestrian mall packed with high-end boutiques and French cafes.",
        "tip_ja": "ジャン・メドサン通りからマセナ広場へと続く街路樹が美しい歩行者天国。ブランド店やカフェでのショッピングに快適。",
        "tip_es": "Avenida peatonal arbolada repleta de boutiques elegantes y terrazas de cafés cerca de Place Masséna.",
        "tip_zh": "连接梅德桑大街与马塞纳广场的大理石林荫步道。两旁高级精选店与法式露天咖啡馆林立。",
        "tip_fr": "Artère piétonne élégante et arborée reliant la place Masséna aux boutiques de mode.",
        "tip_de": "Bäume gesäumte elegante Fußgängerzone mit exklusiven Boutiquen und schönen Straßencafés."
    },
    "nice_29": {
        "tip_en": "Walk up to the 19th-century fortress for sweeping 360-degree views over Cap d'Antibes and the Southern Alps.",
        "tip_ja": "アンティーブの旧市街裏手に聳える16世紀の星型要塞。頂上のテラスからはアンティーブ湾と雪を戴くアルプス山脈の雄大な景色。",
        "tip_es": "Fortaleza del siglo XVI sobre la colina con impresionantes vistas panorámicas de la costa y los Alpes.",
        "tip_zh": "屹立于昂蒂布老城旁高地上的16世纪星形防御要塞。顶层可360度揽尽费拉角海岸与远处连绵山脉。",
        "tip_fr": "Fort polygonal du XVIe siècle offrant un panorama exceptionnel sur le vieil Antibes, la mer et les Alpes.",
        "tip_de": "Imposante Festung aus dem 16. Jahrhundert mit einem fantastischen Panoramablick auf Antibes und die Alpen."
    },
    "nice_30": {
        "tip_en": "Located inside Château Grimaldi where Picasso lived and worked in 1946—see his vibrant Mediterranean ceramics and paintings overlooking the sea.",
        "tip_ja": "1946年にピカソが滞在制作したグリマルディ城。地中海を望むテラスと、ピカソ直筆の絵画や陶芸作品のコレクションが見事。",
        "tip_es": "Ubicado en el Château Grimaldi donde Picasso vivió en 1946, exhibiendo sus pinturas y cerámicas sobre el mar.",
        "tip_zh": "位于毕加索1946年曾居住创作的格里马尔迪城堡内。临海露台与毕加索亲手绘制的陶艺作品极具生命力。",
        "tip_fr": "Installé dans le château Grimaldi où Picasso a séjourné en 1946 : œuvres méditerranéennes face à la mer.",
        "tip_de": "Im Château Grimaldi, in dem Picasso 1946 sein Atelier hatte. Meisterwerke mit Blick auf das Meer."
    },
    "nice_31": {
        "tip_en": "Famous for the Maeght Foundation modern art museum hidden in the pine forest and its artisan glass/sculpture workshops.",
        "tip_ja": "松林の中に近代美術の殿堂『マーグ財団美術館』が佇む芸術の村。ミロやジャコメッティの野外彫刻と迷路のような小道散策。",
        "tip_es": "Pueblo de artistas famoso por la Fundación Maeght en el bosque de pinos con esculturas de Miró y Giacometti.",
        "tip_zh": "隐匿于松林之中的著名艺术家小镇。拥有鼎鼎大名的玛格基金会美术馆（Fondation Maeght），陈列米罗与贾科梅蒂雕塑。",
        "tip_fr": "Village d'artistes mythique abritant la célèbre Fondation Maeght nichée dans les pins avec ses sculptures de Miró.",
        "tip_de": "Berühmtes Künstlerdorf im Hinterland mit der weltbekannten Fondation Maeght inmitten eines Pinienwaldes."
    },
    "nice_32": {
        "tip_en": "Visit Fragonard or Molinard perfume laboratories for a free guided tour and craft your own custom fragrance formula.",
        "tip_ja": "香水の都グラース。フラゴナール（Fragonard）等の調香工場を無料で見学でき、自分だけのオリジナル調香体験（ワークショップ）が可能です。",
        "tip_es": "Visita las históricas fábricas de perfumes Fragonard con tours gratuitos para crear tu propia fragancia.",
        "tip_zh": "世界香水之都格拉斯。可免费参观Fragonard或Molinard调香工厂，并参与调香师工作坊DIY调制个人专属香水。",
        "tip_fr": "Capitale mondiale du parfum. Visitez gratuitement las parfumeries historiques Fragonard et créez votre propre eau de parfum.",
        "tip_de": "Welthauptstadt des Parfums. Kostenlose Führungen bei Fragonard und die Möglichkeit, sein eigenes Parfum zu kreieren."
    },
    "nice_33": {
        "tip_en": "Walk down the Boulevard de la Croisette to view the Red Carpet of the Palais des Festivals where the Cannes Film Festival is held.",
        "tip_ja": "カンヌ国際映画祭の会場『パレ・デ・フェスティバル』のレッドカーペットと手形手形歩道（Allée des Étoiles）で記念撮影！",
        "tip_es": "Fotografíate en la famosa alfombra roja del Palais des Festivals en el bulevar de la Croisette.",
        "tip_zh": "漫步在坎城克鲁瓦塞特大道（Croisette），在举行戛纳电影节的Palais des Festivals红地毯台阶与明星手印墙合影！",
        "tip_fr": "Prenez une photo sur le célèbre tapis rouge du Palais des Festivals le long de la Croisette.",
        "tip_de": "Ein Foto auf dem berühmten roten Teppich des Palais des Festivals an der Croisette machen!"
    },
    "nice_34": {
        "tip_en": "Take the 15-minute boat ferry from Cannes to explore the tranquil island forest and cellars of Monks brewing Lerina liqueur.",
        "tip_ja": "カンヌから船で15分。自動車乗り入れ禁止の静寂な島。修道士が作る名物リキュール『レリナ』と修道院のブドウ畑が美しい。",
        "tip_es": "Toma el ferry de 15 minutos desde Cannes para explorar la isla sin coches y el monasterio donde los monjes elaboran vino.",
        "tip_zh": "从戛纳搭乘15分钟渡轮即可抵达无车净土圣奥诺拉岛。探访修道院修士们亲自种植酿造葡萄酒与Lerina利口酒的葡萄园。",
        "tip_fr": "Embarquez depuis Cannes pour cette île sans voiture et découvrez l'abbaye où les moines produisent leurs propres vins.",
        "tip_de": "15-minütige Überfahrt von Cannes auf die autofreie Insel mit dem historischen Kloster und seinen eigenen Weinen."
    },
    "nice_35": {
        "tip_en": "Rent a kayak or stand-up paddleboard to paddle through the towering 700-meter limestone canyon into Lake Sainte-Croix.",
        "tip_ja": "『ヨーロッパのグランドキャニオン』。高さ700mの断崖の間をエメラルドグリーンの聖十字架湖（ヴェルドン川）からカヤックで進む大自然の絶景。",
        "tip_es": "Alquila un kayak para navegar por el impresionante cañón de 700 metros de profundidad de agua turquesa.",
        "tip_zh": "被称为欧洲的大峡谷。租划一艘电动船或皮划艇，沿着翡翠绿色的水流驶入深高达700米的巍峨巨石峡谷入口。",
        "tip_fr": "Louez un kayak au lac de Sainte-Croix pour vous aventurer au cœur des vertigineuses gorges aux eaux turquoise.",
        "tip_de": "Leihen Sie ein Kajak am See von Sainte-Croix und paddeln Sie in die atemberaubende turquoise Schlucht hinein."
    },
    "nice_36": {
        "tip_en": "Stroll down the green corridor park spanning from the Old Town to the National Theatre with wooden playgrounds and shaded benches.",
        "tip_ja": "旧市街から劇場へと伸びる広大な緑道公園。木製の巨大遊具や季節の花々が咲き誇り、散策やテイクアウトランチに最適な市民の憩い場。",
        "tip_es": "Paseo verde que conecta la ciudad vieja con el teatro, con áreas de juegos de madera y arboledas sombreadas.",
        "tip_zh": "连接老城与国家剧院的大型中央绿廊公园。拥有精美的木质儿童设施与树荫长椅，非常适合散步整休。",
        "tip_fr": "Coulée verte centrale offrant des aires de jeux en bois et des espaces ombragés de la vieille ville au théâtre.",
        "tip_de": "Wunderschöner grüner Parkgürtel durch die Innenstadt mit Holzspielplätzen und schattigen Bänken."
    }
}

lyon_tips = {
    "lyon_1": {
        "tip_en": "Take the funicular railway 'Funiculaire de Fourvière' up the hill. The panoramic view over Lyon's red roofs from the basilica terrace is unbeatable.",
        "tip_ja": "地下鉄チケットで乗れるケーブルカーで一気に丘の上へ。聖堂横のテラスからは、リヨンの赤屋根の街並みとローヌ川・ソーヌ川を一望できます！",
        "tip_es": "Sube en el funicular de Fourvière. La vista panorámica de los tejados rojos de Lyon desde la terraza es espectacular.",
        "tip_zh": "使用普通地铁票乘坐Fourvière缆车直达山顶。大教堂高台露台俯瞰里昂红瓦屋顶与双河交汇的全景堪称绝杀。",
        "tip_fr": "Empruntez le funiculaire de Fourvière (ticket de métro classique). La vue panoramique sur les toits rouges de Lyon est la plus belle de la ville.",
        "tip_de": "Mit der Standseilbahn (Funiculaire) auf den Hügel fahren. Der Panoramablick von der Basilika-Terrasse über Lyon ist unschlagbar."
    },
    "lyon_2": {
        "tip_en": "Visit at 12:00, 14:00, 15:00, or 16:00 to see the 14th-century astronomical clock chime and activate its mechanical wooden figures.",
        "tip_ja": "14世紀のからくり天文時計は12時・14時・15時・16時に動きます。からくり人形が動き出す瞬間を狙って訪問するのがおすすめ！",
        "tip_es": "Visítala a las 12:00, 14:00, 15:00 o 16:00 para ver sonar el reloj astronómico del siglo XIV y sus figuras mecánicas.",
        "tip_zh": "建议在正午12点、14点、15点或16点准时前往，观赏14世纪古董天文钟打点与木偶打鸣表演。",
        "tip_fr": "Soyez présent à 12h, 14h, 15h ou 16h pour voir s'animer l'horloge astronomique du XIVe siècle.",
        "tip_de": "Kommen Sie um 12, 14, 15 oder 16 Uhr, um das historische astronomische Uhrwerk in Aktion zu erleben."
    },
    "lyon_3": {
        "tip_en": "Look for small brass plaques marked 'Traboule' next to heavy wooden doorways. The Longue Traboule (54 Rue Saint-Jean) passes through 4 courtyards!",
        "tip_ja": "建物の扉横にある『Traboule』の金文字プレートが目印。54 Rue Saint-Jeanから始まるロング・トラブールは4つの中庭を通り抜ける名物コース！",
        "tip_es": "Busca las placas de latón 'Traboule' al lado de las puertas. La Longue Traboule en 54 Rue Saint-Jean cruza 4 patios.",
        "tip_zh": "寻找木门旁标有“Traboule”的黄铜小牌。Saint-Jean街54号的“长穿堂廊道”连续穿越4座幽静中庭与拱门！",
        "tip_fr": "Repérez les plaques en laiton 'Traboule'. La Longue Traboule au 54 Rue Saint-Jean traverse 4 cours intérieures magnifiques.",
        "tip_de": "Achten Sie auf die kleinen Messingschilder 'Traboule'. Die Longue Traboule (54 Rue Saint-Jean) führt durch 4 Innenhöfe."
    },
    "lyon_4": {
        "tip_en": "The two grand Roman theatres are completely free to explore. Catch the Nuits de Fourvière outdoor festival if visiting in summer!",
        "tip_ja": "古代ローマの2つの大劇場遺構は完全無料で自由に見学可能！夏の夜には野外芸術祭『ニュイ・ド・フルヴィエール』のステージ会場となります。",
        "tip_es": "Los dos teatros romanos son de acceso gratuito. En verano se celebra el festival Nuits de Fourvière al aire libre.",
        "tip_zh": "古罗马大剧场遗址完全免费对外开放步入。夏季这里会举办极其拉风的“フルヴィエール之夜”露天艺术音乐节。",
        "tip_fr": "Les deux théâtres romains sont en accès libre et gratuit. En été, ils accueillent le festival des Nuits de Fourvière.",
        "tip_de": "Die beiden römischen Theater sind komplett kostenlos zugänglich. Im Sommer findet hier das Festival Nuits de Fourvière statt."
    },
    "lyon_5": {
        "tip_en": "Stroll down Lyon's main pedestrian shopping street stretching between Place Bellecour and Place des Terreaux past Haussmann facades.",
        "tip_ja": "ベルクール広場からテロー広場を結ぶペルソナ歩行者天国。オスマン様式の華やかな建築群を見上げながら買い物や散策が楽しめます。",
        "tip_es": "Pasea por la calle comercial peatonal principal de Lyon entre Place Bellecour y Place des Terreaux.",
        "tip_zh": "连接贝尔库尔广场与泰罗广场的中心大理石步行购物街。沿途尽是雄伟的奥斯曼风格建筑与知名店铺。",
        "tip_fr": "Flânez le long de cette grande rue piétonne commerçante bordée d'immeubles haussmanniens entre Bellecour et Terreaux.",
        "tip_de": "Flanieren Sie auf dieser prächtigen Fußgängerzone mit haussmannschen Fassaden zwischen Bellecour und Terreaux."
    },
    "lyon_6": {
        "tip_en": "Stroll the inner cloisters of this 18th-century hospital converted into a luxury shopping arcade and grand dome cocktail bar.",
        "tip_ja": "18世紀の大病院をリノベした歴史的空間。巨大ドーム（Grand Dôme）下のバー『Le Dôme』でカクテルを楽しむひとときが格別です。",
        "tip_es": "Recorre los claustros de este antiguo hospital del siglo XVIII reconvertido en tiendas de lujo y un bar bajo la gran cúpula.",
        "tip_zh": "18世纪古老皇家医院改建的奢华名品长廊。巨型大圆顶（Grand Dôme）下设的高端鸡尾酒酒吧极具调性。",
        "tip_fr": "Découvrez la cour intérieure de cet ancien hôpital du XVIIIe siècle magnifiquement rénové avec ses boutiques et son bar sous le grand dôme.",
        "tip_de": "Flanieren Sie durch den Innenhof des ehemaligen Krankenhauses aus dem 18. Jahrhundert mit edlen Geschäften und der Bar unter der Kuppel."
    },
    "lyon_7": {
        "tip_en": "Built in 19 BC where delegates of the 64 Gallic tribes met. Free to view from the street on the slopes of Croix-Rousse.",
        "tip_ja": "紀元前19年に建てられた古代ガリア3州の遺構。クロワ・ルースの丘の途中にあり、通りから無料で全景を見学できます。",
        "tip_es": "Construido en el año 19 a.C. donde se reunían las tribus galas. Se contempla libremente desde la calle en Croix-Rousse.",
        "tip_zh": "公元前19年建成的古罗马遗迹。位于Crois-Rousse斜坡旁，在街道旁即可免费全景环顾昔日古城台。",
        "tip_fr": "Construit en 19 av. J.-C., cet amphithéâtre romain est visible gratuitement depuis la rue sur les pentes de la Croix-Rousse.",
        "tip_de": "Im Jahr 19 v. Chr. erbaut. Das antike Amphitheater kann von der Straße an den Hängen der Croix-Rousse kostenfrei betrachtet werden."
    },
    "lyon_8": {
        "tip_en": "Admire the two contrasting Gothic steeples (one stone, one brick) and the glowing white interior on Place Jacobins.",
        "tip_ja": "プレスクィール中心部に立つゴシック様式の教会。左右異なる2つの尖塔（石造りとレンガ造り）の建築様式と夜間のライトアップが見事。",
        "tip_es": "Admira los dos campanarios góticos diferentes y el luminoso interior blanco cerca de la Place des Jacobins.",
        "tip_zh": "拥有左右完全不同材质（一座石造、一座砖造）双塔的哥特式教堂。内饰全白精致浮雕，夜间灯光绝美。",
        "tip_fr": "Remarquez ses deux flèches gothiques différentes (l'une en pierre, l'autre en brique) et son bel intérieur lumineux.",
        "tip_de": "Bewundern Sie die zwei unterschiedlich gestalteten Kirchtürme und das helle gotische Innere am Place Jacobins."
    },
    "lyon_9": {
        "tip_en": "Europe's largest mural (1,200 m²) updated every decade. Look closely at the stairs and people—they are all 3D optical illusions!",
        "tip_ja": "1200㎡に及ぶヨーロッパ最大のだまし絵壁画！人物や階段、店舗の窓はすべて平面に描かれた3Dペイントです。写真撮影が楽しいスポット。",
        "tip_es": "El mural en trompe-l'œil más grande de Europa (1.200 m²). Las escaleras y figuras son ilusiones ópticas en 3D.",
        "tip_zh": "面积达1200平方米的欧洲最大立体错视画（Trompe-l'œil）墙面！楼梯、车辆与行人群全为平画3D效果，合影极其生动。",
        "tip_fr": "La plus grande fresque en trompe-l'œil d'Europe (1200 m²). Les personnages et escaliers sont tous des illusions en 3D !",
        "tip_de": "Das größte Trompe-l'œil-Wandgemälde Europas (1.200 m²). Treppen und Passanten sind verblüffend echte 3D-Illusionen."
    },
    "lyon_10": {
        "tip_en": "Relax in the peaceful central garden courtyard surrounded by 17th-century sculpture arcades right off Place des Terreaux.",
        "tip_ja": "テロー広場横にある17世紀の旧修道院。ブロンズ彫刻が並ぶ静かな回ロップ中庭（庭園）は無料で立ち寄れ、都会の喧騒を離れた休憩に最適。",
        "tip_es": "Relájate en el tranquilo jardín del claustro del siglo XVII rodeado de esculturas junto a Place des Terreaux.",
        "tip_zh": "位于17世纪修道院庭院内。中庭回廊雕塑花园免费开放，是繁华市中心闹中取静的极佳整休之地。",
        "tip_fr": "Reposez-vous dans le magnifique jardin du cloître du XVIIe siècle au cœur du musée, un havre de paix gratuit.",
        "tip_de": "Entspannen Sie im ruhigen Klostergarten des 17. Jahrhunderts im Innenhof des Museums nahe dem Place des Terreaux."
    },
    "lyon_11": {
        "tip_en": "Features ultra-detailed 1:43 scale movie sets (including Alien, Star Wars, and Grand Budapest Hotel) & original props made by film miniaturists.",
        "tip_ja": "映画『エイリアン』や『グランド・ブダペスト・ホテル』の超精密なミニチュア撮影セットと本物の映画小道具コレクション。大人も子供も夢中になります！",
        "tip_es": "Exhibe escenarios de cine en miniatura a escala 1:43 de películas famosas y objetos reales de rodajes de Hollywood.",
        "tip_zh": "展示电影《异形》、《大饭店》等1:43高精度实体电影道具微缩模型与好莱坞真实特效道具，细节令人叹为观止。",
        "tip_fr": "Découvrez d'incroyables décors de cinéma miniatures au 1:43 et de véritables accessoires de films hollywoodiens.",
        "tip_de": "Faszinierende Original-Filmrequisiten und extrem detaillierte Miniatur-Filmkulissen bekannter Hollywood-Streifen."
    },
    "lyon_12": {
        "tip_en": "Futuristic glass architecture at the tip of the Presqu'île where the Rhône and Saône rivers merge. The rooftop bar has great river views.",
        "tip_ja": "ローヌ川とソーヌ川が合流する先端に立つ未来派ガラス建築。最上階のテラスからは二大河川の合流点を見下ろせます。",
        "tip_es": "Edificio de cristal futurista en la confluencia de los ríos Ródano y Saona. La terraza del tejado ofrece grandes vistas.",
        "tip_zh": "耸立于索恩河与罗讷河汇流处最尖端的未来感云朵晶体建筑。屋顶露台可观赏两河交汇处壮阔水景。",
        "tip_fr": "Architecture futuriste spectaculaire à la pointe de la Presqu'île. Le bar en toit-terrasse offre une vue superbe sur la rencontre des fleuves.",
        "tip_de": "Futuristischer Glasbau an der Spitze der Halbinsel, wo Rhône und Saône zusammenfließen. Toller Blick vom Dach."
    },
    "lyon_13": {
        "tip_en": "Houses the world's finest collection of Lyon silk fabrics and 2,000-year-old textiles. (Check opening hours as it undergoes partial renovations).",
        "tip_ja": "リヨンの伝統産業である絹織物（シルク）と世界各国の古代織物コレクション。シルクの街リヨンの歴史を深く学べます。",
        "tip_es": "Conserva la mejor colección de tejidos de seda de Lyon y textiles con más de 2.000 años de historia.",
        "tip_zh": "收藏有里昂著名的历史丝绸织物及跨越2000年历史的纺织艺术品。深入了解丝绸之都的工业底蕴。",
        "tip_fr": "Abrite la plus belle collection de soieries lyonnaises et de textiles anciens précieux du monde.",
        "tip_de": "Beherbergt eine der bedeutendsten Seidensammlungen der Welt und historische Textilien aus zwei Jahrtausenden."
    },
    "lyon_14": {
        "tip_en": "Housed in the former Printing House where Auguste and Louis Lumière invented the Cinématographe camera in 1895. Daily film screenings available.",
        "tip_ja": "1895年にリュミエール兄弟が世界初の映画（シネマトグラフ）を撮影した実家工場跡。映画誕生の歴史的展示と映画館を併設。",
        "tip_es": "Ubicado en la antigua fábrica donde los hermanos Lumière inventaron el cine en 1895. Se proyectan películas clásicas.",
        "tip_zh": "位于1895年卢米埃尔兄弟发明电影放映机（Cinématographe）并拍摄首部电影的实业故居。内设电影历史大厅与重温影院。",
        "tip_fr": "Lieu de naissance du cinéma ! Visitez la maison de la famille Lumière et la première usine de films de l'histoire.",
        "tip_de": "Die Geburtsstätte des Kinos! Das Wohnhaus der Brüder Lumière zeigt die Erfindung des ersten Filmprojektors 1895."
    },
    "lyon_15": {
        "tip_en": "Housed in a 14th-century mansion exploring puppet theatre history and Guignol, Lyon's iconic 1808 satirical wooden puppet.",
        "tip_ja": "1808年にリヨンで誕生した風刺木偶劇キャラクター『ギニョール』と世界各国のマリオネット人形コレクションを展示。",
        "tip_es": "Museo en una mansión del siglo XIV dedicado al teatro de marionetas y al personaje satírico Guignol de Lyon.",
        "tip_zh": "设于14世纪大宅内，专门展出1808年诞生于里昂的著名木偶形象“Guignol”及全球古董木偶珍藏。",
        "tip_fr": "Musée passionnant installé dans un hôtel particulier du XIVe siècle dédié à Guignol et aux marionnettes du monde entier.",
        "tip_de": "Spannendes Marionettenmuseum in einem Palais des 14. Jahrhunderts, gewidmet der Kulturelle-Figur Guignol."
    },
    "lyon_16": {
        "tip_en": "Located inside Palais Saint-Jean showcasing 2,000 items on Lyon's urban development, silk trade, and resistance history.",
        "tip_ja": "サン・ジャン宮殿内。絹織物産業の発展から第二次世界大戦レジスタンス活動まで、リヨンの歴史を辿る市立歴史博物館。",
        "tip_es": "Ubicado en el Palais Saint-Jean sobre la historia urbana, el comercio de la seda y la resistencia de Lyon.",
        "tip_zh": "位于圣让宫（Palais Saint-Jean）内部，展示里昂城市变迁、丝绸贸易及二战时期抵抗运动历史。",
        "tip_fr": "Découvrez l'histoire fascinante de Lyon de l'époque romaine à nos jours au sein du Palais Saint-Jean.",
        "tip_de": "Stadtgeschichtliches Museum im Palais Saint-Jean über die Entwicklung Lyons von den Römern bis heute."
    },
    "lyon_17": {
        "tip_en": "Former headquarters of the Gestapo in Lyon during WWII. Moving exhibition honoring Resistance hero Jean Moulin.",
        "tip_ja": "第二次大戦中にゲシュタポ本部が置かれた建物。レジスタンスの英雄ジャン・ムーランや強制送還の歴史を伝える重要な平和学習施設。",
        "tip_es": "Antigua sede de la Gestapo durante la Segunda Guerra Mundial. Exposición conmovedora sobre la Resistencia francesa.",
        "tip_zh": "二战时期盖世太保在里昂的总部旧址。展示法国抵抗运动英雄让·穆兰与二战反思历史，氛围严肃深刻。",
        "tip_fr": "Ancien siège de la Gestapo. Lieu de mémoire poignant retraçant l'histoire de la Résistance et de Jean Moulin.",
        "tip_de": "Ehemaliges Gestapo-Hauptquartier. Eindringlicher Erinnerungsort zur Geschichte der französischen Résistance."
    },
    "lyon_18": {
        "tip_en": "Features Auguste Rodin's 'The Thinker' and 'The Gates of Hell' bronzes inside a serene 17th-century cloister garden.",
        "tip_ja": "リヨン美術館中庭。ロダンの『考える人』や『地獄の門』のブロンズ像が静かな緑の回廊庭園に展示されており、無料で鑑賞できます。",
        "tip_es": "Exhibe esculturas de bronce de Auguste Rodin como 'El Pensador' en un patio arbolado de acceso libre.",
        "tip_zh": "里昂美术馆中庭开放式绿地花园。免费展示奥古斯特·罗丹的著名雕塑《思考者》与《地狱之门》青铜原作。",
        "tip_fr": "Admirez la sculpture du 'Penseur' de Rodin exposée dans le jardin ombragé du cloître en accès libre.",
        "tip_de": "Im kostenfrei zugänglichen Klostergarten steht Rodins berühmte Bronzeskulptur 'Der Denker'."
    },
    "lyon_19": {
        "tip_en": "Designed by architect Renzo Piano; features temporary exhibitions of contemporary international art near Parc de la Tête d'Or.",
        "tip_ja": "レンゾ・ピアノ設計。テット・ドール公園に隣接する現代美術館。国際的な先端アートの企画展を定期開催。",
        "tip_es": "Diseñado por Renzo Piano con exposiciones temporales de arte contemporáneo internacional junto al Parc de la Tête d'Or.",
        "tip_zh": "由著名建筑大师伦佐·皮亚诺设计。紧邻金头公园，举办多维度的国际当代艺术前沿特展。",
        "tip_fr": "Bâtiment conçu par Renzo Piano proposant de grandes expositions d'art contemporain au bord du parc.",
        "de": "Vom Stararchitekten Renzo Piano entworfenes Museum für wechselnde zeitgenössische Kunstausstellungen."
    },
    "lyon_20": {
        "tip_en": "Known for hosting the Lyon Biennale of Contemporary Art. Located in a sleek building right by the Rhône riverbank.",
        "tip_ja": "リヨン現代アート・ビエンナーレの主要会場。ローヌ川沿いのスタイリッシュな空間で斬新なアート体験ができます。",
        "tip_es": "Sede principal de la Bienal de Arte Contemporáneo de Lyon junto al parque y el río Ródano.",
        "tip_zh": "里昂当代艺术双年展的核心主会场。位于罗讷河畔，展示极具未来感的当代跨界艺术实景展。",
        "tip_fr": "Lieu emblématique accueillant la Biennale d'art contemporain de Lyon au bord du Rhône.",
        "tip_de": "Hauptveranstaltungsort der renommierten Biennale für zeitgenössische Kunst in Lyon."
    },
    "lyon_21": {
        "tip_en": "Open-air housing estate featuring 25 giant outdoor wall murals painted on 1930s social housing blocks by architect Tony Garnier.",
        "tip_ja": "1930年代の集合住宅の壁面に描かれた25大の巨大屋外ウォールアート集落。オープンエアで歩いて見学できます。",
        "tip_es": "Conjunto de 25 pintura murales gigantes pintadas en edificios de viviendas de los años 30 al aire libre.",
        "tip_zh": "由建筑师Tony Garnier设计的露天住宅群。在25座1930年代公寓大楼外墙画满巨幅都市主题壁画。",
        "tip_fr": "Musée à ciel ouvert comprenant 25 peintures murales géantes sur les façades de la cité réalisée par Tony Garnier.",
        "tip_de": "Freilichtmuseum mit 25 riesigen Wandgemälden an den Fassaden einer Wohnsiedlung der 1930er Jahre."
    },
    "lyon_22": {
        "tip_en": "Located at Lyon-Corbas airfield with 30+ historic military and civilian aircraft, helicopters, and engines on display.",
        "tip_ja": "リヨン＝コルバ飛行場内。30機以上の戦闘機、ヘリコプター、航空エンジンが実機展示されたボランティア運営の穴場航空館。",
        "tip_es": "Aeródromo de Lyon-Corbas con más de 30 aviones militares y civiles históricos y helicópteros.",
        "tip_zh": "位于里昂Corbas机场。室内外展出30多架传奇军用战机、民航客机与直升机实体，航空迷必赴。",
        "tip_fr": "Musée passionnant présentant plus de 30 avions et hélicoptères civils et militaires restaurés avec soin.",
        "de": "Luftfahrtmuseum am Flugplatz Lyon-Corbas mit über 30 historischen Flugzeugen und Hubschraubern."
    },
    "lyon_23": {
        "tip_en": "The ultimate indoor food temple of Lyon! Sample Saint-Marcellin cheese from Mère Richard, oysters, and Praline tarts.",
        "tip_ja": "美食の都リヨンの胃袋！『メール・リシャール』のトロトロのチーズ（サン・マルセラン）やカキ、ピンクプラリネのタルトは食の天国です！",
        "tip_es": "¡El templo gastronómico cubierto de Lyon! Prueba el queso Saint-Marcellin de Mère Richard y marisco fresco.",
        "tip_zh": "美餐饮食圣地！汇集法餐教父保罗·博古斯认证的顶部美食。必尝Mère Richard软质干酪与粉红杏仁糖塔。",
        "tip_fr": "Le temple absolu de la gastronomie lyonnaise ! Goûtez le Saint-Marcellin de la Mère Richard et les charcuteries artisanales.",
        "tip_de": "Der Tempel der lyonesischen Gastronomie! Unbedingt den Käse Saint-Marcellin von Mère Richard probieren."
    },
    "lyon_24": {
        "tip_en": "Authentic certified 'Bouchon Lyonnais'. Order the classic Tablier de sapeur (tripe), quenelle de brochet, and Beaujolais wine.",
        "tip_ja": "公認『ブショネル』の伝統ビストロ。名物のクネル（カワカマスの魚肉すり身ソフレ）や豚肉料理を赤ワインと共にどうぞ！",
        "tip_es": "Auténtico bistró tradicional 'Bouchon'. Pide la famosa quenelle de brochet y carne de cerdo con vino Beaujolais.",
        "tip_zh": "获得官方认证的传统里昂小馆（Bouchon）。必点河鱼肉丸（Quenelle）配奶油龙虾酱与博若莱红酒。",
        "tip_fr": "Authentique bouchon lyonnais traditionnel. Savourez une quenelle de brochet sauce nantua et de la charcuterie locale.",
        "tip_de": "Authentischer traditioneller Bouchon Lyonnais. Probieren Sie die berühmte Quenelle de Brochet."
    },
    "lyon_25": {
        "tip_en": "Located inside Grand Hôtel-Dieu exploring French culinary heritage, gastronomy workshops, and food tasting exhibitions.",
        "tip_ja": "グラン・オテル・デュー内。ユネスコ無形文化遺産『フランスの美食術』をテーマにした体験型食文化ミュージアム。",
        "tip_es": "Ubicado en el Grand Hôtel-Dieu dedicado a la gastronomía francesa con talleres y degustaciones.",
        "zh": "位于Grand Hôtel-Dieu内。以联合国非遗“法国美食学”为主题的交互体验展厅与美食品鉴中心。",
        "fr": "Espace dédié à la gastronomie française et à l'art de la table au cœur du Grand Hôtel-Dieu.",
        "de": "Ausstellungszentrum im Grand Hôtel-Dieu, gewidmet der französischen Kochkunst und Gastronomie."
    },
    "lyon_26": {
        "tip_en": "Famous for the 'Tarte à la Praline'—a crunchy pastry filled with crushed pink sugar-coated almonds.",
        "tip_ja": "リヨン名物『タルト・ア・ラ・プラリネ』の有名店。鮮やかなピンク色の甘くてカリカリの杏仁砂糖がぎっしり入った伝統菓子。",
        "tip_es": "Famosa pastelería por su 'Tarte à la Praline', pastel crujiente relleno de almendras rosa con azúcar.",
        "tip_zh": "里昂著名甜品老铺。必尝镇店之宝粉红杏仁甜塔（Tarte à la Praline），颜色瑰丽甜香酥脆。",
        "tip_fr": "Pâtisserie emblématique célèbre pour sa véritable tarte aux pralines rouges croustillantes et ses chocolats.",
        "tip_de": "Konditorei, weltberühmt für ihre leuchtend rosa Tarte aux Pralines mit gekandeten Mandeln."
    },
    "lyon_27": {
        "tip_en": "Legendary bean-to-bar chocolatier since 1953 famed for 'Le Président' chocolate cake created for French President Valéry Giscard d'Estaing.",
        "tip_ja": "1953年創業のショコラティエ。大統領のために作られた名物チョコレートケーキ『Le Président』の濃厚な味わいは感動的！",
        "tip_es": "Chocolatería legendaria desde 1953 conocida por la tarta de chocolate 'Le Président'.",
        "tip_zh": "始于1953年的自烘豆巧克力名门。必尝1975年为法国总统定制的招牌纯黑巧克力蛋糕“Le Président”。",
        "tip_fr": "Chocolatier d'exception depuis 1953, créateur du mythique gâteau en chocolat 'Le Président'.",
        "tip_de": "Legendäre Chocolaterie seit 1953, berühmt für die Schokoladentorte 'Le Président'."
    },
    "lyon_28": {
        "tip_en": "One of Lyon's oldest bouchons operating since 1726 with wooden paneling, red-checked tablecloths, and authentic home-style tripe & sausage.",
        "tip_ja": "1726年創業。リヨン最古のブショネル居酒屋。赤いチェックのテーブルクロスと木造の内装で味わう伝統のソーセージが最高。",
        "tip_es": "Uno de los bouchons más antiguos de Lyon (1726) con manteles de cuadros rojos y comida casera.",
        "tip_zh": "始于1726年里昂最古老的Bouchon小馆。红白格子桌布与古朴木质装潢，提供绝佳的经典里昂自制香肠。",
        "tip_fr": "L'un des plus anciens bouchons de Lyon (1726) servant una cuisine authentique dans un cadre rétro.",
        "de": "Eines der ältesten Traditionswirtshäuser Lyons (1726) mit rot-weiß karierten Tischdecken."
    },
    "lyon_29": {
        "tip_en": "Grand 1836 Art Deco brasserie by Perrache train station. Order the Alsatian Choucroute flambéed with Marc de Bourgogne at your table!",
        "tip_ja": "1836年創業のアール・デコ調の大ブラッスリー。テーブル前で蒸留酒 Marc に火を付けてフランベする『シュークルート』のパフォーマンスが名物！",
        "tip_es": "Gran brasería Art Déco de 1836. Pide la chucrut flambeada en tu mesa frente a la estación de train.",
        "tip_zh": "始于1836年的巨型新艺术风大餐馆。侍者会在桌前现场表演用勃艮第白兰地火焰白菜猪肉锅（Choucroute）。",
        "tip_fr": "Brasserie Art Déco monumentale de 1836. Commandez la choucroute flambée en salle devant vous.",
        "tip_de": "Prachtvolle Art-Déco-Großbrasserie von 1836. Die am Tisch flambierte Choucroute ist spektakulär."
    },
    "lyon_30": {
        "tip_en": "The 3-Michelin-star temple of French cuisine by Paul Bocuse on the banks of the Saône. Book months in advance for the truffle soup VGE!",
        "tip_ja": "フレンチの巨匠ポール・ボキューズの総本山。1975年にエリゼ宮で大統領に捧げた『黒トリュフのパイ包みスープ（VGE）』は一生モノの体験です（数ヶ月前要予約）。",
        "tip_es": "El templo de la gastronomía francesa. Reserva con meses de antelación para probar la sopa de trufas VGE.",
        "tip_zh": "法餐教父保罗·博古斯位于索恩河畔的终极殿堂。提前数月预订，必尝1975年献给总统的黑松露酥皮汤（Soup VGE）。",
        "tip_fr": "Le temple mondial de la gastronomie française ! Réservez plusieurs mois à l'avance pour déguster la soupe aux truffes VGE.",
        "tip_de": "Der weltberühmte Gastronomie-Tempel von Paul Bocuse. Monate im Voraus reservieren für die Trüffelsuppe VGE."
    },
    "lyon_31": {
        "tip_en": "Explore the Renaissance courtyards hidden behind heavy doors along Rue Saint-Jean and Place du Gouvernement.",
        "tip_ja": "ヴュー・リヨン（旧市街）の重厚な木門をそっと開けると、ルネサンス様式のピンクの螺旋階段や静かな中庭が現れる探検感が魅力。",
        "tip_es": "Explora los patios renacentistas ocultos tras las grandes puertas de madera a lo largo de Rue Saint-Jean.",
        "tip_zh": "漫步在旧城圣让街，轻推看起来封闭的重型木门，即可发现内里隐藏着粉色螺旋楼梯与石雕中庭。",
        "tip_fr": "Poussez délicatement les lourdes portes des immeubles de la Rue Saint-Jean pour découvrir de sublimes cours Renaissance.",
        "tip_de": "Gehen Sie durch die Holztore in der Rue Saint-Jean und entdecken Sie versteckte Renaissance-Innenhöfe."
    },
    "lyon_32": {
        "tip_en": "Walk up the 'Pentes' steep stone staircases lined with indie designer shops, artisan cafes, and street art murals.",
        "tip_ja": "かつての絹織物職人（カニュ）の街。坂道（Pentes）の石段沿いには若手デザイナーのショップ、カフェ、壁画が集まりオシャレ。",
        "tip_es": "Sube por las empinadas escaleras de las Pentes repletas de tiendas de diseñadores independientes y arte urbano.",
        "tip_zh": "沿“斜坡”陡峭石梯一路向上，两旁尽是独立设计师艺术工坊、咖啡馆与充满创意的街头涂鸦墙。",
        "tip_fr": "Grimpez les pentes de la Croix-Rousse entre boutiques de créateurs indépendants, cafés branchés et street art.",
        "tip_de": "Erklimmen Sie die steilen Treppen der Pentes mit ihren coolen Designer-Boutiquen und Kunstgalerien."
    },
    "lyon_33": {
        "tip_en": "The iconic 6-story open-air staircase traboule built in 1840 at 9 Place Colbert—a symbol of the Canut silk workers' revolt.",
        "tip_ja": "9 Place Colbertにある6階建ての屋外階段トラブール。絹織物職人（カニュ）の暴動の歴史を象徴するリヨンで最もフォトジェニックな空中階段。",
        "tip_es": "La espectacular traboule de 6 pisos de escaleras abiertas en 9 Place Colbert, símbolo de las revoluciones obreras.",
        "tip_zh": "位于9 Place Colbert的6层露天交错楼梯穿堂廊道。是丝绸工人起义历史的象征，极具几何建筑美感。",
        "tip_fr": "La traboule la plus spectaculaire de Lyon (9 Place Colbert) avec ses escaliers extérieurs sur 6 niveaux.",
        "tip_de": "Faszinierende 6-stöckige offene Treppen-Traboule (9 Place Colbert), Symbol der lyonesischen Arbeiteraufstände."
    },
    "lyon_34": {
        "tip_en": "Features 30 famous historical and modern figures of Lyon (including Paul Bocuse and Saint-Exupéry) painted on a 800 m² building facade.",
        "tip_ja": "サン＝テグジュペリ、ポール・ボキューズ、リュミエール兄弟など、リヨンゆかりの30人の偉人がバルコニーから顔を覗かせるだまし絵壁画。",
        "tip_es": "Famoso mural con 30 personajes históricos de Lyon (como Saint-Exupéry y Paul Bocuse) asomados a los balcones.",
        "tip_zh": "在800平米墙面上栩栩如生刻画着30位里昂历史上著名的伟人（包括《小王子》作者圣埃克苏佩里与博古斯）。",
        "tip_fr": "Fresque représentant 30 lyonnais célèbres (Saint-Exupéry, Paul Bocuse) aux fenêtres d'un immeuble en bord de Saône.",
        "tip_de": "Fassadengemälde mit 30 berühmten Persönlichkeiten Lyons (u.a. Saint-Exupéry und Paul Bocuse) an den Fenstern."
    },
    "lyon_35": {
        "tip_en": "Walk to Boulevard de la Croix-Rousse to view this vibrant giant mural showing neighbourhood life in the silk-weaving district.",
        "tip_ja": "クロワ・ルースの大通りにある壁画。10年ごとに街の変化に合わせて描き直されるため、常に現在のリヨンの生活が映し出されています。",
        "tip_es": "Enorme pintura mural que se actualiza cada década reflejando la vida cotidiana del barrio de la seda.",
        "tip_zh": "位于Croix-Rousse大道的巨幅涂鸦壁画。每隔十年便会根据时代变迁重新打磨绘制，记录街区当下真实生活。",
        "tip_fr": "Grande fresque emblématique mise à jour régulièrement pour représenter la vie du quartier des Canuts.",
        "de": "Riesiges Fassadengemälde, das regelmäßig aktualisiert wird und das Leben im Seidenweber-Viertel zeigt."
    },
    "lyon_36": {
        "tip_en": "Walk across this striking red suspension footbridge over the Saône river for great photo angles of Saint-Georges church tower.",
        "tip_ja": "ソーヌ川に架かる鮮やかな赤い吊り橋。対岸のサン・ジョルジュ教会の尖塔と川面を一緒に撮影できる隠れた絶好のカメラポイント。",
        "tip_es": "Camina por esta pasarela colgante roja sobre el río Saona para tomar buenas fotos de la iglesia de Saint-Georges.",
        "tip_zh": "横跨于索恩河上的鲜红弧形吊桥。是拍摄对岸圣乔治教堂尖塔与水面倒影的绝佳摄影视角。",
        "tip_fr": "Traversez cette passerelle suspendue rouge vif pour admirer el clocher de l'église Saint-Georges se reflétant dans la Saône.",
        "tip_de": "Die rote Hängebrücke über die Saône ist der perfekte Fotospot mit der Kirche Saint-Georges im Hintergrund."
    },
    "lyon_37": {
        "tip_en": "Rent a Vélo'v public bike for just €1.80 to ride down the landscaped traffic-free Rhône riverbanks past barge bars and parks.",
        "tip_ja": "レンタル自転車『Vélo'v』を借りてローヌ川沿いの専用サイクリングロードを走るのが爽快！川沿いの船上バー（Péniche）で一杯飲むのも最高。",
        "tip_es": "Alquila una bicicleta pública Vélo'v para recorrer el paseo del Ródano pasando por bares en barcazas.",
        "tip_zh": "租一辆Vélo'v公共自行车沿着罗讷河畔无车景观绿道骑行！沿途有许多由停泊船只改建的船上酒馆。",
        "tip_fr": "Louez un vélo Vélo'v pour parcourir les berges du Rhône aménagées et boire un verre sur une péniche.",
        "tip_de": "Mieten Sie ein Vélo'v-Fahrrad und radeln Sie die verkehrsfreien Flussufer der Rhône entlang."
    },
    "lyon_38": {
        "tip_en": "Hidden hilltop park gifted by the city of Montreal. Offers the most quiet, uncrowded sunset view over Lyon.",
        "tip_ja": "カナダ・モントリオール市から贈られた小公園。知る人ぞ知る丘の上の隠れた展望台で、混雑なしでリヨン市街の夕焼けを楽しめます！",
        "tip_es": "Parque tranquilo en la colina regala por la ciudad de Montreal. La vista panorámica al atardecer es preciosa.",
        "tip_zh": "由加拿大蒙特利尔市赠送的清静山顶小公园。这里是远离游客喧嚣、静静观赏里昂日落城景的私藏宝地。",
        "tip_fr": "Petit parc méconnu offert par la ville de Montréal offrant une vue panoramique paisible sur la ville.",
        "tip_de": "Ein ruhiger Geheimtipp-Park auf dem Hügel, geschenkt von der Stadt Montreal, mit toller Aussicht zum Sonnenuntergang."
    },
    "lyon_39": {
        "tip_en": "Modern eco-district at the southern tip featuring striking colorful contemporary architecture, water basins, and shopping mall.",
        "tip_ja": "かつての港湾倉庫街を最新エコカルチャー地区へと再開発。斬新なデザイン建築（緑のアナグラ建物など）と水辺のショッピングモール。",
        "tip_es": "Distrito ecológico moderno con arquitectura contemporánea de vanguardia y centros comerciales junto al agua.",
        "tip_zh": "由旧码头仓储区全面改造的现代前卫生态区。拥有一系列撞色未来感现代建筑与滨水商业中心。",
        "tip_fr": "Quartier moderne d'architecture contemporaine colorée et écologique situé entre les deux fleuves.",
        "tip_de": "Moderne Öko-Architektur auf dem ehemaligen Hafengelände an der Spitze der Halbinsel."
    },
    "lyon_40": {
        "tip_en": "Peaceful river island on the Saône with a 5th-century monastery ruin and famous gourmet restaurant Auberge de l'Île.",
        "tip_ja": "ソーヌ川に浮かぶ静かな島。5世紀のロマネスク様式の聖堂遺構があり、都心の喧騒から離れたノスタルジックな散策にぴったり。",
        "tip_es": "Isla idílica en el río Saona con ruinas de un monasterio del siglo V y un famoso restaurante gastronómico.",
        "tip_zh": "索恩河中央一座宁静的小岛。保留有5世纪本笃会修道院遗迹与风景宜人的法式农家古餐馆。",
        "tip_fr": "Île paisible sur la Saône abritant des vestiges d'une abbaye du Ve siècle et un restaurant gastronomique.",
        "tip_de": "Idyllische Flussinsel in der Saône mit Ruinen eines Klosters aus dem 5. Jahrhundert."
    },
    "lyon_41": {
        "tip_en": "Ranked among France's most beautiful villages (30 min drive from Lyon). Famous for its Galette au sucre (warm sugar-butter tart).",
        "tip_ja": "リヨンから車/バスで30分。『フランスで最も美しい村』の一つ。中世の石畳の小道と名物の温かい砂糖タルト（Galette de Pérouges）が絶品。",
        "tip_es": "Uno de los pueblos más bonitos de Francia (a 30 min de Lyon). Prueba su famosa Galette de azúcar recién horneada.",
        "tip_zh": "入选“法国最美小镇”的中世纪巨石村落（距里昂30分钟）。务必品尝热气腾腾的名产黄油糖饼（Galette au sucre）。",
        "tip_fr": "Classé parmi les plus beaux villages de France à 30 min de Lyon. Goûtez la délicieuse galette au sucre chaude.",
        "tip_de": "Eines der schönsten Dörfer Frankreichs (30 Min. von Lyon). Probieren Sie die warme Galette au Sucre."
    },
    "lyon_42": {
        "tip_en": "France's largest urban park featuring a FREE zoo with giraffes and zebras, a lake with rowboats, and giant botanical greenhouses.",
        "tip_ja": "フランス最大の都市公園！園内にはキリンやシマウマが自由に歩く無料動物園、ボートが浮かぶ湖、大温室が広がり完全無料で楽しめます。",
        "tip_es": "El parque urbano más grande de Francia con zoológico GRATUITO con jirafas, lago con barcas e invernaderos botánicos.",
        "tip_zh": "全法国最大的城市绿地公园！内设完全免费开放的大型野生动物园（长颈鹿与斑马）、划船人工湖与巨型大温室。",
        "tip_fr": "Plus grand parc urbain de France abritant un parc zoologique 100% GRATUIT (girafes, zèbres), un lac et de grandes serres.",
        "tip_de": "Größter Stadtpark Frankreichs mit einem KOSTENLOSEN Zoo (Giraffen, Zebras), einem Bootssüff und großen Gewächshäusern."
    },
    "lyon_43": {
        "tip_en": "Catch a live traditional Guignol puppet show in Vieux Lyon—hilarious fun for both kids and adults (performed in French).",
        "tip_ja": "旧市街にあるギニョール劇場。職人が目の前で木偶人形を操る風刺コミックショーは言葉が100%分からなくても楽しめます！",
        "tip_es": "Disfruta de un espectáculo de marionetas tradicionales de Guignol en directo en el Vieux Lyon.",
        "tip_zh": "位于旧城区的Guignol木偶剧场。演员现场操纵传统木偶演绎诙谐风趣的剧目，极其适合家庭观赏。",
        "tip_fr": "Assistez à un spectacle traditionnel de guignol en direct dans le Vieux Lyon pour toute la famille.",
        "tip_de": "Erleben Sie eine traditionelle Guignol-Puppenshow im Vieux Lyon – ein Riesenspaß für die ganze Familie."
    },
    "lyon_44": {
        "tip_en": "Located along the Rhône featuring 40+ aquariums with tropical sharks, piranhas, and tactile pools for kids.",
        "tip_ja": "ローヌ川沿いの水族館。淡水魚からサメやエイが泳ぐ熱帯大水槽まで、雨の日のファミリー観光にぴったりのスポット。",
        "tip_es": "Acuario junto al Ródano con tiburones tropicales, pirañas y tanques táctiles ideales para familias.",
        "tip_zh": "位于罗讷河畔的大型水族馆。展示有热带鲨鱼、食人鱼及触摸互动水池，是雨天带娃的绝佳去处。",
        "tip_fr": "Aquarium situé au bord du Rhône comprenant plus de 40 bassins avec requins et poissons tropicales.",
        "tip_de": "Aquarium an der Rhône mit über 40 Becken, Haien und Rochen – ideal für einen Ausflug bei Regen."
    },
    "lyon_45": {
        "tip_en": "Huge indoor miniature world featuring 70,000 mini residents, moving trains, cars, and animated day-night lighting cycles.",
        "tip_ja": "7万人のミニ人物や動くミニ電車、車、遊園地が精密に再現された屋内ミニチュアテーマパーク。昼と夜が20分おきに入れ替わります！",
        "tip_es": "Parque temático cubierto en miniatura con 70.000 habitantes diminutos y trenes en movimiento.",
        "tip_zh": "巨大全天候室内微缩世界！拥有7万名微型居民、跑动的火车汽车与每20分钟循环一次的日夜打光系统。",
        "tip_fr": "Parc de loisirs miniature animé couvert avec 70 000 personnages, trains en mouvement et effets jour/nuit.",
        "tip_de": "Riesiges überdachtes Miniaturland mit 70.000 Mini-Einwohnern, fahrenden Zügen und Tag-Nacht-Lichtwechsel."
    },
    "lyon_46": {
        "tip_en": "Features an immersive 360-degree digital dome projector for astronomy shows and space exploration exhibits.",
        "tip_ja": "360度ドーム型デジタルプラネタリウム。宇宙の神秘や星空を体験できる最新の科学教育施設。",
        "tip_es": "Proyector digital de cúpula de 360 grados para espectáculos de astronomía y exploraciones espaciales.",
        "tip_zh": "拥有360度全景数字穹顶投影仪的现代天文馆。沉浸感极强，提供精彩的浩瀚宇宙探索秀。",
        "tip_fr": "Planetarium doté d'un dôme numérique à 360° pour des spectacles d'astronomie immersifs.",
        "tip_de": "Planetarium mit einer 360-Grad-Digitalkuppel für faszinierende Weltraum-Shows."
    }
}

bordeaux_tips = {
    "bo_1": {
        "tip_en": "Visit at dusk when the 18th-century palace facade illuminates and reflects perfectly in the 2cm shallow water mirror.",
        "tip_ja": "日没直後のブルーアワーの訪問が最高！宮殿の金色ライトアップが水深2cmの『水鏡（Miroir d'eau）』に完璧に映り込む奇跡の絶景写真が撮れます。",
        "tip_es": "Visítalo al atardecer cuando la fachada del palacio se ilumina y se refleja perfectamente en el agua.",
        "tip_zh": "推荐黄昏华灯初上时前往！18世纪宫殿建筑倒映在2厘米深的‘水镜’中，呈现令人窒息的魔幻美感。",
        "tip_fr": "À admirer au coucher du soleil quand l'éclairage du palais du XVIIIe siècle se reflète magnifiquement sur l'eau.",
        "tip_de": "Besuchen Sie den Platz in der Dämmerung, wenn sich die beleuchtete Fassade perfekt im Wasser spiegelt."
    },
    "bo_2": {
        "tip_en": "Famed for its 12 Corinthian columns topped with statues of Muses and Goddesses. Inspired the design of the Paris Opera Garnier!",
        "tip_ja": "パリのオペラ座のモデルとなった18世紀の新古典主義劇場。正面ファサードの12本のコリンス式柱と女神像が荘厳です。",
        "tip_es": "Teatro neoclásico del siglo XVIII con 12 columnas coronadas por estatuas. Inspiró la Ópera de París.",
        "tip_zh": "巴黎歌剧院（Garnier）的建造灵感原型！正面立着12根矗立着女神雕像的科林斯柱，极具新古典主义气派。",
        "tip_fr": "Chef-d'œuvre néoclassique du XVIIIe siècle avec ses 12 statues de muses. A inspiré l'Opéra Garnier de Paris.",
        "tip_de": "Klassizistisches Meisterwerk des 18. Jahrhunderts mit 12 Musen-Statuen, das die Pariser Oper inspirierte."
    },
    "bo_3": {
        "tip_en": "Climb the 229 steps of the standalone Pey-Berland bell tower for THE ultimate 360-degree view over Bordeaux.",
        "tip_ja": "大聖堂横に独立して立つ『ペイ・ベルランの塔』の229段の階段を登ると、ボルドー市街地を360度見渡す最高の展望台に到達します！",
        "tip_es": "Sube los 229 escalones de la torre campanario Pey-Berland para disfrutar de la mejor vista de Burdeos.",
        "tip_zh": "攀登大教堂旁独立的Pey-Berland钟楼（229级阶梯），顶层是揽尽波尔多红瓦名城与加龙河的全景第一位。",
        "tip_fr": "Grimpez les 229 marches de la Tour Pey-Berland adjacente pour la plus belle vue à 360° sur les toits de Bordeaux.",
        "tip_de": "Erklimmen Sie die 229 Stufen des freistehenden Glockenturms Pey-Berland für die beste Aussicht auf Bordeaux."
    },
    "bo_4": {
        "tip_en": "15th-century fairytale medieval gate. Climb inside to see historical defense displays and views over the Garonne river.",
        "tip_ja": "15世紀の中世の歴史的城門。門内部（有料）に登ると昔の防衛器具やガロンヌ川を眺める窓からの景色が楽しめます。",
        "tip_es": "Puerta medieval del siglo XV. Sube a su interior para ver la exposición de defensa y vistas del río.",
        "tip_zh": "建于15世纪童话般的古老城门。可登入塔楼内部参观古要塞防卫设施并俯瞰加龙河。",
        "tip_fr": "Superbe porte médiévale du XVe siècle. Montez à l'intérieur pour découvrir son histoire et la vue sur la Garonne.",
        "tip_de": "Wunderschönes mittelalterliches Stadttor aus dem 15. Jahrhundert. Der Innenraum bietet tolle Ausblicke auf die Garonne."
    },
    "bo_5": {
        "tip_en": "One of France's oldest belfries featuring a 7.8-ton giant bronze bell 'Armande-Louise' cast in 1775.",
        "tip_ja": "ボルドー旧市街のシンボルである大鐘楼。1775年に鋳造された重さ7.8トンの大鐘『アルマンド＝ルイーズ』が中に吊るされています。",
        "tip_es": "Uno de los campanarios más antiguos de Francia con una campana de bronce gigante de 7.8 toneladas.",
        "tip_zh": "法国最古老的钟楼城门之一。塔楼内部悬挂着1775年铸造、重达7.8吨的巨型青铜古钟“Armande-Louise”。",
        "tip_fr": "L'un des plus anciens beffrois de France abritant la cloche géante 'Armande-Louise' de 7,8 tonnes.",
        "tip_de": "Einer der ältesten Glockentürme Frankreichs mit der 7,8 Tonnen schweren Bronzeglocke 'Armande-Louise'."
    },
    "bo_6": {
        "tip_en": "The standalone Gothic spire 'Flèche Saint-Michel' (114m) is the 2nd tallest bell tower in France. Explore the vintage flea market on Place Saint-Michel below.",
        "tip_ja": "高さ114mの独立したゴシック様式の尖塔。広場では毎週ヴィンテージのフリーマーケット（蚤の市）が開催され賑わいます。",
        "tip_es": "La aguja gótica de 114 metros es el segundo campanario más alto de Francia. Mercado de pulgas abajo.",
        "tip_zh": "高达114米的独立哥特式哥特尖塔，为全法第二高钟楼。教堂下方圣米歇尔广场常举办复古跳蚤集市。",
        "tip_fr": "Sa flèche gothique indépendante de 114m est la 2e plus haute de France. Brocante animée au pied de la basilique.",
        "tip_de": "Der freistehende 114 Meter hohe gotische Turm ist der zweithöchste Frankreichs. Bunter Flohmarkt auf dem Platz."
    },
    "bo_7": {
        "tip_en": "Europe's largest square featuring a 54m column with sea horses and bronze fountain statues symbolizing Liberty.",
        "tip_ja": "ヨーロッパ最大規模の広場！中央に聳える54mの記念柱と、荒波を駆けるブロンズの海馬噴水彫刻の躍動感が圧巻です。",
        "tip_es": "La plaza más grande de Europa con una columna de 54 metros y fuentes con estatuas de caballos marinos de bronce.",
        "tip_zh": "欧洲面积最大的广场！中央耸立着54米高的柱基纪念碑，脚下奔腾的青铜战马巨型喷泉气势极其恢宏。",
        "tip_fr": "La plus grande place d'Europe dotée d'une colonne de 54m et de spectaculaires fontaines aux chevaux marins.",
        "tip_de": "Europas größter unbebauter Platz mit dem 54m hohen Monument und den beeindruckenden Seepferdchen-Fontänen."
    },
    "bo_8": {
        "tip_en": "Remains of a 2nd-century Roman amphitheatre tucked in a residential neighbourhood—free to view from the street edge.",
        "tip_ja": "2世紀のガロ・ローマ時代の巨大円形劇場の遺構。閑静な住宅街の中に突如現れる古代のアーチ遺構を通りから無料で見学できます。",
        "tip_es": "Restos de un anfiteatro romano del siglo II escondidos en un barrio residencial. Visible gratis desde la calle.",
        "tip_zh": "隐匿于安静住宅区中的2世纪古罗马圆形剧场遗迹。在街道旁即可免费全景观赏古石拱砌墙。",
        "tip_fr": "Vestiges romantiques d'un amphithéâtre gallo-romain du IIe siècle visibles gratuitement depuis la rue.",
        "tip_de": "Überreste eines römischen Amphitheaters aus dem 2. Jahrhundert, kostenfrei von der Straße aus zu betrachten."
    },
    "bo_9": {
        "tip_en": "Historic 17-arch stone bridge commissioned by Napoleon Bonaparte. Offers gorgeous sunset views over Place de la Bourse.",
        "tip_ja": "ナポレオンの命により建設された17のアーチを持つ石橋。橋の上からの夕焼けと対岸のブルス広場の景色がロマンチック！",
        "tip_es": "Puente de piedra de 17 arcos mandado construir por Napoleón Bonaparte con espectaculares atardeceres.",
        "tip_zh": "拿破仑下令修建的拥有17座拱洞的古石桥。漫步桥上观赏夕阳斜照在对岸ブルス広場上的金光堪称美绝。",
        "tip_fr": "Pont en pierre de 17 arches commandé par Napoléon Ier. Superbe endroit pour contempler le coucher de soleil sur la ville.",
        "tip_de": "Historische Steinbrücke mit 17 Bögen, von Napoleon in Auftrag gegeben. Herrlicher Ort für Sonnenuntergänge."
    },
    "bo_10": {
        "tip_en": "Imposing medieval castle rebuilt by Viollet-le-Duc in the 19th century—looks like a fairytale fortress set in green woods.",
        "tip_ja": "ノートルダム大聖堂を手掛けた建築家ヴィオレ・ル・デュクが19世紀に内装を再建した中世の絵本のような要塞城。",
        "tip_es": "Impresionante castillo medieval reconstruido por Viollet-le-Duc en el siglo XIX entre frondosos bosques.",
        "tip_zh": "由著名建筑家Viollet-le-Duc于19世纪精心重修的中世纪城堡，矗立于森林绿意中，宛如童话梦幻要塞。",
        "tip_fr": "Spectaculaire château fort médiéval sublimé par Viollet-le-Duc au XIXe siècle au milieu de la forêt.",
        "tip_de": "Spektakuläre mittelalterliche Burg, im 19. Jahrhundert von Viollet-le-Duc restauriert. Wie aus dem Märchenbuch."
    },
    "bo_11": {
        "tip_en": "Moated feudal castle where philosopher Montesquieu lived and wrote 'The Spirit of Law'. Beautiful English landscape park.",
        "tip_ja": "思想家モンテスキューが『法の精神』を執筆した水掘に囲まれた城館。広大な英国式庭園の散策が心地よいです。",
        "tip_es": "Castillo rodeado por un foso donde el filósofo Montesquieu escribió 'El espíritu de las leyes'.",
        "tip_zh": "著名启蒙思想家孟德斯鸠在此撰写《论法的精神》的古堡。周围环绕着碧水护城河与浪漫的英式花园。",
        "tip_fr": "Château entouré de douves où le philosophe Montesquieu a écrit 'L'Esprit des lois'. Magnifique parc à l'anglaise.",
        "de": "Wasserschloss, in dem der Philosoph Montesquieu 'Vom Geist der Gesetze' schrieb. Wunderschöner englischer Park."
    },
    "bo_12": {
        "tip_en": "High-tech wine museum with interactive tasting galleries. Your ticket includes a glass of world wine on the 35m panoramic Belvedere deck!",
        "tip_ja": "デキャンタを模した未来派建築！チケットに最上階8階（35m）の展望デッキでの『世界の名醸ワイン1杯試飲』が含まれています！",
        "tip_es": "Museo interactivo del vino. ¡Tu entrada incluye una copa de vino gratis en la terraza panorámica de 35 metros!",
        "tip_zh": "造型宛如醒酒器的高科技葡萄酒博览馆。门票直接包含在35米高的8楼全景观景台免费品尝一杯世界佳酿！",
        "tip_fr": "Cité du vin interactive à l'architecture audacieuse. Votre billet inclut un verre de vin au belvédère panoramique à 35m !",
        "tip_de": "Interaktives Weinmuseum mit futuristischer Architektur. Das Ticket beinhaltet ein Glas Wein auf der 35m Aussichtsplattform!"
    },
    "bo_13": {
        "tip_en": "World's largest digital art center inside a WWII submarine base. Immersive 360-degree light projections of Klimt, Monet, and Dalí onto water basins.",
        "tip_ja": "第二次大戦中の潜水艦基地を利用した世界最大のデジタルアート空間！巨大な水槽にクリムトやモネの光の絵画が映し出されます。",
        "tip_es": "El centro de arte digital más grande del mundo en una base de submarinos de la II Guerra Mundial con luz sobre el agua.",
        "tip_zh": "利用二战时期建造的潜艇基地打造的全球最大数字艺术中心！克里姆特与莫奈的名画被光影投射在巨大的水槽与水泥巨墙之上。",
        "tip_fr": "Le plus grand centre d'art numérique au monde dans una ancienne base sous-marine de la Seconde Guerre mondiale.",
        "tip_de": "Größtes Zentrum für digitale Kunst der Welt in einer ehemaligen U-Boot-Basis der WWII mit Projektionen auf Wasserbecken."
    },
    "bo_14": {
        "tip_en": "Explores Aquitaine's rich history from Eleanor of Aquitaine to Bordeaux's maritime trade history and Roman artifacts.",
        "tip_ja": "アキテーヌ地方の歴史を辿る大博物館。古代ローマ時代の彫刻、アキテーヌ女公エレノアの歴史、ガロンヌ川の貿易歴史が学べます。",
        "tip_es": "Recorre la rica historia de Aquitania desde la época romana hasta el comercio marítimo de Burdeos.",
        "tip_zh": "展示阿基坦大区自古罗马时代、阿基坦埃莉诺女公爵至波尔多航海贸易鼎盛期的全景历史博物馆。",
        "tip_fr": "Musée passionnant retraçant l'histoire de la région de la Préhistoire à nos jours (trésors gallo-romains).",
        "de": "Spannendes Museum zur Geschichte Aquitaniens von den Römern über Eleanor von Aquitanien bis heute."
    },
    "bo_15": {
        "tip_en": "Housed in two wings of the City Hall featuring Old Master paintings by Delacroix, Rubens, Titian, and Matisse.",
        "tip_ja": "市庁舎裏手に位置する美術館。ドラクロワ、ルーベンス、マティスなどのクラシック絵画コレクションが静かに楽しめます。",
        "tip_es": "Ubicado en el Ayuntamiento con pinturas de maestros clásicos como Delacroix, Rubens y Titian.",
        "tip_zh": "位于市政厅建筑后方两侧展翼内。收藏有德拉克罗瓦、鲁本斯及马蒂斯等名家的高品质古典画作。",
        "tip_fr": "Installé dans les deux ailes de l'Hôtel de Ville abritant des chefs-d'œuvre de Delacroix, Rubens et Matisse.",
        "de": "In zwei Flügeln des Rathauskomplexes mit Meisterwerken von Delacroix, Rubens und Matisse."
    },
    "bo_16": {
        "tip_en": "Housed in a 19th-century brick wool warehouse with soaring vaulted ceilings featuring cutting-edge modern installations.",
        "tip_ja": "19世紀の羊毛倉庫を改装した現代美術館。赤レンガの重厚な天井アーチと先端現代アートのギャップが魅力的。",
        "tip_es": "Museo en un antiguo almacén de lana del siglo XIX con impresionantes bóvedas de ladrillo e instalaciones modernas.",
        "tip_zh": "由19世纪巨型红砖羊毛仓库改建的当代美术馆。高达挑空的红砖拱顶与前沿当代装置艺术形成震撼对比。",
        "tip_fr": "Musée d'art contemporain spectaculaire installé dans un ancien entrepôt de laine du XIXe siècle.",
        "de": "Museum für zeitgenössische Kunst in einem ehemaligen Lagerhaus für Wolle aus dem 19. Jahrhundert."
    },
    "bo_17": {
        "tip_en": "Housed in Hôtel de Lalande displaying 18th-century porcelain, French furniture, design objects, and glass art.",
        "tip_ja": "18世紀のラランド伯爵邸を利用。フランスの伝統的な高級家具、18世紀の磁器、モダンデザインコレクションを展示。",
        "tip_es": "Ubicado en un palacete del siglo XVIII con muebles franceses, porcelana de Burdeos y diseño moderno.",
        "tip_zh": "设于18世纪的Lalande伯爵府邸内。陈列有法国古典皇家家具、瓷器及现代工业设计精品。",
        "tip_fr": "Installé dans un superbe hôtel particulier du XVIIIe siècle dédié aux arts décoratifs et au design.",
        "de": "In einem prächtigen Stadtpalais des 18. Jahrhunderts mit Kunsthandwerk, Möbeln und modernem Design."
    },
    "bo_18": {
        "tip_en": "Maritime museum exploring sea navigation, ship models, ocean exploration, and maritime art near Bassins des Lumières.",
        "tip_ja": "海洋と舟運の総合博物館。巨大な帆船模型や深海探査船、海洋画のコレクションが見事でファミリーにも人気。",
        "tip_es": "Museo marítimo cerca de Bassins des Lumières con maquetas de barcos, arte naval y exploración oceánica.",
        "tip_zh": "紧邻 Bassins des Lumières 的海事博物馆。陈列有精美古董帆船模型、深海潜航器与海洋主题画作。",
        "tip_fr": "Grand musée maritime privé présentant de superbes maquettes de bateaux et l'histoire de la navigation.",
        "tip_de": "Großes Maritimes Museum mit Schiffsmodellen, Meeresforschung und maritimer Kunst."
    },
    "bo_19": {
        "tip_en": "Located inside Place de la Bourse exploring the history of customs, contraband smuggling, and trade taxes since 1785.",
        "tip_ja": "ブルス広場の建物内にあるフランス唯一の税関博物館。歴史的な密輸品や関税の歴史を展示したユニークなスポット。",
        "tip_es": "El único museo de aduanas de Francia ubicado en la Place de la Bourse sobre la historia del contrabando.",
        "tip_zh": "位于ブルス広場建筑物内、全法唯一的海关博物馆。有趣地展出了历史上各种查获的密谋走私品与关税变迁。",
        "tip_fr": "Unique musée national des douanes en France retraçant l'histoire de la douane et des contrebandes sur la Place de la Bourse.",
        "tip_de": "Einziges Zollmuseum Frankreichs am Place de la Bourse über die Geschichte des Zolls und des Schmuggels."
    },
    "bo_20": {
        "tip_en": "Bordeaux's bustling central food market. Enjoy fresh oysters from Arcachon paired with a glass of dry white wine at Sunday lunch!",
        "tip_ja": "ボルドー市民の台所！日曜のランチに、近くのアルカション湾で獲れた新鮮な生牡蠣（Oysters）と冷えた白ワインを市場内のスタンドで味わうのが絶対の習慣です。",
        "tip_es": "¡El ruidoso mercado gourmet de Burdeos! Disfruta de ostras frescas de Arcachón con vino blanco seco los domingos.",
        "tip_zh": "波尔多最火爆的美食大集市！周日午餐时段在市场档口点一盘来自阿尔卡雄湾的现开鲜生蚝并配一杯干白葡萄酒最过瘾。",
        "tip_fr": "Le marché le plus populaire de Bordeaux ! Dégustez des huîtres fraîches du Bassin d'Arcachon avec un verre de blanc le dimanche matin.",
        "tip_de": "Der lebendigste Markt von Bordeaux! Sonntags frische Austern aus Arcachon mit einem Glas Weißwein vor Ort genießen."
    },
    "bo_21": {
        "tip_en": "Authentic regional restaurant. Order Entrecôte marchand de vin (ribeye steak with wine sauce) and Cèpes à la bordelaise.",
        "tip_ja": "地元の食通が通うブラッスリー。ボルドーワインソースの赤身ステーキや地元産セップ茸のソテーをワイン蔵の雰囲気で楽しめます。",
        "tip_es": "Brasserie regional auténtica. Pide el filete entrecôte con salsa de vino y setas cèpes a la bordelesa.",
        "tip_zh": "波尔多地道餐馆。必点红酒汁煎肋眼牛排（Entrecôte marchand de vin）与法式牛肝菌炒波尔多。",
        "tip_fr": "Brasserie chaleureuse bordelaise. Dégustez une entrecôte marchande de vin et des cèpes à la bordelaise.",
        "tip_de": "Traditionelle Brasserie. Probieren Sie das Entrecôte in Rotweinsauce und Steinpilze nach Bordelaiser Art."
    },
    "bo_22": {
        "tip_en": "Bordeaux's signature caramelised rum-vanilla pastry. Compare 'Baillardran' (traditional) with 'La Toque Cuivrée' (crispier and local favorite)!",
        "tip_ja": "ボルドー発祥の伝統焼き菓子『カヌレ』！老舗の『Baillardran』と、地元客に愛される安くてカリカリの『La Toque Cuivrée』の食べ比べが楽しい！",
        "tip_es": "¡El dulce emblemático de Burdeos! Compara el Canelé tradicional de Baillardran con el de La Toque Cuivrée.",
        "tip_zh": "波尔多标志性波尔多朗姆酒香草可丽露（Canelé）！不妨将老字号Baillardran与本地人偏爱且更酥脆性价比高的La Toque Cuivrée对比品尝！",
        "tip_fr": "Le gâteau mythique bordelais parfumé au rhum et à la vanille ! Comparez Baillardran et La Toque Cuivrée.",
        "tip_de": "Das berühmte Bordelaiser Vanille-Rum-Gebäck Canelé! Vergleichen Sie Baillardran mit La Toque Cuivrée."
    },
    "bo_23": {
        "tip_en": "Run by the official Bordeaux Wine Council inside an 18th-century flatiron building. Enjoy grand cru wines by the glass for just €3–€6!",
        "tip_ja": "ボルドーワイン委員会（CIVB）直営バー。フラットアイアン型の歴史的建物で、一流格付けワインのグラスが驚きの€3〜€6で味わえます！",
        "tip_es": "Gestionado por el Consejo del Vino de Burdeos. ¡Disfruta de copas de grandes vinos de Burdeos por solo 3€ a 6€!",
        "tip_zh": "由波尔多葡萄酒官方委员会直营！在这座18世纪熨斗大楼内，只要3–6欧元即可在优雅酒吧享用由侍酒师推荐的高档 Grand Cru 葡萄酒！",
        "tip_fr": "Bar officiel du Conseil des Vins de Bordeaux. Dégustez des grands vins bordelais au verre à prix doux (3 € à 6 €) !",
        "tip_de": "Offizielle Bar des Weinrates von Bordeaux. Hochklassige Bordeaux-Weine im Glas für nur 3 € bis 6 € verkosten!"
    },
    "bo_24": {
        "tip_en": "Classic cafe terrace on Place de la Comédie right opposite the Grand Théâtre. Perfect spot for people watching with coffee.",
        "tip_ja": "コメディ広場のグランド・シアター真向かいにある老舗カフェ。テラス席でエスプレッソを飲みながら行き交う人々を眺めるのに最適。",
        "tip_es": "Café clásico con terraza en la Place de la Comédie frente al Grand Théâtre.",
        "tip_zh": "位于Comédie广场大剧院正对面的优雅咖啡馆露台。坐在外侧喝咖啡观赏广场上穿梭的人流极其舒适。",
        "tip_fr": "Terrasse de café mythique sur la Place de la Comédie face au Grand Théâtre.",
        "tip_de": "Klassisches Café mit Terrasse auf dem Place de la Comédie direkt gegenüber dem Grand Théâtre."
    },
    "bo_25": {
        "tip_en": "Famous single-menu restaurant serving trimmed ribeye steak with secret green sauce and unlimited crispy french fries (expect lines!).",
        "tip_ja": "メニューは秘伝のグリーンソースのステーキのみ！山盛りのフレンチフライがおかわり自由で味わえる大行列の人気店。",
        "tip_es": "Famoso restaurante con un único menú: filete de carne con su salsa verde secreta y patatas fritas ilimitadas.",
        "tip_zh": "火爆大排长龙的单菜谱餐厅！只提供切片肋眼牛排配特制秘方秘制绿酱，以及无限量续添的金黄酥脆薯条。",
        "tip_fr": "Institution célèbre proposant un menu unique : entrecôte avec sa sauce verte secrète et frites à volonté !",
        "tip_de": "Berühmtes Restaurant mit einem einzigen Menü: Steak mit geheimer grüner Sauce und unbegrenzten Pommes Frites."
    },
    "bo_26": {
        "tip_en": "Book châteaux winery tours in advance (Saint-Émilion or Médoc). Half-day tasting tours leave daily from the Bordeaux Tourist Office.",
        "tip_ja": "サン・テミリオンやメドック地区の格付けシャトー（ワイナリー）巡りは事前予約が必須。観光局発の半日バスツアーも便利です。",
        "tip_es": "Reserva tours a las bodegas (Châteaux) de Saint-Émilion o Médoc con antelación desde la Oficina de Turismo.",
        "tip_zh": "探访圣埃美隆或梅多克一级名庄（Châteaux）酒庄必须提前官预。波尔多旅游局每天都有半日游品酒大巴出发。",
        "tip_fr": "Réservez vos visites de châteaux viticoles à Saint-Émilion ou dans le Médoc à l'avance auprès de l'Office de Tourisme.",
        "tip_de": "Weingutsführungen (Châteaux) in Saint-Émilion oder im Médoc im Voraus buchen. Bus-Touren starten täglich."
    },
    "bo_27": {
        "tip_en": "Charming medieval pedestrian cobblestone district packed with wine bars, bistros, and small squares near Place du Parlement.",
        "tip_ja": "パルルマン広場周辺の歴史的石畳エリア。ワインバー、小粋なビストロ、カフェが立ち並び、夜のディナー散策に最高。",
        "tip_es": "Encantador barrio peatonal medieval con calles empedradas lleno de bares de vinos y terrazas.",
        "tip_zh": "由鹅卵石铺就的中世纪古朴步行区。汇聚了无数独立葡萄酒酒吧、优雅小馆与Parlement广场露台。",
        "tip_fr": "Quartier piéton médiéval pavé rempli de bars à vins, de terrasses et de petits bistrots chaleureux.",
        "de": "Malerisches mittelalterliches Fußgängerviertel mit Kopfsteinpflaster, Weinbars und gemütlichen Plätzen."
    },
    "bo_28": {
        "tip_en": "Former wine merchants' quarter turned trendy bohemian hub with antique shops, art galleries, and Sunday organic markets.",
        "tip_ja": "かつてのワイン商人街。現在は骨董品店、ヴィンテージショップ、カフェが集まるオシャレなボヘミアン地区。",
        "tip_es": "Antiguo barrio de comerciantes de vino reconvertido en zona bohemia con tiendas de antigüedades y galerías.",
        "zh": "昔日酒商云集的历史街区。如今重构为汇集骨董古玩店、艺术画廊与周日有机集市的前卫区。",
        "tip_fr": "Ancien quartier des négociants en vin devenu un secteur branché avec ses antiquaires et ses boutiques déco.",
        "tip_de": "Ehemaliges Weinhändlerviertel, heute ein Trendviertel mit Antiquitätenläden, Galerien und Cafés."
    },
    "bo_29": {
        "tip_en": "Rent a city bike or jog down the 4.5km landscaped promenade along the Garonne river past red brick warehouses and gardens.",
        "tip_ja": "ガロンヌ川沿いに広がる長さ4.5kmの美しいリバーサイドプロムナード。自転車走行やサンセット時のウォークが快適。",
        "tip_es": "Recorre el paseo marítimo de 4.5 km a lo largo del río Garona en bicicleta o caminando al atardecer.",
        "tip_zh": "沿着加龙河畔绵延4.5公里的景观海滨长廊骑行或散步。途经老红砖仓库改建的休闲区，观赏落日绝佳。",
        "tip_fr": "Longue promenade aménagée de 4,5 km le long de la Garonne, idéale pour le vélo, la course ou une balade au soleil.",
        "tip_de": "Aktiv auf der 4,5 km langen neu gestalteten Promenade entlang der Garonne spazieren oder Rad fahren."
    },
    "bo_30": {
        "tip_en": "One of Europe's longest pedestrian shopping streets (1.2 km). Stroll past shops starting from Place Comédie towards Porte Dijeaux.",
        "tip_ja": "全長1.2kmにおよぶヨーロッパ最長級の歩行者天国ショッピング街！コメディ広場から始まり服飾店や百貨店が連なります。",
        "tip_es": "Una de las calles comerciales peatonales más largas de Europa (1.2 km) repleta de tiendas de moda.",
        "tip_zh": "全长1.2公里的欧洲最长步道购物街之一！自Comédie广场延伸开来，汇聚各类主流服装连锁与品牌店。",
        "tip_fr": "L'une des plus longues rues piétonnes commerçantes d'Europe (1,2 km) reliant la Comédie à la Victoire.",
        "tip_de": "Eine der längsten Fußgänger-Einkaufsstraßen Europas (1,2 km) voller Mode- und Schuhgeschäfte."
    },
    "bo_31": {
        "tip_en": "Hosts seasonal travelling funfairs, circus performances, and large wine festivals right by the Garonne river.",
        "tip_ja": "川沿いに広がるヨーロッパ最大級の広場。時期によっては大規模な移動遊園地（Foire aux Plaisirs）やワイン祭りが開催されます。",
        "tip_es": "Aloja ferias itinerantes, eventos culturales y grandes festivales del vino a lo largo del río.",
        "tip_zh": "位于加龙河畔的巨型露天广场。季节性会举办盛大的流动游乐场（Foire aux Plaisirs）与葡萄酒大嘉年华。",
        "tip_fr": "Hôte de grandes foires de saison, du cirque et de la Fête du Vin le long de la Garonne.",
        "tip_de": "Veranstaltungsort für große Jahrmärkte (Foire aux Plaisirs), Wanderzirkusse und das Weinfest."
    },
    "bo_32": {
        "tip_en": "Trendy alternative eco-hub inside former military barracks featuring an indoor skatepark, organic bistro, and street art graffiti.",
        "tip_ja": "かつての軍事施設をリノベしたエコ＆カルチャースペース。無農薬オーガニックレストラン、スケートパーク、鮮やかなストリートアート！",
        "tip_es": "Espacio alternativo en un antiguo cuartel militar con skatepark cubierto, restaurante ecológico y grafiteros.",
        "tip_zh": "由旧兵营改建的前卫环保文化生态圈。拥有大型室内滑板场、有机轻食餐厅与炫酷的涂鸦艺术墙。",
        "tip_fr": "Lieu alternatif branché dans une ancienne caserne avec skatepark couvert, bistro bio et fresques de street art.",
        "tip_de": "Trendiges Öko-Kreativzentrum in einer ehemaligen Kaserne mit Indoor-Skatepark, Bio-Bistro und Graffitis."
    },
    "bo_33": {
        "tip_en": "UNESCO World Heritage medieval wine village. Visit the monolithic underground church carved out of solid limestone rock!",
        "tip_ja": "ユネスコ世界遺産のワインの村（ボルドーから列車で35分）。巨大な一枚岩をくり抜いて作られた神秘的な『モノリス地下教会』は必見！",
        "tip_es": "Pueblo medieval vinícola Patrimonio de la Humanidad. Visita la iglesia monolítica subterránea excavada en la roca.",
        "tip_zh": "联合国教科文组织世界遗产中世纪红酒名村（距波尔多火车站35分钟）。切勿错过从一整块巨型石灰岩石开凿出的地下独石教堂（Monolithic Church）！",
        "tip_fr": "Village médiéval viticole classé UNESCO. Ne manquez pas la visite guidée de l'église monolithe souterraine creusée dans la roche !",
        "de": "Mittelalterliches UNESCO-Weindorf. Besuchen Sie die faszinierende unterirdische Monolithkirche im Fels!"
    },
    "bo_34": {
        "tip_en": "Europe's tallest sand dune (100m+ high). Climb the wooden stairs to the crest for sweeping views over the pine ocean and Atlantic Atlantic.",
        "tip_ja": "高さ100mを超えるヨーロッパ最大の砂丘！木製階段で頂上に登ると、緑の松林の海と青い大西洋の水平線が交差する絶景に息を飲みます。",
        "tip_es": "La duna de arena más alta de Europa (+100m). Sube por las escaleras para contemplar el océano y el bosque.",
        "tip_zh": "高逾100米的全欧洲最大巨型沙丘！攀登木楼梯登上沙脊顶端，将连绵绿意松林海与湛蓝大西洋交界线尽收眼底。",
        "tip_fr": "Plus haute dune de sable d'Europe (+100m). Grimpez au sommet pour un panorama grandiose entre forêt de pins et océan Atlantique !",
        "de": "Höchste Sanddüne Europas (über 100m). Der Blick vom Grat über den Atlantik und die Pinienwälder ist unvergesslich."
    },
    "bo_35": {
        "tip_en": "18th-century English-style botanical garden featuring a swan lake, puppet theatre for kids, and Natural History Museum.",
        "tip_ja": "18世紀に造られた美しい英国式公園。白鳥が泳ぐ池、自然史博物館、伝統の操り人形劇場があり市民の憩いの場。",
        "tip_es": "Jardín botánico del siglo XVIII con lago con cisnes, el Museo de Historia Natural y teatro de títeres.",
        "tip_zh": "建于18世纪的英式公立绿地公园。内有天鹅游弋的湖泊、自然历史博物馆与亲子木偶剧场。",
        "tip_fr": "Magnifique jardin à l'anglaise du XVIIIe siècle avec son lac aux cygnes, le Muséum et son guignol.",
        "de": "Wunderschöner englischer Garten des 18. Jahrhunderts mit Schwanensee und dem Naturhistorischen Museum."
    },
    "bo_36": {
        "tip_en": "Interactive science center next to the Chaban-Delmas lift bridge featuring hands-on workshops and stargazing events.",
        "tip_ja": "シャバン・デルマス昇降橋の足元にある体験型科学館。お子様向けの体験展示や夜間の天体観測イベントが人気。",
        "tip_es": "Centro de ciencias interactivo junto al puente elevador Chaban-Delmas con talleres para niños.",
        "tip_zh": "位于 Chaban-Delmas 升降大桥旁的互动科学中心。提供生动趣味的动手实验与星空观赏特别活动。",
        "tip_fr": "Centre de culture scientifique interactif au pied du pont Chaban-Delmas parfait pour les enfants.",
        "de": "Interaktives Wissenschaftszentrum am Fuß der Chaban-Delmas-Brücke mit tollen Mitmach-Ausstellungen."
    },
    "bo_37": {
        "tip_en": "Use the Bat3 public water transport shuttle (uses standard TBM transit tickets) for a budget river cruise along the city front!",
        "tip_ja": "市内交通チケット（TBM）で乗れる水上バス『Bat3』を利用すれば、格安でガロンヌ川のリバークルーズが楽しめます！",
        "tip_es": "Usa la naveta acuática pública Bat3 (funciona con el billete de transporte urbano TBM) para un crucero económico.",
        "tip_zh": "使用普通城市公交卡（TBM）即可乘坐Bat3公共水上巴士！以超低成本享受沿着加龙河两岸风光的轮渡游船体验。",
        "tip_fr": "Prenez le navette fluviale Bat3 (accessible avec un ticket de transport TBM) pour une mini-croisière économique sur la Garonne !",
        "de": "Nutzen Sie das öffentliche Wassertaxi Bat3 (mit TBM-Ticket gültig) für eine günstige Mini-Kreuzfahrt auf der Garonne!"
    },
    "bo_38": {
        "tip_en": "Sprawling 28-hectare park with roaming farm animals, a lake with duck boats, and historic carousels for families.",
        "tip_ja": "28ヘクタールの広大な市民公園。自由に行き来する動物たち（孔雀やヤギ）、ボート池、レトロなメリーゴーラウンドがあり子連れに人気。",
        "tip_es": "Parque de 28 hectáreas con animales de granja en libertad, lago con barcas y carrusel histórico.",
        "tip_zh": "占地28公顷的大型公共森林公园。放养着孔雀与小羊，拥有露天皮划艇湖泊与复古旋转木马。",
        "tip_fr": "Grand parc paysager de 28 hectares avec des animaux de ferme en liberté, un lac et des manèges anciens.",
        "de": "Riesiger 28-Hektar-Park mit frei herumlaufenden Bauernhoftieren, einem See und einem historischen Karussell."
    },
    "bo_39": {
        "tip_en": "Features rare white tigers, jaguars, and a 360-degree glass lodge where you can dine surrounded by big cats.",
        "tip_ja": "ボルドー郊外のペサック動物園。珍しいホワイトタイガーやジャガーが暮らす自然豊かな動物園。",
        "tip_es": "Zoológico cerca de Burdeos con raros tigres blancos, jaguares y recintos inmersivos.",
        "tip_zh": "位于波尔多郊区的Pessac动物园。拥有一对罕见珍贵的白老虎与美洲豹，深受家庭客群喜爱。",
        "tip_fr": "Parc zoologique abritant de rares tigres blancs, des jaguars et des espaces d'immersion.",
        "de": "Zoo bei Bordeaux mit seltenen weißen Tigern, Jaguaren und begehbaren Gehegen."
    },
    "bo_40": {
        "tip_en": "Outdoor treetop adventure park in the pine forest with zip-lines, rope bridges, and climbing courses for all age levels.",
        "tip_ja": "ボルドー近郊の松林の中にあるアスレチックパーク。木々の間に張られたジップラインやロープ橋でアクティブなアドベンチャー！",
        "tip_es": "Parque de aventuras en las copas de los árboles en el bosque de pinos con tirolinas y puentes colgantes.",
        "tip_zh": "松林中的大型树顶高空拓展探险公园。拥有高空滑索、悬空绳桥与多难度攀爬路线。",
        "tip_fr": "Parc d'accrobranche dans la forêt de pins avec tyroliennes et parcours dans les arbres pour tous les âges.",
        "de": "Kletterwald-Abenteuerpark im Pinienwald mit Seilrutschen und Parcours für alle Altersklassen."
    }
}

# Run updates
update_city_tips("nice.json", nice_tips)
update_city_tips("lyon.json", lyon_tips)
update_city_tips("bordeaux.json", bordeaux_tips)

print("🎉 Finished Batch 1 Insider Tips update!")
