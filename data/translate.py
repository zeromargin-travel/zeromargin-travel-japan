import json

master_texts = {
  "par_p_32": {
    "desc": {
      "en": "1889 bakery crafting signature escargot chocolate-pistachio pastries and wood-fired sourdough.",
      "ja": "1889年創業のパン屋。名物のピスタチオとチョコレートのエスカルゴペストリーと薪焼きサワードウが自慢です。",
      "zh": "1889年开业的面包店，手工制作招牌开心果巧克力蜗牛酥和柴火烤制的酸面包。",
      "fr": "Boulangerie de 1889 proposant ses célèbres escargots chocolat-pistache et du pain au levain cuit au feu de bois.",
      "de": "Bäckerei von 1889, die legendäre Pistazien-Schokoladen-Schnecken und holzofengebackenes Sauerteigbrot herstellt.",
      "es": "Panadería de 1889 que elabora los emblemáticos pasteles de caracol de chocolate y pistacho y pan de masa madre al horno de leña.",
      "nl": "Bakkerij uit 1889 die de beroemde chocolade-pistache escargot-gebakjes en houtoven zuurdesembrood maakt."
    },
    "tip": {
      "en": "Artisanal bakery near Canal Saint-Martin. Try their iconic 'Escargot Chocolat Pistache' baked fresh daily.",
      "ja": "サン・マルタン運河近くの職人パン屋。毎日焼きたての象徴的な「エスカルゴ・ショコラ・ピスターシュ」をお試しください。",
      "zh": "圣马丁运河附近的工匠面包店。一定要尝尝他们每天新鲜出炉的招牌“开心果巧克力蜗牛酥”。",
      "fr": "Boulangerie artisanale près du Canal Saint-Martin. Goûtez leur emblématique 'Escargot Chocolat Pistache' cuit sur place.",
      "de": "Handwerksbäckerei nahe dem Canal Saint-Martin. Probieren Sie die ikonische, täglich frisch gebackene 'Escargot Chocolat Pistache'.",
      "es": "Panadería artesanal cerca del Canal Saint-Martin. Prueba su icónico 'Escargot Chocolat Pistache' recién horneado cada día.",
      "nl": "Ambachtelijke bakkerij bij Canal Saint-Martin. Probeer hun iconische 'Escargot Chocolat Pistache', dagelijks vers gebakken."
    },
    "whyThisSpot": {
      "en": "A true Parisian institution offering an authentic 19th-century atmosphere and unforgettable artisanal pastries.",
      "ja": "19世紀の本格的な雰囲気と忘れられない手作りペストリーを提供する、真のパリの象徴的なお店です。",
      "zh": "这是一家真正的巴黎老字号，提供真实的19世纪氛围和令人难忘的手工糕点。",
      "fr": "Une véritable institution parisienne offrant une atmosphère authentique du 19ème siècle et des pâtisseries artisanales inoubliables.",
      "de": "Eine wahre Pariser Institution, die eine authentische Atmosphäre des 19. Jahrhunderts und unvergessliche handwerkliche Backwaren bietet.",
      "es": "Una verdadera institución parisina que ofrece un auténtico ambiente del siglo XIX y unos pasteles artesanales inolvidables.",
      "nl": "Een echt Parijs instituut dat een authentieke 19e-eeuwse sfeer en onvergetelijke ambachtelijke gebakjes biedt."
    }
  },
  "par_p_33": {
    "desc": {
      "en": "Famous arcade cafe near Eiffel Tower known for whipped cream hot chocolate & French macarons.",
      "ja": "エッフェル塔近くの有名なアーケードカフェ。ホイップクリームたっぷりのホットチョコレートとマカロンで知られています。",
      "zh": "埃菲尔铁塔附近著名的拱廊咖啡馆，以鲜奶油热巧克力和法式马卡龙而闻名。",
      "fr": "Célèbre café sous les arcades près de la Tour Eiffel, réputé pour son chocolat chaud chantilly et ses macarons.",
      "de": "Berühmtes Arkadencafé nahe dem Eiffelturm, bekannt für heiße Schokolade mit Schlagsahne und französische Macarons.",
      "es": "Famosa cafetería con arcadas cerca de la Torre Eiffel, conocida por su chocolate caliente con nata y sus macarons franceses.",
      "nl": "Beroemd arcadecafé bij de Eiffeltoren, bekend om warme chocolademelk met slagroom en Franse macarons."
    },
    "tip": {
      "en": "Chic tearoom at Place du Trocadéro famous for its velvety rich hot chocolate served with a giant bowl of homemade chantilly whipped cream.",
      "ja": "トロカデロ広場にあるシックなティールーム。自家製シャンティクリームをたっぷり添えた濃厚なホットチョコレートが有名です。",
      "zh": "位于特罗卡德罗广场的别致茶馆，以其丝滑浓郁的热巧克力和一大碗自制香缇奶油而闻名。",
      "fr": "Salon de thé chic de la Place du Trocadéro célèbre pour son chocolat chaud velouté servi avec un bol géant de crème chantilly maison.",
      "de": "Schicker Teesalon an der Place du Trocadéro, berühmt für samtig reiche heiße Schokolade mit einer riesigen Schale hausgemachter Chantilly-Sahne.",
      "es": "Elegante salón de té en la Place du Trocadéro, famoso por su rico y aterciopelado chocolate caliente servido con un enorme bol de crema chantilly casera.",
      "nl": "Chique theesalon aan de Place du Trocadéro, beroemd om zijn fluweelzachte, rijke warme chocolademelk geserveerd met een gigantische kom zelfgemaakte chantilly-slagroom."
    },
    "whyThisSpot": {
      "en": "Perfect spot to indulge in classic French cafe culture with unbeatable views and premium sweets.",
      "ja": "最高の景色と高級なスイーツを楽しみながら、フランスのクラシックなカフェ文化を堪能するのに最適な場所です。",
      "zh": "这是沉浸在经典法国咖啡馆文化、享受无敌美景和高级甜点的完美地点。",
      "fr": "L'endroit idéal pour s'imprégner de la culture des cafés français avec des vues imprenables et des douceurs haut de gamme.",
      "de": "Der perfekte Ort, um in die klassische französische Café-Kultur mit unschlagbarer Aussicht und erstklassigen Süßigkeiten einzutauchen.",
      "es": "El lugar perfecto para disfrutar de la clásica cultura de cafetería francesa con unas vistas inmejorables y dulces de primera calidad.",
      "nl": "De perfecte plek om te genieten van de klassieke Franse cafécultuur met een onovertroffen uitzicht en eersteklas zoetigheden."
    }
  },
  "par_p_34": {
    "desc": {
      "en": "Jean Nouvel-designed museum of non-Western indigenous art right next to the Eiffel Tower.",
      "ja": "エッフェル塔のすぐそばにある、ジャン・ヌーヴェル設計の非西洋先住民アートの美術館。",
      "zh": "紧邻埃菲尔铁塔、由让·努维尔设计的非西方原住民艺术博物馆。",
      "fr": "Musée d'art indigène non-occidental conçu par Jean Nouvel, situé juste à côté de la Tour Eiffel.",
      "de": "Von Jean Nouvel entworfenes Museum für nicht-westliche indigene Kunst direkt neben dem Eiffelturm.",
      "es": "Museo de arte indígena no occidental diseñado por Jean Nouvel justo al lado de la Torre Eiffel.",
      "nl": "Door Jean Nouvel ontworpen museum voor niet-westerse inheemse kunst vlak naast de Eiffeltoren."
    },
    "tip": {
      "en": "Features a striking vertical living plant wall and peaceful gardens with unique Eiffel Tower views.",
      "ja": "印象的な垂直の植物の壁と、ユニークなエッフェル塔の景色を楽しめる静かな庭園が特徴です。",
      "zh": "这里有引人注目的垂直植物墙和宁静的花园，能欣赏到独特的埃菲尔铁塔景观。",
      "fr": "Il présente un impressionnant mur végétal vertical et des jardins paisibles avec des vues uniques sur la Tour Eiffel.",
      "de": "Besticht durch eine markante vertikale Pflanzenwand und friedliche Gärten mit einzigartigem Blick auf den Eiffelturm.",
      "es": "Cuenta con un impresionante muro vegetal vertical y tranquilos jardines con vistas únicas a la Torre Eiffel.",
      "nl": "Beschikt over een indrukwekkende verticale levende plantenmuur en rustige tuinen met uniek uitzicht op de Eiffeltoren."
    },
    "whyThisSpot": {
      "en": "An extraordinary architectural space offering deep cultural insights away from the typical Parisian tourist trail.",
      "ja": "典型的なパリの観光ルートから離れ、深い文化的な洞察を提供する非日常的な建築空間です。",
      "zh": "一个非凡的建筑空间，提供了远离典型巴黎旅游路线的深刻文化见解。",
      "fr": "Un espace architectural extraordinaire offrant de profondes perspectives culturelles loin des sentiers touristiques parisiens typiques.",
      "de": "Ein außergewöhnlicher architektonischer Raum, der abseits der typischen Pariser Touristenpfade tiefe kulturelle Einblicke bietet.",
      "es": "Un espacio arquitectónico extraordinario que ofrece profundos conocimientos culturales lejos de la típica ruta turística parisina.",
      "nl": "Een buitengewone architectonische ruimte die diepe culturele inzichten biedt, ver weg van de typische Parijse toeristenroute."
    }
  },
  "par_p_35": {
    "desc": {
      "en": "19th-century glass-roofed arcades lined with antique shops, vintage bookstores, and tea salons.",
      "ja": "アンティークショップや古本屋、ティールームが並ぶ、19世紀のガラス屋根のアーケード。",
      "zh": "19世纪的玻璃屋顶拱廊，两旁林立着古董店、古旧书店和茶室。",
      "fr": "Passages couverts du 19ème siècle avec verrières, bordés d'antiquaires, de librairies anciennes et de salons de thé.",
      "de": "Glasdach-Arkaden aus dem 19. Jahrhundert mit Antiquitätenläden, Vintage-Buchhandlungen und Teesalons.",
      "es": "Arcadas con techo de cristal del siglo XIX bordeadas de tiendas de antigüedades, librerías antiguas y salones de té.",
      "nl": "19e-eeuwse arcades met glazen daken vol antiekwinkels, tweedehandsboekhandels en theesalons."
    },
    "tip": {
      "en": "Paris's most elegant covered passage (1823) featuring intricate floor mosaics. Perfect for a rainy day stroll.",
      "ja": "パリで最もエレガントな屋内通路（1823年）。複雑な床のモザイクが特徴で、雨の日の散策に最適です。",
      "zh": "巴黎最优雅的室内通道（1823年），拥有精致的地板马赛克。非常适合雨天漫步。",
      "fr": "Le passage couvert le plus élégant de Paris (1823) avec ses mosaïques au sol complexes. Parfait pour une promenade les jours de pluie.",
      "de": "Pariser eleganteste überdachte Passage (1823) mit kunstvollen Bodenmosaiken. Perfekt für einen Spaziergang an regnerischen Tagen.",
      "es": "El pasaje cubierto más elegante de París (1823) con intrincados mosaicos en el suelo. Perfecto para pasear en un día lluvioso.",
      "nl": "De meest elegante overdekte passage van Parijs (1823) met ingewikkelde vloermozaïeken. Perfect voor een wandeling op een regenachtige dag."
    },
    "whyThisSpot": {
      "en": "Provides a charming historical atmosphere, letting you explore hidden boutiques of old Paris.",
      "ja": "魅力的な歴史的雰囲気を楽しめ、古いパリの隠れたブティックを探索できます。",
      "zh": "提供了迷人的历史氛围，让您可以探索老巴黎隐藏的精品店。",
      "fr": "Offre une atmosphère historique charmante, vous permettant d'explorer les boutiques cachées du vieux Paris.",
      "de": "Bietet eine charmante historische Atmosphäre, in der Sie verborgene Boutiquen des alten Paris entdecken können.",
      "es": "Ofrece un encantador ambiente histórico, permitiéndote explorar boutiques ocultas del antiguo París.",
      "nl": "Biedt een charmante historische sfeer, waardoor u verborgen boetieks van het oude Parijs kunt ontdekken."
    }
  },
  "par_p_36": {
    "desc": {
      "en": "Stunning Neo-Byzantine glass dome & free rooftop terrace for panoramic city views.",
      "ja": "美しいネオビザンチン様式のガラスドームと、市内のパノラマビューを楽しめる無料の屋上テラス。",
      "zh": "令人惊叹的新拜占庭式玻璃圆顶和可欣赏城市全景的免费屋顶露台。",
      "fr": "Superbe dôme en verre néo-byzantin et toit-terrasse gratuit offrant des vues panoramiques sur la ville.",
      "de": "Atemberaubende neobyzantinische Glaskuppel & kostenlose Dachterrasse für einen Panoramablick über die Stadt.",
      "es": "Impresionante cúpula de cristal neobizantina y terraza gratuita en la azotea con vistas panorámicas de la ciudad.",
      "nl": "Prachtige neobyzantijnse glazen koepel en gratis dakterras voor een panoramisch uitzicht over de stad."
    },
    "tip": {
      "en": "Don't miss the 100-year-old stained glass dome inside the main store, then head to the 8th floor for sweeping views of the Opera and Eiffel Tower.",
      "ja": "本館内の100年の歴史を持つステンドグラスドームをお見逃しなく。その後、8階へ向かいオペラ座とエッフェル塔の絶景をお楽しみください。",
      "zh": "千万不要错过总店内百年历史的彩色玻璃圆顶，然后前往8楼欣赏歌剧院和埃菲尔铁塔的壮丽景色。",
      "fr": "Ne manquez pas la coupole centenaire en vitrail dans le magasin principal, puis montez au 8ème étage pour une vue imprenable sur l'Opéra et la Tour Eiffel.",
      "de": "Verpassen Sie nicht die 100 Jahre alte Buntglaskuppel im Hauptgeschäft und fahren Sie dann in den 8. Stock für einen weiten Blick auf die Oper und den Eiffelturm.",
      "es": "No te pierdas la cúpula de vidrieras de 100 años en la tienda principal, luego sube al octavo piso para disfrutar de amplias vistas de la Ópera y la Torre Eiffel.",
      "nl": "Mis de 100 jaar oude glas-in-loodkoepel in de hoofdwinkel niet en ga dan naar de 8e verdieping voor een weids uitzicht op de Opera en de Eiffeltoren."
    },
    "whyThisSpot": {
      "en": "Combines luxury shopping with breathtaking architecture and one of the best free viewpoints in Paris.",
      "ja": "高級ショッピングと息を呑むような建築、そしてパリで最高の無料ビュースポットを兼ね備えています。",
      "zh": "将奢华购物与令人惊叹的建筑结合，并提供巴黎最佳的免费观景点之一。",
      "fr": "Combine le shopping de luxe avec une architecture à couper le souffle et l'un des meilleurs points de vue gratuits de Paris.",
      "de": "Kombiniert Luxus-Shopping mit atemberaubender Architektur und einem der besten kostenlosen Aussichtspunkte in Paris.",
      "es": "Combina compras de lujo con una arquitectura impresionante y uno de los mejores miradores gratuitos de París.",
      "nl": "Combineert luxe winkelen met adembenemende architectuur en een van de beste gratis uitzichtpunten in Parijs."
    }
  },
  "par_p_37": {
    "desc": {
      "en": "Panoramic waterside views of the Eiffel Tower, Musée d'Orsay, and Notre-Dame on a relaxing river cruise.",
      "ja": "リラックスできるリバークルーズで楽しむ、エッフェル塔、オルセー美術館、ノートルダム大聖堂のパノラマ水辺の風景。",
      "zh": "在轻松的游船上欣赏埃菲尔铁塔、奥赛博物馆和巴黎圣母院的全景水岸风光。",
      "fr": "Vues panoramiques au fil de l'eau sur la Tour Eiffel, le Musée d'Orsay et Notre-Dame lors d'une croisière relaxante.",
      "de": "Panoramablick vom Wasser aus auf den Eiffelturm, das Musée d'Orsay und Notre-Dame bei einer entspannenden Flusskreuzfahrt.",
      "es": "Vistas panorámicas junto al agua de la Torre Eiffel, el Museo de Orsay y Notre-Dame en un relajante crucero por el río.",
      "nl": "Panoramisch uitzicht vanaf het water op de Eiffeltoren, het Musée d'Orsay en de Notre-Dame tijdens een ontspannende riviercruise."
    },
    "tip": {
      "en": "Board a cruise right around sunset to experience Paris bathed in golden light on the way out, and fully illuminated on the way back.",
      "ja": "日没頃に乗船すると、行きは黄金色の光に包まれたパリを、帰りは完全にライトアップされたパリを楽しめます。",
      "zh": "在日落时分登船，出发时感受沐浴在金色阳光下的巴黎，返程时欣赏灯火辉煌的夜景。",
      "fr": "Embarquez juste au moment du coucher du soleil pour voir Paris baigné de lumière dorée à l'aller, et entièrement illuminé au retour.",
      "de": "Gehen Sie kurz vor Sonnenuntergang an Bord, um Paris auf dem Hinweg in goldenes Licht getaucht und auf dem Rückweg vollständig beleuchtet zu erleben.",
      "es": "Embarca justo al atardecer para experimentar París bañado en luz dorada a la ida, y completamente iluminado a la vuelta.",
      "nl": "Stap aan boord rond zonsondergang om Parijs badend in gouden licht te ervaren op de heenweg, en volledig verlicht op de terugweg."
    },
    "whyThisSpot": {
      "en": "The absolute best way to see the city's iconic monuments effortlessly from the comfort of the Seine.",
      "ja": "セーヌ川の快適な船上から、パリの象徴的な記念碑を簡単に楽しむ最高の手段です。",
      "zh": "这是舒适地从塞纳河上轻松欣赏这座城市标志性古迹的绝对最佳方式。",
      "fr": "La meilleure façon de voir les monuments emblématiques de la ville sans effort depuis le confort de la Seine.",
      "de": "Die absolut beste Art, die ikonischen Denkmäler der Stadt mühelos und bequem von der Seine aus zu sehen.",
      "es": "La mejor manera de ver los emblemáticos monumentos de la ciudad sin esfuerzo desde la comodidad del Sena.",
      "nl": "De absoluut beste manier om de iconische monumenten van de stad moeiteloos te zien vanaf het comfort van de Seine."
    }
  },
  "par_p_38": {
    "desc": {
      "en": "Bohemian canal walkway famous from the movie Amélie, lined with tree-shaded iron footbridges.",
      "ja": "映画『アメリ』で有名なボヘミアンな運河の遊歩道。木陰の鉄製歩道橋が並んでいます。",
      "zh": "因电影《天使爱美丽》而闻名的波西米亚运河步道，绿树成荫，铁桥横跨。",
      "fr": "Promenade bohème le long du canal, célèbre grâce au film Amélie Poulain, bordée de passerelles en fer ombragées.",
      "de": "Böhmische Kanalpromenade, berühmt aus dem Film Amélie, gesäumt von schattigen Eisenbrücken.",
      "es": "Paseo bohemio por el canal famoso por la película Amélie, bordeado de pasarelas de hierro a la sombra de los árboles.",
      "nl": "Boheemse kanaalwandeling, beroemd uit de film Amélie, omzoomd met met bomen beschaduwde ijzeren loopbruggen."
    },
    "tip": {
      "en": "Stroll along the iron footbridges, watch lock gates open for boats, and visit independent coffee shops and vintage boutiques.",
      "ja": "鉄製の歩道橋を歩き、船を通すために水門が開くのを見て、独立系カフェやヴィンテージショップを訪れましょう。",
      "zh": "漫步在铁制人行桥上，观看船只经过时水闸开启，并参观独立咖啡馆和古着精品店。",
      "fr": "Flânez sur les passerelles en fer, regardez les écluses s'ouvrir pour les bateaux et visitez les cafés indépendants et les boutiques vintage.",
      "de": "Schlendern Sie über die Eisenbrücken, beobachten Sie, wie sich die Schleusen für Boote öffnen, und besuchen Sie unabhängige Cafés und Vintage-Boutiquen.",
      "es": "Pasea por las pasarelas de hierro, observa cómo se abren las esclusas para los barcos y visita cafeterías independientes y boutiques vintage.",
      "nl": "Wandel over de ijzeren loopbruggen, kijk hoe de sluizen opengaan voor boten en bezoek onafhankelijke coffeeshops en vintage boetieks."
    },
    "whyThisSpot": {
      "en": "Offers a trendy, relaxed local vibe away from the crowded city center, perfect for romantic walks.",
      "ja": "混雑した市内中心部から離れ、トレンディでリラックスした地元の雰囲気を提供しており、ロマンチックな散歩に最適です。",
      "zh": "提供远离拥挤市中心的时尚、轻松的本地氛围，非常适合浪漫散步。",
      "fr": "Offre une ambiance locale branchée et détendue, loin du centre-ville bondé, parfaite pour des promenades romantiques.",
      "de": "Bietet eine trendige, entspannte lokale Atmosphäre abseits des überfüllten Stadtzentrums, perfekt für romantische Spaziergänge.",
      "es": "Ofrece un ambiente local moderno y relajado lejos del abarrotado centro de la ciudad, perfecto para paseos románticos.",
      "nl": "Biedt een trendy, ontspannen lokale sfeer weg van het drukke stadscentrum, perfect voor romantische wandelingen."
    }
  },
  "par_p_39": {
    "desc": {
      "en": "Opulent royal palace featuring the breathtaking Hall of Mirrors and vast, meticulously landscaped estate gardens.",
      "ja": "息を呑むような鏡の間と、広大で細部まで手入れされた庭園を特徴とする豪華な王宮。",
      "zh": "奢华的皇家宫殿，以令人惊叹的镜厅和广阔、精心布置的庄园花园为特色。",
      "fr": "Opulent palais royal avec son époustouflante Galerie des Glaces et ses vastes jardins méticuleusement aménagés.",
      "de": "Opulenter Königspalast mit dem atemberaubenden Spiegelsaal und weitläufigen, sorgfältig angelegten Gärten.",
      "es": "Opulento palacio real con el impresionante Salón de los Espejos y extensos jardines meticulosamente cuidados.",
      "nl": "Weelderig koninklijk paleis met de adembenemende Spiegelzaal en uitgestrekte, zorgvuldig aangelegde landgoedtuinen."
    },
    "tip": {
      "en": "Pre-book tickets online to skip the massive queues. Rent a golf cart or bike to fully explore the sprawling gardens and Marie Antoinette's estate.",
      "ja": "大行列を避けるために事前にオンラインでチケットを予約してください。広大な庭園やマリー・アントワネットの領地を探索するには、ゴルフカートや自転車のレンタルが便利です。",
      "zh": "提前在网上预订门票以跳过长长的队伍。租一辆高尔夫球车或自行车，全面探索广阔的花园和玛丽·安托瓦内特的庄园。",
      "fr": "Réservez vos billets en ligne pour éviter les files d'attente. Louez une voiturette de golf ou un vélo pour explorer les vastes jardins et le domaine de Marie-Antoinette.",
      "de": "Buchen Sie Tickets vorab online, um die langen Schlangen zu umgehen. Mieten Sie ein Golfkart oder Fahrrad, um die weitläufigen Gärten und das Anwesen von Marie Antoinette zu erkunden.",
      "es": "Reserva las entradas online para evitar las enormes colas. Alquila un carrito de golf o una bicicleta para explorar completamente los extensos jardines y la finca de María Antonieta.",
      "nl": "Boek tickets vooraf online om de enorme rijen over te slaan. Huur een golfkar of fiets om de uitgestrekte tuinen en het landgoed van Marie Antoinette volledig te verkennen."
    },
    "whyThisSpot": {
      "en": "A monumental symbol of French royal absolute power, showcasing unmatched artistic and architectural grandeur.",
      "ja": "フランス王室の絶対的権力の記念碑的象徴であり、比類のない芸術的および建築的壮大さを示しています。",
      "zh": "法国王室绝对权力的不朽象征，展现了无与伦比的艺术和建筑宏伟。",
      "fr": "Un symbole monumental du pouvoir absolu royal français, mettant en valeur une grandeur artistique et architecturale inégalée.",
      "de": "Ein monumentales Symbol der französischen königlichen absoluten Macht, das unvergleichliche künstlerische und architektonische Pracht zeigt.",
      "es": "Un símbolo monumental del poder absoluto de la realeza francesa, que muestra una grandeza artística y arquitectónica inigualable.",
      "nl": "Een monumentaal symbool van de absolute macht van de Franse royalty, met een ongeëvenaarde artistieke en architectonische grandeur."
    }
  },
  "par_p_41": {
    "desc": {
      "en": "Stunning medieval royal palace turned revolutionary prison, infamous for holding Marie Antoinette.",
      "ja": "革命中に刑務所となった見事な中世の王宮。マリー・アントワネットが収監されていたことで有名です。",
      "zh": "令人惊叹的中世纪王宫，后来变成了革命时期的监狱，因关押玛丽·安托瓦内特而臭名昭著。",
      "fr": "Superbe palais royal médiéval devenu prison révolutionnaire, célèbre pour avoir détenu Marie-Antoinette.",
      "de": "Atemberaubender mittelalterlicher Königspalast, der zum Revolutionsgefängnis wurde und berüchtigt dafür ist, Marie Antoinette gefangen gehalten zu haben.",
      "es": "Impresionante palacio real medieval convertido en prisión revolucionaria, tristemente célebre por haber albergado a María Antonieta.",
      "nl": "Prachtig middeleeuws koninklijk paleis dat een revolutionaire gevangenis werd, berucht vanwege het vasthouden van Marie Antoinette."
    },
    "tip": {
      "en": "Discover the incredible Gothic architecture of the Salle des Gens d'Armes and use the augmented reality Histopad to see how it looked centuries ago.",
      "ja": "憲兵の間の素晴らしいゴシック建築を発見し、ARヒストパッドを使って何世紀も前の姿を確認しましょう。",
      "zh": "探索宪兵大厅令人惊叹的哥特式建筑，并使用增强现实 Histopad 看看它几个世纪前的样子。",
      "fr": "Découvrez l'incroyable architecture gothique de la Salle des Gens d'Armes et utilisez l'Histopad en réalité augmentée pour voir à quoi elle ressemblait il y a des siècles.",
      "de": "Entdecken Sie die unglaubliche gotische Architektur des Salle des Gens d'Armes und nutzen Sie das Augmented-Reality-Histopad, um zu sehen, wie es vor Jahrhunderten aussah.",
      "es": "Descubre la increíble arquitectura gótica de la Salle des Gens d'Armes y usa el Histopad de realidad aumentada para ver cómo lucía hace siglos.",
      "nl": "Ontdek de ongelooflijke gotische architectuur van de Salle des Gens d'Armes en gebruik de augmented reality Histopad om te zien hoe het er eeuwen geleden uitzag."
    },
    "whyThisSpot": {
      "en": "A deeply evocative historical site offering a stark contrast between royal splendor and the grim reality of the Revolution.",
      "ja": "王室の栄華と革命の厳しい現実との際立ったコントラストを提供する、深く心に響く歴史的場所です。",
      "zh": "一个极具感染力的历史遗迹，展现了皇室的辉煌与大革命残酷现实之间的鲜明对比。",
      "fr": "Un site historique profondément évocateur offrant un contraste saisissant entre la splendeur royale et la sombre réalité de la Révolution.",
      "de": "Eine zutiefst eindrucksvolle historische Stätte, die einen starken Kontrast zwischen königlicher Pracht und der düsteren Realität der Revolution bietet.",
      "es": "Un sitio histórico profundamente evocador que ofrece un marcado contraste entre el esplendor real y la sombría realidad de la Revolución.",
      "nl": "Een diep suggestieve historische locatie die een schril contrast biedt tussen koninklijke pracht en de grimmige realiteit van de Revolutie."
    }
  },
  "par_p_42": {
    "desc": {
      "en": "Paris's oldest planned square in the Marais district, enclosed by elegant red-brick arcades and the home of Victor Hugo.",
      "ja": "マレ地区にあるパリ最古の計画広場。エレガントな赤レンガのアーケードに囲まれ、ヴィクトル・ユゴーの家があります。",
      "zh": "巴黎玛黑区最古老的规划广场，被优雅的红砖拱廊环绕，维克多·雨果的故居也在这里。",
      "fr": "La plus ancienne place planifiée de Paris dans le Marais, entourée d'élégantes arcades en briques rouges et abritant la maison de Victor Hugo.",
      "de": "Der älteste geplante Platz von Paris im Marais, umschlossen von eleganten roten Backsteinarkaden und der Heimat von Victor Hugo.",
      "es": "La plaza planificada más antigua de París en el Marais, rodeada de elegantes arcadas de ladrillo rojo y hogar de Victor Hugo.",
      "nl": "Het oudste geplande plein van Parijs in de wijk Marais, omgeven door elegante rode bakstenen arcades en de thuisbasis van Victor Hugo."
    },
    "tip": {
      "en": "Stroll through the perfectly symmetrical gardens, admire the architecture, and visit the free Maison de Victor Hugo located right on the square.",
      "ja": "完全な対称をなす庭園を散策し、建築を堪能し、広場に位置する無料のヴィクトル・ユゴーの家を訪れてください。",
      "zh": "漫步于完美对称的花园中，欣赏建筑，并参观广场上免费开放的维克多·雨果故居。",
      "fr": "Promenez-vous dans les jardins parfaitement symétriques, admirez l'architecture et visitez la Maison de Victor Hugo gratuite située sur la place.",
      "de": "Spazieren Sie durch die perfekt symmetrischen Gärten, bewundern Sie die Architektur und besuchen Sie das kostenlose Maison de Victor Hugo direkt am Platz.",
      "es": "Pasea por los jardines perfectamente simétricos, admira la arquitectura y visita la Maison de Victor Hugo (entrada gratuita) ubicada en la plaza.",
      "nl": "Wandel door de perfect symmetrische tuinen, bewonder de architectuur en bezoek het gratis Maison de Victor Hugo, direct aan het plein."
    },
    "whyThisSpot": {
      "en": "A peaceful, breathtaking architectural gem that captures the upscale charm and history of the Marais district.",
      "ja": "マレ地区の高級な魅力と歴史を捉えた、平和で息を呑むような建築の宝石です。",
      "zh": "一颗宁静、令人惊叹的建筑明珠，捕捉了玛黑区的高档魅力和历史。",
      "fr": "Un joyau architectural paisible et époustouflant qui capture le charme haut de gamme et l'histoire du Marais.",
      "de": "Ein friedliches, atemberaubendes architektonisches Juwel, das den gehobenen Charme und die Geschichte des Marais-Viertels einfängt.",
      "es": "Una joya arquitectónica pacífica e impresionante que captura el encanto elegante y la historia del barrio de Marais.",
      "nl": "Een vredig, adembenemend architectonisch juweeltje dat de chique charme en geschiedenis van de wijk Marais weerspiegelt."
    }
  },
  "par_p_44": {
    "desc": {
      "en": "Frank Gehry's modern architectural masterpiece hosting world-class contemporary art exhibitions in the Bois de Boulogne.",
      "ja": "ブローニュの森にあるフランク・ゲーリーの現代建築の傑作。世界クラスの現代美術展を開催しています。",
      "zh": "位于布洛涅森林的弗兰克·盖里现代建筑杰作，举办世界级的当代艺术展览。",
      "fr": "Chef-d'œuvre de l'architecture moderne de Frank Gehry accueillant des expositions d'art contemporain de renommée mondiale dans le bois de Boulogne.",
      "de": "Frank Gehrys modernes architektonisches Meisterwerk, das hochkarätige Ausstellungen zeitgenössischer Kunst im Bois de Boulogne beherbergt.",
      "es": "La obra maestra de la arquitectura moderna de Frank Gehry que alberga exposiciones de arte contemporáneo de primer nivel en el Bois de Boulogne.",
      "nl": "Frank Gehry's moderne architectonische meesterwerk waar hedendaagse kunsttentoonstellingen van wereldklasse worden gehouden in het Bois de Boulogne."
    },
    "tip": {
      "en": "Admire the stunning glass 'sails' and head to the upper outdoor terraces for a magnificent panoramic view over Paris and La Défense.",
      "ja": "見事なガラスの「帆」を鑑賞し、上層部の屋外テラスへ向かい、パリとラ・デファンスの素晴らしいパノラマビューを楽しんでください。",
      "zh": "欣赏令人惊叹的玻璃“风帆”，并前往上层户外露台，饱览巴黎和拉德芳斯的壮丽全景。",
      "fr": "Admirez les superbes 'voiles' de verre et rendez-vous sur les terrasses extérieures supérieures pour une magnifique vue panoramique sur Paris et La Défense.",
      "de": "Bewundern Sie die atemberaubenden Glas-'Segel' und gehen Sie auf die oberen Außenterrassen für einen herrlichen Panoramablick über Paris und La Défense.",
      "es": "Admira las impresionantes 'velas' de cristal y dirígete a las terrazas al aire libre superiores para disfrutar de una magnífica vista panorámica sobre París y La Défense.",
      "nl": "Bewonder de prachtige glazen 'zeilen' en ga naar de bovenste buitenterrassen voor een prachtig panoramisch uitzicht over Parijs en La Défense."
    },
    "whyThisSpot": {
      "en": "A cutting-edge fusion of ambitious architecture and premier global art collections that redefines the Parisian landscape.",
      "ja": "野心的な建築と世界有数のアートコレクションが融合し、パリの景観を再定義する最先端のスポットです。",
      "zh": "雄心勃勃的建筑与全球顶级艺术收藏的尖端融合，重新定义了巴黎的景观。",
      "fr": "Une fusion avant-gardiste entre une architecture ambitieuse et de grandes collections d'art mondiales qui redéfinit le paysage parisien.",
      "de": "Eine hochmoderne Verschmelzung von anspruchsvoller Architektur und führenden globalen Kunstsammlungen, die die Pariser Landschaft neu definiert.",
      "es": "Una fusión de vanguardia de arquitectura ambiciosa y colecciones de arte mundiales de primer nivel que redefine el paisaje parisino.",
      "nl": "Een baanbrekende fusie van ambitieuze architectuur en vooraanstaande wereldwijde kunstcollecties die het Parijse landschap herdefinieert."
    }
  },
  "par_p_45": {
    "desc": {
      "en": "Latin Quarter museum dedicated to the Middle Ages, famous for the magnificent 'The Lady and the Unicorn' tapestries.",
      "ja": "カルチエ・ラタンにある中世専門の博物館。見事な「貴婦人と一角獣」のタペストリーで有名です。",
      "zh": "位于拉丁区的中世纪博物馆，以宏伟的《女士与独角兽》挂毯而闻名。",
      "fr": "Musée du Quartier Latin consacré au Moyen Âge, célèbre pour la magnifique tenture de 'La Dame à la Licorne'.",
      "de": "Museum im Quartier Latin, das dem Mittelalter gewidmet ist und für die prächtigen Wandteppiche 'Die Dame mit dem Einhorn' berühmt ist.",
      "es": "Museo del Barrio Latino dedicado a la Edad Media, famoso por los magníficos tapices de 'La dama y el unicornio'.",
      "nl": "Museum in het Quartier Latin gewijd aan de Middeleeuwen, beroemd om de prachtige wandtapijten van 'De Vrouwe en de Eenhoorn'."
    },
    "tip": {
      "en": "Step back in time to explore ancient Roman baths preserved right under the museum, alongside unparalleled medieval artifacts.",
      "ja": "時代を遡り、比類のない中世の遺物とともに、博物館の地下に保存されている古代ローマの公衆浴場を探索してください。",
      "zh": "穿越回过去，探索保存在博物馆下方的古罗马浴场，以及无与伦比的中世纪文物。",
      "fr": "Remontez le temps pour explorer les anciens thermes romains préservés juste sous le musée, aux côtés d'objets médiévaux sans précédent.",
      "de": "Machen Sie eine Zeitreise, um antike römische Bäder zu erkunden, die direkt unter dem Museum erhalten sind, zusammen mit unvergleichlichen mittelalterlichen Artefakten.",
      "es": "Retrocede en el tiempo para explorar los antiguos baños romanos conservados justo debajo del museo, junto con artefactos medievales incomparables.",
      "nl": "Ga terug in de tijd om de oude Romeinse baden te verkennen die direct onder het museum bewaard zijn gebleven, naast ongeëvenaarde middeleeuwse artefacten."
    },
    "whyThisSpot": {
      "en": "A rare opportunity to experience medieval life and art within the ancient walls of a 15th-century residence and 1st-century thermal baths.",
      "ja": "15世紀の邸宅と1世紀の公衆浴場の古代の壁の中で、中世の生活や芸術を体験できる貴重な機会です。",
      "zh": "这是在15世纪的住宅和1世纪的浴场古老墙壁内体验中世纪生活和艺术的罕见机会。",
      "fr": "Une occasion rare de découvrir la vie et l'art du Moyen Âge dans les murs anciens d'une résidence du 15ème siècle et de thermes du 1er siècle.",
      "de": "Eine seltene Gelegenheit, mittelalterliches Leben und Kunst in den alten Mauern einer Residenz aus dem 15. Jahrhundert und von Thermen aus dem 1. Jahrhundert zu erleben.",
      "es": "Una oportunidad única de experimentar la vida y el arte medievales dentro de los antiguos muros de una residencia del siglo XV y baños termales del siglo I.",
      "nl": "Een zeldzame kans om het middeleeuwse leven en de kunst te ervaren binnen de oude muren van een 15e-eeuwse residentie en 1e-eeuwse thermale baden."
    }
  },
  "par_p_46": {
    "desc": {
      "en": "World-famous Disney theme park featuring Sleeping Beauty Castle & Marvel Avengers Campus.",
      "ja": "眠れる森の美女の城とマーベル・アベンジャーズ・キャンパスがある世界的に有名なディズニー・テーマパーク。",
      "zh": "世界著名的迪士尼主题公园，拥有睡美人城堡和漫威复仇者校园。",
      "fr": "Parc à thème Disney de renommée mondiale comprenant le Château de la Belle au Bois Dormant et le Marvel Avengers Campus.",
      "de": "Weltberühmter Disney-Themenpark mit dem Dornröschenschloss und dem Marvel Avengers Campus.",
      "es": "Parque temático de Disney mundialmente famoso que cuenta con el Castillo de la Bella Durmiente y el Marvel Avengers Campus.",
      "nl": "Wereldberoemd Disney-themapark met het kasteel van Doornroosje en Marvel Avengers Campus."
    },
    "tip": {
      "en": "Features two parks: Disneyland Park and Walt Disney Studios. The pink Sleeping Beauty Castle is considered the most romantic Disney castle worldwide. 40 min via RER A train.",
      "ja": "ディズニーランド・パークとウォルト・ディズニー・スタジオの2つのパークがあります。ピンク色の城は世界で最もロマンチックと言われます。RER A線で40分。",
      "zh": "包括两个乐园：迪士尼乐园和华特迪士尼影城。粉色的睡美人城堡被认为是全球最浪漫的。乘坐RER A线40分钟可达。",
      "fr": "Comprend deux parcs : le Parc Disneyland et les Walt Disney Studios. Le château rose de la Belle au Bois Dormant est le plus romantique au monde. À 40 min en RER A.",
      "de": "Umfasst zwei Parks: Disneyland Park und Walt Disney Studios. Das rosa Dornröschenschloss gilt als das romantischste weltweit. 40 Minuten mit dem RER A-Zug.",
      "es": "Cuenta con dos parques: Disneyland Park y Walt Disney Studios. El castillo rosa de la Bella Durmiente es considerado el más romántico del mundo. A 40 min en tren RER A.",
      "nl": "Heeft twee parken: Disneyland Park en Walt Disney Studios. Het roze Kasteel van Doornroosje wordt beschouwd als het meest romantische ter wereld. 40 min via RER A trein."
    },
    "whyThisSpot": {
      "en": "The ultimate family destination combining classic Disney magic with unique Parisian flair and spectacular nighttime shows.",
      "ja": "クラシックなディズニーの魔法とパリならではの魅力、そして壮大なナイトショーを組み合わせた最高の家族の目的地。",
      "zh": "终极家庭度假胜地，将经典的迪士尼魔法与独特的巴黎风情以及壮观的夜间表演相结合。",
      "fr": "La destination familiale par excellence alliant la magie classique de Disney à une touche parisienne unique et des spectacles nocturnes spectaculaires.",
      "de": "Das ultimative Familienziel, das klassische Disney-Magie mit einzigartigem Pariser Flair und spektakulären Abendshows kombiniert.",
      "es": "El destino familiar por excelencia que combina la magia clásica de Disney con un toque parisino único y espectaculares espectáculos nocturnos.",
      "nl": "De ultieme familiebestemming die klassieke Disney-magie combineert met een unieke Parijse flair en spectaculaire avondshows."
    }
  },
  "par_p_47": {
    "desc": {
      "en": "Stunning glass-roofed museum in Jardin des Plantes featuring a procession of 7,000 taxidermy animals.",
      "ja": "パリ植物園にあるガラス屋根の見事な博物館で、7,000体もの動物の剥製の大行進が展示されています。",
      "zh": "位于植物园内、令人惊叹的玻璃屋顶博物馆，展出由7000只动物标本组成的壮观游行。",
      "fr": "Superbe musée à verrière dans le Jardin des Plantes, présentant une caravane de 7 000 animaux naturalisés.",
      "de": "Atemberaubendes Museum mit Glasdach im Jardin des Plantes mit einer Prozession von 7.000 präparierten Tieren.",
      "es": "Impresionante museo con techo de cristal en el Jardin des Plantes que presenta una procesión de 7000 animales disecados.",
      "nl": "Prachtig museum met glazen dak in de Jardin des Plantes met een stoet van 7.000 opgezette dieren."
    },
    "tip": {
      "en": "Located inside the Jardin des Plantes, this museum features a dramatic procession of taxidermy African savanna animals under a soaring glass roof.",
      "ja": "植物園内にあるこの博物館は、高いガラス屋根の下でアフリカのサバンナの動物の劇的な行進を展示しています。",
      "zh": "这座博物馆位于植物园内，在巨大的玻璃屋顶下展示着戏剧性的非洲大草原动物标本游行。",
      "fr": "Situé dans le Jardin des Plantes, ce musée présente une impressionnante caravane d'animaux de la savane africaine sous une immense verrière.",
      "de": "Dieses Museum befindet sich im Jardin des Plantes und bietet eine dramatische Prozession von präparierten afrikanischen Savannentieren unter einem riesigen Glasdach.",
      "es": "Ubicado dentro del Jardin des Plantes, este museo presenta una dramática procesión de animales disecados de la sabana africana bajo un enorme techo de cristal.",
      "nl": "Gelegen in de Jardin des Plantes, dit museum toont een dramatische stoet van opgezette Afrikaanse savannedieren onder een enorm glazen dak."
    },
    "whyThisSpot": {
      "en": "A visually spectacular and educational experience that vividly brings global biodiversity to life for all ages.",
      "ja": "世界中の生物多様性を全世代に向けて生き生きと蘇らせる、視覚的に壮観で教育的な体験。",
      "zh": "一场视觉上的壮观和教育体验，为各个年龄段生动呈现了全球生物多样性。",
      "fr": "Une expérience visuellement spectaculaire et éducative qui donne vie à la biodiversité mondiale pour tous les âges.",
      "de": "Ein visuell spektakuläres und lehrreiches Erlebnis, das die globale Artenvielfalt für alle Altersgruppen lebendig werden lässt.",
      "es": "Una experiencia visualmente espectacular y educativa que da vida a la biodiversidad mundial para todas las edades.",
      "nl": "Een visueel spectaculaire en educatieve ervaring die de wereldwijde biodiversiteit levendig tot leven brengt voor alle leeftijden."
    }
  },
  "par_p_48": {
    "desc": {
      "en": "Europe's largest science museum featuring the interactive Cité des Enfants and the Geode IMAX sphere.",
      "ja": "インタラクティブな子供向け施設「シテ・デ・ザンファン」とIMAXシアターの球体「ジェオード」を備えたヨーロッパ最大の科学博物館。",
      "zh": "欧洲最大的科学博物馆，设有互动式的儿童城和Geode IMAX球幕影院。",
      "fr": "Le plus grand musée des sciences d'Europe, avec la Cité des Enfants interactive et la sphère IMAX de la Géode.",
      "de": "Europas größtes Wissenschaftsmuseum mit der interaktiven Cité des Enfants und der Geode IMAX-Kugel.",
      "es": "El museo de ciencias más grande de Europa, con la interactiva Cité des Enfants y la esfera Geode IMAX.",
      "nl": "Het grootste wetenschapsmuseum van Europa met de interactieve Cité des Enfants en de Geode IMAX-bol."
    },
    "tip": {
      "en": "Reserve time slots for the Cité des Enfants interactive zone online in advance. Don't miss exploring the real Argonaut submarine outside!",
      "ja": "子供向けインタラクティブゾーンの入場枠はオンラインで事前予約してください。屋外にある本物の潜水艦「アルゴノート」の探索もお見逃しなく！",
      "zh": "提前在网上预约儿童城互动区的名额。千万别错过探索外面的真实Argonaut潜艇！",
      "fr": "Réservez à l'avance en ligne vos créneaux pour la zone interactive de la Cité des Enfants. Ne manquez pas d'explorer le vrai sous-marin Argonaute à l'extérieur !",
      "de": "Reservieren Sie vorab online Zeitfenster für den interaktiven Bereich der Cité des Enfants. Verpassen Sie nicht, das echte U-Boot Argonaute draußen zu erkunden!",
      "es": "Reserva plazas para la zona interactiva Cité des Enfants con antelación online. ¡No te pierdas explorar el submarino real Argonaute en el exterior!",
      "nl": "Reserveer vooraf online tijdvakken voor de interactieve zone van de Cité des Enfants. Mis niet de kans om de echte Argonaute onderzeeër buiten te verkennen!"
    },
    "whyThisSpot": {
      "en": "An unmatched wonderland of hands-on science and technology that captivates curious minds of every age.",
      "ja": "あらゆる年齢層の好奇心をとらえて離さない、実践的な科学と技術の比類なきワンダーランド。",
      "zh": "无与伦比的动手科学与技术仙境，吸引着各个年龄段充满好奇心的人。",
      "fr": "Un pays des merveilles inégalé de sciences et technologies interactives qui captive les esprits curieux de tous âges.",
      "de": "Ein unvergleichliches Wunderland der angewandten Wissenschaft und Technik, das neugierige Köpfe jeden Alters fesselt.",
      "es": "Un país de las maravillas inigualable de ciencia y tecnología prácticas que cautiva a mentes curiosas de todas las edades.",
      "nl": "Een ongeëvenaard wonderland van praktijkgerichte wetenschap en technologie dat nieuwsgierige geesten van elke leeftijd fascineert."
    }
  },
  "par_p_49": {
    "desc": {
      "en": "Historic 45-acre children's amusement park in Bois de Boulogne with rides, puppet shows, and farm animals.",
      "ja": "ブローニュの森にある歴史的な遊園地。乗り物、人形劇、農場の動物が楽しめます。",
      "zh": "位于布洛涅森林的占地45英亩的历史儿童游乐园，拥有游乐设施、木偶戏和农场动物。",
      "fr": "Parc d'attractions historique pour enfants dans le bois de Boulogne avec manèges, spectacles de marionnettes et animaux de ferme.",
      "de": "Historischer, 45 Hektar großer Kinder-Vergnügungspark im Bois de Boulogne mit Fahrgeschäften, Puppentheater und Bauernhoftieren.",
      "es": "Histórico parque de atracciones infantil de 45 acres en el Bois de Boulogne con atracciones, espectáculos de marionetas y animales de granja.",
      "nl": "Historisch 45 hectare groot kinderpretpark in het Bois de Boulogne met attracties, poppenkasten en boerderijdieren."
    },
    "tip": {
      "en": "A perfect family escape in the Bois de Boulogne. It's a charming, less-crowded alternative to larger theme parks with gentle rides and a small farm.",
      "ja": "ブローニュの森にある完璧な家族向けの避暑地。小さな農場や穏やかな乗り物があり、混雑の少ない魅力的な代替手段です。",
      "zh": "布洛涅森林中完美的家庭度假胜地。这里有温和的游乐设施和小型农场，是大型主题公园的迷人且不那么拥挤的替代方案。",
      "fr": "Une escapade parfaite en famille dans le Bois de Boulogne. C'est une alternative charmante et moins fréquentée aux grands parcs d'attractions.",
      "de": "Ein perfekter Familienausflug im Bois de Boulogne. Eine charmante, weniger überfüllte Alternative zu größeren Themenparks mit sanften Fahrgeschäften.",
      "es": "Una escapada familiar perfecta en el Bois de Boulogne. Es una alternativa encantadora y menos concurrida a los grandes parques temáticos con atracciones suaves.",
      "nl": "Een perfect familie-uitje in het Bois de Boulogne. Een charmant, minder druk alternatief voor grotere themaparken met rustige attracties."
    },
    "whyThisSpot": {
      "en": "Blends Parisian charm with classic amusement, offering a nostalgic, nature-filled retreat for young families.",
      "ja": "パリの魅力とクラシックな娯楽が融合し、若い家族にノスタルジックで自然豊かな隠れ家を提供します。",
      "zh": "将巴黎风情与经典的娱乐相融合，为年轻家庭提供了一个怀旧、充满自然气息的避风港。",
      "fr": "Mêle le charme parisien aux divertissements classiques, offrant une retraite nostalgique en pleine nature pour les jeunes familles.",
      "de": "Verbindet Pariser Charme mit klassischen Vergnügungen und bietet einen nostalgischen, naturnahen Rückzugsort für junge Familien.",
      "es": "Combina el encanto parisino con el entretenimiento clásico, ofreciendo un refugio nostálgico y lleno de naturaleza para las familias jóvenes.",
      "nl": "Combineert Parijse charme met klassiek amusement en biedt een nostalgisch, natuurrijk toevluchtsoord voor jonge gezinnen."
    }
  },
  "par_p_51": {
    "desc": {
      "en": "Underground aquarium at Trocadéro featuring 13,000 sea creatures, a shark tunnel, and a touching pool.",
      "ja": "トロカデロ広場の地下にある水族館。13,000匹の海洋生物、サメのトンネル、ふれあいプールがあります。",
      "zh": "位于特罗卡德罗的地下水族馆，拥有13000只海洋生物、鲨鱼隧道和触摸池。",
      "fr": "Aquarium souterrain au Trocadéro avec 13 000 créatures marines, un tunnel aux requins et un bassin tactile.",
      "de": "Unterirdisches Aquarium am Trocadéro mit 13.000 Meeresbewohnern, einem Haitunnel und einem Streichelbecken.",
      "es": "Acuario subterráneo en el Trocadéro con 13.000 criaturas marinas, un túnel de tiburones y una piscina táctil.",
      "nl": "Ondergronds aquarium bij Trocadéro met 13.000 zeedieren, een haaientunnel en een aanraakzwembad."
    },
    "tip": {
      "en": "Located near the Trocadéro, this underground aquarium is great for families. Experience the shark tunnel and catch one of the mermaid shows.",
      "ja": "トロカデロの近くにあるこの地下水族館は家族連れに最適です。サメのトンネルを体験し、マーメイドショーをお見逃しなく。",
      "zh": "这座地下水族馆位于特罗卡德罗附近，非常适合家庭游玩。体验鲨鱼隧道，看一场美人鱼表演吧。",
      "fr": "Situé près du Trocadéro, cet aquarium souterrain est idéal pour les familles. Profitez du tunnel aux requins et assistez aux spectacles de sirènes.",
      "de": "Dieses unterirdische Aquarium nahe dem Trocadéro ist ideal für Familien. Erleben Sie den Haitunnel und sehen Sie sich eine der Meerjungfrauen-Shows an.",
      "es": "Ubicado cerca del Trocadéro, este acuario subterráneo es ideal para familias. Experimenta el túnel de tiburones y no te pierdas el show de sirenas.",
      "nl": "Gelegen bij de Trocadéro, dit ondergrondse aquarium is geweldig voor gezinnen. Ervaar de haaientunnel en bekijk een van de zeemeerminshows."
    },
    "whyThisSpot": {
      "en": "A surprising aquatic escape right in the city center, offering a magical and engaging experience for kids.",
      "ja": "市の中心部にある驚きの水中の世界。子供たちに魔法のような魅力的な体験を提供します。",
      "zh": "市中心令人惊喜的水下世界，为孩子们提供神奇而迷人的体验。",
      "fr": "Une échappée aquatique surprenante en plein centre-ville, offrant une expérience magique et captivante pour les enfants.",
      "de": "Ein überraschender Ausflug in die Unterwasserwelt mitten im Stadtzentrum, der Kindern ein magisches Erlebnis bietet.",
      "es": "Una sorprendente escapada acuática justo en el centro de la ciudad, que ofrece una experiencia mágica y atractiva para los niños.",
      "nl": "Een verrassende aquatische ontsnapping midden in het stadscentrum, die kinderen een magische en boeiende ervaring biedt."
    }
  },
  "par_p_53": {
    "desc": {
      "en": "Historic royal garden between the Louvre and Place de la Concorde with tree-lined promenades and a summer funfair.",
      "ja": "ルーヴル美術館とコンコルド広場の間にある歴史的な王室庭園。並木道や夏期の移動遊園地があります。",
      "zh": "位于卢浮宫和协和广场之间的历史皇家花园，绿树成荫，夏季还有游乐场。",
      "fr": "Jardin royal historique entre le Louvre et la Place de la Concorde avec promenades arborées et fête foraine estivale.",
      "de": "Historischer königlicher Garten zwischen dem Louvre und der Place de la Concorde mit baumgesäumten Promenaden und einem Sommer-Vergnügungspark.",
      "es": "Histórico jardín real entre el Louvre y la Place de la Concorde con paseos arbolados y una feria de verano.",
      "nl": "Historische koninklijke tuin tussen het Louvre en Place de la Concorde met met bomen omzoomde promenades en een zomerkermis."
    },
    "tip": {
      "en": "Stretching between the Louvre and Place de la Concorde. In summer (June–August), a funfair with a giant Ferris wheel operates inside the park.",
      "ja": "ルーヴル美術館とコンコルド広場の間に位置しています。夏（6月〜8月）には、園内で巨大な観覧車のある遊園地がオープンします。",
      "zh": "横跨卢浮宫和协和广场之间。夏季（6月至8月），公园内会开设一个带有巨大摩天轮的游乐场。",
      "fr": "S'étend entre le Louvre et la Place de la Concorde. En été (juin-août), une fête foraine avec une grande roue géante s'installe dans le parc.",
      "de": "Erstreckt sich zwischen dem Louvre und der Place de la Concorde. Im Sommer (Juni–August) gibt es im Park einen Jahrmarkt mit Riesenrad.",
      "es": "Se extiende entre el Louvre y la Place de la Concorde. En verano (junio-agosto), hay una feria con una noria gigante en el interior del parque.",
      "nl": "Uitgestrekt tussen het Louvre en Place de la Concorde. In de zomer (juni-augustus) is er een kermis met een reuzenrad in het park."
    },
    "whyThisSpot": {
      "en": "An iconic outdoor haven offering leisurely strolls, art, and vibrant seasonal activities in the heart of Paris.",
      "ja": "パリの中心部で、のんびりとした散歩、アート、そして活気ある季節のイベントを楽しめる象徴的な屋外のオアシス。",
      "zh": "巴黎市中心标志性的户外天堂，提供悠闲的散步、艺术欣赏和充满活力的季节性活动。",
      "fr": "Un havre de paix emblématique offrant promenades, art et activités saisonnières animées au cœur de Paris.",
      "de": "Ein ikonischer Rückzugsort im Freien, der entspannte Spaziergänge, Kunst und lebhafte saisonale Aktivitäten im Herzen von Paris bietet.",
      "es": "Un refugio al aire libre icónico que ofrece paseos, arte y vibrantes actividades estacionales en el corazón de París.",
      "nl": "Een iconische buitenoase die ontspannende wandelingen, kunst en levendige seizoensgebonden activiteiten biedt in het hart van Parijs."
    }
  },
  "par_p_54": {
    "desc": {
      "en": "Historic aviation museum at Le Bourget featuring original Concorde supersonic jets & space rockets.",
      "ja": "ル・ブルジェにある歴史的な航空博物館。本物のコンコルド超音速旅客機やロケットが展示されています。",
      "zh": "位于布尔歇的历史航空博物馆，展出原版的协和超音速客机和太空火箭。",
      "fr": "Musée historique de l'aviation au Bourget présentant d'authentiques jets supersoniques Concorde et des fusées spatiales.",
      "de": "Historisches Luftfahrtmuseum in Le Bourget mit originalen Concorde-Überschalljets und Weltraumraketen.",
      "es": "Histórico museo de la aviación en Le Bourget que presenta aviones supersónicos Concorde originales y cohetes espaciales.",
      "nl": "Historisch luchtvaartmuseum op Le Bourget met originele Concorde supersonische jets en ruimteraketten."
    },
    "tip": {
      "en": "Located at Le Bourget Airport, this is the only place in the world where you can step inside two actual supersonic Concorde aircraft side by side.",
      "ja": "ル・ブルジェ空港に位置し、2機の本物の超音速コンコルドの内部に入ることができる世界で唯一の場所です。",
      "zh": "位于布尔歇机场，这是世界上唯一一个可以同时走进两架真实的超音速协和客机的地方。",
      "fr": "Situé à l'aéroport du Bourget, c'est le seul endroit au monde où vous pouvez pénétrer à l'intérieur de deux véritables Concorde côte à côte.",
      "de": "Am Flughafen Le Bourget gelegen, ist dies der einzige Ort auf der Welt, an dem man in zwei echte Concorde-Überschallflugzeuge nebeneinander steigen kann.",
      "es": "Ubicado en el aeropuerto de Le Bourget, este es el único lugar del mundo donde puedes entrar a dos aviones supersónicos Concorde reales uno al lado del otro.",
      "nl": "Gelegen op Le Bourget Airport, dit is de enige plek ter wereld waar je in twee echte supersonische Concorde-vliegtuigen naast elkaar kunt stappen."
    },
    "whyThisSpot": {
      "en": "A thrilling journey through aerospace history that lets you get incredibly close to legendary flying machines.",
      "ja": "伝説的な飛行機械に信じられないほど近づくことができる、航空宇宙の歴史を巡るスリリングな旅。",
      "zh": "一场激动人心的航空航天历史之旅，让您能令人难以置信地近距离接触传奇飞行器。",
      "fr": "Un voyage passionnant à travers l'histoire de l'aérospatiale qui vous permet de vous approcher incroyablement près d'appareils légendaires.",
      "de": "Eine spannende Reise durch die Geschichte der Luft- und Raumfahrt, die Sie legendären Flugmaschinen unglaublich nahe bringt.",
      "es": "Un emocionante viaje a través de la historia aeroespacial que te permite acercarte increíblemente a máquinas voladoras legendarias.",
      "nl": "Een spannende reis door de geschiedenis van de lucht- en ruimtevaart waarmee u ongelooflijk dicht bij legendarische vliegmachines kunt komen."
    }
  },
  "par_p_55": {
    "desc": {
      "en": "Interactive chocolate museum tracing 4,000 years of cacao history with live chocolate-making demonstrations.",
      "ja": "カカオの4000年の歴史をたどり、実演のチョコレート作りを楽しめるインタラクティブなチョコレート博物館。",
      "zh": "互动式巧克力博物馆，追溯了4000年的可可历史，并有现场巧克力制作演示。",
      "fr": "Musée du chocolat interactif retraçant 4 000 ans d'histoire du cacao avec des démonstrations en direct.",
      "de": "Interaktives Schokoladenmuseum, das 4.000 Jahre Kakao-Geschichte mit Live-Demonstrationen der Schokoladenherstellung nachzeichnet.",
      "es": "Museo interactivo del chocolate que repasa 4000 años de historia del cacao con demostraciones en vivo de elaboración de chocolate.",
      "nl": "Interactief chocolademuseum dat 4.000 jaar cacaogeschiedenis volgt met live chocolademaakdemonstraties."
    },
    "tip": {
      "en": "Gourmet chocolate museum featuring live chocolate-making demonstrations by master chocolatiers and unlimited tastings throughout the tour.",
      "ja": "一流のショコラティエによるチョコレート作りの実演と、ツアー中の食べ放題のテイスティングを特徴とするグルメチョコレート博物館。",
      "zh": "美食巧克力博物馆，有大师级巧克力师现场演示制作过程，以及在整个游览过程中无限量品尝。",
      "fr": "Musée gourmand proposant des démonstrations par des maîtres chocolatiers et des dégustations à volonté tout au long de la visite.",
      "de": "Gourmet-Schokoladenmuseum mit Live-Vorführungen von Meister-Chocolatiers und unbegrenzten Verkostungen während der gesamten Tour.",
      "es": "Museo de chocolate gourmet que ofrece demostraciones en vivo por maestros chocolateros y degustaciones ilimitadas durante el recorrido.",
      "nl": "Gourmet chocolademuseum met live chocoladedemonstraties door meester-chocolatiers en onbeperkte proeverijen gedurende de hele tour."
    },
    "whyThisSpot": {
      "en": "A delightfully delicious experience that engages all senses and satisfies every sweet tooth.",
      "ja": "五感を刺激し、甘いもの好きを満たす、最高に美味しくて楽しい体験。",
      "zh": "一场令人愉悦的美味体验，调动所有感官，满足每一个甜食爱好者。",
      "fr": "Une expérience délicieusement exquise qui éveille tous les sens et satisfait les amateurs de douceurs.",
      "de": "Ein herrlich köstliches Erlebnis, das alle Sinne anspricht und jede Naschkatze zufriedenstellt.",
      "es": "Una experiencia deliciosamente exquisita que involucra todos los sentidos y satisface a los más golosos.",
      "nl": "Een heerlijk verrukkelijke ervaring die alle zintuigen prikkelt en elke zoetekauw tevreden stelt."
    }
  },
  "rtm_ro_6": {
    "desc": {
      "en": "UNESCO World Heritage site featuring a historic drainage network of 19 monumental 18th-century working windmills.",
      "ja": "18世紀に建てられた19基の記念碑的な稼働する風車による歴史的排水ネットワークを特徴とするユネスコ世界遺産。",
      "zh": "联合国教科文组织世界遗产，拥有由19座18世纪历史悠久的工作风车组成的排水网络。",
      "fr": "Site du patrimoine mondial de l'UNESCO présentant un réseau de drainage historique de 19 moulins à vent monumentaux du XVIIIe siècle en activité.",
      "de": "UNESCO-Weltkulturerbe mit einem historischen Entwässerungsnetz aus 19 monumentalen, noch funktionierenden Windmühlen aus dem 18. Jahrhundert.",
      "es": "Patrimonio Mundial de la UNESCO que cuenta con una red histórica de drenaje de 19 molinos de viento monumentales en funcionamiento del siglo XVIII.",
      "nl": "UNESCO-werelderfgoed met een historisch afwateringsnetwerk van 19 monumentale 18e-eeuwse werkende windmolens."
    },
    "tip": {
      "en": "Board Waterbus Line 20 from Erasmusbrug (transfer at Ridderkerk to Driehoeksveer) or seasonal direct ferries. Canal paths are free to cycle.",
      "ja": "エラスムス橋から水上バス20番線に乗り（リッデルケルクで乗り換え）、または季節限定の直行フェリーで。運河の道はサイクリング無料です。",
      "zh": "从伊拉斯谟桥乘坐20路水上巴士（在里德凯尔克换乘）或季节性直达渡轮。运河小道可免费骑行。",
      "fr": "Prenez le Waterbus Ligne 20 depuis Erasmusbrug ou les ferries directs saisonniers. Les pistes cyclables le long des canaux sont gratuites.",
      "de": "Nehmen Sie die Waterbus-Linie 20 ab Erasmusbrug oder saisonale Direktfähren. Die Radwege an den Kanälen können kostenlos befahren werden.",
      "es": "Toma el Waterbus Línea 20 desde Erasmusbrug (transbordo en Ridderkerk) o los ferries directos de temporada. Los caminos del canal son gratis para andar en bicicleta.",
      "nl": "Neem Waterbus Lijn 20 vanaf de Erasmusbrug (overstappen bij Ridderkerk op het Driehoeksveer) of de seizoensgebonden directe veerboten. Fietsen over de kanaalpaden is gratis."
    },
    "whyThisSpot": {
      "en": "An iconic Dutch landscape offering an unmatched glimpse into the country's centuries-old battle against the water.",
      "ja": "オランダを象徴する風景で、数世紀にわたる水との戦いの歴史を垣間見ることができます。",
      "zh": "标志性的荷兰景观，让您一窥该国几个世纪以来与水的抗争史。",
      "fr": "Un paysage néerlandais emblématique offrant un aperçu inégalé de la bataille séculaire du pays contre l'eau.",
      "de": "Eine ikonische niederländische Landschaft, die einen unvergleichlichen Einblick in den jahrhundertelangen Kampf des Landes gegen das Wasser bietet.",
      "es": "Un paisaje holandés icónico que ofrece una visión inigualable de la batalla de siglos del país contra el agua.",
      "nl": "Een iconisch Nederlands landschap dat een ongeëvenaarde blik biedt op de eeuwenoude strijd van het land tegen het water."
    }
  }
}

with open("/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_chunk_8.json", "r") as f:
    data = json.load(f)

for item in data:
    spot = item["spot"]
    sid = spot["id"]
    if sid in master_texts:
        for lang, translation in master_texts[sid]["desc"].items():
            if lang == "en":
                spot["desc"] = translation
            spot[f"desc_{lang}"] = translation
            
        for lang, translation in master_texts[sid]["tip"].items():
            if lang == "en":
                spot["tip"] = translation
                spot["insiderTip"] = translation # just in case
            spot[f"tip_{lang}"] = translation
            
        for lang, translation in master_texts[sid]["whyThisSpot"].items():
            spot[f"whyThisSpot_{lang}"] = translation

with open("/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_written_8.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated 21 spots with multilingual Master Texts.")
