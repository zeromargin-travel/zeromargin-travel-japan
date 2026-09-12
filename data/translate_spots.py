import json

data_path = "/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_chunk_3.json"
out_path = "/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_written_3.json"

with open(data_path, "r", encoding="utf-8") as f:
    spots = json.load(f)

updates = {
    "cgn_c_27": {
        "desc": {
            "en": "A bustling central square and transport hub in Cologne, renowned for its upscale shopping passages, department stores, and dynamic atmosphere.",
            "ja": "ケルン中心部の活気ある交通結節点広場。高級ショッピングパサージュやデパートが立ち並び、ダイナミックな雰囲気が魅力です。",
            "zh": "科隆市中心繁华的交通枢纽广场，以其高档购物通道、百货商店和充满活力的氛围而闻名。",
            "fr": "Place centrale animée et pôle de transport de Cologne, réputée pour ses passages commerçants haut de gamme, ses grands magasins et son atmosphère dynamique.",
            "de": "Ein belebter zentraler Platz und Verkehrsknotenpunkt in Köln, bekannt für seine gehobenen Einkaufspassagen, Kaufhäuser und dynamische Atmosphäre.",
            "es": "Animada plaza central y centro de transporte en Colonia, famosa por sus exclusivos pasajes comerciales, grandes almacenes y un ambiente dinámico.",
            "nl": "Een levendig centraal plein en verkeersknooppunt in Keulen, beroemd om zijn luxe winkelpassages, warenhuizen en dynamische sfeer."
        },
        "tip": {
            "en": "Visit during winter (from late November) to experience the magical 'Markt der Engel' (Angel's Market) and its breathtaking star-shaped illuminations.",
            "ja": "冬（11月下旬〜）に訪れて、魔法のような『天使のクリスマス市（Markt der Engel）』と息をのむような星型のイルミネーションを体験してください。",
            "zh": "冬季（11月下旬起）来访，体验神奇的“天使市场”（Markt der Engel）及其令人惊叹的星形照明。",
            "fr": "Visitez en hiver (à partir de fin novembre) pour découvrir le féérique « Marché des Anges » et ses superbes illuminations en forme d'étoiles.",
            "de": "Besuchen Sie uns im Winter (ab Ende November), um den magischen 'Markt der Engel' und seine atemberaubenden sternförmigen Illuminationen zu erleben.",
            "es": "Visítalo en invierno (desde finales de noviembre) para experimentar el mágico 'Markt der Engel' (Mercado de los Ángeles) y sus impresionantes iluminaciones en forma de estrella.",
            "nl": "Bezoek in de winter (vanaf eind november) om de magische 'Markt der Engel' en de adembenemende stervormige verlichting te ervaren."
        },
        "whyThisSpot": {
            "en": "It seamlessly blends modern retail therapy with rich local history, making it an essential and vibrant starting point for any Cologne itinerary.",
            "ja": "モダンなショッピングと豊かな地元の歴史がシームレスに融合しており、ケルン観光の活気に満ちた出発点として欠かせない場所です。",
            "zh": "它将现代购物体验与丰富的当地历史完美融合，使其成为任何科隆行程中不可或缺且充满活力的起点。",
            "fr": "Il allie parfaitement le shopping moderne à la riche histoire locale, ce qui en fait un point de départ essentiel et dynamique pour tout itinéraire à Cologne.",
            "de": "Es verbindet nahtlos modernes Einkaufen mit reicher lokaler Geschichte und ist ein wesentlicher und lebendiger Ausgangspunkt für jede Köln-Reise.",
            "es": "Combina a la perfección las compras modernas con la rica historia local, convirtiéndose en un punto de partida esencial y vibrante para cualquier itinerario por Colonia.",
            "nl": "Het combineert naadloos modern winkelen met een rijke lokale geschiedenis, waardoor het een essentieel en levendig startpunt is voor elke reisroute door Keulen."
        }
    },
    "cgn_c_31": {
        "desc": {
            "en": "A massive, four-story historic beer hall in the heart of the Old Town, dedicated to 'Cologne's Heroes' with fascinating traditional murals.",
            "ja": "旧市街の中心部に位置する4階建ての巨大な歴史的ビアホール。魅力的な伝統的壁画とともに「ケルンの英雄たち」を讃えています。",
            "zh": "位于老城区中心的巨大的四层历史悠久的啤酒馆，以迷人的传统壁画向“科隆英雄”致敬。",
            "fr": "Une immense brasserie historique de quatre étages au cœur de la vieille ville, dédiée aux « Héros de Cologne » avec de fascinantes fresques traditionnelles.",
            "de": "Ein riesiges, vierstöckiges historisches Brauhaus im Herzen der Altstadt, das mit faszinierenden traditionellen Wandmalereien den 'Kölner Helden' gewidmet ist.",
            "es": "Una enorme cervecería histórica de cuatro pisos en el corazón del casco antiguo, dedicada a los 'Héroes de Colonia' con fascinantes murales tradicionales.",
            "nl": "Een enorme, historische bierhal van vier verdiepingen in het hart van de oude stad, gewijd aan de 'Helden van Keulen' met fascinerende traditionele muurschilderingen."
        },
        "tip": {
            "en": "Grab a table in the historic vaulted stone cellar (Gewölbekeller) and enjoy traditional Kölsch beer in an authentic, lively atmosphere.",
            "ja": "歴史的な石造りの地下丸天井（Gewölbekeller）の席を確保し、本格的で活気に満ちた雰囲気の中で伝統的なケルシュビールをお楽しみください。",
            "zh": "在历史悠久的拱形石窖（Gewölbekeller）里找个座位，在正宗、热闹的氛围中享用传统的科隆啤酒。",
            "fr": "Prenez une table dans la cave voûtée en pierre historique (Gewölbekeller) et dégustez une bière Kölsch traditionnelle dans une atmosphère authentique et animée.",
            "de": "Sichern Sie sich einen Tisch im historischen Steingewölbekeller und genießen Sie traditionelles Kölsch in authentischer, lebhafter Atmosphäre.",
            "es": "Toma una mesa en la histórica bodega de piedra abovedada (Gewölbekeller) y disfruta de una cerveza Kölsch tradicional en un ambiente auténtico y animado.",
            "nl": "Neem plaats in de historische stenen gewelfkelder (Gewölbekeller) en geniet van traditioneel Kölsch-bier in een authentieke, levendige sfeer."
        },
        "whyThisSpot": {
            "en": "It offers a deep dive into Cologne's legendary beer culture and history, providing an unforgettable, authentic German dining and drinking experience.",
            "ja": "ケルンの伝説的なビール文化と歴史を深く探求でき、忘れられない本格的なドイツの食事と飲酒の体験を提供します。",
            "zh": "它深入探讨了科隆传奇的啤酒文化和历史，提供令人难忘、正宗的德国餐饮体验。",
            "fr": "Elle offre une plongée profonde dans la légendaire culture et histoire de la bière de Cologne, offrant une expérience culinaire et brassicole allemande authentique et inoubliable.",
            "de": "Es bietet einen tiefen Einblick in Kölns legendäre Bierkultur und Geschichte und sorgt für ein unvergessliches, authentisches deutsches Ess- und Trinkerlebnis.",
            "es": "Ofrece una inmersión profunda en la legendaria cultura e historia de la cerveza de Colonia, brindando una experiencia gastronómica y de bebida alemana auténtica e inolvidable.",
            "nl": "Het biedt een diepe duik in de legendarische biercultuur en geschiedenis van Keulen en zorgt voor een onvergetelijke, authentieke Duitse eet- en drinkervaring."
        }
    },
    "fra_f_34": {
        "desc": {
            "en": "Germany's oldest independent museum of Jewish history and culture, beautifully housed in the magnificent historical Rothschild Palace.",
            "ja": "ドイツで最も古い独立したユダヤの歴史と文化の博物館。壮大な歴史的建造物であるロスチャイルド宮殿に美しく収容されています。",
            "zh": "德国最古老的独立犹太历史和文化博物馆，精美地坐落在宏伟的历史建筑罗斯柴尔德宫内。",
            "fr": "Le plus ancien musée indépendant d'histoire et de culture juive d'Allemagne, magnifiquement abrité dans le magnifique palais historique Rothschild.",
            "de": "Deutschlands ältestes unabhängiges Museum für jüdische Geschichte und Kultur, wunderschön untergebracht im prächtigen historischen Rothschild-Palais.",
            "es": "El museo independiente de historia y cultura judía más antiguo de Alemania, bellamente ubicado en el magnífico e histórico Palacio Rothschild.",
            "nl": "Het oudste onafhankelijke museum voor Joodse geschiedenis en cultuur van Duitsland, prachtig gehuisvest in het magnifieke historische Rothschild-paleis."
        },
        "tip": {
            "en": "Relax in the light-filled library café in the new annex, and savor traditional Jewish pastries alongside a cup of excellent coffee.",
            "ja": "新館の光あふれる図書カフェでリラックスし、美味しいコーヒーとともに伝統的なユダヤのペイストリーをご堪能ください。",
            "zh": "在附楼光线充足的图书馆咖啡厅里放松身心，品尝传统的犹太糕点和一杯美味的咖啡。",
            "fr": "Détendez-vous dans le café-bibliothèque baigné de lumière de la nouvelle annexe et savourez des pâtisseries juives traditionnelles accompagnées d'une excellente tasse de café.",
            "de": "Entspannen Sie im lichtdurchfluteten Bibliotheks-Café im neuen Anbau und genießen Sie traditionelles jüdisches Gebäck bei einer hervorragenden Tasse Kaffee.",
            "es": "Relájate en la luminosa cafetería biblioteca del nuevo anexo y saborea la repostería tradicional judía junto a una excelente taza de café.",
            "nl": "Ontspan in het zonovergoten bibliotheekcafé in de nieuwe vleugel en geniet van traditioneel Joods gebak met een uitstekende kop koffie."
        },
        "whyThisSpot": {
            "en": "An emotionally resonant and highly educational destination that meticulously preserves and presents centuries of rich Jewish heritage and stories.",
            "ja": "何世紀にもわたる豊かなユダヤの遺産と物語を細心の注意を払って保存・展示している、感情に響く非常に教育的な場所です。",
            "zh": "一个引起情感共鸣且极具教育意义的目的地，精心保存和展示了几个世纪以来丰富的犹太遗产和故事。",
            "fr": "Une destination émotionnellement résonnante et hautement éducative qui préserve et présente méticuleusement des siècles de riche héritage et d'histoires juives.",
            "de": "Ein emotional berührendes und hochgradig lehrreiches Ziel, das jahrhundertelanges reiches jüdisches Erbe und Geschichten sorgfältig bewahrt und präsentiert.",
            "es": "Un destino de resonancia emocional y altamente educativo que preserva y presenta meticulosamente siglos de rico patrimonio e historias judías.",
            "nl": "Een emotioneel resonerende en zeer educatieve bestemming die eeuwenlang rijk Joods erfgoed en verhalen zorgvuldig bewaart en presenteert."
        }
    },
    "fra_f_45": {
        "desc": {
            "en": "A charming retro streetcar operating since 1977, offering a unique, nostalgic sightseeing tour through Frankfurt's vibrant streets and iconic sights.",
            "ja": "1977年から運行している魅力的なレトロ市電。フランクフルトの活気ある通りや象徴的な名所を巡る、ユニークでノスタルジックな観光ツアーを提供します。",
            "zh": "一辆自 1977 年开始运营的迷人复古有轨电车，提供穿越法兰克福繁华街道和标志性景点的独特、怀旧的观光之旅。",
            "fr": "Un charmant tramway rétro en service depuis 1977, offrant une visite touristique nostalgique et unique à travers les rues animées et les sites emblématiques de Francfort.",
            "de": "Eine charmante Retro-Straßenbahn, die seit 1977 in Betrieb ist und eine einzigartige, nostalgische Sightseeing-Tour durch Frankfurts lebhafte Straßen und zu ikonischen Sehenswürdigkeiten bietet.",
            "es": "Un encantador tranvía retro en funcionamiento desde 1977, que ofrece un recorrido turístico único y nostálgico por las vibrantes calles y lugares emblemáticos de Frankfurt.",
            "nl": "Een charmante retro-tram die al sinds 1977 rijdt en een unieke, nostalgische sightseeingtour biedt door de levendige straten en iconische bezienswaardigheden van Frankfurt."
        },
        "tip": {
            "en": "Operates on weekends only! The ticket includes a delightful bottle of local apple wine (Ebbelwei) and a bag of pretzels to enjoy during the ride.",
            "ja": "週末のみ運行！チケットには、乗車中に楽しめる地元産のアップルワイン（エッベルヴァイ）のボトル1本とプレッツェルの小袋が含まれています。",
            "zh": "仅在周末运营！门票包括一瓶令人愉悦的当地苹果酒（Ebbelwei）和一袋椒盐卷饼，可在乘车期间享用。",
            "fr": "Circule uniquement le week-end ! Le billet comprend une délicieuse bouteille de vin de pomme local (Ebbelwei) et un sachet de bretzels à déguster pendant le trajet.",
            "de": "Fährt nur an Wochenenden! Im Ticketpreis enthalten sind eine köstliche Flasche lokaler Apfelwein (Ebbelwei) und eine Tüte Brezeln für die Fahrt.",
            "es": "¡Funciona solo los fines de semana! El billete incluye una deliciosa botella de vino de manzana local (Ebbelwei) y una bolsa de pretzels para disfrutar durante el viaje.",
            "nl": "Rijdt alleen in het weekend! Het kaartje is inclusief een heerlijk flesje lokale appelwijn (Ebbelwei) en een zakje pretzels om tijdens de rit van te genieten."
        },
        "whyThisSpot": {
            "en": "It is undeniably the most fun and nostalgic way to see the city's landmarks while enjoying traditional local culinary treats on the move.",
            "ja": "移動しながら地元の伝統的な名物料理を楽しみつつ、街のランドマークを見て回れる、間違いなく最も楽しくノスタルジックな方法です。",
            "zh": "无可否认，这是在移动中一边欣赏城市地标一边享用传统当地美食的最有趣、最怀旧的方式。",
            "fr": "C'est indéniablement le moyen le plus amusant et le plus nostalgique de voir les monuments de la ville tout en dégustant des spécialités culinaires locales traditionnelles en mouvement.",
            "de": "Es ist unbestreitbar die unterhaltsamste und nostalgischste Art, die Wahrzeichen der Stadt zu sehen, während man unterwegs traditionelle lokale kulinarische Köstlichkeiten genießt.",
            "es": "Es, sin duda, la forma más divertida y nostálgica de ver los lugares emblemáticos de la ciudad mientras se disfrutan delicias culinarias locales tradicionales en movimiento.",
            "nl": "Het is ongetwijfeld de leukste en meest nostalgische manier om de bezienswaardigheden van de stad te bekijken terwijl je onderweg geniet van traditionele lokale culinaire lekkernijen."
        }
    },
    "ham_h_2": {
        "desc": {
            "en": "Hamburg's iconic concert hall, featuring a stunning wave-like glass structure soaring gracefully above a historic red-brick warehouse in the bustling harbor.",
            "ja": "ハンブルクを象徴するコンサートホール。活気ある港の歴史的な赤レンガ倉庫の上に、波打つような美しいガラスの構造物が優雅にそびえ立ちます。",
            "zh": "汉堡标志性的音乐厅，拥有令人惊叹的波浪形玻璃结构，优雅地耸立在繁华港口历史悠久的红砖仓库上方。",
            "fr": "La salle de concert emblématique de Hambourg, dotée d'une superbe structure en verre ondulante qui s'élève gracieusement au-dessus d'un entrepôt historique en briques rouges dans le port animé.",
            "de": "Hamburgs ikonische Konzerthalle mit einer atemberaubenden wellenförmigen Glasstruktur, die sich anmutig über einem historischen Backsteinspeicher im geschäftigen Hafen erhebt.",
            "es": "La icónica sala de conciertos de Hamburgo, con una impresionante estructura de vidrio en forma de ola que se eleva con gracia sobre un histórico almacén de ladrillo rojo en el bullicioso puerto.",
            "nl": "De iconische concertzaal van Hamburg, met een prachtige golfachtige glasstructuur die sierlijk uittorent boven een historisch pakhuis van rode baksteen in de bruisende haven."
        },
        "tip": {
            "en": "Access to the 37m-high Plaza viewing deck requires a ticket. Ride 'The Tube', an 82m curved escalator, for a breathtaking panoramic spatial experience.",
            "ja": "高さ37mのプラザ展望デッキへのアクセスにはチケットが必要です。長さ82mの湾曲したエスカレーター「The Tube」に乗って、息をのむようなパノラマ空間体験を！",
            "zh": "进入 37 米高的广场观景台需要门票。乘坐 82 米长的弧形自动扶梯“The Tube”，体验令人叹为观止的全景空间体验。",
            "fr": "L'accès à la plateforme d'observation Plaza, à 37 m de haut, nécessite un billet. Empruntez « The Tube », un escalier mécanique incurvé de 82 m, pour une expérience spatiale panoramique à couper le souffle.",
            "de": "Der Zugang zur 37 m hohen Plaza-Aussichtsplattform erfordert ein Ticket. Fahren Sie mit der 82 m langen gebogenen Rolltreppe 'The Tube' für ein atemberaubendes räumliches Panoramaerlebnis.",
            "es": "El acceso a la plataforma de observación Plaza de 37 m de altura requiere un billete. Sube a 'The Tube', una escalera mecánica curva de 82 m, para vivir una experiencia espacial panorámica impresionante.",
            "nl": "Toegang tot het 37 meter hoge Plaza-uitkijkdek vereist een kaartje. Rijd met 'The Tube', een 82 meter lange gebogen roltrap, voor een adembenemende ruimtelijke panorama-ervaring."
        },
        "whyThisSpot": {
            "en": "An architectural masterpiece that perfectly symbolizes Hamburg's rich maritime heritage and modern artistic spirit, offering the absolute best views in the entire city.",
            "ja": "ハンブルクの豊かな海洋遺産と現代の芸術的精神を完璧に象徴する建築の傑作であり、街全体で最高の景色を提供します。",
            "zh": "这是一座建筑杰作，完美地象征着汉堡丰富的海洋遗产和现代艺术精神，提供全城绝对最佳的景观。",
            "fr": "Un chef-d'œuvre architectural qui symbolise parfaitement le riche héritage maritime et l'esprit artistique moderne de Hambourg, offrant les vues absolument meilleures de toute la ville.",
            "de": "Ein architektonisches Meisterwerk, das Hamburgs reiches maritimes Erbe und seinen modernen künstlerischen Geist perfekt symbolisiert und die absolut besten Aussichten der ganzen Stadt bietet.",
            "es": "Una obra maestra arquitectónica que simboliza a la perfección el rico patrimonio marítimo y el espíritu artístico moderno de Hamburgo, ofreciendo las mejores vistas de toda la ciudad.",
            "nl": "Een architectonisch meesterwerk dat het rijke maritieme erfgoed en de moderne artistieke geest van Hamburg perfect symboliseert en het allerbeste uitzicht van de hele stad biedt."
        }
    },
    "ham_h_13": {
        "desc": {
            "en": "A premier museum of applied arts, design, and photography, renowned globally for its extensive Art Nouveau furniture and exquisite Asian craft collections.",
            "ja": "応用美術、デザイン、写真の主要な美術館であり、広範なアール・ヌーヴォーの家具と絶妙なアジアの工芸品コレクションで世界的に有名です。",
            "zh": "首屈一指的应用艺术、设计和摄影博物馆，以其丰富的新艺术风格家具和精美的亚洲工艺品收藏而闻名全球。",
            "fr": "Un musée de premier plan des arts appliqués, du design et de la photographie, mondialement réputé pour son vaste mobilier Art nouveau et ses exquises collections d'artisanat asiatique.",
            "de": "Ein führendes Museum für angewandte Kunst, Design und Fotografie, das weltweit für seine umfangreichen Jugendstilmöbel und exquisiten asiatischen Kunsthandwerkssammlungen bekannt ist.",
            "es": "Un museo de primer nivel de artes aplicadas, diseño y fotografía, reconocido a nivel mundial por sus extensos muebles Art Nouveau y sus exquisitas colecciones de artesanía asiática.",
            "nl": "Een vooraanstaand museum voor toegepaste kunst, design en fotografie, wereldwijd beroemd om zijn uitgebreide art-nouveaumeubels en prachtige Aziatische ambachtscollecties."
        },
        "tip": {
            "en": "Don't miss the Parisian Tearoom exhibit, featuring fully original Art Nouveau furniture from the 1900 Paris Exposition—a true visual and historical delight.",
            "ja": "1900年のパリ万国博覧会で展示された完全なオリジナルのアール・ヌーヴォー家具を特徴とするパリジャン・ティールームの展示はお見逃しなく。真の視覚的、歴史的喜びです。",
            "zh": "不要错过巴黎茶室展览，其特色是 1900 年巴黎世博会上完全原创的新艺术风格家具——真正的视觉和历史享受。",
            "fr": "Ne manquez pas l'exposition du Salon de thé parisien, qui présente des meubles Art nouveau entièrement originaux de l'Exposition universelle de Paris de 1900, un véritable délice visuel et historique.",
            "de": "Verpassen Sie nicht die Ausstellung des Pariser Teesalons, die vollständig originale Jugendstilmöbel der Pariser Weltausstellung von 1900 zeigt – ein wahrer visueller und historischer Genuss.",
            "es": "No te pierdas la exposición del Salón de Té Parisino, que presenta muebles Art Nouveau completamente originales de la Exposición de París de 1900: una verdadera delicia visual e histórica.",
            "nl": "Mis de tentoonstelling van de Parijse tearoom niet, met volledig originele art-nouveaumeubels van de wereldtentoonstelling in Parijs van 1900 - een waar visueel en historisch genot."
        },
        "whyThisSpot": {
            "en": "An absolute must-visit for design lovers, offering a world-class, inspirational journey through visual culture, fashion, and meticulous historical craftsmanship.",
            "ja": "デザイン愛好家にとって絶対に訪れるべき場所であり、視覚文化、ファッション、細部までこだわった歴史的な職人技を巡る、世界クラスの刺激的な旅を提供します。",
            "zh": "设计爱好者的绝对必游之地，提供一次世界级的、鼓舞人心的视觉文化、时尚和细致的历史工艺之旅。",
            "fr": "Un incontournable absolu pour les amateurs de design, offrant un voyage inspirant de classe mondiale à travers la culture visuelle, la mode et le savoir-faire historique méticuleux.",
            "de": "Ein absolutes Muss für Designliebhaber, das eine inspirierende Reise von Weltklasse durch visuelle Kultur, Mode und akribische historische Handwerkskunst bietet.",
            "es": "Una visita obligada absoluta para los amantes del diseño, que ofrece un viaje inspirador de clase mundial a través de la cultura visual, la moda y la meticulosa artesanía histórica.",
            "nl": "Een absolute must voor designliefhebbers en biedt een inspirerende reis van wereldklasse door visuele cultuur, mode en nauwgezet historisch vakmanschap."
        }
    },
    "ham_h_14": {
        "desc": {
            "en": "One of Europe's largest and most prestigious contemporary art and photography centers, strikingly set within beautifully converted 19th-century market halls.",
            "ja": "ヨーロッパ最大かつ最も権威のある現代美術と写真のセンターの1つ。美しく改装された19世紀の市場ホール内に印象的に設置されています。",
            "zh": "欧洲最大、最负盛名的当代艺术和摄影中心之一，引人注目地坐落于经过精美改造的 19 世纪市场大厅内。",
            "fr": "L'un des centres d'art contemporain et de photographie les plus vastes et les plus prestigieux d'Europe, remarquablement installé dans des halles de marché du XIXe siècle magnifiquement reconverties.",
            "de": "Eines der größten und renommiertesten Zentren für zeitgenössische Kunst und Fotografie in Europa, eindrucksvoll in wunderschön umgebauten Markthallen aus dem 19. Jahrhundert untergebracht.",
            "es": "Uno de los centros de arte contemporáneo y fotografía más grandes y prestigiosos de Europa, sorprendentemente ubicado dentro de hermosos mercados del siglo XIX reconvertidos.",
            "nl": "Een van Europa's grootste en meest prestigieuze centra voor hedendaagse kunst en fotografie, opvallend gevestigd in prachtig verbouwde 19e-eeuwse markthallen."
        },
        "tip": {
            "en": "Explore the House of Photography (Haus der Photographie) to admire world-class, large-scale photographic exhibitions displayed in a breathtaking industrial space.",
            "ja": "写真の家（Haus der Photographie）を探索し、息をのむような工業空間に展示された世界クラスの大規模な写真展を鑑賞してください。",
            "zh": "探索摄影之家（Haus der Photographie），在令人叹为观止的工业空间中欣赏世界级的大型摄影展览。",
            "fr": "Explorez la Maison de la Photographie (Haus der Photographie) pour admirer des expositions photographiques à grande échelle de classe mondiale présentées dans un espace industriel à couper le souffle.",
            "de": "Erkunden Sie das Haus der Photographie, um erstklassige, großformatige Fotoausstellungen in einem atemberaubenden Industrieraum zu bewundern.",
            "es": "Explora la Casa de la Fotografía (Haus der Photographie) para admirar exposiciones fotográficas a gran escala de primer nivel en un espacio industrial impresionante.",
            "nl": "Verken het Huis van de Fotografie (Haus der Photographie) om grootschalige fototentoonstellingen van wereldklasse te bewonderen die in een adembenemende industriële ruimte worden tentoongesteld."
        },
        "whyThisSpot": {
            "en": "A spectacular fusion of raw historical industrial architecture and cutting-edge contemporary art, providing a visually overwhelming and deeply moving experience.",
            "ja": "生の歴史的工業建築と最先端の現代美術の壮大な融合であり、視覚的に圧倒的で深く感動的な体験を提供します。",
            "zh": "原始历史工业建筑与前沿当代艺术的壮观融合，提供视觉上压倒性且感人至深的体验。",
            "fr": "Une fusion spectaculaire d'architecture industrielle historique brute et d'art contemporain de pointe, offrant une expérience visuellement bouleversante et profondément émouvante.",
            "de": "Eine spektakuläre Verschmelzung von roher historischer Industriearchitektur und hochmoderner zeitgenössischer Kunst, die ein visuell überwältigendes und tief bewegendes Erlebnis bietet.",
            "es": "Una fusión espectacular de arquitectura industrial histórica y en bruto y arte contemporáneo de vanguardia, que proporciona una experiencia visualmente abrumadora y profundamente conmovedora.",
            "nl": "Een spectaculaire fusie van ruwe historische industriële architectuur en vooruitstrevende hedendaagse kunst, die een visueel overweldigende en diep ontroerende ervaring biedt."
        }
    },
    "ham_h_33": {
        "desc": {
            "en": "A groundbreaking immersive social exhibition where visually impaired guides expertly lead visitors through a simulated world of complete and utter darkness.",
            "ja": "視覚障害のあるガイドが、完全な暗闇のシミュレートされた世界を通して訪問者を巧みに導く、画期的な没入型ソーシャル展示会。",
            "zh": "一个开创性的沉浸式社交展览，由视力受损的导游熟练地带领游客穿过一个完全黑暗的模拟世界。",
            "fr": "Une exposition sociale immersive révolutionnaire où des guides malvoyants mènent avec expertise les visiteurs à travers un monde simulé d'obscurité complète et totale.",
            "de": "Eine bahnbrechende immersive soziale Ausstellung, in der sehbehinderte Guides die Besucher fachkundig durch eine simulierte Welt völliger Dunkelheit führen.",
            "es": "Una innovadora exposición social inmersiva donde guías con discapacidad visual conducen de manera experta a los visitantes a través de un mundo simulado de oscuridad total y absoluta.",
            "nl": "Een baanbrekende meeslepende sociale tentoonstelling waar visueel gehandicapte gidsen bezoekers vakkundig leiden door een gesimuleerde wereld van complete en totale duisternis."
        },
        "tip": {
            "en": "Heighten your senses as you navigate a simulated park, boat ride, and city street in total darkness, relying entirely on touch, sound, and smell.",
            "ja": "シミュレートされた公園、ボート乗り、街の通りを真っ暗闇の中で移動し、触覚、聴覚、嗅覚に完全に頼ることで、感覚を研ぎ澄ませましょう。",
            "zh": "当您在完全黑暗中穿梭于模拟公园、乘船游览和城市街道时，完全依靠触觉、听觉和嗅觉来提升您的感官。",
            "fr": "Aiguisez vos sens en naviguant dans un parc simulé, une promenade en bateau et une rue de la ville dans l'obscurité totale, en vous fiant entièrement au toucher, à l'ouïe et à l'odorat.",
            "de": "Schärfen Sie Ihre Sinne, während Sie sich in völliger Dunkelheit durch einen simulierten Park, eine Bootsfahrt und eine Stadtstraße bewegen und sich dabei ganz auf Tastsinn, Gehör und Geruch verlassen.",
            "es": "Agudiza tus sentidos mientras navegas por un parque simulado, un paseo en barco y una calle de la ciudad en total oscuridad, confiando completamente en el tacto, el sonido y el olfato.",
            "nl": "Scherp je zintuigen terwijl je in volledige duisternis door een gesimuleerd park, een boottocht en een stadsstraat navigeert en daarbij volledig vertrouwt op tast, geluid en reuk."
        },
        "whyThisSpot": {
            "en": "A profound, perspective-altering experience that powerfully builds empathy and completely challenges your everyday perception of the world around you.",
            "ja": "共感を強力に育み、私たちの周りの世界に対する日常の認識に完全に疑問を投げかける、深く、視点を変える体験。",
            "zh": "这是一种深刻的、改变视角的体验，它有力地建立同理心，并完全挑战您对周围世界的日常认知。",
            "fr": "Une expérience profonde et bouleversante qui suscite puissamment l'empathie et remet complètement en question votre perception quotidienne du monde qui vous entoure.",
            "de": "Eine tiefgreifende, perspektivverändernde Erfahrung, die auf kraftvolle Weise Empathie aufbaut und Ihre alltägliche Wahrnehmung der Welt um Sie herum völlig in Frage stellt.",
            "es": "Una experiencia profunda que altera la perspectiva, desarrolla poderosamente la empatía y desafía por completo tu percepción diaria del mundo que te rodea.",
            "nl": "Een diepgaande, perspectiefveranderende ervaring die op krachtige wijze empathie opbouwt en uw dagelijkse perceptie van de wereld om u heen volledig uitdaagt."
        }
    },
    "ham_h_34": {
        "desc": {
            "en": "A highly interactive chocolate museum where visitors joyfully trace the fascinating journey from raw cocoa bean to finished chocolate bar, engaging all their senses.",
            "ja": "生のコカオ豆から完成した板チョコまでの魅力的な旅を、五感すべてを使って楽しくたどることができる非常にインタラクティブなチョコレート博物館。",
            "zh": "一个高度互动的巧克力博物馆，游客可以在这里愉快地追溯从生可可豆到成品巧克力的迷人旅程，调动所有的感官。",
            "fr": "Un musée du chocolat hautement interactif où les visiteurs retracent avec joie le fascinant voyage de la fève de cacao crue à la tablette de chocolat finie, en sollicitant tous leurs sens.",
            "de": "Ein hochgradig interaktives Schokoladenmuseum, in dem Besucher die faszinierende Reise von der rohen Kakaobohne bis zur fertigen Tafel Schokolade mit allen Sinnen freudig verfolgen.",
            "es": "Un museo del chocolate muy interactivo donde los visitantes trazan con alegría el fascinante viaje desde el grano de cacao crudo hasta la tableta de chocolate terminada, involucrando todos sus sentidos.",
            "nl": "Een zeer interactief chocolademuseum waar bezoekers met plezier de fascinerende reis volgen van rauwe cacaoboon tot afgewerkte chocoladereep, waarbij al hun zintuigen worden geprikkeld."
        },
        "tip": {
            "en": "The absolute highlight of the tour is creating your very own custom chocolate bar, choosing from a wide and delicious variety of nuts, fruits, and fun toppings.",
            "ja": "ツアーの絶対的なハイライトは、ナッツ、フルーツ、楽しいトッピングの幅広く美味しい種類から選んで、自分だけのオリジナル板チョコを作ることです。",
            "zh": "这次旅行的绝对亮点是制作您自己的定制巧克力，从各种美味的坚果、水果和有趣的配料中进行选择。",
            "fr": "Le clou absolu de la visite est la création de votre propre tablette de chocolat personnalisée, en choisissant parmi une grande et délicieuse variété de noix, de fruits et de garnitures amusantes.",
            "de": "Der absolute Höhepunkt der Tour ist die Kreation Ihrer eigenen, individuellen Tafel Schokolade, wobei Sie aus einer großen und köstlichen Auswahl an Nüssen, Früchten und lustigen Toppings wählen können.",
            "es": "Lo más destacado del recorrido es crear tu propia tableta de chocolate personalizada, eligiendo entre una amplia y deliciosa variedad de nueces, frutas y aderezos divertidos.",
            "nl": "Het absolute hoogtepunt van de tour is het maken van je eigen gepersonaliseerde chocoladereep, waarbij je kunt kiezen uit een grote en heerlijke variëteit aan noten, fruit en leuke toppings."
        },
        "whyThisSpot": {
            "en": "A deliciously fun, hands-on, and highly educational experience that is absolutely perfect for families, couples, and any true chocolate enthusiast.",
            "ja": "家族連れ、カップル、そして真のチョコレート愛好家にとって絶対に完璧な、美味しくて楽しく、実践的で非常に教育的な体験です。",
            "zh": "一种美味有趣、亲身实践且极具教育意义的体验，绝对适合家庭、情侣和任何真正的巧克力爱好者。",
            "fr": "Une expérience délicieusement amusante, pratique et hautement éducative, absolument parfaite pour les familles, les couples et tout véritable amateur de chocolat.",
            "de": "Ein köstlich unterhaltsames, praktisches und höchst lehrreiches Erlebnis, das absolut perfekt für Familien, Paare und jeden wahren Schokoladenliebhaber ist.",
            "es": "Una experiencia deliciosamente divertida, práctica y muy educativa que es absolutamente perfecta para familias, parejas y cualquier verdadero entusiasta del chocolate.",
            "nl": "Een heerlijk leuke, praktische en zeer leerzame ervaring die absoluut perfect is voor gezinnen, stellen en elke echte chocoladeliefhebber."
        }
    },
    "ham_h_46": {
        "desc": {
            "en": "A stunning 19th-century neoclassical country house set gracefully within a beautiful, expansive English-style landscape garden overlooking the Elbe River.",
            "ja": "エルベ川を見下ろす美しく広大な英国風の風景庭園内に優雅に佇む、見事な19世紀の新古典主義のカントリーハウス。",
            "zh": "一座令人惊叹的 19 世纪新古典主义乡村别墅，优雅地坐落在俯瞰易北河的美丽而广阔的英式景观花园内。",
            "fr": "Une superbe maison de campagne néoclassique du XIXe siècle gracieusement située dans un magnifique et vaste jardin paysager de style anglais surplombant l'Elbe.",
            "de": "Ein atemberaubendes klassizistisches Landhaus aus dem 19. Jahrhundert, das anmutig in einem wunderschönen, weitläufigen Landschaftsgarten im englischen Stil mit Blick auf die Elbe liegt.",
            "es": "Una impresionante casa de campo neoclásica del siglo XIX situada con gracia dentro de un hermoso y extenso jardín paisajístico de estilo inglés con vistas al río Elba.",
            "nl": "Een prachtig 19e-eeuws neoklassiek landhuis sierlijk gelegen in een prachtige, uitgestrekte landschapstuin in Engelse stijl met uitzicht op de rivier de Elbe."
        },
        "tip": {
            "en": "Stand on the white colonnaded terrace on the south side of Jenisch Haus for a magnificent, sweeping view of the Elbe River across the rolling green lawns.",
            "ja": "イェーニッシュ・ハウス南側の白い列柱のあるテラスに立つと、なだらかな緑の芝生越しにエルベ川の壮大なパノラマビューが楽しめます。",
            "zh": "站在杰尼施别墅南侧的白色柱廊露台上，越过起伏的绿色草坪，欣赏易北河壮丽的广阔全景。",
            "fr": "Tenez-vous sur la terrasse à colonnades blanches du côté sud de la Jenisch Haus pour une vue magnifique et panoramique sur l'Elbe à travers les pelouses verdoyantes et vallonnées.",
            "de": "Stellen Sie sich auf die weiße Säulenterrasse an der Südseite des Jenisch-Hauses für einen herrlichen, weiten Blick auf die Elbe über die sanft abfallenden grünen Rasenflächen.",
            "es": "Párate en la terraza con columnatas blancas en el lado sur de Jenisch Haus para disfrutar de una vista magnífica y amplia del río Elba a través de los ondulados jardines verdes.",
            "nl": "Ga op het witte zuilenterras aan de zuidkant van Jenisch Haus staan voor een prachtig, weids uitzicht op de rivier de Elbe over de glooiende groene gazons."
        },
        "whyThisSpot": {
            "en": "It offers a tranquil, picturesque escape from the bustling city center, flawlessly blending grand aristocratic architecture with serene, unspoiled natural beauty.",
            "ja": "賑やかな市内中心部から逃れ、壮大な貴族の建築と静かで手付かずの自然の美しさを完璧に融合させた、静かで絵のように美しい場所を提供します。",
            "zh": "它提供了一个宁静、风景如画的逃离繁华市中心的好去处，完美融合了宏伟的贵族建筑与宁静、原始的自然美景。",
            "fr": "Il offre une évasion pittoresque et tranquille du centre-ville animé, mêlant parfaitement l'architecture aristocratique grandiose à une beauté naturelle sereine et préservée.",
            "de": "Es bietet einen ruhigen, malerischen Rückzugsort vom geschäftigen Stadtzentrum und verbindet makellos großartige aristokratische Architektur mit ruhiger, unberührter natürlicher Schönheit.",
            "es": "Ofrece una escapada tranquila y pintoresca del bullicioso centro de la ciudad, combinando a la perfección la gran arquitectura aristocrática con una belleza natural serena y virgen.",
            "nl": "Het biedt een rustige, pittoreske ontsnapping uit het bruisende stadscentrum, waarbij grootse aristocratische architectuur naadloos wordt gecombineerd met serene, ongerepte natuurlijke schoonheid."
        }
    },
    "ham_h_49": {
        "desc": {
            "en": "A magnificent, historic spa and wave pool complex originally built in 1914, featuring exquisite, restored Art Deco architecture and extensive sauna facilities.",
            "ja": "1914年に建てられた壮大で歴史的なスパと波のプールの複合施設。精巧に復元されたアールデコ建築と充実したサウナ施設が特徴です。",
            "zh": "一座宏伟的历史悠久的水疗和波浪池综合体，最初建于 1914 年，拥有精美且经过修复的装饰艺术建筑和广泛的桑拿设施。",
            "fr": "Un magnifique complexe historique de spa et de piscine à vagues construit à l'origine en 1914, doté d'une architecture Art Déco exquise et restaurée ainsi que de vastes installations de sauna.",
            "de": "Ein prächtiger, historischer Spa- und Wellenbadkomplex, der ursprünglich 1914 erbaut wurde und sich durch exquisite, restaurierte Art-déco-Architektur und umfangreiche Saunaanlagen auszeichnet.",
            "es": "Un magnífico e histórico complejo de spa y piscina de olas construido originalmente en 1914, que cuenta con una exquisita y restaurada arquitectura Art Deco y amplias instalaciones de sauna.",
            "nl": "Een prachtig, historisch spa- en golfslagbadcomplex oorspronkelijk gebouwd in 1914, met voortreffelijke, gerestaureerde art-deco-architectuur en uitgebreide saunafaciliteiten."
        },
        "tip": {
            "en": "Swim in the classic wave pool, beautifully illuminated by natural light streaming through the stunning Art Deco glass ceiling, for a truly elegant wellness experience.",
            "ja": "素晴らしいアールデコ調のガラス天井から差し込む自然光に美しく照らされたクラシックな波のプールで泳ぎ、真にエレガントなウェルネス体験を。",
            "zh": "在经典的波浪池中畅游，令人惊叹的装饰艺术玻璃天花板透进来的自然光将其照得格外美丽，为您带来真正优雅的健康体验。",
            "fr": "Nagez dans la piscine à vagues classique, magnifiquement éclairée par la lumière naturelle filtrant à travers le superbe plafond en verre Art Déco, pour une expérience de bien-être vraiment élégante.",
            "de": "Schwimmen Sie im klassischen Wellenbad, das wunderbar durch das natürliche Licht erleuchtet wird, welches durch die atemberaubende Art-déco-Glasdecke strömt, für ein wirklich elegantes Wellness-Erlebnis.",
            "es": "Nada en la clásica piscina de olas, bellamente iluminada por la luz natural que entra por el impresionante techo de cristal Art Deco, para disfrutar de una experiencia de bienestar verdaderamente elegante.",
            "nl": "Zwem in het klassieke golfslagbad, prachtig verlicht door natuurlijk licht dat door het prachtige art-deco glazen plafond stroomt, voor een werkelijk elegante wellness-ervaring."
        },
        "whyThisSpot": {
            "en": "A luxurious and historically rich wellness oasis, perfect for relaxing in grand style and soaking aching muscles after a long, busy day of city sightseeing.",
            "ja": "豪華で歴史豊かなウェルネスのオアシスであり、長くて忙しい市内観光の後に、壮大なスタイルでリラックスし、痛む筋肉を癒すのに最適です。",
            "zh": "豪华且历史丰富的健康绿洲，非常适合在漫长、繁忙的城市观光后以盛大的风格放松身心并浸泡酸痛的肌肉。",
            "fr": "Une oasis de bien-être luxueuse et riche en histoire, parfaite pour se détendre en grand style et soulager les muscles endoloris après une longue journée de visites en ville.",
            "de": "Eine luxuriöse und historisch reiche Wellness-Oase, perfekt, um nach einem langen, geschäftigen Sightseeing-Tag im großen Stil zu entspannen und schmerzende Muskeln zu beruhigen.",
            "es": "Un oasis de bienestar lujoso y rico en historia, perfecto para relajarse a lo grande y aliviar los músculos adoloridos después de un largo y ajetreado día de turismo por la ciudad.",
            "nl": "Een luxueuze en historisch rijke wellness-oase, perfect om in grootse stijl te ontspannen en pijnlijke spieren te laten weken na een lange, drukke dag sightseeing in de stad."
        }
    },
    "hdb_hd_33": {
        "desc": {
            "en": "A brilliant interactive, hands-on science museum dedicated to optical illusions, perception experiments, light, and physics, perfectly designed for curious visitors of all ages.",
            "ja": "目の錯覚、知覚の実験、光、物理学に特化した素晴らしいインタラクティブで実践的な科学博物館。あらゆる年齢の好奇心旺盛な訪問者向けに完璧に設計されています。",
            "zh": "一个精彩的互动、动手科学博物馆，致力于光学错觉、感知实验、光和物理学，专为所有年龄段好奇的游客量身定制。",
            "fr": "Un brillant musée scientifique interactif et pratique dédié aux illusions d'optique, aux expériences de perception, à la lumière et à la physique, parfaitement conçu pour les visiteurs curieux de tous âges.",
            "de": "Ein brillantes interaktives Mitmach-Wissenschaftsmuseum, das sich optischen Täuschungen, Wahrnehmungsexperimenten, Licht und Physik widmet und perfekt für neugierige Besucher jeden Alters konzipiert ist.",
            "es": "Un brillante museo de ciencias interactivo y práctico dedicado a las ilusiones ópticas, experimentos de percepción, luz y física, perfectamente diseñado para visitantes curiosos de todas las edades.",
            "nl": "Een briljant interactief, praktisch wetenschapsmuseum gewijd aan optische illusies, perceptie-experimenten, licht en fysica, perfect ontworpen voor nieuwsgierige bezoekers van alle leeftijden."
        },
        "tip": {
            "en": "A fantastic rainy-day activity! Kids and adults alike will love the mind-bending Ames room illusion, the giant engaging puzzles, and interactive shadow experiments.",
            "ja": "雨の日の最高のアクティビティ！子供も大人も、心を揺さぶるエイムズの部屋の錯覚、巨大で魅力的なパズル、インタラクティブな影の実験を気に入るはずです。",
            "zh": "绝佳的雨天活动！儿童和成人都将喜欢令人费解的艾姆斯房间错觉、巨大的引人入胜的谜题以及互动的阴影实验。",
            "fr": "Une activité fantastique pour les jours de pluie ! Les enfants comme les adultes adoreront l'illusion époustouflante de la chambre d'Ames, les puzzles géants captivants et les expériences interactives sur les ombres.",
            "de": "Eine fantastische Aktivität für Regentage! Kinder und Erwachsene werden gleichermaßen die verblüffende Ames-Raum-Illusion, die riesigen fesselnden Puzzles und interaktiven Schattenexperimente lieben.",
            "es": "¡Una fantástica actividad para un día de lluvia! Tanto a los niños como a los adultos les encantará la alucinante ilusión de la habitación de Ames, los rompecabezas gigantes e interactivos experimentos de sombras.",
            "nl": "Een fantastische activiteit voor een regenachtige dag! Zowel kinderen als volwassenen zullen dol zijn op de verbijsterende Ames-kamerillusie, de gigantische boeiende puzzels en interactieve schaduwexperimenten."
        },
        "whyThisSpot": {
            "en": "It brilliantly combines deep educational value with pure entertainment, making complex scientific concepts highly accessible and incredibly fun for the entire family.",
            "ja": "深い教育的価値と純粋なエンターテイメントを見事に組み合わせ、複雑な科学的概念を家族全員が非常にアクセスしやすく、信じられないほど楽しいものにしています。",
            "zh": "它将深度的教育价值与纯粹的娱乐完美地结合在一起，使整个家庭都能轻松获得极其有趣的复杂科学概念。",
            "fr": "Il combine brillamment une profonde valeur éducative avec un pur divertissement, rendant les concepts scientifiques complexes très accessibles et incroyablement amusants pour toute la famille.",
            "de": "Es verbindet auf brillante Weise tiefen pädagogischen Wert mit purer Unterhaltung und macht komplexe wissenschaftliche Konzepte für die ganze Familie leicht zugänglich und unglaublich unterhaltsam.",
            "es": "Combina de manera brillante un profundo valor educativo con puro entretenimiento, haciendo que los conceptos científicos complejos sean muy accesibles e increíblemente divertidos para toda la familia.",
            "nl": "Het combineert op briljante wijze diepe educatieve waarde met puur entertainment, waardoor complexe wetenschappelijke concepten zeer toegankelijk en ongelooflijk leuk worden voor het hele gezin."
        }
    },
    "lyn_lyon_2": {
        "desc": {
            "en": "A majestic Gothic cathedral proudly standing in the heart of Vieux Lyon, renowned for its stunning medieval stained glass and a remarkably rare 14th-century astronomical clock.",
            "ja": "ヴュー・リヨンの中心部に誇らしげに立つ壮大なゴシック様式の大聖堂。見事な中世のステンドグラスと非常に珍しい14世紀の天文時計で有名です。",
            "zh": "一座雄伟的哥特式大教堂骄傲地矗立在里昂老城的中心，以其令人惊叹的中世纪彩色玻璃和非常罕见的 14 世纪天文钟而闻名。",
            "fr": "Une majestueuse cathédrale gothique fièrement dressée au cœur du Vieux Lyon, réputée pour ses superbes vitraux médiévaux et son horloge astronomique remarquablement rare du XIVe siècle.",
            "de": "Eine majestätische gotische Kathedrale, die stolz im Herzen der Altstadt von Lyon steht, bekannt für ihre atemberaubenden mittelalterlichen Buntglasfenster und eine bemerkenswert seltene astronomische Uhr aus dem 14. Jahrhundert.",
            "es": "Una majestuosa catedral gótica que se erige orgullosa en el corazón del Vieux Lyon, famosa por sus impresionantes vidrieras medievales y un reloj astronómico notablemente raro del siglo XIV.",
            "nl": "Een majestueuze gotische kathedraal die trots in het hart van Vieux Lyon staat, beroemd om zijn prachtige middeleeuwse glas-in-loodramen en een opmerkelijk zeldzame 14e-eeuwse astronomische klok."
        },
        "tip": {
            "en": "Visit exactly at 12:00, 14:00, 15:00, or 16:00 to watch the historic astronomical clock chime and see its intricate, centuries-old mechanical figures spring to life.",
            "ja": "歴史的な天文時計の鐘の音と、何世紀も前の複雑な機械仕掛けの人形が動き出すのを見るには、正確に12:00、14:00、15:00、または16:00に訪れてください。",
            "zh": "务必在 12:00、14:00、15:00 或 16:00 准时参观，观看历史悠久的天文钟敲响，并欣赏其复杂的、拥有几个世纪历史的机械玩偶焕发生机。",
            "fr": "Visitez exactement à 12h00, 14h00, 15h00 ou 16h00 pour regarder sonner l'horloge astronomique historique et voir ses figures mécaniques complexes et séculaires s'animer.",
            "de": "Besuchen Sie uns genau um 12:00, 14:00, 15:00 oder 16:00 Uhr, um das Läuten der historischen astronomischen Uhr zu beobachten und zu sehen, wie ihre komplizierten, jahrhundertealten mechanischen Figuren zum Leben erwachen.",
            "es": "Visítala exactamente a las 12:00, 14:00, 15:00 o 16:00 para ver y escuchar el histórico reloj astronómico y ver cómo sus intrincadas figuras mecánicas centenarias cobran vida.",
            "nl": "Bezoek precies om 12:00, 14:00, 15:00 of 16:00 uur om de historische astronomische klok te horen luiden en te zien hoe de ingewikkelde, eeuwenoude mechanische figuren tot leven komen."
        },
        "whyThisSpot": {
            "en": "A breathtaking and awe-inspiring architectural marvel that perfectly captures the deep spiritual and profound historical essence of medieval Lyon.",
            "ja": "中世リヨンの深い精神的、そして深遠な歴史的本質を完璧に捉えた、息をのむほど荘厳な建築の驚異です。",
            "zh": "一座令人惊叹且令人敬畏的建筑奇迹，完美地捕捉了中世纪里昂深刻的精神和深厚的历史精髓。",
            "fr": "Une merveille architecturale à couper le souffle et impressionnante qui capture parfaitement l'essence spirituelle profonde et historique profonde du Lyon médiéval.",
            "de": "Ein atemberaubendes und ehrfurchtgebietendes architektonisches Wunderwerk, das die tiefe spirituelle und tiefgreifende historische Essenz des mittelalterlichen Lyon perfekt einfängt.",
            "es": "Una maravilla arquitectónica impresionante e imponente que captura a la perfección la profunda esencia espiritual e histórica de la Lyon medieval.",
            "nl": "Een adembenemend en ontzagwekkend architectonisch wonder dat perfect de diepe spirituele en diepgaande historische essentie van het middeleeuwse Lyon vastlegt."
        }
    },
    "lyn_lyon_4": {
        "desc": {
            "en": "One of Europe's absolute largest and most impressive pedestrian squares, famously dominated by a grand, imposing equestrian statue of King Louis XIV at its very center.",
            "ja": "ヨーロッパ最大かつ最も印象的な歩行者広場の1つであり、その中心にはルイ14世の雄大で堂々とした騎馬像があることで有名です。",
            "zh": "欧洲绝对最大、最令人印象深刻的步行广场之一，其正中心矗立着宏伟、气势磅礴的路易十四国王骑马雕像，因此而闻名。",
            "fr": "L'une des places piétonnes les plus vastes et les plus impressionnantes d'Europe, célèbre pour sa grande et imposante statue équestre du roi Louis XIV en son centre.",
            "de": "Einer der absolut größten und beeindruckendsten Fußgängerplätze Europas, der berühmt für eine große, imposante Reiterstatue von König Ludwig XIV. in seiner Mitte ist.",
            "es": "Una de las plazas peatonales más grandes e impresionantes de Europa, famosa por estar dominada por una gran e imponente estatua ecuestre del rey Luis XIV en su mismo centro.",
            "nl": "Een van Europa's absoluut grootste en meest indrukwekkende voetgangerspleinen, beroemd om zijn grote, imposante ruiterstandbeeld van koning Lodewijk XIV in het hart."
        },
        "tip": {
            "en": "Enjoy the vast, sunlit open space and fantastic clear views of the iconic Fourvière Hill. It's the absolute perfect starting point for exploring the city's main shopping districts.",
            "ja": "広大で太陽の光が降り注ぐオープンスペースと、象徴的なフルヴィエールの丘の素晴らしい遮るもののない景色をお楽しみください。街の主要なショッピング地区を探索するための絶対に完璧な出発点です。",
            "zh": "享受广阔、阳光充足的开阔空间以及标志性的富维耶山美妙的清晰景色。这是探索该市主要购物区的绝对完美起点。",
            "fr": "Profitez du vaste espace ouvert baigné de soleil et de la vue imprenable fantastique sur l'emblématique colline de Fourvière. C'est le point de départ absolument parfait pour explorer les principaux quartiers commerçants de la ville.",
            "de": "Genießen Sie den weiten, sonnendurchfluteten Freiraum und die fantastische freie Aussicht auf den berühmten Fourvière-Hügel. Es ist der absolut perfekte Ausgangspunkt, um die wichtigsten Einkaufsviertel der Stadt zu erkunden.",
            "es": "Disfruta del vasto espacio abierto bañado por el sol y de las fantásticas vistas despejadas de la icónica colina de Fourvière. Es el punto de partida absolutamente perfecto para explorar los principales distritos comerciales de la ciudad.",
            "nl": "Geniet van de uitgestrekte, zonovergoten open ruimte en het fantastische onbelemmerde uitzicht op de iconische heuvel van Fourvière. Het is het absoluut perfecte startpunt voor het verkennen van de belangrijkste winkelstraten van de stad."
        },
        "whyThisSpot": {
            "en": "It serves as the true beating heart of Lyon, offering an incredible sense of scale, great photo opportunities, and easy, central access to the city's absolute best attractions.",
            "ja": "リヨンの真の鼓動の中心として機能し、信じられないほどのスケール感、素晴らしい写真撮影の機会、そして街の絶対的な最高のアトラクションへの簡単で中心的なアクセスを提供します。",
            "zh": "它作为里昂真正跳动的心脏，提供令人难以置信的规模感、绝佳的拍照机会，并能轻松从中心位置前往该市绝对最佳的景点。",
            "fr": "Elle sert de véritable cœur battant de Lyon, offrant une incroyable sensation de grandeur, de superbes opportunités de photos et un accès central facile aux meilleures attractions absolues de la ville.",
            "de": "Es dient als das wahre schlagende Herz von Lyon und bietet ein unglaubliches Gefühl für die Größe, tolle Fotomotive und einen einfachen, zentralen Zugang zu den absolut besten Attraktionen der Stadt.",
            "es": "Sirve como el verdadero corazón palpitante de Lyon, ofreciendo una increíble sensación de escala, excelentes oportunidades para tomar fotos y un acceso fácil y central a las mejores atracciones de la ciudad.",
            "nl": "Het fungeert als het ware kloppende hart van Lyon, biedt een ongelooflijk gevoel voor schaal, geweldige fotomomenten en gemakkelijke, centrale toegang tot de absoluut beste attracties van de stad."
        }
    },
    "lyn_lyon_6": {
        "desc": {
            "en": "A magnificent 12th-century former hospital, flawlessly and painstakingly restored into a luxurious heritage landmark featuring grand courtyards, fine dining, and chic boutique shops.",
            "ja": "壮大な12世紀の旧病院。壮大な中庭、高級レストラン、シックなブティックショップを備えた豪華な遺産のランドマークに、完璧かつ細心の注意を払って復元されました。",
            "zh": "一座宏伟的 12 世纪前医院，经过完美、精心的修复，成为一座拥有宏大庭院、高级餐饮和别致精品店的豪华遗产地标。",
            "fr": "Un magnifique ancien hôpital du XIIe siècle, parfaitement et minutieusement restauré pour devenir un luxueux monument patrimonial comprenant de grandes cours, des restaurants gastronomiques et des boutiques chics.",
            "de": "Ein prächtiges ehemaliges Krankenhaus aus dem 12. Jahrhundert, das makellos und sorgfältig zu einem luxuriösen historischen Wahrzeichen mit großen Innenhöfen, gehobener Gastronomie und schicken Boutiquen restauriert wurde.",
            "es": "Un magnífico antiguo hospital del siglo XII, impecable y minuciosamente restaurado para convertirlo en un lujoso hito patrimonial que cuenta con grandes patios, excelentes restaurantes y elegantes boutiques.",
            "nl": "Een prachtig 12e-eeuws voormalig ziekenhuis, feilloos en zorgvuldig gerestaureerd tot een luxueus erfgoedmonument met grote binnenplaatsen, verfijnde restaurants en chique boetieks."
        },
        "tip": {
            "en": "Stroll through the deeply elegant inner cloisters and treat yourself to a signature cocktail at 'Le Dôme' bar, breathtakingly situated beneath a spectacular, towering dome.",
            "ja": "非常にエレガントな内側の回廊を散策し、見事でそびえ立つドームの下という息をのむような場所にあるバー「Le Dôme」で、特製カクテルをご堪能ください。",
            "zh": "漫步于极其优雅的内部回廊，在位于壮观、高耸的圆顶下方、令人叹为观止的“Le Dôme”酒吧犒劳自己一杯招牌鸡尾酒。",
            "fr": "Promenez-vous dans les cloîtres intérieurs profondément élégants et offrez-vous un cocktail signature au bar 'Le Dôme', situé de manière époustouflante sous un dôme spectaculaire et imposant.",
            "de": "Schlendern Sie durch die zutiefst eleganten inneren Kreuzgänge und gönnen Sie sich einen Signature-Cocktail in der Bar 'Le Dôme', die atemberaubend unter einer spektakulären, hoch aufragenden Kuppel liegt.",
            "es": "Pasea por los claustros interiores profundamente elegantes y date un capricho con un cóctel de autor en el bar 'Le Dôme', situado de manera impresionante bajo una cúpula espectacular e imponente.",
            "nl": "Wandel door de diep elegante binnenkloosters en trakteer uzelf op een kenmerkende cocktail in bar 'Le Dôme', adembenemend gelegen onder een spectaculaire, torenhoge koepel."
        },
        "whyThisSpot": {
            "en": "A stunning, world-class example of historical preservation seamlessly meeting modern luxury, creating an atmosphere of unparalleled, sophisticated elegance and charm.",
            "ja": "歴史的保存が現代のラグジュアリーとシームレスに出会うという、世界クラスの見事な例であり、比類のない洗練されたエレガンスと魅力の雰囲気を作り出しています。",
            "zh": "这是历史保护与现代奢华无缝结合的令人惊叹的世界级典范，营造出无与伦比、精致优雅和迷人的氛围。",
            "fr": "Un exemple époustouflant et de classe mondiale de préservation historique rencontrant harmonieusement le luxe moderne, créant une atmosphère d'une élégance et d'un charme sophistiqués et inégalés.",
            "de": "Ein atemberaubendes, weltklasse Beispiel für historische Erhaltung, die nahtlos mit modernem Luxus zusammentrifft und eine Atmosphäre von beispielloser, raffinierter Eleganz und Charme schafft.",
            "es": "Un ejemplo impresionante y de primer nivel de preservación histórica que se une a la perfección con el lujo moderno, creando una atmósfera de elegancia y encanto incomparables y sofisticados.",
            "nl": "Een verbluffend voorbeeld van wereldklasse van historisch behoud dat naadloos samengaat met moderne luxe, waardoor een sfeer van ongeëvenaarde, verfijnde elegantie en charme ontstaat."
        }
    },
    "lyn_lyon_7": {
        "desc": {
            "en": "A deeply historical Roman amphitheater built in 19 BC on the scenic slopes of Croix-Rousse, where delegates from 64 Gallic tribes once gathered in antiquity.",
            "ja": "クロワ・ルースの風光明媚な斜面に紀元前19年に建てられた、歴史の深い古代ローマの円形劇場。かつて64のガリア部族の代表が集まった場所です。",
            "zh": "一座具有深厚历史渊源的罗马圆形剧场，建于公元前 19 年，位于克鲁瓦鲁斯风景秀丽的斜坡上，古代 64 个高卢部落的代表曾齐聚于此。",
            "fr": "Un amphithéâtre romain profondément historique construit en 19 avant J.-C. sur les pentes pittoresques de la Croix-Rousse, où des délégués de 64 tribus gauloises se réunissaient autrefois dans l'Antiquité.",
            "de": "Ein zutiefst historisches römisches Amphitheater, das 19 v. Chr. an den malerischen Hängen von Croix-Rousse erbaut wurde und in dem sich in der Antike einst Delegierte von 64 gallischen Stämmen versammelten.",
            "es": "Un anfiteatro romano profundamente histórico construido en el 19 a. C. en las pintorescas laderas de Croix-Rousse, donde los delegados de 64 tribus galas se reunían en la antigüedad.",
            "nl": "Een zeer historisch Romeins amfitheater gebouwd in 19 v.Chr. op de schilderachtige hellingen van Croix-Rousse, waar afgevaardigden van 64 Gallische stammen zich in de oudheid ooit verzamelden."
        },
        "tip": {
            "en": "The fascinating ruins are freely visible from the street. It's a remarkably peaceful spot to pause and reflect before exploring the vibrant neighborhood just above.",
            "ja": "この魅力的な遺跡は通りから無料で見ることができます。すぐ上の活気ある地区を探索する前に、立ち止まって物思いにふけるのに非常に静かな場所です。",
            "zh": "令人着迷的遗址可以从街上免费看到。这是一个非常宁静的地点，在探索上方充满活力的街区之前，可以在此稍作停留和思考。",
            "fr": "Les ruines fascinantes sont librement visibles depuis la rue. C'est un endroit remarquablement paisible pour faire une pause et réfléchir avant d'explorer le quartier animé juste au-dessus.",
            "de": "Die faszinierenden Ruinen sind von der Straße aus frei sichtbar. Es ist ein bemerkenswert friedlicher Ort, um innezuhalten und nachzudenken, bevor man das lebendige Viertel direkt darüber erkundet.",
            "es": "Las fascinantes ruinas se pueden ver libremente desde la calle. Es un lugar notablemente tranquilo para detenerse y reflexionar antes de explorar el vibrante barrio que se encuentra justo arriba.",
            "nl": "De fascinerende ruïnes zijn gratis vanaf de straat te bezichtigen. Het is een opmerkelijk vredige plek om te pauzeren en na te denken voordat u de levendige wijk net erboven verkent."
        },
        "whyThisSpot": {
            "en": "An evocative, easily accessible piece of ancient Roman history that is seamlessly and beautifully woven right into the everyday fabric of the modern city.",
            "ja": "近代都市の日常の構造にシームレスかつ美しく織り込まれた、記憶を呼び起こす、簡単にアクセスできる古代ローマの歴史の一部。",
            "zh": "一段令人回味、易于接近的古罗马历史，它无缝且美丽地融入了现代城市的日常肌理中。",
            "fr": "Un morceau évocateur et facilement accessible de l'histoire romaine antique qui est parfaitement et magnifiquement tissé directement dans le tissu quotidien de la ville moderne.",
            "de": "Ein eindrucksvolles, leicht zugängliches Stück antiker römischer Geschichte, das nahtlos und wunderschön direkt in das alltägliche Gefüge der modernen Stadt eingewoben ist.",
            "es": "Un fragmento evocador y de fácil acceso de la antigua historia romana que está perfectamente y bellamente tejido en el tejido cotidiano de la ciudad moderna.",
            "nl": "Een suggestief, gemakkelijk toegankelijk stuk oude Romeinse geschiedenis dat naadloos en prachtig is verweven in het alledaagse weefsel van de moderne stad."
        }
    },
    "lyn_lyon_8": {
        "desc": {
            "en": "A striking Flamboyant Gothic church prominently situated on the Presqu'île peninsula, notable for its distinctive asymmetric spires and a deeply rich crypt history.",
            "ja": "プレスキル半島に目立って位置する印象的なフランボワイヤン・ゴシック様式の教会。特徴的な非対称の尖塔と非常に豊かな地下室の歴史で知られています。",
            "zh": "一座引人注目的华丽哥特式教堂，醒目地坐落在普雷斯吉勒半岛上，以其独特的不对称尖塔和极其丰富的地下室历史而闻名。",
            "fr": "Une impressionnante église gothique flamboyante située en bonne place sur la presqu'île, remarquable pour ses flèches asymétriques distinctives et une histoire de crypte profondément riche.",
            "de": "Eine markante Kirche im Flamboyant-Gotik-Stil, die prominent auf der Halbinsel Presqu'île liegt und für ihre unverwechselbaren asymmetrischen Türme und eine äußerst reiche Krypta-Geschichte bekannt ist.",
            "es": "Una llamativa iglesia de estilo gótico flamígero situada de manera prominente en la península de Presqu'île, notable por sus agujas asimétricas distintivas y una historia de cripta muy rica.",
            "nl": "Een opvallende Flamboyante gotische kerk, prominent gelegen op het schiereiland Presqu'île, opmerkelijk vanwege zijn opvallende asymmetrische torenspitsen en een zeer rijke cryptegeschiedenis."
        },
        "tip": {
            "en": "Admire the two delightfully contrasting Gothic steeples—one crafted of stone, one of brick—and soak in the glowing, luminous white interior near Place Jacobins.",
            "ja": "石造りとレンガ造りの2つの見事に対照的なゴシック様式の尖塔を鑑賞し、ジャコバン広場近くの輝くように明るい白い内部空間に浸ってください。",
            "zh": "欣赏两座令人愉悦的对比鲜明的哥特式尖塔——一座是石头的，一座是砖的——并沉浸在雅各宾广场附近发光、明亮的白色内部中。",
            "fr": "Admirez les deux clochers gothiques délicieusement contrastés — l'un en pierre, l'autre en brique — et imprégnez-vous de l'intérieur blanc et lumineux près de la place des Jacobins.",
            "de": "Bewundern Sie die beiden herrlich kontrastierenden gotischen Kirchtürme – einer aus Stein, der andere aus Backstein – und tauchen Sie ein in das leuchtend helle, weiße Innere in der Nähe des Place Jacobins.",
            "es": "Admira los dos campanarios góticos que contrastan maravillosamente, uno de piedra y otro de ladrillo, y sumérgete en el interior blanco y luminoso cerca de Place Jacobins.",
            "nl": "Bewonder de twee prachtig contrasterende gotische torenspitsen - een van steen, de ander van baksteen - en geniet van het gloeiende, lichtgevende witte interieur in de buurt van Place Jacobins."
        },
        "whyThisSpot": {
            "en": "A visual and architectural gem that offers quiet spiritual contemplation alongside fascinating, eclectic structural details in the very center of town.",
            "ja": "街のまさに中心部で、魅力的で折衷的な構造の細部とともに、静かな精神的熟考を提供する視覚的および建築的な宝石です。",
            "zh": "一颗视觉和建筑上的宝石，在市中心提供安静的精神冥想以及迷人、折衷的结构细节。",
            "fr": "Un joyau visuel et architectural qui offre une contemplation spirituelle silencieuse aux côtés de détails structurels fascinants et éclectiques en plein centre-ville.",
            "de": "Ein visuelles und architektonisches Juwel, das neben faszinierenden, vielseitigen strukturellen Details mitten im Zentrum der Stadt stille spirituelle Kontemplation bietet.",
            "es": "Una joya visual y arquitectónica que ofrece una contemplación espiritual tranquila junto con detalles estructurales fascinantes y eclécticos en el mismo centro de la ciudad.",
            "nl": "Een visueel en architectonisch juweeltje dat rustige spirituele contemplatie biedt naast fascinerende, eclectische structurele details in het hart van de stad."
        }
    },
    "lyn_lyon_9": {
        "desc": {
            "en": "Europe's absolute largest trompe-l'œil mural, an astonishing piece spanning 1,200 m² in Lyon's historic and vibrant Croix-Rousse district.",
            "ja": "ヨーロッパで絶対的に最大のだまし絵の壁画。リヨンの歴史的で活気あるクロワ・ルース地区にまたがる1,200㎡の驚異的な作品です。",
            "zh": "欧洲绝对最大的错视画壁画，这是位于里昂历史悠久且充满活力的克鲁瓦鲁斯区的一幅占地 1,200 平方米的惊人作品。",
            "fr": "La plus grande fresque murale en trompe-l'œil absolue d'Europe, une œuvre étonnante s'étendant sur 1 200 m² dans le quartier historique et animé de la Croix-Rousse à Lyon.",
            "de": "Europas absolut größtes Trompe-l'œil-Wandgemälde, ein erstaunliches Werk, das sich über 1.200 m² im historischen und lebendigen Viertel Croix-Rousse in Lyon erstreckt.",
            "es": "El mural en trompe-l'œil más grande de Europa, una obra asombrosa que abarca 1.200 m² en el histórico y vibrante barrio de Croix-Rousse de Lyon.",
            "nl": "Europa's absoluut grootste trompe-l'œil-muurschildering, een verbazingwekkend kunstwerk dat 1.200 m² beslaat in de historische en levendige wijk Croix-Rousse in Lyon."
        },
        "tip": {
            "en": "The mural is cleverly updated every decade to reflect neighborhood changes. Step close to inspect the mind-bending 3D optical illusion stairs and painted figures!",
            "ja": "壁画は地区の変化を反映して10年ごとに巧みに更新されます。近づいて、心を揺さぶる3Dの目の錯覚の階段と描かれた人物を観察してください！",
            "zh": "壁画巧妙地每十年更新一次，以反映社区的变化。走近仔细观察令人费解的 3D 光学错觉楼梯和彩绘人物！",
            "fr": "La fresque est intelligemment mise à jour chaque décennie pour refléter les changements du quartier. Approchez-vous pour inspecter les marches d'illusion d'optique 3D ahurissantes et les personnages peints !",
            "de": "Das Wandgemälde wird clever alle zehn Jahre aktualisiert, um die Veränderungen in der Nachbarschaft widerzuspiegeln. Treten Sie näher heran, um die verblüffenden 3D-Treppen mit optischer Täuschung und die gemalten Figuren zu inspizieren!",
            "es": "El mural se actualiza hábilmente cada década para reflejar los cambios del vecindario. ¡Acércate para inspeccionar las alucinantes escaleras de ilusión óptica en 3D y las figuras pintadas!",
            "nl": "De muurschildering wordt slim elk decennium bijgewerkt om buurtveranderingen weer te geven. Kom dichtbij om de verbijsterende 3D optische illusie trappen en geschilderde figuren te inspecteren!"
        },
        "whyThisSpot": {
            "en": "A wildly fun, incredibly photogenic masterpiece of urban street art that tells the ongoing, living story of the neighborhood's people and culture.",
            "ja": "近隣の人々と文化の継続的で生きた物語を語る、非常に楽しく、信じられないほど写真映えする都市ストリートアートの傑作。",
            "zh": "这是一幅极其有趣、极具照片吸引力的城市街头艺术杰作，讲述了该街区人们和文化不断发展、生动的故事。",
            "fr": "Un chef-d'œuvre follement amusant et incroyablement photogénique de l'art urbain de la rue qui raconte l'histoire vivante et continue des habitants et de la culture du quartier.",
            "de": "Ein unheimlich lustiges, unglaublich fotogenes Meisterwerk der städtischen Straßenkunst, das die fortlaufende, lebendige Geschichte der Menschen und der Kultur des Viertels erzählt.",
            "es": "Una obra maestra de arte urbano callejero tremendamente divertida e increíblemente fotogénica que cuenta la historia viva y continua de la gente y la cultura del barrio.",
            "nl": "Een waanzinnig leuk, ongelooflijk fotogeniek meesterwerk van stedelijke street art dat het voortdurende, levende verhaal vertelt van de mensen en de cultuur in de wijk."
        }
    },
    "lyn_lyon_10": {
        "desc": {
            "en": "A remarkably charming riverside castle that houses a world-class vintage automobile collection, including rare early models and historically significant cars.",
            "ja": "希少な初期モデルや歴史的に重要な車など、世界クラスのヴィンテージ自動車コレクションを所蔵する、驚くほど魅力的な川沿いの城。",
            "zh": "一座非常迷人的河畔城堡，收藏着世界级的老式汽车，包括稀有的早期型号和具有重大历史意义的汽车。",
            "fr": "Un château de bord de rivière remarquablement charmant qui abrite une collection d'automobiles anciennes de classe mondiale, comprenant des modèles anciens rares et des voitures d'une importance historique.",
            "de": "Ein bemerkenswert charmantes Schloss am Flussufer, das eine Weltklasse-Sammlung von Oldtimern beherbergt, darunter seltene frühe Modelle und historisch bedeutsame Autos.",
            "es": "Un castillo junto al río notablemente encantador que alberga una colección de automóviles antiguos de clase mundial, que incluye modelos antiguos raros y automóviles de importancia histórica.",
            "nl": "Een opmerkelijk charmant kasteel aan de rivier dat een vintage autocollectie van wereldklasse huisvest, inclusief zeldzame vroege modellen en historisch belangrijke auto's."
        },
        "tip": {
            "en": "Explore the extensive grounds and outbuildings. Automobile enthusiasts will be thoroughly amazed by the impeccably maintained, century-old engine designs.",
            "ja": "広大な敷地と離れを探索してください。自動車愛好家は、完璧にメンテナンスされた1世紀前のエンジン設計に完全に驚かれることでしょう。",
            "zh": "探索广阔的场地和附属建筑。汽车爱好者会对维护得无可挑剔的百年发动机设计感到彻底惊叹。",
            "fr": "Explorez le vaste domaine et les dépendances. Les passionnés d'automobile seront complètement émerveillés par les conceptions de moteurs centenaires impeccablement entretenus.",
            "de": "Erkunden Sie das weitläufige Gelände und die Nebengebäude. Autoliebhaber werden von den tadellos gewarteten, jahrhundertealten Motorenkonstruktionen völlig begeistert sein.",
            "es": "Explora los extensos terrenos y las dependencias. Los entusiastas del automóvil quedarán completamente asombrados con los diseños de motores centenarios impecablemente mantenidos.",
            "nl": "Verken het uitgestrekte terrein en de bijgebouwen. Autoliefhebbers zullen volkomen verbaasd zijn over de onberispelijk onderhouden, eeuwenoude motorontwerpen."
        },
        "whyThisSpot": {
            "en": "An entirely unique blend of French aristocratic castle architecture and a deep, passionate dive into the golden, pioneering age of the automobile.",
            "ja": "フランスの貴族の城の建築と、自動車の黄金の開拓時代への深く情熱的な探求という、全くユニークな融合です。",
            "zh": "法国贵族城堡建筑的完全独特融合，以及对汽车黄金先锋时代的深入、充满激情的探索。",
            "fr": "Un mélange tout à fait unique d'architecture de château aristocratique français et d'une plongée profonde et passionnée dans l'âge d'or et pionnier de l'automobile.",
            "de": "Eine völlig einzigartige Mischung aus französischer aristokratischer Schlossarchitektur und einem tiefen, leidenschaftlichen Eintauchen in das goldene, bahnbrechende Zeitalter des Automobils.",
            "es": "Una combinación completamente única de arquitectura de castillo aristocrático francés y una inmersión profunda y apasionada en la era pionera y dorada del automóvil.",
            "nl": "Een totaal unieke mix van Franse aristocratische kasteelarchitectuur en een diepe, gepassioneerde duik in het gouden, baanbrekende tijdperk van de auto."
        }
    },
    "lyn_lyon_12": {
        "desc": {
            "en": "A boldly futuristic glass and steel museum dramatically poised at the confluence of the Rhône and Saône rivers, exploring natural science and world civilizations.",
            "ja": "ローヌ川とソーヌ川の合流点にドラマチックに位置する、自然科学と世界文明を探求する大胆で未来的なガラスと鋼の博物館。",
            "zh": "一座大胆的未来派玻璃和钢铁博物馆，戏剧性地坐落在罗纳河和索恩河的交汇处，探索自然科学和世界文明。",
            "fr": "Un musée audacieusement futuriste en verre et en acier, situé de manière spectaculaire au confluent du Rhône et de la Saône, explorant les sciences naturelles et les civilisations du monde.",
            "de": "Ein kühnes, futuristisches Glas- und Stahlmuseum, das dramatisch am Zusammenfluss von Rhône und Saône liegt und Naturwissenschaften sowie Weltzivilisationen erforscht.",
            "es": "Un museo de vidrio y acero audazmente futurista, situado espectacularmente en la confluencia de los ríos Ródano y Saona, que explora las ciencias naturales y las civilizaciones del mundo.",
            "nl": "Een gedurfd futuristisch glas- en staalmuseum, dramatisch gelegen aan de samenvloeiing van de rivieren de Rhône en de Saône, dat de natuurwetenschappen en wereldculturen verkent."
        },
        "tip": {
            "en": "Take the time to visit the stunning rooftop bar; it offers unparalleled, sweeping views of where the two great rivers finally merge together.",
            "ja": "見事な屋上バーをぜひ訪れてください。2つの大河が最終的に合流する場所の、比類のない素晴らしいパノラマビューを提供しています。",
            "zh": "花点时间参观令人惊叹的屋顶酒吧；这里提供两条大河最终交汇处无与伦比的开阔全景。",
            "fr": "Prenez le temps de visiter le superbe bar sur le toit ; il offre une vue imprenable et panoramique sans précédent sur l'endroit où les deux grands fleuves se rejoignent enfin.",
            "de": "Nehmen Sie sich Zeit für einen Besuch der atemberaubenden Rooftop-Bar; sie bietet einen unvergleichlichen, weiten Blick darauf, wo die beiden großen Flüsse schließlich zusammenfließen.",
            "es": "Tómate el tiempo para visitar el impresionante bar de la azotea; ofrece unas vistas panorámicas incomparables del lugar donde finalmente se unen los dos grandes ríos.",
            "nl": "Neem de tijd om de prachtige bar op het dak te bezoeken; het biedt een ongeëvenaard, weids uitzicht op de plek waar de twee grote rivieren eindelijk samenkomen."
        },
        "whyThisSpot": {
            "en": "Its striking, cutting-edge architecture and incredibly thought-provoking exhibits make it an unforgettable, intellectual highlight of any trip to Lyon.",
            "ja": "その印象的で最先端の建築と信じられないほど示唆に富む展示は、リヨン旅行の忘れられない知的なハイライトになります。",
            "zh": "其引人注目的前沿建筑和令人难以置信的引人深思的展览，使其成为任何里昂之旅中令人难忘的智力亮点。",
            "fr": "Son architecture saisissante et avant-gardiste, ainsi que ses expositions incroyablement stimulantes, en font un point culminant intellectuel inoubliable de tout voyage à Lyon.",
            "de": "Seine markante, hochmoderne Architektur und die unglaublich zum Nachdenken anregenden Exponate machen es zu einem unvergesslichen, intellektuellen Höhepunkt jeder Reise nach Lyon.",
            "es": "Su arquitectura sorprendente y vanguardista, y sus exposiciones increíblemente estimulantes lo convierten en un punto culminante intelectual e inolvidable de cualquier viaje a Lyon.",
            "nl": "De opvallende, hypermoderne architectuur en ongelooflijk tot nadenken stemmende tentoonstellingen maken het tot een onvergetelijk, intellectueel hoogtepunt van elke reis naar Lyon."
        }
    },
    "lyn_lyon_15": {
        "desc": {
            "en": "A beautiful, sprawling Renaissance palace housing both Lyon's History Museum and a captivating World Puppetry Museum completely dedicated to Guignol.",
            "ja": "リヨンの歴史博物館と、ギニョールに完全に捧げられた魅力的な世界人形劇博物館の両方を収容する、美しく広大なルネッサンス様式の宮殿。",
            "zh": "一座美丽、广阔的文艺复兴时期宫殿，内有里昂历史博物馆和完全致力于吉尼奥尔的迷人的世界木偶博物馆。",
            "fr": "Un magnifique et vaste palais de la Renaissance abritant à la fois le musée d'histoire de Lyon et un captivant musée mondial de la marionnette entièrement dédié à Guignol.",
            "de": "Ein wunderschöner, weitläufiger Renaissancepalast, der sowohl das Geschichtsmuseum von Lyon als auch ein faszinierendes Weltmarionettenmuseum beherbergt, das vollständig Guignol gewidmet ist.",
            "es": "Un hermoso y extenso palacio renacentista que alberga el Museo de Historia de Lyon y un cautivador Museo Mundial de las Marionetas completamente dedicado a Guignol.",
            "nl": "Een prachtig, uitgestrekt renaissancepaleis met zowel het historisch museum van Lyon als een boeiend wereldpoppentheatermuseum dat volledig is gewijd aan Guignol."
        },
        "tip": {
            "en": "Immerse yourself in the rich puppet theatre history and discover the origins of Guignol, Lyon's iconic and fiercely satirical 1808 wooden puppet.",
            "ja": "豊かな人形劇の歴史に浸り、1808年に誕生したリヨンの象徴的で猛烈な風刺を込めた木偶『ギニョール』の起源を発見してください。",
            "zh": "沉浸在丰富的木偶剧历史中，探索吉尼奥尔（Guignol）的起源，这是 1808 年里昂标志性且极具讽刺意味的木偶。",
            "fr": "Plongez dans la riche histoire du théâtre de marionnettes et découvrez les origines de Guignol, la marionnette en bois emblématique et farouchement satirique de Lyon de 1808.",
            "de": "Tauchen Sie ein in die reiche Geschichte des Marionettentheaters und entdecken Sie die Ursprünge von Guignol, Lyons ikonischer und bissig satirischer Holzpuppe aus dem Jahr 1808.",
            "es": "Sumérgete en la rica historia del teatro de marionetas y descubre los orígenes de Guignol, la icónica y ferozmente satírica marioneta de madera de Lyon de 1808.",
            "nl": "Dompel jezelf onder in de rijke geschiedenis van het poppentheater en ontdek de oorsprong van Guignol, de iconische en fel satirische houten pop uit Lyon uit 1808."
        },
        "whyThisSpot": {
            "en": "It delightfully combines the architectural splendor of the Renaissance with a deep, uniquely engaging look into Lyon's vibrant cultural and theatrical soul.",
            "ja": "ルネッサンスの建築的壮麗さと、リヨンの活気に満ちた文化や演劇の魂への深く、ユニークに魅力的な考察を、見事に組み合わせています。",
            "zh": "它将文艺复兴时期的建筑辉煌与对里昂充满活力的文化和戏剧灵魂进行深入、独特且引人入胜的探索完美地结合在一起。",
            "fr": "Il combine délicieusement la splendeur architecturale de la Renaissance avec un regard profond et unique sur l'âme culturelle et théâtrale vibrante de Lyon.",
            "de": "Es verbindet auf wunderbare Weise die architektonische Pracht der Renaissance mit einem tiefen, einzigartig fesselnden Blick in die lebendige kulturelle und theatralische Seele Lyons.",
            "es": "Combina deliciosamente el esplendor arquitectónico del Renacimiento con una mirada profunda y singularmente atractiva a la vibrante alma cultural y teatral de Lyon.",
            "nl": "Het combineert de architectonische pracht van de Renaissance op verrukkelijke wijze met een diepe, uniek boeiende blik in de levendige culturele en theatrale ziel van Lyon."
        }
    }
}

for item in spots:
    spot = item["spot"]
    sid = spot["id"]
    if sid in updates:
        for field in ["desc", "tip", "whyThisSpot"]:
            for lang in ["en", "ja", "zh", "fr", "de", "es", "nl"]:
                key = f"{field}_{lang}"
                if field == "tip":
                    key = f"tip_{lang}"
                    if f"insiderTip_{lang}" in spot:
                        key = f"insiderTip_{lang}"
                spot[key] = updates[sid][field][lang]

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(spots, f, ensure_ascii=False, indent=2)
