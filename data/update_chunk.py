import json

data_file = "/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_chunk_5.json"
output_file = "/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_written_5.json"

with open(data_file, "r", encoding="utf-8") as f:
    spots = json.load(f)

# The new high-quality content generated for each spot in all 7 languages.
updates = {
    "mrs_ma_17": {
        "desc": {
            "en": "A premier contemporary art museum exhibiting major Pop Art, Nouveau Réalisme, and Arte Povera masterpieces from the 1960s onward.",
            "ja": "1960年代以降のポップアート、ヌーヴォー・レアリスム、アルテ・ポーヴェラの傑作を展示する世界有数の現代美術館。",
            "zh": "首屈一指的当代艺术博物馆，展出20世纪60年代以来的波普艺术、新现实主义和贫穷艺术杰作。",
            "fr": "Musée d'art contemporain de premier plan exposant des chefs-d'œuvre du Pop Art, du Nouveau Réalisme et de l'Arte Povera des années 1960 à nos jours.",
            "de": "Ein führendes Museum für zeitgenössische Kunst, das Meisterwerke der Pop Art, des Nouveau Réalisme und der Arte Povera ab den 1960er Jahren ausstellt.",
            "es": "Un destacado museo de arte contemporáneo que exhibe obras maestras del Pop Art, el Nuevo Realismo y el Arte Povera desde la década de 1960.",
            "nl": "Een vooraanstaand museum voor hedendaagse kunst dat meesterwerken van Pop Art, Nouveau Réalisme en Arte Povera vanaf de jaren 60 tentoonstelt."
        },
        "tip": {
            "en": "Reopened in 2023 with a spectacular new design. Don't miss the cutting-edge international sculptures and the iconic Warhol collection.",
            "ja": "2023年に壮大な新デザインでリニューアルオープン。最先端の国際的な彫刻と象徴的なウォーホル・コレクションは見逃せません。",
            "zh": "2023年以壮丽的新设计重新开放。千万不要错过前沿的国际雕塑和标志性的沃霍尔收藏。",
            "fr": "Rouvert en 2023 avec un nouveau design spectaculaire. Ne manquez pas les sculptures internationales avant-gardistes et la collection emblématique de Warhol.",
            "de": "2023 mit einem spektakulären neuen Design wiedereröffnet. Verpassen Sie nicht die hochmodernen internationalen Skulpturen und die ikonische Warhol-Sammlung.",
            "es": "Reabierto en 2023 con un espectacular nuevo diseño. No te pierdas las vanguardistas esculturas internacionales y la icónica colección de Warhol.",
            "nl": "In 2023 heropend met een spectaculair nieuw ontwerp. Mis de geavanceerde internationale sculpturen en de iconische Warhol-collectie niet."
        },
        "whyThisSpot": {
            "en": "It offers an unparalleled, immersive dive into modern artistic expression within a breathtaking, newly renovated architectural space.",
            "ja": "息を呑むような改装された建築空間で、現代アートの表現に深く浸れる比類のない体験を提供します。",
            "zh": "它在一个令人惊叹的全新翻修建筑空间内，提供无与伦比的、沉浸式的现代艺术体验。",
            "fr": "Il offre une plongée immersive et inégalée dans l'expression artistique moderne, au sein d'un espace architectural époustouflant récemment rénové.",
            "de": "Es bietet ein unvergleichliches, immersives Eintauchen in den modernen künstlerischen Ausdruck in einem atemberaubenden, neu renovierten architektonischen Raum.",
            "es": "Ofrece una inmersión inigualable en la expresión artística moderna dentro de un impresionante espacio arquitectónico recientemente renovado.",
            "nl": "Het biedt een ongeëvenaarde, meeslepende duik in moderne artistieke expressie in een adembenemende, onlangs gerenoveerde architectonische ruimte."
        }
    },
    "mrs_ma_18": {
        "desc": {
            "en": "A fascinating natural history museum housed inside the magnificent Palais Longchamp, featuring rich Provençal paleontology, minerals, and zoology.",
            "ja": "壮麗なロンシャン宮殿内にあり、プロヴァンス地方の豊かな古生物学、鉱物、動物学の標本を展示する魅力的な自然史博物館。",
            "zh": "这座迷人的自然历史博物馆位于宏伟的隆尚宫内，展出丰富的普罗旺斯古生物学、矿物学和动物学标本。",
            "fr": "Fascinant muséum d'histoire naturelle abrité dans le magnifique Palais Longchamp, présentant une riche paléontologie, minéralogie et zoologie provençales.",
            "de": "Ein faszinierendes Naturkundemuseum im prächtigen Palais Longchamp mit einer reichen Sammlung an Paläontologie, Mineralien und Zoologie der Provence.",
            "es": "Un fascinante museo de historia natural ubicado en el magnífico Palais Longchamp, que presenta una rica paleontología, mineralogía y zoología provenzal.",
            "nl": "Een fascinerend natuurhistorisch museum gevestigd in het prachtige Palais Longchamp, met een rijke Provençaalse paleontologie, mineralogie en zoölogie."
        },
        "tip": {
            "en": "Located in the left wing of Palais Longchamp. Make sure to see the 18th-century cabinet of curiosities and the impressive dinosaur fossils.",
            "ja": "ロンシャン宮殿の左翼に位置しています。18世紀の驚異の部屋（ヴンダーカンマー）や印象的な恐竜の化石は必見です。",
            "zh": "位于隆尚宫的左翼。千万不要错过18世纪的珍奇屋和令人印象深刻的恐龙化石。",
            "fr": "Situé dans l'aile gauche du Palais Longchamp. Ne manquez pas le cabinet de curiosités du XVIIIe siècle et les impressionnants fossiles de dinosaures.",
            "de": "Befindet sich im linken Flügel des Palais Longchamp. Verpassen Sie nicht das Kuriositätenkabinett aus dem 18. Jahrhundert und die beeindruckenden Dinosaurierfossilien.",
            "es": "Ubicado en el ala izquierda del Palais Longchamp. Asegúrate de ver el gabinete de curiosidades del siglo XVIII y los impresionantes fósiles de dinosaurios.",
            "nl": "Gelegen in de linkervleugel van Palais Longchamp. Zorg ervoor dat u het rariteitenkabinet uit de 18e eeuw en de indrukwekkende dinosaurusfossielen ziet."
        },
        "whyThisSpot": {
            "en": "It perfectly combines architectural grandeur with scientific wonders, making it a captivating educational experience for all ages.",
            "ja": "建築の壮大さと科学の驚異を完璧に融合させており、あらゆる年齢層にとって魅力的な教育体験となります。",
            "zh": "它将建筑的宏伟与科学的奇迹完美结合，为所有年龄段的游客带来引人入胜的教育体验。",
            "fr": "Il allie parfaitement la grandeur architecturale aux merveilles scientifiques, offrant une expérience éducative captivante pour tous les âges.",
            "de": "Es verbindet auf perfekte Weise architektonische Pracht mit wissenschaftlichen Wundern und macht es zu einem fesselnden Bildungserlebnis für alle Altersgruppen.",
            "es": "Combina a la perfección la grandeza arquitectónica con las maravillas científicas, convirtiéndolo en una experiencia educativa cautivadora para todas las edades.",
            "nl": "Het combineert perfect architectonische grandeur met wetenschappelijke wonderen, waardoor het een boeiende educatieve ervaring is voor alle leeftijden."
        }
    },
    "mrs_ma_19": {
        "desc": {
            "en": "A vast, alternative creative arts complex inside a former tobacco factory, featuring contemporary galleries, a skatepark, and a rooftop bar.",
            "ja": "元タバコ工場を利用した広大なオルタナティブ・アート複合施設。現代アートギャラリー、スケートパーク、ルーフトップバーを備えています。",
            "zh": "一家由前烟草工厂改造而成的庞大另类创意艺术综合体，设有当代画廊、滑板公园和屋顶酒吧。",
            "fr": "Un vaste complexe artistique alternatif installé dans une ancienne usine de tabac, comprenant des galeries contemporaines, un skatepark et un bar sur le toit.",
            "de": "Ein riesiger, alternativer Kreativkomplex in einer ehemaligen Tabakfabrik mit zeitgenössischen Galerien, einem Skatepark und einer Bar auf dem Dach.",
            "es": "Un vasto complejo alternativo de artes creativas dentro de una antigua fábrica de tabaco, que cuenta con galerías contemporáneas, un parque de patinaje y un bar en la azotea.",
            "nl": "Een enorm, alternatief creatief kunstcomplex in een voormalige tabaksfabriek, met hedendaagse galerijen, een skatepark en een bar op het dak."
        },
        "tip": {
            "en": "Head to the immense rooftop terrace in the evening for sunset DJ sets, panoramic city views, and a buzzing local atmosphere.",
            "ja": "夕方には広大な屋上テラスへ。サンセットDJイベント、街のパノラマビュー、そして活気ある地元の雰囲気を楽しめます。",
            "zh": "傍晚前往巨大的屋顶露台，享受日落DJ表演、城市全景和充满活力的当地氛围。",
            "fr": "Rendez-vous sur l'immense toit-terrasse en soirée pour des sets de DJ au coucher du soleil, des vues panoramiques sur la ville et une atmosphère locale animée.",
            "de": "Besuchen Sie abends die riesige Dachterrasse für DJ-Sets bei Sonnenuntergang, einen Panoramablick auf die Stadt und eine lebhafte lokale Atmosphäre.",
            "es": "Sube a la inmensa terraza en la azotea al atardecer para disfrutar de sesiones de DJ, vistas panorámicas de la ciudad y un ambiente local vibrante.",
            "nl": "Ga 's avonds naar het immense dakterras voor DJ-sets bij zonsondergang, een panoramisch uitzicht over de stad en een bruisende lokale sfeer."
        },
        "whyThisSpot": {
            "en": "It is the beating heart of Marseille's urban culture, showcasing the city's raw, creative, and dynamic modern spirit.",
            "ja": "マルセイユの都市文化の鼓動の中心であり、街のありのままの創造的でダイナミックな現代の精神を示しています。",
            "zh": "这里是马赛城市文化的跳动之心，展现了这座城市原始、富有创意且充满活力的现代精神。",
            "fr": "C'est le cœur battant de la culture urbaine marseillaise, mettant en valeur l'esprit moderne, brut, créatif et dynamique de la ville.",
            "de": "Es ist das schlagende Herz der urbanen Kultur Marseilles und zeigt den rauen, kreativen und dynamischen modernen Geist der Stadt.",
            "es": "Es el corazón palpitante de la cultura urbana de Marsella, mostrando el espíritu moderno crudo, creativo y dinámico de la ciudad.",
            "nl": "Het is het kloppende hart van de stedelijke cultuur van Marseille en toont de rauwe, creatieve en dynamische moderne geest van de stad."
        }
    },
    "mrs_ma_20": {
        "desc": {
            "en": "An exquisite ceramics museum in Château Borély, displaying 17th to 18th-century Marseille tin-glazed faience pottery and haute couture.",
            "ja": "ボレリー宮殿内にある精巧な陶磁器博物館。17世紀から18世紀のマルセイユ特産の錫釉陶器（ファイアンス）とオートクチュールを展示しています。",
            "zh": "博雷利城堡内一座精美的陶瓷博物馆，展示了 17 至 18 世纪马赛的锡釉彩陶和高级时装。",
            "fr": "Un musée de la céramique exquis au Château Borély, exposant des faïences stannifères marseillaises des XVIIe et XVIIIe siècles et de la haute couture.",
            "de": "Ein exquisites Keramikmuseum im Château Borély, das zinnglasierte Fayence-Töpferei und Haute Couture aus Marseille aus dem 17. und 18. Jahrhundert zeigt.",
            "es": "Un exquisito museo de cerámica en el Château Borély, que exhibe cerámica de loza esmaltada con estaño de Marsella de los siglos XVII y XVIII y alta costura.",
            "nl": "Een prachtig keramiekmuseum in Château Borély, met tin-geglazuurde faience-aardewerk en haute couture uit Marseille uit de 17e tot 18e eeuw."
        },
        "tip": {
            "en": "Combine your visit with a stroll through the surrounding Parc Borély and admire the stunning Neoclassical interior architecture.",
            "ja": "見学の後は、周囲のボレリー公園の散策と、見事な新古典主義の室内装飾の鑑賞を組み合わせるのがおすすめです。",
            "zh": "建议将您的参观与在周围的博雷利公园漫步结合起来，并欣赏令人惊叹的新古典主义室内建筑。",
            "fr": "Combinez votre visite avec une promenade dans le parc Borély environnant et admirez la magnifique architecture intérieure néoclassique.",
            "de": "Kombinieren Sie Ihren Besuch mit einem Spaziergang durch den umliegenden Parc Borély und bewundern Sie die atemberaubende neoklassizistische Innenarchitektur.",
            "es": "Combina tu visita con un paseo por el parque Borély que lo rodea y admira la impresionante arquitectura interior neoclásica.",
            "nl": "Combineer uw bezoek met een wandeling door het omliggende Parc Borély en bewonder de prachtige neoklassieke interieurarchitectuur."
        },
        "whyThisSpot": {
            "en": "It elegantly preserves the refined artisanal heritage and luxurious aristocratic lifestyle of historic Provence.",
            "ja": "歴史的なプロヴァンスの洗練された職人技の遺産と、豪華な貴族のライフスタイルを優雅に保存しています。",
            "zh": "它优雅地保存了历史悠久的普罗旺斯地区精致的手工遗产和奢华的贵族生活方式。",
            "fr": "Il préserve avec élégance le patrimoine artisanal raffiné et le luxueux style de vie aristocratique de la Provence historique.",
            "de": "Es bewahrt auf elegante Weise das raffinierte handwerkliche Erbe und den luxuriösen aristokratischen Lebensstil der historischen Provence.",
            "es": "Conserva con elegancia el refinado patrimonio artesanal y el lujoso estilo de vida aristocrático de la histórica Provenza.",
            "nl": "Het behoudt op elegante wijze het verfijnde ambachtelijke erfgoed en de luxueuze aristocratische levensstijl van de historische Provence."
        }
    },
    "mrs_ma_21": {
        "desc": {
            "en": "An iconic coastal restaurant in Vallon des Auffes enforcing the authentic Bouillabaisse Charter, serving legendary fish stew by the water.",
            "ja": "ヴァロン・デ・ゾフにある象徴的な海辺のレストラン。本物の『ブイヤベース憲章』を守り、水辺で伝説的な魚のシチューを提供しています。",
            "zh": "瓦隆德奥菲斯一家标志性的沿海餐厅，严格执行正宗的马赛鱼汤宪章，在水边供应传奇的炖鱼。",
            "fr": "Restaurant côtier emblématique du Vallon des Auffes appliquant l'authentique Charte de la Bouillabaisse, servant un légendaire ragoût de poisson au bord de l'eau.",
            "de": "Ein legendäres Küstenrestaurant im Vallon des Auffes, das die authentische Bouillabaisse-Charta anwendet und legendären Fischeintopf direkt am Wasser serviert.",
            "es": "Un icónico restaurante costero en Vallon des Auffes que aplica la auténtica Carta de la Bullabesa, sirviendo un legendario guiso de pescado junto al agua.",
            "nl": "Een iconisch kustrestaurant in Vallon des Auffes dat het authentieke Bouillabaisse-handvest handhaaft en legendarische visstoofpot aan het water serveert."
        },
        "tip": {
            "en": "Reserve well in advance for a table by the window. You must order their multi-fish Bouillabaisse, served traditionally in two courses with rouille.",
            "ja": "窓際の席は早めの予約が必須です。伝統的な2コースで提供され、ルイユソースが添えられた数種類の魚のブイヤベースは絶対に注文してください。",
            "zh": "请务必提前预订靠窗的座位。您必须品尝他们用多种鱼熬制的马赛鱼汤，传统上分为两道菜，配以大蒜辣椒酱。",
            "fr": "Réservez bien à l'avance pour une table près de la fenêtre. Vous devez commander leur Bouillabaisse aux multiples poissons, servie traditionnellement en deux services avec de la rouille.",
            "de": "Reservieren Sie rechtzeitig für einen Tisch am Fenster. Bestellen Sie unbedingt die Bouillabaisse aus verschiedenen Fischen, die traditionell in zwei Gängen mit Rouille serviert wird.",
            "es": "Reserva con mucha antelación para conseguir una mesa junto a la ventana. Debes pedir su Bullabesa de varios pescados, servida tradicionalmente en dos platos con rouille.",
            "nl": "Reserveer ruim van tevoren voor een tafel bij het raam. U moet hun Bouillabaisse van meerdere vissen bestellen, traditioneel geserveerd in twee gangen met rouille."
        },
        "whyThisSpot": {
            "en": "It delivers the quintessential Marseille culinary experience in a breathtakingly picturesque, movie-like fishing port setting.",
            "ja": "絵画のように美しい映画のような漁港の景色の中で、マルセイユの真髄とも言える料理体験を提供します。",
            "zh": "它在如诗如画、宛如电影场景般的渔港环境中，提供最正宗的马赛烹饪体验。",
            "fr": "Il offre la quintessence de l'expérience culinaire marseillaise dans un port de pêche au cadre pittoresque et digne d'un film.",
            "de": "Es bietet das ultimative kulinarische Erlebnis Marseilles in einer atemberaubend malerischen, filmreifen Fischerhafenkulisse.",
            "es": "Ofrece la quintaesencia de la experiencia culinaria de Marsella en el entorno de un puerto pesquero de película, impresionantemente pintoresco.",
            "nl": "Het levert de ultieme culinaire ervaring van Marseille in een adembenemend pittoreske, filmachtige vissershavenomgeving."
        }
    },
    "mrs_ma_22": {
        "desc": {
            "en": "A historic and elegant Old Port restaurant globally renowned for its meticulously authentic bouillabaisse and fresh Mediterranean seafood platters.",
            "ja": "旧港にある歴史的でエレガントなレストラン。細部まで本格的なブイヤベースと新鮮な地中海シーフードの盛り合わせで世界的に有名です。",
            "zh": "一家历史悠久且优雅的老港口餐厅，以其精心制作的正宗马赛鱼汤和新鲜的地中海海鲜拼盘享誉全球。",
            "fr": "Un restaurant historique et élégant du Vieux-Port, mondialement réputé pour sa bouillabaisse méticuleusement authentique et ses plateaux de fruits de mer méditerranéens frais.",
            "de": "Ein historisches und elegantes Restaurant am Alten Hafen, das weltweit für seine akribisch authentische Bouillabaisse und frische mediterrane Meeresfrüchteplatten bekannt ist.",
            "es": "Un restaurante histórico y elegante en el Puerto Viejo, mundialmente famoso por su bullabesa meticulosamente auténtica y platos de mariscos frescos del Mediterráneo.",
            "nl": "Een historisch en elegant restaurant in de Oude Haven, wereldwijd bekend om zijn zorgvuldig authentieke bouillabaisse en verse mediterrane visplateaus."
        },
        "tip": {
            "en": "As a founding member of the 1980 Bouillabaisse Charter, the soup here is rich and theatrical. Pair it with a crisp local white wine.",
            "ja": "1980年のブイヤベース憲章の創設メンバーとして、ここのスープは濃厚でドラマチックです。キリッとした地元の白ワインと合わせてお楽しみください。",
            "zh": "作为1980年马赛鱼汤宪章的创始成员，这里的汤底浓郁且极具仪式感。建议搭配清脆的当地白葡萄酒享用。",
            "fr": "En tant que membre fondateur de la Charte de la Bouillabaisse de 1980, la soupe y est riche et théâtrale. Accompagnez-la d'un vin blanc local sec.",
            "de": "Als Gründungsmitglied der Bouillabaisse-Charta von 1980 ist die Suppe hier reichhaltig und theatralisch. Kombinieren Sie sie mit einem frischen lokalen Weißwein.",
            "es": "Como miembro fundador de la Carta de la Bullabesa de 1980, la sopa aquí es rica y teatral. Acompáñala con un vino blanco local crujiente.",
            "nl": "Als stichtend lid van het Bouillabaisse-handvest van 1980 is de soep hier rijk en theatraal. Combineer het met een frisse lokale witte wijn."
        },
        "whyThisSpot": {
            "en": "It is an institution of French gastronomy, offering a luxurious deep-dive into the rich seafood traditions of southern France.",
            "ja": "フランス美食の殿堂であり、南フランスの豊かなシーフードの伝統を贅沢に深く味わうことができます。",
            "zh": "它是法国美食的殿堂，让您奢华地深入体验法国南部丰富的海鲜传统。",
            "fr": "C'est une institution de la gastronomie française, offrant une plongée luxueuse dans les riches traditions de fruits de mer du sud de la France.",
            "de": "Es ist eine Institution der französischen Gastronomie und bietet ein luxuriöses Eintauchen in die reichen Meeresfrüchte-Traditionen Südfrankreichs.",
            "es": "Es una institución de la gastronomía francesa, que ofrece una inmersión lujosa en las ricas tradiciones de mariscos del sur de Francia.",
            "nl": "Het is een instituut van de Franse gastronomie en biedt een luxueuze duik in de rijke zeevruchtentradities van Zuid-Frankrijk."
        }
    },
    "mrs_ma_23": {
        "desc": {
            "en": "A vibrant, traditional morning fish market along the Old Port where local fishermen sell their freshest daily catch straight from their wooden boats.",
            "ja": "旧港沿いで毎朝開かれる活気に満ちた伝統的な魚市場。地元の漁師が木造船から直接、その日獲れた最も新鮮な魚介類を販売しています。",
            "zh": "老港沿岸一个充满活力的传统早间鱼市，当地渔民在这里直接从木船上出售每天最新鲜的渔获。",
            "fr": "Un marché aux poissons matinal, vibrant et traditionnel le long du Vieux-Port, où les pêcheurs locaux vendent leurs prises du jour les plus fraîches directement depuis leurs bateaux en bois.",
            "de": "Ein lebhafter, traditioneller morgendlicher Fischmarkt am Alten Hafen, wo lokale Fischer ihren frischesten Tagesfang direkt von ihren Holzbooten aus verkaufen.",
            "es": "Un mercado de pescado matutino, vibrante y tradicional, a lo largo del Puerto Viejo, donde los pescadores locales venden su pesca más fresca del día directamente desde sus barcos de madera.",
            "nl": "Een levendige, traditionele ochtendvismarkt langs de Oude Haven waar lokale vissers hun meest verse dagvangst rechtstreeks vanaf hun houten boten verkopen."
        },
        "tip": {
            "en": "Arrive between 8:00 and 9:30 AM to catch the lively banter and see the strange, colorful rockfish destined for the city's bouillabaisse.",
            "ja": "朝8時から9時半の間に到着すると、活気あるやり取りや、街のブイヤベースに使われる色鮮やかで珍しい岩礁魚を見ることができます。",
            "zh": "请在早上8:00至9:30之间到达，体验热闹的讨价还价，并观赏注定要用来熬制马赛鱼汤的各种色彩斑斓的奇怪石鱼。",
            "fr": "Arrivez entre 8h00 et 9h30 pour assister aux échanges animés et voir les poissons de roche étranges et colorés destinés à la bouillabaisse de la ville.",
            "de": "Kommen Sie zwischen 8:00 und 9:30 Uhr an, um die lebhaften Gespräche zu erleben und die seltsamen, bunten Felsenfische zu sehen, die für die Bouillabaisse der Stadt bestimmt sind.",
            "es": "Llega entre las 8:00 y las 9:30 a.m. para captar el animado parloteo y ver los extraños y coloridos peces de roca destinados a la bullabesa de la ciudad.",
            "nl": "Kom tussen 8.00 en 9.30 uur aan om het levendige gebabbel te horen en de vreemde, kleurrijke rotsvissen te zien die bestemd zijn voor de bouillabaisse van de stad."
        },
        "whyThisSpot": {
            "en": "It provides a vivid, unfiltered glimpse into the authentic daily life and centuries-old maritime soul of Marseille.",
            "ja": "マルセイユの飾らない本物の日常生活と、何世紀にもわたる海洋の魂を鮮明に垣間見ることができます。",
            "zh": "它生动地展示了马赛原汁原味的日常景象，让您一瞥这座城市几个世纪以来的海洋之魂。",
            "fr": "Il offre un aperçu vivant et authentique de la vie quotidienne et de l'âme maritime séculaire de Marseille.",
            "de": "Es bietet einen lebendigen, ungefilterten Einblick in das authentische Alltagsleben und die jahrhundertealte maritime Seele Marseilles.",
            "es": "Ofrece una visión vívida y sin filtros de la auténtica vida cotidiana y el alma marítima centenaria de Marsella.",
            "nl": "Het biedt een levendige, ongefilterde blik in het authentieke dagelijkse leven en de eeuwenoude maritieme ziel van Marseille."
        }
    },
    "mrs_ma_24": {
        "desc": {
            "en": "A bustling, multi-ethnic street market deeply scented with North African spices, fresh mint, exotic herbs, and Middle Eastern pastries.",
            "ja": "北アフリカのスパイス、新鮮なミント、エキゾチックなハーブ、中東のペストリーの香りが深く漂う、活気に満ちた多民族のストリートマーケット。",
            "zh": "一个熙熙攘攘的多民族街头市场，空气中弥漫着北非香料、新鲜薄荷、异国香草和中东糕点的浓郁香气。",
            "fr": "Un marché de rue animé et multiethnique, profondément parfumé d'épices nord-africaines, de menthe fraîche, d'herbes exotiques et de pâtisseries du Moyen-Orient.",
            "de": "Ein geschäftiger, multiethnischer Straßenmarkt mit dem intensiven Duft von nordafrikanischen Gewürzen, frischer Minze, exotischen Kräutern und nahöstlichem Gebäck.",
            "es": "Un bullicioso mercado callejero multiétnico profundamente perfumado con especias norteafricanas, menta fresca, hierbas exóticas y pasteles de Oriente Medio.",
            "nl": "Een bruisende, multi-etnische straatmarkt die diep geurt naar Noord-Afrikaanse kruiden, verse munt, exotische kruiden en gebak uit het Midden-Oosten."
        },
        "tip": {
            "en": "Visit 'Saladin Épices du Monde' for Harissa and spices, then grab a hot mint tea and a slice of honey-soaked Baklava from a nearby vendor.",
            "ja": "「Saladin Épices du Monde」でハリッサやスパイスを購入した後は、近くの屋台で温かいミントティーと蜂蜜たっぷりのバクラヴァを楽しんでください。",
            "zh": "前往“Saladin Épices du Monde”购买大蒜辣椒酱和香料，然后在附近的摊位买一杯热薄荷茶和一块浸满蜂蜜的果仁蜜饼。",
            "fr": "Visitez 'Saladin Épices du Monde' pour la harissa et les épices, puis prenez un thé à la menthe chaud et une part de baklava imbibé de miel chez un vendeur à proximité.",
            "de": "Besuchen Sie 'Saladin Épices du Monde' für Harissa und Gewürze, holen Sie sich dann einen heißen Minztee und ein Stück in Honig getränktes Baklava von einem nahegelegenen Stand.",
            "es": "Visita 'Saladin Épices du Monde' para comprar Harissa y especias, luego toma un té de menta caliente y un trozo de Baklava bañado en miel de un vendedor cercano.",
            "nl": "Bezoek 'Saladin Épices du Monde' voor Harissa en kruiden, pak dan een hete muntthee en een stuk in honing gedrenkte Baklava van een nabijgelegen verkoper."
        },
        "whyThisSpot": {
            "en": "It is a sensory explosion that beautifully highlights Marseille's rich history as a diverse, welcoming Mediterranean crossroads.",
            "ja": "多様で歓迎的な地中海の交差点としてのマルセイユの豊かな歴史を美しく浮き彫りにする、感覚の爆発です。",
            "zh": "这是一场感官的爆发，完美地展现了马赛作为多元、包容的地中海十字路口的丰富历史。",
            "fr": "C'est une explosion sensorielle qui met magnifiquement en lumière la riche histoire de Marseille en tant que carrefour méditerranéen diversifié et accueillant.",
            "de": "Es ist eine sensorische Explosion, die Marseilles reiche Geschichte als vielfältiger, einladender mediterraner Knotenpunkt auf wunderbare Weise unterstreicht.",
            "es": "Es una explosión sensorial que destaca maravillosamente la rica historia de Marsella como un crisol mediterráneo diverso y acogedor.",
            "nl": "Het is een zintuiglijke explosie die de rijke geschiedenis van Marseille als een divers, gastvrij mediterraan kruispunt prachtig benadrukt."
        }
    },
    "mrs_ma_29": {
        "desc": {
            "en": "Marseille's oldest and most atmospheric neighborhood, characterized by steep cobblestone alleys, vibrant street murals, and artisan workshops.",
            "ja": "急勾配の石畳の路地、鮮やかな壁画、職人の工房が特徴的な、マルセイユで最も古く、最も雰囲気のある地区。",
            "zh": "马赛最古老、最具氛围的街区，以陡峭的鹅卵石小巷、充满活力的街头壁画和工匠作坊为特色。",
            "fr": "Le quartier le plus ancien et le plus atmosphérique de Marseille, caractérisé par ses ruelles pavées escarpées, ses peintures murales vibrantes et ses ateliers d'artisans.",
            "de": "Marseilles ältestes und stimmungsvollstes Viertel, das sich durch steile Kopfsteinpflastergassen, lebhafte Straßenmalereien und Kunsthandwerksbetriebe auszeichnet.",
            "es": "El barrio más antiguo y con más encanto de Marsella, caracterizado por sus empinadas callejuelas empedradas, sus vibrantes murales callejeros y sus talleres artesanales.",
            "nl": "De oudste en meest sfeervolle wijk van Marseille, gekenmerkt door steile geplaveide steegjes, levendige straatmuurschilderingen en ambachtelijke werkplaatsen."
        },
        "tip": {
            "en": "Get wonderfully lost in the maze of streets. Look out for the 'Navettes' biscuits bakery and relax at a sunny terrace in Place des Pistoles.",
            "ja": "迷路のような通りでわざと迷子になってみましょう。伝統的なビスケット「ナヴェット」のパン屋を探し、ピストル広場の日当たりの良いテラスでくつろいでください。",
            "zh": "在这座迷宫般的街道中尽情迷失吧。留意出售传统“Navettes”饼干的烘焙店，并在手枪广场阳光明媚的露台上放松身心。",
            "fr": "Perdez-vous joyeusement dans le labyrinthe des rues. Cherchez la boulangerie de 'Navettes' et détendez-vous sur une terrasse ensoleillée de la Place des Pistoles.",
            "de": "Verlieren Sie sich wunderbar im Labyrinth der Straßen. Halten Sie Ausschau nach der Bäckerei für 'Navettes'-Kekse und entspannen Sie sich auf einer sonnigen Terrasse am Place des Pistoles.",
            "es": "Piérdete maravillosamente en el laberinto de calles. Busca la panadería de galletas 'Navettes' y relájate en una soleada terraza en la Place des Pistoles.",
            "nl": "Verdwaal heerlijk in de wirwar van straatjes. Kijk uit naar de bakkerij van 'Navettes'-koekjes en ontspan op een zonnig terras op de Place des Pistoles."
        },
        "whyThisSpot": {
            "en": "It blends profound history with a modern bohemian vibe, acting as a living, breathing open-air museum of Mediterranean culture.",
            "ja": "深い歴史と現代のボヘミアンな雰囲気が融合し、地中海文化の生きた野外博物館として機能しています。",
            "zh": "它将深厚的历史与现代波西米亚氛围融合在一起，宛如一座生机勃勃的地中海文化露天博物馆。",
            "fr": "Il allie une histoire profonde à une ambiance bohème moderne, agissant comme un musée à ciel ouvert vivant et respirant de la culture méditerranéenne.",
            "de": "Es verbindet tiefe Geschichte mit einem modernen unkonventionellen Vibe und fungiert als lebendiges Freilichtmuseum der mediterranen Kultur.",
            "es": "Combina una profunda historia con un ambiente bohemio moderno, actuando como un museo al aire libre vivo y palpitante de la cultura mediterránea.",
            "nl": "Het combineert een diepgaande geschiedenis met een moderne bohemien vibe, en fungeert als een levend, ademend openluchtmuseum van de mediterrane cultuur."
        }
    },
    "mrs_ma_30": {
        "desc": {
            "en": "A deeply picturesque fishing cove tucked snugly beneath a grand stone bridge arch, filled with brightly colored, traditional wooden 'pointu' boats.",
            "ja": "壮大な石橋のアーチの下にすっぽりと隠れた、非常に絵になる小さな漁港。鮮やかな色に塗られた伝統的な木造船「ポワンチュ」が浮かんでいます。",
            "zh": "一个极具画面感的捕鱼海湾，舒适地隐藏在一座宏伟的石桥拱门下，停满了色彩鲜艳的传统木制“尖角船”。",
            "fr": "Une crique de pêche profondément pittoresque, nichée sous l'arche d'un grand pont en pierre, remplie de bateaux traditionnels en bois colorés appelés 'pointus'.",
            "de": "Eine zutiefst malerische Fischerbucht, die sich gemütlich unter einem großen steinernen Brückenbogen versteckt und mit bunten, traditionellen hölzernen 'Pointu'-Booten gefüllt ist.",
            "es": "Una cala de pescadores profundamente pintoresca escondida bajo el arco de un gran puente de piedra, llena de barcos tradicionales de madera 'pointu' de colores brillantes.",
            "nl": "Een uiterst pittoreske vissersbaai, knus verborgen onder een grote stenen brugboog, vol met felgekleurde, traditionele houten 'pointu'-boten."
        },
        "tip": {
            "en": "Come during the late afternoon to walk down the steep stairs, take golden-hour photos, and grab an aperitif by the gentle waves.",
            "ja": "午後遅くに訪れ、急な階段を下りて夕暮れ時の黄金色の写真を撮り、穏やかな波のそばで食前酒を楽しんでください。",
            "zh": "建议在傍晚时分顺着陡峭的楼梯走下来，拍摄黄金时刻的照片，并在轻柔的海浪声中享用开胃酒。",
            "fr": "Venez en fin d'après-midi pour descendre les escaliers raides, prendre des photos à l'heure dorée et prendre un apéritif au bord des douces vagues.",
            "de": "Kommen Sie am späten Nachmittag, um die steile Treppe hinunterzugehen, Fotos zur goldenen Stunde zu machen und einen Aperitif an den sanften Wellen zu nehmen.",
            "es": "Ven a última hora de la tarde para bajar las empinadas escaleras, tomar fotos en la hora dorada y tomar un aperitivo junto a las suaves olas.",
            "nl": "Kom in de late namiddag om de steile trappen af te dalen, foto's te maken tijdens het gouden uur en een aperitief te drinken bij de zachte golven."
        },
        "whyThisSpot": {
            "en": "It feels like a secret, timeless Mediterranean postcard hidden away from the bustling urban center.",
            "ja": "賑やかな都心から離れて隠された、秘密の時代を超越した地中海の絵葉書のように感じられます。",
            "zh": "它感觉就像一张秘密的、超越时间的地中海明信片，远离了喧嚣的市中心。",
            "fr": "On a l'impression d'être dans une carte postale méditerranéenne secrète et intemporelle, cachée de l'agitation du centre urbain.",
            "de": "Es fühlt sich an wie eine geheime, zeitlose mediterrane Postkarte, die abseits des geschäftigen Stadtzentrums versteckt ist.",
            "es": "Se siente como una postal mediterránea secreta y atemporal escondida del bullicioso centro urbano.",
            "nl": "Het voelt als een geheime, tijdloze mediterrane ansichtkaart, verborgen voor het bruisende stedelijke centrum."
        }
    },
    "mrs_ma_32": {
        "desc": {
            "en": "A thoroughly bohemian artistic quarter blanketed in vivid street art graffiti, featuring vintage thrift stores, indie music venues, and lively cafe terraces.",
            "ja": "鮮やかなストリートアートのグラフィティに覆われた徹底的なボヘミアン芸術地区。ヴィンテージの古着屋、インディーズのライブハウス、活気あるカフェのテラスがあります。",
            "zh": "一个完全波西米亚风格的艺术区，墙上布满了生动的街头涂鸦，拥有复古旧货店、独立音乐场所和热闹的咖啡馆露台。",
            "fr": "Un quartier artistique profondément bohème, recouvert de graffitis de street art éclatants, comprenant des friperies vintage, des salles de musique indépendante et des terrasses de café animées.",
            "de": "Ein durch und durch unkonventionelles Künstlerviertel, das mit lebhaften Street-Art-Graffitis übersät ist und Vintage-Secondhand-Läden, Indie-Musikclubs und belebte Café-Terrassen bietet.",
            "es": "Un barrio artístico completamente bohemio cubierto de vibrantes grafitis de arte callejero, que cuenta con tiendas de segunda mano vintage, locales de música indie y animadas terrazas de cafés.",
            "nl": "Een door en door bohemien artistieke wijk, bedekt met levendige straatkunstgraffiti, met vintage kringloopwinkels, indiemuziekpodia en levendige caféterrassen."
        },
        "tip": {
            "en": "Climb the famous colorful steps from the market. It is the absolute best area to grab craft beers and mingle with local creators.",
            "ja": "市場から続く有名なカラフルな階段を登ってください。クラフトビールを飲みながら地元のクリエイターと交流するのに最適なエリアです。",
            "zh": "从市场爬上著名的彩色阶梯。这里是喝精酿啤酒、与当地创作者交流的绝佳去处。",
            "fr": "Montez les célèbres marches colorées depuis le marché. C'est le meilleur quartier pour déguster des bières artisanales et se mêler aux créateurs locaux.",
            "de": "Steigen Sie die berühmten bunten Treppen vom Markt hinauf. Es ist die absolut beste Gegend, um Craft-Biere zu trinken und sich unter die lokalen Schöpfer zu mischen.",
            "es": "Sube las famosas escaleras coloridas desde el mercado. Es la mejor zona para tomar cervezas artesanales y mezclarse con los creadores locales.",
            "nl": "Beklim de beroemde kleurrijke trappen vanaf de markt. Het is de allerbeste wijk om ambachtelijke bieren te drinken en te mengen met lokale makers."
        },
        "whyThisSpot": {
            "en": "It expresses Marseille's rebellious, creative, and endlessly cool underground spirit in an explosion of color and sound.",
            "ja": "マルセイユの反抗的で創造的、そして限りなくクールなアンダーグラウンドの精神を、色彩と音の爆発で表現しています。",
            "zh": "它在色彩与声音的爆发中，表达了马赛反叛、富有创造力以及无比酷炫的地下精神。",
            "fr": "Il exprime l'esprit underground rebelle, créatif et infiniment cool de Marseille dans une explosion de couleurs et de sons.",
            "de": "Es drückt Marseilles rebellischen, kreativen und unendlich coolen Underground-Geist in einer Explosion von Farben und Klängen aus.",
            "es": "Expresa el espíritu clandestino rebelde, creativo e infinitamente genial de Marsella en una explosión de color y sonido.",
            "nl": "Het drukt de opstandige, creatieve en eindeloos coole underground-geest van Marseille uit in een explosie van kleur en geluid."
        }
    },
    "mrs_ma_35": {
        "desc": {
            "en": "A breathtaking coastal national park comprising soaring, stark white limestone cliffs diving into brilliantly turquoise, labyrinthine fjord inlets.",
            "ja": "白くそびえ立つ石灰岩の崖が、迷路のようなターコイズブルーの入り江に飛び込む、息を呑むほど美しい海岸の国立公園。",
            "zh": "一个令人惊叹的沿海国家公园，由高耸的纯白石灰岩悬崖和潜入迷宫般碧蓝峡湾的海湾组成。",
            "fr": "Un parc national côtier à couper le souffle, composé de falaises de calcaire d'un blanc immaculé plongeant dans des criques de fjords labyrinthiques d'un turquoise éclatant.",
            "de": "Ein atemberaubender Küsten-Nationalpark, bestehend aus hoch aufragenden, strahlend weißen Kalksteinklippen, die in leuchtend türkisfarbene, labyrinthartige Fjordbuchten eintauchen.",
            "es": "Un impresionante parque nacional costero compuesto por imponentes acantilados de piedra caliza blanca que se sumergen en ensenadas de fiordos laberínticos de un azul turquesa brillante.",
            "nl": "Een adembenemend nationaal kustpark met torenhoge, spierwitte kalkrotsen die in briljant turquoise, labyrintische fjordinhammen duiken."
        },
        "tip": {
            "en": "Always check the 'Mes Calanques' app before hiking; trails close in summer due to fire risks. Carry at least 2 liters of water per person.",
            "ja": "ハイキングの前には必ず「Mes Calanques」アプリを確認してください。夏場は火災のリスクによりトレイルが閉鎖されます。1人あたり最低2リットルの水を持参してください。",
            "zh": "徒步前务必查看“Mes Calanques”应用程序；夏季小径可能会因火灾风险而关闭。每人至少携带2升水。",
            "fr": "Vérifiez toujours l'application 'Mes Calanques' avant de partir en randonnée ; les sentiers ferment en été en raison des risques d'incendie. Prévoyez au moins 2 litres d'eau par personne.",
            "de": "Überprüfen Sie vor dem Wandern immer die App 'Mes Calanques'; Wegen Waldbrandgefahr werden Wege im Sommer gesperrt. Nehmen Sie mindestens 2 Liter Wasser pro Person mit.",
            "es": "Comprueba siempre la aplicación 'Mes Calanques' antes de hacer senderismo; los senderos cierran en verano por riesgo de incendio. Lleva al menos 2 litros de agua por persona.",
            "nl": "Controleer altijd de 'Mes Calanques'-app voordat u gaat wandelen; paden sluiten in de zomer vanwege brandgevaar. Neem minimaal 2 liter water per persoon mee."
        },
        "whyThisSpot": {
            "en": "It is an awe-inspiring natural wonder offering some of the most spectacular wild hiking and swimming terrain in Europe.",
            "ja": "ヨーロッパで最も壮大で野生のハイキングと水泳の地形を提供する、畏敬の念を抱かせる自然の驚異です。",
            "zh": "这是一个令人惊叹的自然奇观，提供欧洲最壮观的野生徒步和游泳地形。",
            "fr": "C'est une merveille naturelle impressionnante offrant certains des terrains de randonnée sauvage et de baignade les plus spectaculaires d'Europe.",
            "de": "Es ist ein beeindruckendes Naturwunder, das einige der spektakulärsten wilden Wander- und Schwimmgebiete Europas bietet.",
            "es": "Es una maravilla natural impresionante que ofrece algunos de los terrenos más espectaculares para practicar senderismo salvaje y natación en Europa.",
            "nl": "Het is een ontzagwekkend natuurwonder dat enkele van de meest spectaculaire wilde wandel- en zwemgebieden in Europa biedt."
        }
    },
    "mrs_ma_39": {
        "desc": {
            "en": "A highly enjoyable tourist road train that leisurely chugs from the Old Port along the scenic coastal road up to the basilica.",
            "ja": "旧港から風光明媚な海岸沿いの道を大聖堂までゆっくりと走る、非常に楽しい観光用ロードトレイン。",
            "zh": "一辆非常有趣的旅游公路列车，从老港出发，沿着风景如画的沿海公路悠闲地驶向大教堂。",
            "fr": "Un petit train routier touristique très agréable qui roule tranquillement depuis le Vieux-Port le long de la route côtière pittoresque jusqu'à la basilique.",
            "de": "Ein äußerst unterhaltsamer Touristenstraßenzug, der gemütlich vom Alten Hafen entlang der malerischen Küstenstraße bis zur Basilika tuckert.",
            "es": "Un tren turístico muy agradable que avanza tranquilamente desde el Puerto Viejo a lo largo de la pintoresca carretera costera hasta la basílica.",
            "nl": "Een zeer plezierige toeristische wegtrein die rustig van de Oude Haven langs de schilderachtige kustweg naar de basiliek tuft."
        },
        "tip": {
            "en": "Perfect for families with tired children, it spares you the incredibly steep uphill climb while providing audioguide history along the route.",
            "ja": "疲れた子供連れの家族に最適です。とてつもなく急な上り坂を避けることができ、ルート沿いでは音声ガイドで歴史を学べます。",
            "zh": "非常适合带着疲惫孩子的家庭，它可以让您免去攀爬陡峭山坡的辛苦，同时沿途提供语音导游历史讲解。",
            "fr": "Idéal pour les familles avec des enfants fatigués, il vous épargne la montée incroyablement raide tout en fournissant une histoire audioguidée tout au long du trajet.",
            "de": "Perfekt für Familien mit müden Kindern, es erspart Ihnen den unglaublich steilen Anstieg und bietet gleichzeitig einen Audioguide zur Geschichte entlang der Route.",
            "es": "Perfecto para familias con niños cansados, le ahorra la subida increíblemente empinada y proporciona una audioguía sobre la historia a lo largo de la ruta.",
            "nl": "Perfect voor gezinnen met vermoeide kinderen, het bespaart u de ongelooflijk steile klim terwijl u onderweg naar een audiogids met geschiedenis kunt luisteren."
        },
        "whyThisSpot": {
            "en": "It turns a tough transit into a charming, breezy sightseeing attraction highlighting the dramatic coastal curves of Marseille.",
            "ja": "厳しい移動を、マルセイユのドラマチックな海岸線のカーブを際立たせる、魅力的で風通しの良い観光アトラクションに変えます。",
            "zh": "它将一段艰难的旅程变成了一个迷人、轻松的观光景点，凸显了马赛戏剧性的海岸线弧度。",
            "fr": "Il transforme un trajet difficile en une attraction touristique charmante et aérée, mettant en valeur les spectaculaires courbes côtières de Marseille.",
            "de": "Es verwandelt einen anstrengenden Transit in eine charmante, luftige Sightseeing-Attraktion, die die dramatischen Küstenkurven von Marseille hervorhebt.",
            "es": "Convierte un tránsito difícil en una atracción turística encantadora y con brisa que resalta las dramáticas curvas costeras de Marsella.",
            "nl": "Het verandert een zware doorvoer in een charmante, luchtige bezienswaardigheid die de dramatische kustcurven van Marseille benadrukt."
        }
    },
    "mrs_ma_40": {
        "desc": {
            "en": "Exciting sightseeing boat cruises departing the Old Port to explore the infamous Château d'If and the majestic sea cliffs of the Calanques.",
            "ja": "旧港から出発し、悪名高いイフ城とカランクの雄大な海食崖を探索する、エキサイティングな観光ボートクルーズ。",
            "zh": "激动人心的观光游船从老港出发，探索臭名昭著的伊夫堡和卡朗格雄伟的海崖。",
            "fr": "Des croisières touristiques passionnantes en bateau au départ du Vieux-Port pour explorer le célèbre Château d'If et les majestueuses falaises marines des Calanques.",
            "de": "Spannende Sightseeing-Bootsfahrten ab dem Alten Hafen, um das berüchtigte Château d'If und die majestätischen Meeresklippen der Calanques zu erkunden.",
            "es": "Emocionantes cruceros turísticos en barco que salen del Puerto Viejo para explorar el famoso Castillo de If y los majestuosos acantilados de las Calanques.",
            "nl": "Spannende rondvaartboten vertrekken vanuit de Oude Haven om het beruchte Château d'If en de majestueuze zeekliffen van de Calanques te verkennen."
        },
        "tip": {
            "en": "Book the full-day Calanques tour to truly appreciate the sheer scale of the limestone cliffs. Bring a windbreaker as the open sea gets chilly.",
            "ja": "石灰岩の崖の途方もないスケールを真に鑑賞するには、1日カランクツアーを予約してください。外海は冷え込むのでウィンドブレーカーを持参しましょう。",
            "zh": "预订全日卡朗格游览，才能真正体会石灰岩悬崖的磅礴气势。由于外海风大较冷，请带上防风夹克。",
            "fr": "Réservez l'excursion d'une journée complète dans les Calanques pour apprécier pleinement l'immensité des falaises de calcaire. Apportez un coupe-vent car la pleine mer se rafraîchit.",
            "de": "Buchen Sie die ganztägige Calanques-Tour, um die enorme Größe der Kalksteinklippen wirklich würdigen zu können. Bringen Sie eine Windjacke mit, da es auf dem offenen Meer kühl wird.",
            "es": "Reserva el recorrido de día completo por las Calanques para apreciar realmente la inmensidad de los acantilados de piedra caliza. Lleva un cortavientos, ya que el mar abierto se enfría.",
            "nl": "Boek de volledige dagtour door de Calanques om de enorme omvang van de kalkrotsen echt te waarderen. Neem een windjack mee, want de open zee kan fris worden."
        },
        "whyThisSpot": {
            "en": "It is undeniably the most relaxing and panoramic way to witness Marseille's coastal geography without the intense physical exertion of hiking.",
            "ja": "ハイキングのような激しい運動をすることなく、マルセイユの海岸地理を最もリラックスしてパノラマで見る方法であることは間違いありません。",
            "zh": "这无疑是欣赏马赛海岸地理环境最放松、最能享受全景的方式，免去了徒步旅行的剧烈体力消耗。",
            "fr": "C'est indéniablement le moyen le plus relaxant et panoramique d'admirer la géographie côtière de Marseille sans l'effort physique intense de la randonnée.",
            "de": "Es ist unbestreitbar die entspannendste und panoramischste Art, Marseilles Küstengeografie zu erleben, ohne die intensive körperliche Anstrengung des Wanderns.",
            "es": "Es, sin duda, la forma más relajante y panorámica de presenciar la geografía costera de Marsella sin el intenso esfuerzo físico del senderismo.",
            "nl": "Het is onmiskenbaar de meest ontspannende en panoramische manier om de kustgeografie van Marseille te aanschouwen zonder de zware fysieke inspanning van wandelen."
        }
    },
    "mrs_ma_41": {
        "desc": {
            "en": "An expansive and lively coastal beach park featuring sweeping sandy shores, wide grassy lawns, splash areas, and a famous international skate bowl.",
            "ja": "広々とした砂浜、広い芝生、水遊び場、有名な国際的スケートボウルを備えた、広大で活気のある海岸沿いのビーチパーク。",
            "zh": "一个广阔而热闹的沿海海滩公园，拥有宽阔的沙滩、宽广的草坪、戏水区和著名的国际滑板碗。",
            "fr": "Un vaste parc balnéaire côtier animé, comprenant de grandes étendues de sable, de vastes pelouses, des aires de jeux d'eau et un célèbre bowl de skate international.",
            "de": "Ein weitläufiger und lebhafter Küstenstrandpark mit weitläufigen Sandstränden, breiten Rasenflächen, Wasserspielplätzen und einem berühmten internationalen Skate-Bowl.",
            "es": "Un amplio y animado parque de playa costero que cuenta con extensas costas arenosas, amplios prados de césped, zonas de chapoteo y un famoso skate bowl internacional.",
            "nl": "Een uitgestrekt en levendig kustpark met uitgestrekte zandstranden, brede grasvelden, spettergebieden en een beroemde internationale skatebowl."
        },
        "tip": {
            "en": "It's the ultimate summer hangout. Rent a bike to ride the coastal path, then cool down with a swim and grab a gelato nearby.",
            "ja": "究極の夏のたまり場です。自転車を借りて海岸沿いの道を走り、泳いで涼んだ後は近くでジェラートを楽しみましょう。",
            "zh": "这里是绝佳的夏日聚会场所。租一辆自行车沿着沿海小径骑行，然后游泳凉爽一下，并在附近买个冰淇淋。",
            "fr": "C'est le lieu de rendez-vous estival par excellence. Louez un vélo pour parcourir le sentier côtier, puis rafraîchissez-vous avec une baignade et prenez une glace à proximité.",
            "de": "Es ist der ultimative sommerliche Treffpunkt. Mieten Sie ein Fahrrad, um den Küstenweg entlang zu fahren, kühlen Sie sich dann beim Schwimmen ab und holen Sie sich ein Gelato in der Nähe.",
            "es": "Es el lugar de encuentro veraniego definitivo. Alquila una bicicleta para recorrer el camino costero, luego refréscate con un baño y toma un helado cerca.",
            "nl": "Het is de ultieme zomerse ontmoetingsplek. Huur een fiets om over het kustpad te rijden, koel dan af met een duik en haal een gelato in de buurt."
        },
        "whyThisSpot": {
            "en": "It perfectly channels the energetic, outdoorsy, and sun-drenched lifestyle of southern French seaside culture.",
            "ja": "南フランスの海辺の文化の、エネルギッシュでアウトドア志向、そして太陽が降り注ぐライフスタイルを完璧に体現しています。",
            "zh": "它完美地传达了法国南部海滨文化中充满活力、热爱户外运动和阳光普照的生活方式。",
            "fr": "Il canalise parfaitement le style de vie énergique, axé sur le plein air et baigné de soleil de la culture balnéaire du sud de la France.",
            "de": "Es kanalisiert perfekt den energiegeladenen, naturverbundenen und sonnenverwöhnten Lebensstil der südfranzösischen Küstenkultur.",
            "es": "Canaliza a la perfección el estilo de vida enérgico, amante del aire libre y bañado por el sol de la cultura costera del sur de Francia.",
            "nl": "Het weerspiegelt perfect de energieke, buitenleven-gerichte en zonovergoten levensstijl van de Zuid-Franse kustcultuur."
        }
    },
    "mrs_ma_42": {
        "desc": {
            "en": "A highly entertaining family amusement park located just outside Marseille, featuring Wild West-themed rides, roller coasters, and engaging live shows.",
            "ja": "マルセイユのすぐ郊外にある非常に楽しい家族向けの遊園地で、西部劇をテーマにした乗り物、ジェットコースター、魅力的なライブショーが楽しめます。",
            "zh": "位于马赛郊外的一家非常有趣的家庭游乐园，提供狂野西部主题的游乐设施、过山车和引人入胜的现场表演。",
            "fr": "Un parc d'attractions familial très divertissant situé juste à l'extérieur de Marseille, proposant des manèges sur le thème du Far West, des montagnes russes et des spectacles captivants.",
            "de": "Ein äußerst unterhaltsamer Familien-Freizeitpark vor den Toren Marseilles mit Fahrgeschäften im Wildwest-Stil, Achterbahnen und spannenden Live-Shows.",
            "es": "Un parque de atracciones familiar muy entretenido situado a las afueras de Marsella, con atracciones temáticas del Salvaje Oeste, montañas rusas y atractivos espectáculos en vivo.",
            "nl": "Een zeer vermakelijk familiepretpark net buiten Marseille, met attracties met een Wild West-thema, achtbanen en boeiende liveshows."
        },
        "tip": {
            "en": "Great for kids aged 4-12. Arrive early to hit the water rides before it gets too hot, and catch the mid-day Western stunt show.",
            "ja": "4〜12歳の子供に最適です。暑くなる前にウォーターアトラクションを楽しむために早めに到着し、真昼のウエスタンスタントショーをお見逃しなく。",
            "zh": "非常适合 4-12 岁的儿童。尽早到达，赶在天气变热之前体验水上游乐设施，并观看中午的西部特技表演。",
            "fr": "Idéal pour les enfants de 4 à 12 ans. Arrivez tôt pour profiter des attractions aquatiques avant qu'il ne fasse trop chaud, et assistez au spectacle de cascades western de midi.",
            "de": "Toll für Kinder im Alter von 4-12 Jahren. Kommen Sie früh, um die Wasserbahnen zu nutzen, bevor es zu heiß wird, und sehen Sie sich die Western-Stuntshow am Mittag an.",
            "es": "Ideal para niños de 4 a 12 años. Llega temprano para disfrutar de las atracciones acuáticas antes de que haga demasiado calor y asiste al espectáculo de acrobacias del Oeste del mediodía.",
            "nl": "Geweldig voor kinderen van 4-12 jaar. Kom vroeg om de waterattracties te bezoeken voordat het te heet wordt, en vang de western-stuntshow in de middag."
        },
        "whyThisSpot": {
            "en": "It provides a hassle-free, highly interactive day of joyful escapism for families looking for non-historical entertainment.",
            "ja": "歴史的でないエンターテイメントを求める家族に、手間のかからない、非常にインタラクティブで楽しい現実逃避の1日を提供します。",
            "zh": "它为寻求非历史类娱乐活动的家庭提供了一个无忧无虑、高度互动的欢乐逃避之旅。",
            "fr": "Il offre une journée d'évasion joyeuse, sans tracas et très interactive pour les familles à la recherche de divertissements non historiques.",
            "de": "Es bietet einen unkomplizierten, hochinteraktiven Tag voller freudiger Realitätsflucht für Familien, die auf der Suche nach nichthistorischer Unterhaltung sind.",
            "es": "Proporciona un día sin complicaciones y altamente interactivo de alegre escapismo para las familias que buscan entretenimiento no histórico.",
            "nl": "Het biedt een probleemloze, zeer interactieve dag vol vreugdevol escapisme voor gezinnen die op zoek zijn naar niet-historisch entertainment."
        }
    },
    "mrs_ma_43": {
        "desc": {
            "en": "A vast, lush suburban nature park providing peaceful pony rides, an educational animal farm, challenging tree-top adventure courses, and scenic picnic areas.",
            "ja": "のどかなポニー乗馬、教育的な動物農場、やりがいのあるツリートップアドベンチャーコース、見晴らしの良いピクニックエリアを備えた広大で緑豊かな郊外の自然公園。",
            "zh": "一个广阔、郁郁葱葱的郊区自然公园，提供宁静的小马骑行、教育性的动物农场、具有挑战性的树顶探险课程以及风景优美的野餐区。",
            "fr": "Un vaste parc naturel de banlieue luxuriant proposant de paisibles promenades à poney, une ferme pédagogique, des parcours accrobranche stimulants et des aires de pique-nique pittoresques.",
            "de": "Ein weitläufiger, üppiger Vorort-Naturpark mit friedlichem Ponyreiten, einem pädagogischen Tierbauernhof, anspruchsvollen Hochseilgärten und malerischen Picknickplätzen.",
            "es": "Un vasto y exuberante parque natural suburbano que ofrece tranquilos paseos en poni, una granja de animales educativa, desafiantes cursos de aventuras en los árboles y pintorescas zonas de picnic.",
            "nl": "Een uitgestrekt, weelderig natuurpark in de voorsteden met rustige ponyritten, een educatieve dierenboerderij, uitdagende boomkroonpaden en pittoreske picknickplaatsen."
        },
        "tip": {
            "en": "Bring your own carrots and apples for the farm animals. The tree-top climbing courses are excellent for tiring out energetic teens.",
            "ja": "農場の動物たちのためにニンジンやリンゴを持参しましょう。ツリートップクライミングのコースは、元気なティーンエイジャーを疲れさせるのに最適です。",
            "zh": "带上自己的胡萝卜和苹果喂食农场动物。树顶攀岩课程非常适合消耗精力充沛的青少年的体力。",
            "fr": "Apportez vos propres carottes et pommes pour les animaux de la ferme. Les parcours d'accrobranche sont excellents pour fatiguer les adolescents énergiques.",
            "de": "Bringen Sie Ihre eigenen Karotten und Äpfel für die Tiere auf dem Bauernhof mit. Die Hochseilgärten eignen sich hervorragend, um energiegeladene Teenager auszupowern.",
            "es": "Trae tus propias zanahorias y manzanas para los animales de la granja. Los cursos de escalada en los árboles son excelentes para cansar a los adolescentes enérgicos.",
            "nl": "Neem je eigen wortels en appels mee voor de boerderijdieren. De klimparcoursen in de boomtoppen zijn uitstekend geschikt om energieke tieners moe te maken."
        },
        "whyThisSpot": {
            "en": "It is an expansive, breath-of-fresh-air sanctuary where families can easily reconnect with nature without straying far from the city.",
            "ja": "都市部から遠く離れることなく、家族が簡単に自然と触れ合うことができる、広々とした新鮮な空気の聖域です。",
            "zh": "这是一个广阔的、呼吸新鲜空气的庇护所，家庭无需远离城市即可轻松地重新与自然亲近。",
            "fr": "C'est un vaste sanctuaire où l'on respire l'air frais, permettant aux familles de renouer facilement avec la nature sans s'éloigner de la ville.",
            "de": "Es ist ein weitläufiges Refugium mit frischer Luft, in dem Familien leicht wieder mit der Natur in Kontakt treten können, ohne sich weit von der Stadt zu entfernen.",
            "es": "Es un santuario amplio y lleno de aire fresco donde las familias pueden reconectar fácilmente con la naturaleza sin alejarse de la ciudad.",
            "nl": "Het is een uitgestrekt toevluchtsoord met frisse lucht waar gezinnen gemakkelijk weer in contact kunnen komen met de natuur zonder ver van de stad af te dwalen."
        }
    },
    "muc_m_1": {
        "desc": {
            "en": "Munich's grand central square, internationally famous for the whimsical Glockenspiel chime show and the spectacular Neo-Gothic facade of the New Town Hall.",
            "ja": "風変わりなグロッケンシュピールのショーと、新市庁舎の壮大なネオ・ゴシック様式のファサードで国際的に有名な、ミュンヘンの壮大な中央広場。",
            "zh": "慕尼黑宏伟的中心广场，以异想天开的钟琴表演和新市政厅壮观的新哥特式外墙而闻名于世。",
            "fr": "La grande place centrale de Munich, de renommée internationale pour le spectacle fantastique de son carillon (Glockenspiel) et la façade néo-gothique spectaculaire du Nouvel Hôtel de Ville.",
            "de": "Münchens großer zentraler Platz, international berühmt für das wunderliche Glockenspiel und die spektakuläre neugotische Fassade des Neuen Rathauses.",
            "es": "La gran plaza central de Múnich, internacionalmente famosa por el caprichoso espectáculo del carillón Glockenspiel y la espectacular fachada neogótica del Nuevo Ayuntamiento.",
            "nl": "Het grote centrale plein van München, internationaal beroemd om de grillige Glockenspiel-show en de spectaculaire neogotische façade van het Nieuwe Stadhuis."
        },
        "tip": {
            "en": "Arrive 15 minutes before 11:00 AM or 12:00 PM to secure a good viewing spot for the Glockenspiel, and watch out for pickpockets in the crowd.",
            "ja": "グロッケンシュピールをよく見るために、午前11時または午後12時の15分前に到着し、人混みの中のスリに気をつけてください。",
            "zh": "在上午 11:00 或中午 12:00 前 15 分钟到达，以确保获得观看钟琴的良好位置，并在人群中当心扒手。",
            "fr": "Arrivez 15 minutes avant 11h00 ou 12h00 pour vous assurer une bonne place pour observer le Glockenspiel, et faites attention aux pickpockets dans la foule.",
            "de": "Kommen Sie 15 Minuten vor 11:00 oder 12:00 Uhr an, um sich einen guten Aussichtspunkt für das Glockenspiel zu sichern, und achten Sie im Gedränge auf Taschendiebe.",
            "es": "Llega 15 minutos antes de las 11:00 a.m. o las 12:00 p.m. para asegurar un buen lugar de observación para el Glockenspiel, y ten cuidado con los carteristas en la multitud.",
            "nl": "Kom 15 minuten voor 11.00 uur of 12.00 uur aan om zeker te zijn van een goede kijkplek voor het Glockenspiel, en pas op voor zakkenrollers in de menigte."
        },
        "whyThisSpot": {
            "en": "It is the undeniable historical and cultural core of Munich, providing an awe-inspiring introduction to Bavarian architectural splendor.",
            "ja": "ミュンヘンの紛れもない歴史的、文化的中心であり、バイエルン建築の壮大さを畏敬の念を持って紹介してくれます。",
            "zh": "它是慕尼黑不可否认的历史和文化核心，为您展示令人叹为观止的巴伐利亚建筑之美。",
            "fr": "C'est le cœur historique et culturel incontestable de Munich, offrant une introduction impressionnante à la splendeur architecturale bavaroise.",
            "de": "Es ist der unbestreitbare historische und kulturelle Kern Münchens und bietet eine beeindruckende Einführung in die bayerische architektonische Pracht.",
            "es": "Es el innegable núcleo histórico y cultural de Múnich, que proporciona una introducción impresionante al esplendor arquitectónico bávaro.",
            "nl": "Het is de onmiskenbare historische en culturele kern van München, en biedt een ontzagwekkende kennismaking met de Beierse architectonische pracht."
        }
    },
    "muc_m_2": {
        "desc": {
            "en": "A monumental Gothic brick cathedral defining Munich's skyline, featuring distinctive twin onion domes and the legendary 'Devil's Footprint' at its entrance.",
            "ja": "ミュンヘンのスカイラインを定義する記念碑的なゴシック様式のレンガ造りの大聖堂。特徴的な双子の玉ねぎ型ドームと、入り口にある伝説の「悪魔の足跡」が特徴です。",
            "zh": "一座标志着慕尼黑天际线的具有纪念意义的哥特式砖砌大教堂，拥有独特的双洋葱头圆顶，入口处还有传奇的“恶魔脚印”。",
            "fr": "Une cathédrale monumentale en briques gothiques qui définit l'horizon de Munich, caractérisée par ses deux dômes en oignon distinctifs et la légendaire 'Empreinte du Diable' à son entrée.",
            "de": "Eine monumentale gotische Backsteinkathedrale, die Münchens Skyline prägt, mit markanten Zwiebeltürmen und dem legendären 'Teufelstritt' am Eingang.",
            "es": "Una monumental catedral gótica de ladrillo que define el horizonte de Múnich, con distintivas cúpulas gemelas en forma de cebolla y la legendaria 'Huella del Diablo' en su entrada.",
            "nl": "Een monumentale gotische bakstenen kathedraal die de skyline van München bepaalt, met opvallende dubbele uivormige koepels en de legendarische 'Voetafdruk van de Duivel' bij de ingang."
        },
        "tip": {
            "en": "Find the Devil's Footprint near the entrance. From that exact spot, the side windows are visually blocked by massive pillars, creating a fascinating optical illusion.",
            "ja": "入り口近くで悪魔の足跡を探してください。その正確な場所から見ると、巨大な柱によって側面の窓が視覚的に遮られ、魅力的な錯覚を生み出します。",
            "zh": "在入口附近找到恶魔的脚印。从那个确切的位置看，侧窗在视觉上被巨大的柱子挡住了，产生了迷人的光学错觉。",
            "fr": "Trouvez l'Empreinte du Diable près de l'entrée. Depuis ce point précis, les fenêtres latérales sont visuellement masquées par des piliers massifs, créant une illusion d'optique fascinante.",
            "de": "Finden Sie den Teufelstritt in der Nähe des Eingangs. Von diesem genauen Punkt aus werden die Seitenfenster optisch von massiven Säulen verdeckt, was eine faszinierende optische Täuschung erzeugt.",
            "es": "Busca la Huella del Diablo cerca de la entrada. Desde ese punto exacto, las ventanas laterales quedan visualmente bloqueadas por enormes pilares, creando una fascinante ilusión óptica.",
            "nl": "Vind de Voetafdruk van de Duivel bij de ingang. Vanaf die exacte plek worden de zijramen visueel geblokkeerd door massieve pilaren, waardoor een fascinerende optische illusie ontstaat."
        },
        "whyThisSpot": {
            "en": "It is an unmissable symbol of the city's enduring faith, shrouded in captivating folklore and offering quiet grandeur amidst the city bustle.",
            "ja": "魅惑的な民間伝承に包まれ、街の喧騒の中で静かな壮大さを提供する、街の不朽の信仰の必見のシンボルです。",
            "zh": "这是这座城市持久信仰的不容错过的象征，笼罩在迷人的民间传说中，在城市的喧嚣中呈现出宁静的壮丽。",
            "fr": "C'est un symbole incontournable de la foi pérenne de la ville, entouré de folklore captivant et offrant une grandeur tranquille au milieu de l'agitation de la ville.",
            "de": "Es ist ein unübersehbares Symbol für den unerschütterlichen Glauben der Stadt, umhüllt von fesselnder Folklore und bietet stille Pracht inmitten des Trubels der Stadt.",
            "es": "Es un símbolo imperdible de la fe perdurable de la ciudad, envuelto en un folclore cautivador y que ofrece una grandeza tranquila en medio del bullicio de la ciudad.",
            "nl": "Het is een onmisbaar symbool van het blijvende geloof van de stad, gehuld in boeiende folklore en met een stille grandeur te midden van de drukte van de stad."
        }
    },
    "muc_m_3": {
        "desc": {
            "en": "The lavish former royal palace of the Wittelsbach monarchs, boasting the stunning Renaissance Antiquarium hall and a dazzling crown jewel Treasury.",
            "ja": "ヴィッテルスバッハ家の豪華な旧王宮。見事なルネッサンス様式のアンティクアリウム・ホールとまばゆいばかりの王冠の宝石が並ぶ宝物館を誇っています。",
            "zh": "维特尔斯巴赫君主奢华的旧皇宫，拥有令人惊叹的文艺复兴时期的古物馆和令人眼花缭乱的皇冠珠宝库。",
            "fr": "Le somptueux ancien palais royal des monarques Wittelsbach, doté de la superbe salle Renaissance de l'Antiquarium et d'un Trésor de joyaux de la couronne éblouissant.",
            "de": "Der üppige ehemalige Königspalast der Wittelsbacher-Monarchen mit dem atemberaubenden Renaissance-Antiquarium-Saal und einer schillernden Kronjuwelen-Schatzkammer.",
            "es": "El fastuoso antiguo palacio real de los monarcas de Wittelsbach, que cuenta con el impresionante salón Antiquarium renacentista y un deslumbrante Tesoro de joyas de la corona.",
            "nl": "Het weelderige voormalige koninklijke paleis van de Wittelsbach-monarchen, met de prachtige renaissance-Antiquarium-zaal en een schitterende schatkamer met kroonjuwelen."
        },
        "tip": {
            "en": "Purchase the combo ticket to see both the Residenz and the Treasury. Don't forget to rub the noses of the bronze lions outside for good luck!",
            "ja": "レジデンツと宝物館の両方を見学できる共通チケットを購入してください。幸運のために外にあるブロンズのライオンの鼻をこするのを忘れないでください！",
            "zh": "购买联票参观王宫和宝物馆。别忘了摸摸外面青铜狮子的鼻子以求好运！",
            "fr": "Achetez le billet combiné pour voir à la fois la Résidence et le Trésor. N'oubliez pas de frotter le nez des lions en bronze à l'extérieur pour vous porter chance !",
            "de": "Kaufen Sie das Kombiticket, um sowohl die Residenz als auch die Schatzkammer zu besichtigen. Vergessen Sie nicht, die Nasen der Bronzelöwen draußen für viel Glück zu reiben!",
            "es": "Compra la entrada combinada para ver tanto la Residencia como el Tesoro. ¡No olvides frotar las narices de los leones de bronce afuera para la buena suerte!",
            "nl": "Koop het combiticket om zowel de Residenz als de Schatkamer te zien. Vergeet niet over de neuzen van de bronzen leeuwen buiten te wrijven voor geluk!"
        },
        "whyThisSpot": {
            "en": "It is an incredibly rich, sprawling journey through Bavarian royal history, featuring some of the most opulent interior design in Europe.",
            "ja": "ヨーロッパで最も豪華なインテリアデザインを特徴とする、バイエルン王室の歴史を巡る信じられないほど豊かで広大な旅です。",
            "zh": "这是一段极其丰富、广阔的巴伐利亚王室历史之旅，拥有欧洲最奢华的室内设计。",
            "fr": "C'est un voyage incroyablement riche et vaste à travers l'histoire royale bavaroise, présentant certaines des décorations intérieures les plus opulentes d'Europe.",
            "de": "Es ist eine unglaublich reiche, weitläufige Reise durch die bayerische Königsgeschichte und bietet einige der opulentesten Inneneinrichtungen in Europa.",
            "es": "Es un viaje increíblemente rico y extenso a través de la historia real bávara, con algunos de los diseños de interiores más opulentos de Europa.",
            "nl": "Het is een ongelooflijk rijke, uitgestrekte reis door de koninklijke geschiedenis van Beieren, met enkele van de meest weelderige interieurontwerpen van Europa."
        }
    },
    "nce_nice_1": {
        "desc": {
            "en": "The iconic 7-kilometer Mediterranean seaside boulevard, beautifully lined with swaying palm trees, legendary blue chairs, and glamorous beach clubs.",
            "ja": "揺れるヤシの木、伝説的な青い椅子、グラマラスなビーチクラブが美しく立ち並ぶ、象徴的な7kmの地中海海沿いの大通り。",
            "zh": "这条全长7公里的标志性地中海海滨大道，两旁种满了摇曳的棕榈树，摆放着传奇的蓝色椅子和迷人的海滩俱乐部。",
            "fr": "L'emblématique boulevard balnéaire méditerranéen de 7 kilomètres, magnifiquement bordé de palmiers majestueux, de légendaires chaises bleues et de clubs de plage glamour.",
            "de": "Der ikonische, 7 Kilometer lange mediterrane Küstenboulevard, wunderschön gesäumt von sich wiegenden Palmen, legendären blauen Stühlen und glamourösen Strandclubs.",
            "es": "El emblemático bulevar marítimo mediterráneo de 7 kilómetros, hermosamente bordeado de palmeras, legendarias sillas azules y glamurosos clubes de playa.",
            "nl": "De iconische 7 kilometer lange mediterrane boulevard aan zee, prachtig omzoomd met wuivende palmbomen, legendarische blauwe stoelen en glamoureuze strandclubs."
        },
        "tip": {
            "en": "Rent a bike or simply stroll during the late afternoon. Walk up to Castle Hill at sunset for the ultimate panoramic photo of the sweeping bay.",
            "ja": "自転車を借りるか、午後遅くに単に散歩を楽しんでください。夕暮れ時にキャッスルヒルに登り、広がる湾の究極のパノラマ写真を撮りましょう。",
            "zh": "租一辆自行车或在傍晚时分漫步。在日落时分爬上城堡山，拍摄整个海湾的极致全景照片。",
            "fr": "Louez un vélo ou promenez-vous simplement en fin d'après-midi. Montez à la Colline du Château au coucher du soleil pour la photo panoramique ultime de la magnifique baie.",
            "de": "Mieten Sie ein Fahrrad oder schlendern Sie einfach am späten Nachmittag entlang. Gehen Sie bei Sonnenuntergang zum Schlosshügel hinauf, um das ultimative Panoramafoto der weitläufigen Bucht zu machen.",
            "es": "Alquila una bicicleta o simplemente pasea a última hora de la tarde. Sube a la Colina del Castillo al atardecer para obtener la mejor foto panorámica de la amplia bahía.",
            "nl": "Huur een fiets of wandel gewoon in de late namiddag. Loop bij zonsondergang naar Castle Hill voor de ultieme panoramafoto van de weidse baai."
        },
        "whyThisSpot": {
            "en": "It is the sun-kissed soul of Nice, offering a flawless, quintessential French Riviera experience where the city beautifully meets the sea.",
            "ja": "それはニースの太陽の光を浴びた魂であり、都市が海と美しく出会う、完璧で典型的なフレンチ・リヴィエラの体験を提供します。",
            "zh": "这里是尼斯沐浴在阳光下的灵魂，为您提供完美、典型的法国里维埃拉体验，城市与大海在此完美交融。",
            "fr": "C'est l'âme baignée de soleil de Nice, offrant une expérience de la Côte d'Azur typique et sans faille, là où la ville rencontre magnifiquement la mer.",
            "de": "Es ist die sonnenverwöhnte Seele von Nizza und bietet ein makelloses, typisches French-Riviera-Erlebnis, bei dem die Stadt auf wunderbare Weise auf das Meer trifft.",
            "es": "Es el alma besada por el sol de Niza, que ofrece una experiencia impecable y por excelencia de la Riviera francesa donde la ciudad se encuentra bellamente con el mar.",
            "nl": "Het is de zonovergoten ziel van Nice, die een onberispelijke, typische Franse Rivièra-ervaring biedt waar de stad op prachtige wijze de zee ontmoet."
        }
    }
}

for item in spots:
    spot_id = item["spot"]["id"]
    if spot_id in updates:
        # Update desc, tip, whyThisSpot for all languages
        for lang in ["en", "ja", "zh", "fr", "de", "es", "nl"]:
            item["spot"][f"desc_{lang}"] = updates[spot_id]["desc"][lang]
            item["spot"][f"tip_{lang}"] = updates[spot_id]["tip"][lang]
            item["spot"][f"whyThisSpot_{lang}"] = updates[spot_id]["whyThisSpot"][lang]

# Save to the new file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(spots, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(updates)} spots and wrote to {output_file}")
