import json
import os

# -------------------------------------------------------------
# Munich (60 Spots) Zero-Overlap & Practical Tips Refinement
# -------------------------------------------------------------

munich_refinements = {
    "m_1": { # Marienplatz & Neues Rathaus
        "tip_en": "⏰ Watch the mechanical Glockenspiel chime with 32 life-sized figures daily at 11:00 AM & 12:00 PM (plus 5:00 PM Mar–Oct) from the central square.",
        "tip_ja": "⏰ 仕掛け時計（Glockenspiel）のからくり人形ショーは毎日11:00と12:00（3月〜10月は17:00も追加）にスタート。広場中央から見上げると32体の人形のダンスがバッチリ見えます！",
        "tip_es": "⏰ Mira el carillón mecánico Glockenspiel con 32 figuras a tamaño real a las 11:00 y 12:00 h (y 17:00 h de mar. a oct.).",
        "tip_zh": "⏰ 钟楼偶戏人偶表演于每天11:00与12:00（3月至10月加演17:00场）准时开演！站在广场中央仰望观赏效果最佳。",
        "tip_fr": "⏰ Admirez le carillon mécanique du Glockenspiel à 11h et 12h (ainsi qu'à 17h de mars à octobre) au centre de la place.",
        "tip_de": "⏰ Das berühmte Glockenspiel mit 32 lebensgroßen Figuren spielt täglich um 11:00 und 12:00 Uhr (März–Okt. auch 17:00 Uhr)."
    },
    "m_2": { # Frauenkirche
        "tip_en": " Step onto the black tile 'Devil's Footprint' (Teufelstritt) at the entrance foyer. Look towards the altar—the columns block all side windows, making it seem windowless!",
        "tip_ja": " 入口風除室にある黒いタイル『悪魔の足跡（Teufelstritt）』の上に立ってください！祭壇方向を見ると列柱に隠れて側面の窓がすべて見えなくなり、悪魔が騙された伝説の視界を体験できます。",
        "tip_es": " Ponte sobre la 'Pisada del Diablo' en la entrada. Al mirar hacia el altar, las columnas ocultan las ventanas laterales.",
        "tip_zh": " 踩在入口地板黑色的“恶魔脚印”（Teufelstritt）之上！面向主祭坛，侧面所有窗户被石柱掩盖，重现恶魔被骗的古老传说视界。",
        "tip_fr": " Placez-vous sur l’'Empreinte du Diable' à l'entrée. En regardant l'autel, les colonnes masquent toutes les fenêtres.",
        "tip_de": " Stellen Sie sich auf den schwarzen 'Teufelstritt' im Eingangsbereich. Der Blick zum Altar lässt alle Seitenfenster verschwinden!"
    },
    "m_3": { # Residenz
        "tip_en": "🎟️ Buy the combined Residenz + Treasury (Schatzkammer) + Cuvilliés Theatre ticket. Touch the nose of the bronze lions at the Residenzstraße entrance for good luck!",
        "tip_ja": "🎟️ 宮殿・宝物館・キュビリエ劇場の3館共通チケットが圧倒的にお得。レジデンツ通りの入口に置かれたブロンズライオン像の鼻を触ると幸運が訪れるおまじないも忘れずに！",
        "tip_es": "🎟️ Compra la entrada combinada de Palacio + Tesoro + Teatro Cuvilliés. ¡Toca la nariz de los leones de bronce para la suerte!",
        "tip_zh": "🎟️ 强烈推荐加购包含宝物馆与Cuvilliés洛可可剧院的联票。入口处摸一摸青铜狮子雕像的鼻子可带来好运！",
        "tip_fr": "🎟️ Achetez le billet combiné Palais + Trésor + Théâtre Cuvilliés. Touchez le museau des lions en bronze pour porter bonheur !",
        "de": "🎟️ Kombiticket für Residenz + Schatzkammer + Cuvilliés-Theater kaufen. Die Nase der Bronzelöwen am Eingang für Glück berühren!"
    },
    "m_4": { # Schloss Nymphenburg
        "tip_en": "📸 Walk past the grand front canal to photograph swans gliding with the palace in the background. Don't miss King Ludwig I's Gallery of Beauties inside.",
        "tip_ja": "📸 正面の長い水路沿いは白鳥が泳ぎ宮殿が水面に映る写真スポット。宮殿内部ではルートヴィヒ1世が愛した女性36人の肖像画が並ぶ『美人画ギャラリー』が見どころです。",
        "tip_es": "📸 Pasea por el canal frontal para fotografiar cisnes con el palacio de fondo. Visita la Galería de las Bellezas en el interior.",
        "tip_zh": "📸 漫步于正前方长达数百米的水道，拍下天鹅在水面游弋与宫殿相映成趣的景象。内有著名的“美人画廊”。",
        "tip_fr": "📸 Promenez-vous le long du grand canal pour photographier les cygnes avec le château en arrière-plan. Visitez la Galerie des Beautés.",
        "de": "📸 Am Schlosskanal spazieren für Fotos der Schwäne vor der Palastkulisse. In der Residenz die Schönheitengalerie besuchen."
    },
    "m_5": { # Englischer Garten & Eisbachwelle
        "tip_en": "🏄 Watch urban surfers ride the permanent standing wave on the Eisbach river at the southern tip near Haus der Kunst day or night!",
        "tip_ja": "🏄 公園南端（ハウス・デア・クンスト横）のアイスバッハ川で、年中無休で川波に乗る『リバーサーフィン』の見学が熱い！橋の上からの見学は無料です。",
        "tip_es": "🏄 Observa a los surfistas urbanos cabalgar la ola permanente del río Eisbach junto a la Haus der Kunst a cualquier hora.",
        "tip_zh": "🏄 在公园南端（Haus der Kunst 旁）的 Eisbach 溪流看永不停歇的激流“河道冲浪”！桥上观看完全免费。",
        "tip_fr": "🏄 Admirez les surfeurs urbains défier la vague permanente de la rivière Eisbach au sud du parc près de la Haus der Kunst.",
        "de": "🏄 Den Flusssurfern an der stehenden Eisbachwelle nahe dem Haus der Kunst vom Brückensteg aus zusehen!"
    },
    "m_6": { # Viktualienmarkt
        "tip_en": "🍽️ Buy fresh pretzels, Obatzda (Bavarian spiced cheese spread), and Weisswurst sausages from stalls, then sit at the central beer garden under the Maypole!",
        "tip_ja": "🍽️ 市場の店で焼きたてプレッツェルやバイエルン特製チーズペースト『オバツダ』をテイクアウトし、メイポール下のビアガーデンで冷えた生ビールと一緒に食べるのが地元流！",
        "tip_es": "🍽️ Compra pretzels frescos y queso Obatzda en los puestos y siéntate en el jardín de cerveza central bajo el Maypole.",
        "tip_zh": "🍽️ 在各熟食摊位购买现做普雷结面包与巴伐利亚起司酱（Obatzda），拿到中央五月花柱下的大型露天啤酒花园享用！",
        "tip_fr": "🍽️ Achetez des pretzels frais et du fromage Obatzda aux étals, puis installez-vous au biergarten sous le mât de mai.",
        "de": "🍽️ Brezeln und Obatzda an den Ständen kaufen und im zentralen Biergarten unter dem Maibaum genießen!"
    },
    "m_7": { # Hofbräuhaus München
        "tip_en": "🍺 Grab an unreserved wooden table in the ground floor 'Schwammerl' hall; order a 1-liter Maß of Hofbräu Original beer and pork knuckle (Schweinshaxe)!",
        "tip_ja": "🍺 1階の巨大な木製テーブル席（予約不要）へ相席で座りましょう！1リットルジョッキ（Maß）のビールと皮がカリカリの『シュヴァインスハクセ（豚ひざ肉のロースト）』を注文するのが鉄板！",
        "tip_es": "🍺 Siéntate en una mesa de madera compartida en la planta baja; ¡pide una jarra Maß de 1 litro y codillo de cerdo (Schweinshaxe)!",
        "tip_zh": "🍺 步入一楼挑高木桌大厅寻找空位拼桌！点上一扎1升装（Maß）生啤酒与外皮酥脆的红烧烤猪膝（Schweinshaxe）。",
        "tip_fr": "🍺 Installez-vous sur une grande table en bois au rez-de-chaussée ; commandez une chope d'un litre (Maß) et un jarret de porc !",
        "de": "🍺 An den großen Holztischen im Erdgeschoss Platz nehmen; eine Maß Bier und Schweinshaxe mit Knödel bestellen!"
    },
    "m_8": { # Deutsches Museum
        "tip_en": "🎟️ Prioritize the Mining Exhibit (underground tunnels) and High Voltage Demonstration (lightning shows at 11:00 AM & 2:00 PM). Plan at least 4 hours!",
        "tip_ja": "🎟️ 地下鉱山ツアーと、毎日11:00/14:00に開催される高電圧実験（人工雷ショー）は絶対必見！見どころが多すぎるため最低3〜4時間の所要時間を見込みましょう。",
        "tip_es": "🎟️ No te pierdas la mina subterránea y la exhibición de alto voltaje (rayos a las 11:00 y 14:00 h). Reserva al menos 4 horas.",
        "tip_zh": "🎟️ 绝不可错过地下矿井与每天11:00/14:00的人工高压放电闪电演示！展馆极其庞大，建议预留至少4小时以上。",
        "tip_fr": "🎟️ Ne manquez pas la mine souterraine et la démo haute tension (éclairs à 11h et 14h). Prévoyez au moins 4 heures !",
        "de": "🎟️ Die Untertage-Schaubergwerk-Tour und die Hochspannungs-Blitzshow (11:00 & 14:00 Uhr) nicht verpassen! 4 Std. einplanen."
    },
    "m_15": { # Alter Peter (St. Peter's Church Tower)
        "tip_en": "📸 Climb the 306 steep wooden steps of the tower for THE top photospot looking straight down over Marienplatz and the Glockenspiel.",
        "tip_ja": "📸 306段の急な階段を登った塔頂テラスは、マリエン広場と新市庁舎を眼下に収めるミュンヘン最高のカメラアングル！天気が良ければアルプス山脈まで見えます。",
        "tip_es": "📸 Sube los 306 escalones de la torre para tomar la mejor foto sobre Marienplatz y el ayuntamiento desde arriba.",
        "tip_zh": "📸 攀登306级木梯登上塔顶观景台！这是俯瞰马利亚广场与新市政厅全景的“第一名胜摄影机位”。",
        "tip_fr": "📸 Montez les 306 marches de la tour pour le plus beau panorama sur la place Marienplatz et l'Hôtel de Ville.",
        "de": "📸 306 Stufen auf den Turm steigen für das beste Panorama auf den Marienplatz und das Rathaus!"
    },
    "m_35": { # Sendlinger Tor & Karlsplatz
        "tip_en": "🛷 In summer, kids splash in the giant fountain jets; in winter (Nov–Jan), the entire square turns into an open-air ice skating rink!",
        "tip_ja": "🛷 カールス広場（Stachus）中央の大噴水は夏場は涼しい水遊びスポット、11月下旬〜1月にはロマンチックな屋外アイススケートリンクに変身します！",
        "tip_es": "🛷 En verano, la gran fuente es refrescante; en invierno (nov-ene), la plaza se convierte en una pista de patinaje sobre hielo.",
        "tip_zh": "🛷 夏季喷泉水花四溢凉爽宜人；每年11月下旬至次年1月，整个广场会变身为浪漫的露天溜冰场！",
        "tip_fr": "🛷 En été, la grande fontaine est rafraîchissante ; en hiver (nov-janv), la place devient une patinoire à ciel ouvert !",
        "de": "🛷 Im Sommer erfrischt die große Fontäne; im Winter (Nov–Jan) verwandelt sich der Platz in eine Eisbahn!"
    },
    "m_36": { # Flaucher & Isarauen River Park
        "tip_en": "🧺 Pack a blanket, snacks, and cold beers to join locals relaxing on the natural gravel banks along the Isar river for a sunny afternoon.",
        "tip_ja": "🧺 レジャーシートとお菓子、冷えたビールを持参して、清流イザール川の砂利浜で日光浴や川遊びを楽しむのが地元ミュンヘン市民の週末の楽しみ方！",
        "tip_es": "🧺 Lleva una manta, aperitivos y cerveza fría para disfrutar de una tarde soleada en las playas de grava del río Isar.",
        "tip_zh": "🧺 自备野餐垫与冰镇啤酒，坐在伊萨尔河石滩草地上日光浴或浅滩戏水，体验当地人的悠闲假日。",
        "tip_fr": "🧺 Apportez une couverture, des encas et de la bière fraîche pour vous détendre sur les berges en gravier de l'Isar.",
        "de": "🧺 Decke, Snacks und kühles Bier mitnehmen und den Nachmittag am Kiesstrand der Isar genießen."
    },
    "m_37": { # Dallmayr Delikatessenhaus
        "tip_en": "🛍️ Head to the ground floor coffee counter where baristas weigh freshly roasted coffee beans in antique porcelain scales for premium souvenirs.",
        "tip_ja": "🛍️ 1階奥のコーヒー売場へ！アンティークのデルフト焼き風磁器秤で計量してくれる挽きたてコーヒー豆や、金箔箱入りのDallmayr紅茶はお土産に大人気。",
        "tip_es": "🛍️ Ve al mostrador de café donde pesan los granos recién tostados en balanzas de porcelana antiguas para regalar.",
        "tip_zh": "🛍️ 直奔一楼古典咖啡专柜！看咖啡师用复古青花瓷称现场称重拿取烘焙咖啡豆，礼盒包装极具档次。",
        "tip_fr": "🛍️ Allez au comptoir à café où les grains sont pesés dans de magnifiques balances en porcelaine anciennes.",
        "de": "🛍️ Am Kaffeestand frisch geröstete Kaffeebohnen in antiken Porzellanwaagen abwiegen lassen – perfektes Souvenir!"
    },
    "m_38": { # Schneider Bräuhaus
        "tip_en": "🍽️ Pair Schneider Weisse TAP7 beer with a traditional warm Weisswurst (white sausage) served in hot water with sweet Bavarian mustard and pretzels before 12 PM!",
        "tip_ja": "🍽️ 午前中（12時まで）の訪問が必須！名物の白ソーセージ（Weißwurst）をお湯の入った深皿で注文し、甘いマスタードと焼きたてプレッツェル、小麦生ビールと合わせるのがバイエルンの伝統朝食。",
        "tip_es": "🍽️ ¡Pide las salchichas blancas Weisswurst servidas en agua caliente antes de las 12:00 h con mostaza dulce y sal de pretzel!",
        "tip_zh": "🍽️ 建议正午前前往！按传统点一份放在热汤碗里的巴伐利亚白香肠（Weißwurst），蘸甜芥末酱配普雷结面包与小麦啤酒。",
        "tip_fr": "🍽️ Dégustez les saucisses blanches (Weisswurst) servies dans l'eau chaude avant 12h avec moutarde douce et bretzel !",
        "de": "🍽️ Vor 12 Uhr die traditionellen Weißwürste im heißen Wasser mit süßem Senf, Brezel und Weizenbier bestellen!"
    },
    "m_39": { # Café Frischhut (Der Schmalznudel)
        "tip_en": "🍽️ Order hot piping-hot 'Schmalznudel' (traditional Bavarian lard-fried doughnut) straight out of the bubbling oil pan with a warm Milchkaffee!",
        "tip_ja": "🍽️ 揚げ場の大きな油鍋で職人が次々に揚げる熱々の『シュマルツヌーデル（バイエルン風伝統揚げドーナツ）』を注文！サクサク熱々をミルクカフェと一緒に召し上がれ。",
        "tip_es": "🍽️ Pide una 'Schmalznudel' caliente recién sacada del aceite hirviendo acompañada de un Milchkaffee con leche.",
        "tip_zh": "🍽️ 点一份刚从油锅拉出、热气腾腾酥脆的巴伐利亚炸油饼（Schmalznudel），配上一杯热牛奶咖啡堪称绝配。",
        "tip_fr": "🍽️ Commandez une 'Schmalznudel' (beignet bavard) toute chaude sortie du bain d'huile avec un Milchkaffee !",
        "de": "🍽️ Eine frische heiße Schmalznudel direkt aus dem Frittierfett mit einem Milchkaffee am Tresen bestellen!"
    },
    "m_40": { # Café Luitpold
        "tip_en": "🍽️ Sit under the glass palm atrium to sample their signature 'Luitpold-Torte' (layered dark chocolate & marzipan cake) with freshly brewed espresso.",
        "tip_ja": "🍽️ ヤシの木が広がる美しいガラス張りのアトリウム席で、看板ケーキ『ルイトポルト・トルテ（濃厚ダークチョコとマジパンの多層ケーキ）』をエスプレッソと共に楽しむ優雅なカフェタイム。",
        "tip_es": "🍽️ Siéntate bajo el atrio de cristal para probar la tarta de la casa 'Luitpold-Torte' de chocolate negro y mazapán.",
        "tip_zh": "🍽️ 坐在玻璃棕榈中庭里，品尝镇店招牌“Luitpold-Torte”（黑巧克力与杏仁糖膏多层蛋糕）配现磨浓缩咖啡。",
        "tip_fr": "🍽️ Installez-vous sous la verrière pour déguster la 'Luitpold-Torte' signature au chocolat noir et marzipan.",
        "de": "🍽️ Im Palmen-Atrium die berühmte Luitpold-Torte (Dunkle Schokolade und Marzipan) mit Espresso genießen."
    },
    "m_44": { # Müller'sches Volksbad
        "tip_en": "👙 Swim under soaring neo-baroque stucco ceilings in the 30°C main pool or relax in the Roman-Irish steam baths (swimming caps not required).",
        "tip_ja": "👙 1901年建築の壮麗なアール・ヌーヴォーのフレスコ天井を見上げながら30℃の温水プールで泳ぐ最高の贅沢！ローマ風サウナや蒸気浴エリアも併設されています（スイムキャップ不要）。",
        "tip_es": "👙 Nada bajo los techos con frescos neobarrocos en la piscina de 30°C o relájate en los baños de vapor romanos.",
        "tip_zh": "👙 在30°C温水泳池中仰泳，抬头尽是1901年新巴洛克宫殿水彩天顶！内设罗马蒸汽桑拿浴场（无需带泳帽）。",
        "tip_fr": "👙 Nagez sous les plafonds néo-baroques de la piscine chauffée à 30°C ou détendez-vous dans les bains romains.",
        "de": "👙 Unter den neobarocken Stuckdecken im 30°C warmen Becken schwimmen oder im römischen Dampfbad entspannen."
    },
    "m_45": { # Werksviertel-Mitte & Umadum
        "tip_en": " Ride the 78-meter 'Umadum' giant Ferris wheel for clear views extending to the Bavarian Alps, then check out the rooftop urban sheep farm!",
        "tip_ja": " 高さ78mの観覧車『Umadum』に乗ると天気が良い日はアルプス山脈まで一望！コンテナビルの屋上で本物の羊が放牧されているユニークな光景も必見。",
        "tip_es": " Sube a la gran rueda Umadum de 78 m para ver los Alpes y visita las ovejas que pastan en el tejado de un edificio.",
        "tip_zh": " 乘坐78米高的 Umadum 摩天轮，晴天可远眺巴伐利亚阿尔卑斯雪山，别忘了看楼顶集装箱屋顶放牧的真正羊群！",
        "tip_fr": " Montez dans la grande roue Umadum de 78m pour voir les Alpes et visitez les moutons qui paissent sur le toit d'un bâtiment.",
        "de": " Mit dem 78m Riesenrad Umadum fahren für den Blick bis zu den Alpen und die Schafe auf dem Gebäudedach besuchen!"
    },
    "m_46": { # Schloss Neuschwanstein
        "tip_en": "🎟️ Book interior castle tickets on the official website 3-4 weeks in advance! Walk 15 minutes beyond Marienbrücke bridge for uncrowded postcard views.",
        "tip_ja": "🎟️ 城内見学チケットは公式サイトで3〜4週間前に事前予約が絶対！混雑するマリエン橋を渡り、さらに奥の山道を15分登ると静かな絶景写真ポイントに到達します。",
        "tip_es": "🎟️ ¡Reserva las entradas al interior 3 o 4 semanas antes en la web oficial! Camina 15 min más allá del puente Marienbrücke sin aglomeraciones.",
        "tip_zh": "🎟️ 城堡内部参观门票必须提前3-4周在官网预订！穿过拥挤的Marienbrücke桥再往前走15分钟山道，能拍到无杂人的完美名信片大片。",
        "tip_fr": "🎟️ Réservez vos billets pour l'intérieur 3 à 4 semaines à l'avance sur le site officiel ! Marchez 15 min après le pont Marienbrücke pour être tranquille.",
        "de": "🎟️ Innenbesichtigungstickets 3–4 Wochen vorab online buchen! 15 Min. über die Marienbrücke hinausgehen für den besten ruhigen Fotospot."
    },
    "m_47": { # Wieskirche
        "tip_en": "⛪ Free entrance to admire the world-class Rococo ceiling frescos. Respectful quiet is required; avoid visiting during active Sunday mass services.",
        "tip_ja": "⛪ 入場無料。草木が茂るのどかな風景の中に建つ奇跡のロココ聖堂。日曜日の礼拝（ミサ）時間を避け、静かにフレスコ天頂画を鑑賞しましょう。",
        "tip_es": "⛪ Entrada libre para admirar los frescos rococó. Respeta el silencio y evita las horas de misa los domingos.",
        "tip_zh": "⛪ 免费入内。矗立于草地之上的洛可可天顶画艺术殿堂。请保持肃静，建议避开周日正正式礼拜弥撒时段。",
        "tip_fr": "⛪ Entrée libre pour admirer les fresques rococó. Respectez le silence et évitez les heures de messe le dimanche.",
        "de": "⛪ Freier Eintritt zu den weltberühmten Rokoko-Deckenfresken. Ruhiges Verhalten erwünscht (Gottesdienstzeiten beachten)."
    },
    "m_51": { # Starnberger See
        "tip_en": "🚆 Take the S6 train from Munich Central (30 min) directly to Starnberg station on the lake shore. Rent an electric boat or board the passenger cruise!",
        "tip_ja": "🚆 ミュンヘン中央駅からS6電車でわずか30分で湖畔のシュタルンベルク駅に到着！駅前の桟橋から電動レンタルボートに乗るか大型遊覧船クルーズを楽しめます。",
        "tip_es": "🚆 Toma el tren S6 desde la estación central (30 min) directo a la orilla del lago. ¡Alquila un barco eléctrico!",
        "tip_zh": "🚆 从慕尼黑主火车站搭乘 S6 城铁仅需30分钟直达湖畔！可在车站前码头租划电动船或登客运游船环湖。",
        "tip_fr": "🚆 Prenez le train S6 depuis la gare centrale (30 min) jusqu'au bord du lac. Louez un bateau électrique ou embarquez en croisière !",
        "de": "🚆 Mit der S-Bahn S6 vom Hauptbahnhof (30 Min.) direkt an den See fahren. Elektroboot mieten oder Schiffsrundfahrt machen!"
    },
    "m_53": { # Schloss Linderhof
        "tip_en": "⛲ Watch the 25-meter golden Flora fountain shoot water into the air directly in front of the palace every hour on the hour!",
        "tip_ja": "⛲ 宮殿正面の池で毎時00分に噴き上がる『25mの金色のフローラ大噴水ショー』は必見！ルートヴィヒ2世の豪華な人工洞窟（Venus Grotte）見学もセットで。",
        "tip_es": "⛲ ¡Observa el gran chorro de 25 metros de la fuente dorada de Flora disparar agua frente al palacio cada hora en punto!",
        "tip_zh": "⛲ 宫殿正面水池每逢整点（如12:00、13:00）会喷涌出高达25米的金色Flora巨型喷泉，气势绝伦！",
        "tip_fr": "⛲ Admirez le grand jet de 25 mètres de la fontaine dorée de Flore jaillir devant le château toutes les heures pile !",
        "de": "⛲ Alle volle Stunde schießt die 25 Meter hohe goldene Flora-Fontäne im Teich vor dem Schloss empor!"
    },
    "m_54": { # Kloster Ettal
        "tip_en": "🛍️ Visit the monastery shop to sample authentic 'Ettaler Klosterlikör' distilled by monks using 50 secret alpine herbs since medieval times.",
        "tip_ja": "🛍️ 修道院の直営店へ！修道士が50種類のアルプスハーブから秘伝製法で造る伝統の薬草リキュール『Ettaler Klosterlikör』の試飲・購入ができます。",
        "tip_es": "🛍️ Visita la tienda del monasterio para probar el licor de hierbas 'Ettaler Klosterlikör' elaborado por monjes desde la Edad Media.",
        "tip_zh": "🛍️ 探访修道院直营小店！品尝修士们使用50种自采集阿尔卑斯高山草药酿造的古法药草利口酒“Ettaler Klosterlikör”。",
        "tip_fr": "🛍️ Visitez la boutique du monastère pour goûter à la liqueur d'herbes 'Ettaler Klosterlikör' préparée par les moines.",
        "de": "🛍️ Im Klosterladen den von den Mönchen aus 50 Alpenkräutern hergestellten 'Ettaler Klosterlikör' verkosten!"
    },
    "m_56": { # Zugspitze & Eibsee
        "tip_en": "🎟️ Take the Cable Car Zugspitze up to the 2,962m summit for 4-country views, then descend via the Cogwheel mountain train for a complete loop pass!",
        "tip_ja": "🎟️ アイプ湖から最新ロープウェイで一気に山頂（2,962m）へ登り、帰りは山腹を貫く登山電車（歯車列車）で下山する周遊ルートが爽快！エメラルド色のアイプ湖散策も必至。",
        "tip_es": "🎟️ Sube en el teleférico hasta la cumbre a 2.962m y baja en el tren de cremallera para completar el circuito panorámico.",
        "tip_zh": "🎟️ 从艾布湖搭乘全景索道电缆车登顶2,962米，下山乘坐穿山齿轨火车，完成完美环形体验！",
        "tip_fr": "🎟️ Montez en téléphérique au sommet à 2962m et redescendez en train à crémaillère pour un circuit complet !",
        "de": "🎟️ Mit der Seilbahn Zugspitze auf 2.962m fahren und mit der Zahnradbahn wieder hinab – die perfekte Rundtour!"
    },
    "m_57": { # Tegernsee & Schliersee
        "tip_en": "🍺 Head to Herzogliches Bräustüberl Tegernsee right next to the lake for unpasteurized Tegernseer Hell beer on the outdoor water-view terrace!",
        "tip_ja": "🍺 湖畔の名門醸造所レストラン『Herzogliches Bräustüberl』の湖を望むテラス席で、冷えた『Tegernseer Hell』生ビールとプレッツェルを味わう至福の時間！",
        "tip_es": "🍺 Ve a la cervecería Herzogliches Bräustüberl junto al agua para disfrutar de una cerveza Tegernseer Hell helada en la terraza.",
        "tip_zh": "🍺 探访紧邻湖畔的名门酿造所大酒家“Herzogliches Bräustüberl”，坐在临湖露台品尝冰镇 Tegernseer Hell 纯麦生啤！",
        "tip_fr": "🍺 Allez à la brasserie Herzogliches Bräustüberl au bord de l'eau pour déguster une bière fraîche Tegernseer Hell en terrasse.",
        "de": "🍺 Im Herzoglichen Bräustüberl direkt am Seeufer auf der Terrasse ein kühles Tegernseer Hell genießen!"
    },
    "m_58": { # Therme Erding
        "tip_en": "👙 Bring your swimsuit & flip-flops! Relax in 34°C thermal pools under real palm trees or try the virtual reality water slides at Galaxy Water Park.",
        "tip_ja": "👙 水着・サンダル・バスタオルを持参！本物のヤシの木が茂る34℃の巨大温泉プールや、VRゴーグルをつけて滑る最新水上スライダー『Galaxy』で1日中楽しめます。",
        "tip_es": "👙 ¡Lleva traje de baño y chanclas! Relájate en piscinas térmicas a 34°C bajo palmeras reales o prueba los toboganes de realidad virtual.",
        "tip_zh": "👙 自备泳衣、拖鞋与大浴巾！在棕榈树荫下34°C恒温温泉池放松，体验戴VR眼镜滑行的 Galaxy 刺激滑水道。",
        "tip_fr": "👙 Apportez maillot de bain et claquettes ! Détendez-vous dans les bassins thermaux à 34°C sous les palmiers ou essayez les toboggans VR.",
        "de": "👙 Badesachen & Badelatschen mitnehmen! Bei 34°C unter echten Palmen entspannen oder VR-Wasserrutschen testen."
    },
    "m_59": { # Freising & Weihenstephan
        "tip_en": "🍺 Dine at the hilltop Bräustüberl Weihenstephan—the world's oldest active brewery (since AD 1040)—for fresh unfiltered Hefeweissbier and sausage platters!",
        "tip_ja": "🍺 西暦1040年（約1000年前）創業の『世界最古の現役醸造所』直営丘の上レストランへ！無濾過のヴァイスビア（Hefeweissbier）と名物バイエルンプレートが絶品です。",
        "tip_es": "🍺 Cena en la cervecería activa más antigua del mundo (desde 1040 d.C.) en la colina, disfrutando de una Hefeweissbier sin filtrar.",
        "tip_zh": "🍺 登上山顶前往公元1040年创办的“全球最古老现役啤酒厂”直营大酒家，品尝未过滤的原浆小麦生啤酒（Hefeweissbier）。",
        "tip_fr": "🍺 Dînez à la brasserie en activité la plus ancienne du monde (depuis 1040 apr. J.-C.) et dégustez une bière Hefeweissbier non filtrée.",
        "de": "🍺 In der ältesten aktiven Brauerei der Welt (seit 1040 n. Chr.) auf dem Hügel ein naturtrübes Hefeweissbier genießen!"
    },
    "m_60": { # Bavaria Filmstadt
        "tip_en": "🎬 Step inside the real 55-meter submarine film set used in 'Das Boot' or ride on the back of Falkor the Luckdragon from 'The NeverEnding Story'!",
        "tip_ja": "🎬 名作映画『U・ボート』撮影で使われた全長55mの本物の潜水艦内部へ潜入！映画『ネバーエンディング・ストーリー』の白い竜ファルコンの背中に乗る写真体験も大人気。",
        "tip_es": "🎬 Entra en el submarino real de 55 m de la película 'Das Boot' o sube al lomo del dragón Falkor de 'La historia interminable'.",
        "tip_zh": "🎬 步入经典电影《U-艇》（Das Boot）长达55米的真实潜艇拍摄道具内部，或骑在《无尽的故事》白龙 Falkor 身上体验绿幕合成！",
        "tip_fr": "🎬 Entrez à l'intérieur du véritable sous-marin de 55m du film 'Das Boot' ou montez sur le dos du dragon Falkor !",
        "de": "🎬 Das echte 55-Meter-U-Boot aus dem Film 'Das Boot' begehen oder auf dem Glücksdrachen Fuchur aus der 'Unendlichen Geschichte' reiten!"
    }
}

# Apply refinements to munich.json
fpath = "data/cities/munich.json"
with open(fpath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for s in data['spots']:
    sid = s['id']
    if sid in munich_refinements:
        up = munich_refinements[sid]
        for k, v in up.items():
            s[k] = v
        s['tip'] = up.get('tip_en', s.get('tip', ''))
        count += 1

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Refined {count} spots in munich.json")
