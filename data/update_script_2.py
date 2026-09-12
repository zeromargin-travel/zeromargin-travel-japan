import json
import os

input_file = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_written_4.json'
output_file = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_written_4.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Master texts for the remaining 11 spots
updates = {
  "lyn_lyon_40": {
    "desc_en": "A peaceful, car-free green island nestled in the Saône river, featuring atmospheric ruins of a 5th-century monastery and picturesque stone cottages.",
    "desc_ja": "ソーヌ川に抱かれた静かで車のない緑の島。5世紀の修道院の雰囲気のある遺跡や、絵のように美しい石造りのコテージがあります。",
    "desc_es": "Una apacible isla verde sin coches enclavada en el río Saona, con ruinas evocadoras de un monasterio del siglo V y pintorescas casas de piedra.",
    "desc_zh": "一个位于索恩河中的宁静、无车的绿色岛屿，拥有 5 世纪修道院的氛围遗迹和风景如画的石制小屋。",
    "desc_fr": "Une île verdoyante paisible et sans voiture nichée au milieu de la Saône, abritant les ruines évocatrices d'un monastère du Ve siècle et des maisons en pierre pittoresques.",
    "desc_de": "Eine friedliche, autofreie grüne Insel eingebettet im Fluss Saône, mit stimmungsvollen Ruinen eines Klosters aus dem 5. Jahrhundert und malerischen Steinhäusern.",
    "desc_nl": "Een vredig, autovrij groen eiland genesteld in de rivier de Saône, met sfeervolle ruïnes van een 5e-eeuws klooster en pittoreske stenen huisjes.",
    
    "tip_en": "It's the perfect spot for a lazy afternoon escape. Only part of the island is public, so respect private areas while enjoying the serene river views.",
    "tip_ja": "のんびりとした午後の逃避行に最適なスポットです。島の一部のみが一般公開されているため、静かな川の景色を楽しみながらプライベートエリアを尊重してください。",
    "tip_es": "Es el lugar perfecto para una escapada de tarde perezosa. Solo una parte de la isla es pública, así que respeta las áreas privadas mientras disfrutas de las serenas vistas al río.",
    "tip_zh": "这里是度过慵懒午后时光的完美去处。岛上只有部分区域对公众开放，因此在欣赏宁静河景的同时，请尊重私人区域。",
    "tip_fr": "C'est l'endroit idéal pour une escapade l'après-midi en toute détente. Seule une partie de l'île est publique, veuillez donc respecter les espaces privés tout en profitant de la vue sereine sur le fleuve.",
    "tip_de": "Es ist der perfekte Ort für einen faulen Nachmittagsausflug. Nur ein Teil der Insel ist öffentlich, respektieren Sie also private Bereiche, während Sie den ruhigen Blick auf den Fluss genießen.",
    "tip_nl": "Het is de perfecte plek voor een luie middag ontsnapping. Slechts een deel van het eiland is openbaar, dus respecteer privégebieden terwijl u geniet van het serene uitzicht op de rivier.",

    "whyThisSpot_en": "A fairytale escape from city life that feels like stepping back into the Middle Ages right in Lyon.",
    "whyThisSpot_ja": "リヨンにいながらにして中世にタイムスリップしたような、都会の喧騒から逃れるおとぎ話のような空間。",
    "whyThisSpot_es": "Una escapada de cuento de hadas de la vida de la ciudad que te hace sentir como si retrocedieras a la Edad Media justo en Lyon.",
    "whyThisSpot_zh": "一个如同童话般的避风港，逃离城市喧嚣，感觉就像在里昂直接穿越回中世纪。",
    "whyThisSpot_fr": "Une évasion féérique loin de la vie urbaine qui donne l'impression de remonter le temps jusqu'au Moyen Âge en plein Lyon.",
    "whyThisSpot_de": "Ein märchenhafter Zufluchtsort aus dem Stadtleben, der sich anfühlt wie eine Zeitreise ins Mittelalter mitten in Lyon.",
    "whyThisSpot_nl": "Een sprookjesachtige ontsnapping aan het stadsleven die voelt alsof je terug in de tijd stapt naar de Middeleeuwen, midden in Lyon."
  },
  "lyn_lyon_41": {
    "desc_en": "Ranked as one of France's Most Beautiful Villages, this immaculately preserved medieval fortified town boasts 15th-century stone ramparts and authentic cobblestone alleys.",
    "desc_ja": "「フランスの最も美しい村」の 1 つにランクされている、この見事に保存された中世の要塞都市は、15 世紀の石造りの城壁と本物の石畳の路地を誇っています。",
    "desc_es": "Clasificado como uno de los pueblos más bellos de Francia, este pueblo fortificado medieval impecablemente conservado cuenta con murallas de piedra del siglo XV y auténticos callejones adoquinados.",
    "desc_zh": "被评为“法国最美村庄”之一，这座保存完好的中世纪防御小镇拥有 15 世纪的石造城墙和原汁原味的鹅卵石小巷。",
    "desc_fr": "Classé parmi les Plus Beaux Villages de France, cette ville fortifiée médiévale impeccablement préservée possède des remparts en pierre du XVe siècle et d'authentiques ruelles pavées.",
    "desc_de": "Als eines der schönsten Dörfer Frankreichs eingestuft, verfügt diese makellos erhaltene mittelalterliche Festungsstadt über Steinwälle aus dem 15. Jahrhundert und authentische Kopfsteinpflastergassen.",
    "desc_nl": "Geclassificeerd als een van de mooiste dorpen van Frankrijk, beschikt dit onberispelijk bewaarde middeleeuwse vestingstadje over 15e-eeuwse stenen wallen en authentieke geplaveide steegjes.",

    "tip_en": "Wear comfortable shoes for the uneven cobblestones, and absolutely do not leave without eating a warm slice of their legendary 'Galette de Pérouges' with cider.",
    "tip_ja": "でこぼこした石畳のため歩きやすい靴を履き、伝説の「ペルージュのガレット」の温かいスライスとシードルを食べずに帰らないでください。",
    "tip_es": "Usa zapatos cómodos para los adoquines irregulares y no te vayas sin comer una rebanada caliente de su legendaria 'Galette de Pérouges' con sidra.",
    "tip_zh": "穿上舒适的鞋子以应对不平坦的鹅卵石，并绝对不要错过品尝传说中的“佩鲁日国王饼”（配苹果酒），记得趁热吃。",
    "tip_fr": "Portez des chaussures confortables pour marcher sur les pavés inégaux, et ne partez surtout pas sans avoir goûté une part chaude de la légendaire « Galette de Pérouges » accompagnée de cidre.",
    "tip_de": "Tragen Sie bequeme Schuhe für das unebene Kopfsteinpflaster und gehen Sie auf keinen Fall, ohne ein warmes Stück ihrer legendären 'Galette de Pérouges' mit Apfelwein gegessen zu haben.",
    "tip_nl": "Draag comfortabele schoenen voor de ongelijke kasseien en vertrek absoluut niet zonder een warm stuk van hun legendarische 'Galette de Pérouges' met cider te hebben gegeten.",

    "whyThisSpot_en": "A visually stunning time capsule perfect for history buffs and food lovers alike, just a short trip from Lyon.",
    "whyThisSpot_ja": "リヨンからわずかな距離にある、歴史愛好家にも美食家にも最適な、視覚的に素晴らしいタイムカプセルです。",
    "whyThisSpot_es": "Una cápsula del tiempo visualmente impresionante perfecta para los amantes de la historia y los amantes de la comida, a un corto viaje desde Lyon.",
    "whyThisSpot_zh": "一个视觉上令人惊叹的时间胶囊，非常适合历史爱好者和美食爱好者，距离里昂仅一小段路程。",
    "whyThisSpot_fr": "Une capsule temporelle visuellement époustouflante, idéale pour les passionnés d'histoire et les gourmands, à quelques minutes de Lyon.",
    "whyThisSpot_de": "Eine visuell atemberaubende Zeitkapsel, die perfekt für Geschichtsinteressierte und Feinschmecker gleichermaßen ist, nur einen kurzen Ausflug von Lyon entfernt.",
    "whyThisSpot_nl": "Een visueel verbluffende tijdcapsule perfect voor zowel geschiedenisliefhebbers als fijnproevers, op slechts een kort ritje van Lyon."
  },
  "lyn_lyon_42": {
    "desc_en": "A sprawling 117-hectare urban oasis in the heart of Lyon, featuring France's largest public park, a free botanical garden, a vast boating lake, and a completely free zoo.",
    "desc_ja": "リヨンの中心部にある広さ117ヘクタールの都会のオアシス。フランス最大の公共公園、無料の植物園、広大なボート湖、完全無料の動物園があります。",
    "desc_es": "Un extenso oasis urbano de 117 hectáreas en el corazón de Lyon, que cuenta con el parque público más grande de Francia, un jardín botánico gratuito, un gran lago para botes y un zoológico completamente gratuito.",
    "desc_zh": "里昂市中心一片广阔的 117 公顷城市绿洲，这里有法国最大的公园、免费的植物园、宽阔的划船湖和完全免费的动物园。",
    "desc_fr": "Une vaste oasis urbaine de 117 hectares au cœur de Lyon, comprenant le plus grand parc public de France, un jardin botanique gratuit, un grand lac de plaisance et un zoo entièrement gratuit.",
    "desc_de": "Eine weitläufige 117 Hektar große städtische Oase im Herzen von Lyon, mit Frankreichs größtem öffentlichem Park, einem kostenlosen botanischen Garten, einem riesigen Bootssee und einem komplett kostenlosen Zoo.",
    "desc_nl": "Een uitgestrekte stedelijke oase van 117 hectare in het hart van Lyon, met het grootste openbare park van Frankrijk, een gratis botanische tuin, een groot roeivijver en een volledig gratis dierentuin.",
    
    "tip_en": "Rent a 'rosalie' (multi-person pedal car) to explore the extensive grounds efficiently, and don't miss the African Plain exhibit in the zoo where giraffes roam freely.",
    "tip_ja": "広大な敷地を効率的に探索するには「ロザリー」（多人数用ペダルカー）をレンタルしてください。動物園のアフリカ平原の展示ではキリンが自由に歩き回っており必見です。",
    "tip_es": "Alquila un 'rosalie' (coche a pedales para varias personas) para explorar los extensos terrenos de manera eficiente, y no te pierdas la exhibición de la Llanura Africana en el zoológico donde las jirafas deambulan libremente.",
    "tip_zh": "租一辆“rosalie”（多人脚踏车）即可高效游览广阔的庭院，千万不要错过动物园里的非洲平原展区，那里有长颈鹿在自由漫步。",
    "tip_fr": "Louez une 'rosalie' (voiture à pédales multi-places) pour explorer efficacement les vastes étendues, et ne manquez pas l'exposition de la Plaine Africaine dans le zoo où les girafes errent en liberté.",
    "tip_de": "Mieten Sie ein 'Rosalie' (Mehrpersonen-Tretauto), um das weitläufige Gelände effizient zu erkunden, und verpassen Sie nicht die Ausstellung der afrikanischen Ebene im Zoo, wo Giraffen frei herumlaufen.",
    "tip_nl": "Huur een 'rosalie' (meerpersoons trapauto) om het uitgestrekte terrein efficiënt te verkennen, en mis de Afrikaanse Vlakte-expositie in de dierentuin niet, waar giraffen vrij rondlopen.",

    "whyThisSpot_en": "The absolute best free family activity in Lyon, offering endless outdoor entertainment for all ages.",
    "whyThisSpot_ja": "リヨンで絶対に最高の無料ファミリーアクティビティ。すべての年齢層に無限のアウトドアエンターテイメントを提供します。",
    "whyThisSpot_es": "La mejor actividad familiar gratuita absoluta en Lyon, que ofrece entretenimiento al aire libre sin fin para todas las edades.",
    "whyThisSpot_zh": "里昂绝对最佳的免费家庭活动，为所有年龄段的人提供无尽的户外娱乐。",
    "whyThisSpot_fr": "La meilleure activité familiale gratuite de Lyon, offrant des divertissements en plein air sans fin pour tous les âges.",
    "whyThisSpot_de": "Die absolut beste kostenlose Familienaktivität in Lyon, die endlose Outdoor-Unterhaltung für alle Altersgruppen bietet.",
    "whyThisSpot_nl": "De absoluut beste gratis familieactiviteit in Lyon, met eindeloos buitenvermaak voor alle leeftijden."
  },
  "lyn_lyon_44": {
    "desc_en": "An immersive riverside aquarium housing over 5,000 diverse marine creatures across 47 tanks, featuring thrilling shark encounters and interactive touch pools.",
    "desc_ja": "47 の水槽に 5,000 匹を超える多様な海の生き物が飼育されている没入型の川沿いの水族館。スリル満点のサメとの遭遇やインタラクティブなタッチ プールが特徴です。",
    "desc_es": "Un acuario inmersivo junto al río que alberga a más de 5.000 diversas criaturas marinas en 47 tanques, que cuenta con emocionantes encuentros con tiburones y piscinas táctiles interactivas.",
    "desc_zh": "一个沉浸式河滨水族馆，在 47 个水族箱中饲养着 5000 多种海洋生物，特色是惊险的鲨鱼遭遇战和互动触摸池。",
    "desc_fr": "Un aquarium immersif en bord de rivière abritant plus de 5 000 créatures marines diverses réparties dans 47 bassins, avec des rencontres palpitantes avec des requins et des bassins tactiles interactifs.",
    "desc_de": "Ein immersives Aquarium am Flussufer, das über 5.000 verschiedene Meereslebewesen in 47 Becken beherbergt, mit aufregenden Hai-Begegnungen und interaktiven Tastbecken.",
    "desc_nl": "Een meeslepend aquarium aan de rivier dat meer dan 5.000 verschillende zeedieren in 47 aquaria huisvest, met spannende haaienontmoetingen en interactieve aanraakbaden.",
    
    "tip_en": "Time your visit with the daily feeding sessions (especially the sharks) for maximum excitement. It's fully air-conditioned, making it perfect for hot summer days.",
    "tip_ja": "最大限の興奮を得るために、毎日の餌やりセッション（特にサメ）に合わせて訪問のタイミングを合わせてください。完全冷暖房完備で暑い夏の日にも最適です。",
    "tip_es": "Calcula tu visita con las sesiones de alimentación diarias (especialmente los tiburones) para obtener la máxima emoción. Está totalmente climatizado, por lo que es perfecto para los calurosos días de verano.",
    "tip_zh": "在每天的喂食时间（尤其是鲨鱼）去参观，可以体验最大的刺激。里面有充足的空调，非常适合炎热的夏天。",
    "tip_fr": "Faites coïncider votre visite avec les séances de nourrissage quotidiennes (notamment des requins) pour un maximum de sensations fortes. L'espace est entièrement climatisé, idéal pour les chaudes journées d'été.",
    "tip_de": "Planen Sie Ihren Besuch mit den täglichen Fütterungszeiten (insbesondere bei den Haien), um maximale Spannung zu erleben. Es ist voll klimatisiert und daher perfekt für heiße Sommertage.",
    "tip_nl": "Plan uw bezoek tijdens de dagelijkse voedersessies (vooral de haaien) voor maximale opwinding. Het is volledig voorzien van airconditioning, dus perfect voor hete zomerdagen.",

    "whyThisSpot_en": "A fantastic, educational half-day excursion that kids will adore, rain or shine.",
    "whyThisSpot_ja": "晴れでも雨でも子供たちが喜ぶ、素晴らしい教育的な半日旅行。",
    "whyThisSpot_es": "Una fantástica excursión educativa de medio día que a los niños les encantará, llueva o haga sol.",
    "whyThisSpot_zh": "这是一次奇妙的、有教育意义的半日游，无论晴天雨天孩子们都会喜欢。",
    "whyThisSpot_fr": "Une fantastique excursion éducative d'une demi-journée que les enfants vont adorer, qu'il pleuve ou qu'il vente.",
    "whyThisSpot_de": "Ein fantastischer, lehrreicher Halbtagesausflug, den Kinder bei jedem Wetter lieben werden.",
    "whyThisSpot_nl": "Een fantastische, educatieve excursie van een halve dag waar kinderen dol op zullen zijn, weer of geen weer."
  },
  "lyn_lyon_45": {
    "desc_en": "France's largest miniature animated park, bringing Lyon and fantastical worlds to life through incredibly detailed dioramas and thousands of moving figures.",
    "desc_ja": "フランス最大のミニチュアアニメーションパーク。信じられないほど詳細なジオラマと何千もの動くフィギュアを通じて、リヨンと幻想的な世界を生き生きと表現します。",
    "desc_es": "El parque animado en miniatura más grande de Francia, que da vida a Lyon y a mundos fantásticos a través de dioramas increíblemente detallados y miles de figuras en movimiento.",
    "desc_zh": "法国最大的微缩动画公园，通过极其详细的立体模型和成千上万的活动人物，将里昂和奇幻世界带入生活。",
    "desc_fr": "Le plus grand parc animé miniature de France, donnant vie à Lyon et à des mondes fantastiques à travers des dioramas incroyablement détaillés et des milliers de figurines animées.",
    "desc_de": "Frankreichs größter animierter Miniaturpark, der Lyon und fantastische Welten durch unglaublich detaillierte Dioramen und Tausende von beweglichen Figuren zum Leben erweckt.",
    "desc_nl": "Het grootste geanimeerde miniatuurpark van Frankrijk, dat Lyon en fantastische werelden tot leven brengt door middel van ongelooflijk gedetailleerde diorama's en duizenden bewegende figuren.",
    
    "tip_en": "Look closely! Hidden among the beautiful scenery are hilarious Easter eggs, famous movie characters, and a spectacular day-to-night light cycle every 20 minutes.",
    "tip_ja": "よく見てください！美しい景色の間に、面白いイースターエッグ、有名な映画のキャラクター、20分ごとの壮観な昼と夜の光のサイクルが隠されています。",
    "tip_es": "¡Fíjate bien! Escondidos entre los hermosos paisajes hay divertidos huevos de Pascua, famosos personajes de películas y un espectacular ciclo de luz de día y de noche cada 20 minutos.",
    "tip_zh": "仔细看！美丽的风景中隐藏着搞笑的复活节彩蛋、著名的电影人物，以及每 20 分钟一次的壮观昼夜灯光循环。",
    "tip_fr": "Regardez bien ! Cachés parmi les paysages magnifiques se trouvent des clins d'œil hilarants, des personnages de films célèbres et un cycle de lumière jour/nuit spectaculaire toutes les 20 minutes.",
    "tip_de": "Schauen Sie genau hin! Versteckt in der wunderschönen Landschaft sind lustige Easter Eggs, berühmte Filmfiguren und alle 20 Minuten ein spektakulärer Tag-Nacht-Lichtzyklus.",
    "tip_nl": "Kijk goed! Verborgen tussen het prachtige landschap zijn hilarische paaseieren, beroemde filmpersonages en een spectaculaire dag-tot-nacht lichtcyclus elke 20 minuten.",

    "whyThisSpot_en": "A charming and meticulously crafted attraction that delights both adults' inner child and young kids.",
    "whyThisSpot_ja": "大人の遊び心と子供たちの両方を喜ばせる、魅力的で細心の注意を払って作られたアトラクション。",
    "whyThisSpot_es": "Una atracción encantadora y meticulosamente diseñada que hace las delicias tanto del niño interior de los adultos como de los más pequeños.",
    "whyThisSpot_zh": "一个迷人且精心制作的景点，能满足成年人的童心，也让小孩子们高兴。",
    "whyThisSpot_fr": "Une attraction charmante et méticuleusement conçue qui ravit à la fois l'enfant intérieur des adultes et les jeunes enfants.",
    "whyThisSpot_de": "Eine charmante und sorgfältig gestaltete Attraktion, die sowohl das innere Kind von Erwachsenen als auch junge Kinder erfreut.",
    "whyThisSpot_nl": "Een charmante en zorgvuldig vervaardigde attractie die zowel het innerlijke kind van volwassenen als jonge kinderen behaagt."
  },
  "lyn_lyon_46": {
    "desc_en": "A state-of-the-art planetarium featuring immersive 360-degree cosmic projection shows and interactive astronomy exhibits unraveling the mysteries of the universe.",
    "desc_ja": "宇宙の謎を解き明かす没入型の 360 度宇宙投影ショーやインタラクティブな天文学の展示を特徴とする最先端のプラネタリウム。",
    "desc_es": "Un planetario de última generación que presenta espectáculos inmersivos de proyección cósmica de 360 grados y exhibiciones interactivas de astronomía que desentrañan los misterios del universo.",
    "desc_zh": "一座最先进的天象馆，拥有沉浸式 360 度宇宙投影秀和互动天文学展览，带您揭开宇宙的神秘面纱。",
    "desc_fr": "Un planétarium ultramoderne proposant des spectacles de projection cosmique immersifs à 360 degrés et des expositions interactives sur l'astronomie perçant les mystères de l'univers.",
    "desc_de": "Ein hochmodernes Planetarium mit beeindruckenden interaktiven 360-Grad-Projektionsshows über den Kosmos und interaktiven Astronomieausstellungen, die die Geheimnisse des Universums entschlüsseln.",
    "desc_nl": "Een ultramodern planetarium met meeslepende 360-graden kosmische projectieshows en interactieve astronomietentoonstellingen die de mysteries van het universum ontrafelen.",

    "tip_en": "Book tickets in advance online. The spectacular dome shows are generally in French, but audio guides in English are available for most projections.",
    "tip_ja": "事前にオンラインでチケットを予約してください。壮大なドームショーは通常フランス語ですが、ほとんどの投影で英語のオーディオガイドを利用できます。",
    "tip_es": "Reserva las entradas con antelación online. Los espectaculares espectáculos en la cúpula son generalmente en francés, pero hay audioguías en inglés disponibles para la mayoría de las proyecciones.",
    "tip_zh": "请提前在网上订票。壮观的穹顶表演通常是法语，但大多数放映都提供英语语音导览。",
    "tip_fr": "Réservez vos billets à l'avance en ligne. Les spectacles sous le dôme spectaculaires sont généralement en français, mais des audioguides en anglais sont disponibles pour la plupart des projections.",
    "tip_de": "Buchen Sie Tickets im Voraus online. Die spektakulären Kuppelshows sind in der Regel auf Französisch, aber für die meisten Projektionen stehen Audioguides auf Englisch zur Verfügung.",
    "tip_nl": "Boek tickets van tevoren online. De spectaculaire koepelshows zijn over het algemeen in het Frans, maar voor de meeste projecties zijn er audiogidsen in het Engels beschikbaar.",

    "whyThisSpot_en": "An awe-inspiring journey through space and time that makes science accessible and magical for the whole family.",
    "whyThisSpot_ja": "家族全員にとって科学を身近で魔法のようなものにする、時空を超えた畏敬の念を抱かせる旅。",
    "whyThisSpot_es": "Un viaje impresionante a través del espacio y el tiempo que hace que la ciencia sea accesible y mágica para toda la familia.",
    "whyThisSpot_zh": "一段穿越时空、令人敬畏的旅程，让全家人都能以神奇的方式接触科学。",
    "whyThisSpot_fr": "Un voyage impressionnant à travers l'espace et le temps qui rend la science accessible et magique pour toute la famille.",
    "whyThisSpot_de": "Eine ehrfurchtgebietende Reise durch Raum und Zeit, die Wissenschaft für die ganze Familie zugänglich und magisch macht.",
    "whyThisSpot_nl": "Een ontzagwekkende reis door ruimte en tijd die wetenschap toegankelijk en magisch maakt voor het hele gezin."
  },
  "mrs_ma_5": {
    "desc_en": "A mighty 17th-century star-shaped citadel built under Louis XIV, guarding the Old Port of Marseille and offering rich military history alongside panoramic harbor views.",
    "desc_ja": "マルセイユ旧港を守る、ルイ 14 世の時代に建てられた 17 世紀の強大な星型の城塞。豊かな軍事の歴史と港のパノラマの景色を楽しめます。",
    "desc_es": "Una poderosa ciudadela en forma de estrella del siglo XVII construida bajo Luis XIV, que custodia el Puerto Viejo de Marsella y ofrece una rica historia militar junto con vistas panorámicas del puerto.",
    "desc_zh": "这是一座建于路易十四时期，拥有强大 17 世纪星形城堡。它守卫着马赛旧港，不仅承载着丰富的军事历史，还能欣赏到港口的全景。",
    "desc_fr": "Une puissante citadelle en forme d'étoile du XVIIe siècle construite sous Louis XIV, gardant le Vieux-Port de Marseille et offrant une riche histoire militaire ainsi qu'une vue panoramique sur le port.",
    "desc_de": "Eine mächtige sternförmige Zitadelle aus dem 17. Jahrhundert, erbaut unter Ludwig XIV., die den Alten Hafen von Marseille bewacht und reiche Militärgeschichte sowie einen Panoramablick auf den Hafen bietet.",
    "desc_nl": "Een machtige 17e-eeuwse stervormige citadel gebouwd onder Lodewijk XIV, die de oude haven van Marseille bewaakt en een rijke militaire geschiedenis biedt naast een panoramisch uitzicht op de haven.",

    "tip_en": "Parts of the fort are still an active military base, but public areas occasionally open for tours. The exterior grounds provide unbeatable sunset photo opportunities of the harbor.",
    "tip_ja": "要塞の一部は現在も軍事基地として使用されていますが、公共エリアは時折ツアーのために公開されます。外の敷地からは、港の最高の夕日の写真を撮ることができます。",
    "tip_es": "Partes de la fortaleza siguen siendo una base militar activa, pero las áreas públicas a veces se abren para visitas. Los terrenos exteriores ofrecen oportunidades inmejorables para tomar fotos del puerto al atardecer.",
    "tip_zh": "堡垒的某些部分仍然是现役军事基地，但公共区域偶尔会开放参观。堡垒外部区域提供了拍摄港口日落绝佳照片的完美地点。",
    "tip_fr": "Une partie du fort est toujours une base militaire active, mais les espaces publics s'ouvrent parfois aux visites. Les terrains extérieurs offrent des opportunités imbattables de photos du coucher de soleil sur le port.",
    "tip_de": "Teile der Festung sind immer noch ein aktiver Militärstützpunkt, aber öffentliche Bereiche werden gelegentlich für Touren geöffnet. Das Außengelände bietet unschlagbare Möglichkeiten für Fotos des Hafens bei Sonnenuntergang.",
    "tip_nl": "Delen van het fort zijn nog steeds een actieve militaire basis, maar openbare ruimtes zijn af en toe geopend voor rondleidingen. Het buitenterrein biedt onverslaanbare fotomomenten van de haven bij zonsondergang.",

    "whyThisSpot_en": "An iconic symbol of Marseille's strategic maritime past with the best vantage point over the Old Port.",
    "whyThisSpot_ja": "マルセイユの戦略的海洋の過去の象徴であり、旧港を一望できる最高の視点です。",
    "whyThisSpot_es": "Un símbolo icónico del pasado marítimo estratégico de Marsella con el mejor punto de vista sobre el Puerto Viejo.",
    "whyThisSpot_zh": "这是马赛战略性海洋历史的标志性象征，拥有俯瞰旧港的最佳视角。",
    "whyThisSpot_fr": "Un symbole emblématique du passé maritime stratégique de Marseille avec le meilleur point de vue sur le Vieux-Port.",
    "whyThisSpot_de": "Ein ikonisches Symbol für Marseilles strategische maritime Vergangenheit mit dem besten Aussichtspunkt über den Alten Hafen.",
    "whyThisSpot_nl": "Een iconisch symbool van het strategische maritieme verleden van Marseille met het beste uitkijkpunt over de oude haven."
  },
  "mrs_ma_9": {
    "desc_en": "The legendary, undulating home stadium of Olympique de Marseille, offering an electrifying atmosphere for football fans and fascinating behind-the-scenes stadium tours.",
    "desc_ja": "オリンピック・マルセイユの伝説的な波打つホームスタジアム。サッカーファンに刺激的な雰囲気と、魅力的な舞台裏のスタジアムツアーを提供しています。",
    "desc_es": "El legendario y ondulante estadio del Olympique de Marsella, que ofrece un ambiente electrizante para los aficionados al fútbol y fascinantes visitas guiadas entre bastidores del estadio.",
    "desc_zh": "奥林匹克马赛队传奇且起伏的主体育场，为足球迷提供令人兴奋的氛围以及引人入胜的幕后体育场之旅。",
    "desc_fr": "Le stade légendaire et ondulant de l'Olympique de Marseille, offrant une atmosphère électrisante aux fans de football et des visites fascinantes des coulisses du stade.",
    "desc_de": "Das legendäre, wellenförmige Heimstadion von Olympique Marseille bietet Fußballfans eine elektrisierende Atmosphäre und faszinierende Stadionführungen hinter die Kulissen.",
    "desc_nl": "Het legendarische, golvende thuisstadion van Olympique de Marseille, met een opwindende sfeer voor voetbalfans en fascinerende stadionrondleidingen achter de schermen.",

    "tip_en": "Book the guided tour to access the players' locker rooms and walk out through the tunnel to the pitch. Attending a live match here is a fiery, unforgettable experience.",
    "tip_ja": "ガイド付きツアーを予約して、選手たちのロッカールームにアクセスし、トンネルを抜けてピッチに出ましょう。ここでライブ試合を観戦することは、熱烈で忘れられない体験です。",
    "tip_es": "Reserva la visita guiada para acceder a los vestuarios de los jugadores y salir por el túnel al campo. Asistir a un partido en vivo aquí es una experiencia apasionante e inolvidable.",
    "tip_zh": "预订导览服务，进入球员更衣室，并穿过通道走到球场。在这里观看现场比赛将是一次激动人心、令人难忘的体验。",
    "tip_fr": "Réservez la visite guidée pour accéder aux vestiaires des joueurs et emprunter le tunnel jusqu'au terrain. Assister à un match en direct ici est une expérience enflammée et inoubliable.",
    "tip_de": "Buchen Sie die Führung, um Zugang zu den Umkleidekabinen der Spieler zu erhalten und durch den Tunnel zum Spielfeld hinauszugehen. Ein Live-Spiel hier zu besuchen, ist ein feuriges, unvergessliches Erlebnis.",
    "tip_nl": "Boek de rondleiding om toegang te krijgen tot de kleedkamers van de spelers en loop door de tunnel het veld op. Een live wedstrijd bijwonen is hier een vurige, onvergetelijke ervaring.",

    "whyThisSpot_en": "A temple of modern sports culture where the passionate heartbeat of Marseille is felt most strongly.",
    "whyThisSpot_ja": "マルセイユの情熱的な鼓動が最も強く感じられる近代スポーツ文化の殿堂。",
    "whyThisSpot_es": "Un templo de la cultura deportiva moderna donde se siente con más fuerza el latido apasionado de Marsella.",
    "whyThisSpot_zh": "一座现代体育文化殿堂，在这里可以最强烈地感受到马赛热情的心跳。",
    "whyThisSpot_fr": "Un temple de la culture sportive moderne où le cœur passionné de Marseille se fait le plus ressentir.",
    "whyThisSpot_de": "Ein Tempel der modernen Sportkultur, wo der leidenschaftliche Herzschlag von Marseille am stärksten zu spüren ist.",
    "whyThisSpot_nl": "Een tempel van de moderne sportcultuur waar de hartstochtelijke hartslag van Marseille het sterkst te voelen is."
  },
  "mrs_ma_10": {
    "desc_en": "A formidable island fortress turned infamous prison, immortalized by Alexandre Dumas in 'The Count of Monte Cristo', set dramatically in the Mediterranean Sea.",
    "desc_ja": "地中海に劇的に位置する、「モンテ・クリスト伯」でアレクサンドル・デュマによって不朽の名声を与えられた、悪名高い監獄となった恐るべき島の要塞。",
    "desc_es": "Una formidable fortaleza isleña convertida en prisión infame, inmortalizada por Alejandro Dumas en 'El conde de Montecristo', situada espectacularmente en el mar Mediterráneo.",
    "desc_zh": "一座坚不可摧的岛屿堡垒变成了臭名昭著的监狱，因大仲马的《基督山伯爵》而不朽，戏剧性地坐落在地中海上。",
    "desc_fr": "Une formidable forteresse insulaire devenue une prison infâme, immortalisée par Alexandre Dumas dans « Le Comte de Monte-Cristo », située de manière spectaculaire dans la mer Méditerranée.",
    "desc_de": "Eine gewaltige Inselfestung, die zu einem berüchtigten Gefängnis wurde und von Alexandre Dumas in 'Der Graf von Monte Christo' unsterblich gemacht wurde, in dramatischer Lage im Mittelmeer.",
    "desc_nl": "Een formidabel eilandfort dat een beruchte gevangenis werd, onsterfelijk gemaakt door Alexandre Dumas in 'De graaf van Monte Cristo', dramatisch gelegen in de Middellandse Zee.",

    "tip_en": "Take the Frioul If Express ferry from the Old Port. Book online in advance, as boats fill up quickly in summer. Strong winds (Mistral) can sometimes cancel the crossings.",
    "tip_ja": "旧港から Frioul If Express フェリーをご利用ください。夏は船がすぐに満席になるので、オンラインで事前に予約してください。強風（ミストラル）により運航がキャンセルされる場合があります。",
    "tip_es": "Toma el ferry Frioul If Express desde el Puerto Viejo. Reserva en línea con antelación, ya que los barcos se llenan rápidamente en verano. Los vientos fuertes (Mistral) a veces pueden cancelar los cruces.",
    "tip_zh": "从旧港乘坐 Frioul If Express 渡轮。由于夏季船只很快客满，请提前在线预订。强风 (Mistral) 有时会导致航班取消。",
    "tip_fr": "Prenez le ferry Frioul If Express depuis le Vieux-Port. Réservez en ligne à l'avance, car les bateaux se remplissent vite en été. Des vents forts (Mistral) peuvent parfois annuler les traversées.",
    "tip_de": "Nehmen Sie die Fähre Frioul If Express vom Alten Hafen. Buchen Sie im Voraus online, da die Boote im Sommer schnell ausgebucht sind. Starke Winde (Mistral) können die Überfahrten manchmal ausfallen lassen.",
    "tip_nl": "Neem de Frioul If Express-veerboot vanuit de oude haven. Boek vooraf online, want in de zomer zijn de boten snel vol. Harde wind (Mistral) kan de overtochten soms annuleren.",

    "whyThisSpot_en": "It masterfully blends dramatic literary fiction with dark Renaissance history amidst stunning coastal scenery.",
    "whyThisSpot_ja": "ドラマチックな文学的フィクションとルネッサンスの暗い歴史、素晴らしい海岸の景色が見事に調和しています。",
    "whyThisSpot_es": "Combina magistralmente la ficción literaria dramática con la oscura historia del Renacimiento en medio de impresionantes paisajes costeros.",
    "whyThisSpot_zh": "它巧妙地将戏剧性的文学小说与黑暗的文艺复兴历史以及令人惊叹的海岸风光融为一体。",
    "whyThisSpot_fr": "Il mélange magistralement la fiction littéraire dramatique à la sombre histoire de la Renaissance au milieu de paysages côtiers époustouflants.",
    "whyThisSpot_de": "Es mischt meisterhaft dramatische literarische Fiktion mit dunkler Renaissance-Geschichte inmitten einer atemberaubenden Küstenkulisse.",
    "whyThisSpot_nl": "Het combineert meesterlijk dramatische literaire fictie met duistere renaissancistische geschiedenis te midden van een prachtig kustlandschap."
  },
  "mrs_ma_14": {
    "desc_en": "A comprehensive history museum preserving 26 centuries of Marseille's past, directly adjoined by an open-air archaeological park displaying ancient Greek port ruins.",
    "desc_ja": "マルセイユの 26 世紀にわたる過去を保存する総合歴史博物館。古代ギリシャの港の遺跡を展示する野外考古学公園に隣接しています。",
    "desc_es": "Un museo de historia integral que conserva 26 siglos del pasado de Marsella, contiguo directamente por un parque arqueológico al aire libre que exhibe las ruinas de un antiguo puerto griego.",
    "desc_zh": "一座全面保存马赛 26 个世纪历史的综合博物馆，直接毗邻一个露天考古公园，展示着古希腊港口的遗址。",
    "desc_fr": "Un musée d'histoire complet retraçant 26 siècles du passé de Marseille, jouxtant directement un parc archéologique en plein air exposant les ruines d'un ancien port grec.",
    "desc_de": "Ein umfassendes Geschichtsmuseum, das 26 Jahrhunderte von Marseilles Vergangenheit bewahrt, direkt neben einem archäologischen Freiluftpark, der antike griechische Hafenruinen zeigt.",
    "desc_nl": "Een uitgebreid historisch museum dat 26 eeuwen van het verleden van Marseille bewaart, direct grenzend aan een archeologisch openluchtpark met oude Griekse havenruïnes.",

    "tip_en": "Start with the impressive ancient Greek hull inside, then take a peaceful walk through the outdoor Jardin des Vestiges right in the center of a modern shopping district.",
    "tip_ja": "内部の印象的な古代ギリシャの船体から始まり、近代的なショッピング街の中心にある屋外のジャルダン デ ヴェスティージュ (遺跡の庭園) を静かに散歩しましょう。",
    "tip_es": "Comienza con el impresionante casco griego antiguo en el interior, luego da un tranquilo paseo por el Jardin des Vestiges al aire libre justo en el centro de un moderno distrito comercial.",
    "tip_zh": "从室内令人印象深刻的古希腊船体开始参观，然后在这个地处现代购物中心内的户外遗迹花园 (Jardin des Vestiges) 中宁静漫步。",
    "tip_fr": "Commencez par admirer l'impressionnante coque d'un navire grec antique à l'intérieur, puis promenez-vous paisiblement dans le Jardin des Vestiges en plein air, situé en plein cœur d'un quartier commerçant moderne.",
    "tip_de": "Beginnen Sie mit dem beeindruckenden antiken griechischen Schiffsrumpf im Inneren und machen Sie dann einen ruhigen Spaziergang durch den Jardin des Vestiges im Freien, direkt im Zentrum eines modernen Einkaufsviertels.",
    "tip_nl": "Begin met de indrukwekkende oude Griekse romp binnen en maak daarna een rustige wandeling door de Jardin des Vestiges in de openlucht, midden in een modern winkelgebied.",

    "whyThisSpot_en": "A brilliant contrast between the bustling modern city and its deep ancient roots as Massalia.",
    "whyThisSpot_ja": "賑やかな近代都市と、マッサリアとしての深く古代のルーツとの見事なコントラスト。",
    "whyThisSpot_es": "Un brillante contraste entre la bulliciosa ciudad moderna y sus profundas raíces antiguas como Massalia.",
    "whyThisSpot_zh": "繁华的现代城市与其作为马萨利亚的深厚古代根源之间的鲜明对比。",
    "whyThisSpot_fr": "Un contraste saisissant entre la ville moderne animée et ses profondes racines antiques de Massalia.",
    "whyThisSpot_de": "Ein brillanter Kontrast zwischen der pulsierenden modernen Stadt und ihren tiefen antiken Wurzeln als Massalia.",
    "whyThisSpot_nl": "Een briljant contrast tussen de bruisende moderne stad en zijn diepe oude wortels als Massalia."
  },
  "mrs_ma_15": {
    "desc_en": "Housed in the magnificent Palais Longchamp, this prestigious fine arts museum displays a stellar collection of European paintings and sculptures from the 16th to 19th centuries.",
    "desc_ja": "壮大なロンシャン宮殿内にあるこの権威ある美術館には、16 世紀から 19 世紀のヨーロッパの絵画や彫刻の素晴らしいコレクションが展示されています。",
    "desc_es": "Ubicado en el magnífico Palais Longchamp, este prestigioso museo de bellas artes exhibe una colección estelar de pinturas y esculturas europeas del siglo XVI al XIX.",
    "desc_zh": "这座享有盛誉的艺术博物馆位于宏伟的隆尚宫内，展示了 16 至 19 世纪欧洲绘画和雕塑的一流藏品。",
    "desc_fr": "Installé dans le magnifique Palais Longchamp, ce prestigieux musée des beaux-arts abrite une collection exceptionnelle de peintures et de sculptures européennes du XVIe au XIXe siècle.",
    "desc_de": "Dieses prestigeträchtige Museum der schönen Künste ist im prächtigen Palais Longchamp untergebracht und zeigt eine herausragende Sammlung europäischer Gemälde und Skulpturen vom 16. bis zum 19. Jahrhundert.",
    "desc_nl": "Dit prestigieuze museum voor schone kunsten is gehuisvest in het magnifieke Palais Longchamp en toont een uitstekende collectie Europese schilderijen en sculpturen uit de 16e tot de 19e eeuw.",

    "tip_en": "The museum is stunning, but don't miss exploring the grandiose fountains and park of the Palais Longchamp outside—arguably Marseille's most photogenic monument.",
    "tip_ja": "博物館は見事ですが、外の壮大な噴水とロンシャン宮殿の公園を散策することをお見逃しなく。間違いなくマルセイユで最も写真映えする記念碑です。",
    "tip_es": "El museo es impresionante, pero no te pierdas explorar las grandiosas fuentes y el parque del Palais Longchamp en el exterior, posiblemente el monumento más fotogénico de Marsella.",
    "tip_zh": "博物馆本身令人惊叹，但也不要错过探索外部宏伟的喷泉和隆尚宫公园——这可以说是马赛最上镜的纪念碑。",
    "tip_fr": "Le musée est magnifique, mais ne manquez pas d'explorer les fontaines grandioses et le parc du Palais Longchamp à l'extérieur, sans doute le monument le plus photogénique de Marseille.",
    "tip_de": "Das Museum ist atemberaubend, aber verpassen Sie nicht, die grandiosen Brunnen und den Park des Palais Longchamp draußen zu erkunden – wohl das fotogenste Denkmal von Marseille.",
    "tip_nl": "Het museum is prachtig, maar vergeet niet de grandioze fonteinen en het park van het Palais Longchamp buiten te verkennen - ongetwijfeld het meest fotogenieke monument van Marseille.",

    "whyThisSpot_en": "It combines world-class art appreciation with some of the most breathtaking palatial architecture in Southern France.",
    "whyThisSpot_ja": "世界クラスの芸術鑑賞と、南フランスで最も息をのむような宮殿建築のいくつかを組み合わせています。",
    "whyThisSpot_es": "Combina la apreciación del arte de clase mundial con una de las arquitecturas palaciegas más impresionantes del sur de Francia.",
    "whyThisSpot_zh": "它将世界一流的艺术欣赏与法国南部一些最令人惊叹的宫殿建筑结合在一起。",
    "whyThisSpot_fr": "Il allie une appréciation de l'art de classe mondiale à l'une des architectures palatiales les plus époustouflantes du sud de la France.",
    "whyThisSpot_de": "Es kombiniert erstklassige Kunstbetrachtung mit einigen der atemberaubendsten Palastarchitekturen in Südfrankreich.",
    "whyThisSpot_nl": "Het combineert de waardering van kunst van wereldklasse met een van de meest adembenemende paleisarchitectuur in Zuid-Frankrijk."
  }
}

for item in data:
    spot_id = item['spot']['id']
    if spot_id in updates:
        for k, v in updates[spot_id].items():
            item['spot'][k] = v

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Done writing to", output_file)
