import json
import os

input_file = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_chunk_4.json'
output_file = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_written_4.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Master texts for the 21 spots
updates = {
  "lyn_lyon_18": {
    "desc_en": "Descend into history at this underground archaeological museum seamlessly built into the Fourvière hillside, preserving magnificent Roman relics alongside the iconic ancient theatres.",
    "desc_ja": "フルヴィエールの丘の中腹にシームレスに組み込まれたこの地下考古学博物館で歴史を感じてください。象徴的な古代劇場とともに壮大なローマの遺物が保存されています。",
    "desc_es": "Desciende a la historia en este museo arqueológico subterráneo construido a la perfección en la ladera de Fourvière, conservando magníficas reliquias romanas junto a los antiguos teatros.",
    "desc_zh": "在这个无缝建在富维耶山坡上的地下考古博物馆中感受历史，在标志性的古剧院旁保存着宏伟的罗马遗迹。",
    "desc_fr": "Plongez dans l'histoire dans ce musée archéologique souterrain parfaitement intégré à la colline de Fourvière, préservant de magnifiques vestiges romains aux côtés des anciens théâtres emblématiques.",
    "desc_de": "Tauchen Sie in diesem unterirdischen archäologischen Museum, das nahtlos in den Hügel Fourvière integriert ist, in die Geschichte ein und bewahren Sie prächtige römische Relikte neben den berühmten antiken Theatern.",
    "desc_nl": "Daal af in de geschiedenis in dit ondergrondse archeologische museum dat naadloos is ingebouwd in de heuvel Fourvière, waar prachtige Romeinse relikwieën worden bewaard naast de iconische oude theaters.",
    
    "tip_en": "Don't miss the stunning mosaic floors and the large window offering a unique perspective of the Roman theatre outside.",
    "tip_ja": "見事なモザイクの床と、外のローマ劇場のユニークな視点を提供する大きな窓をお見逃しなく。",
    "tip_es": "No te pierdas los impresionantes suelos de mosaico y el gran ventanal que ofrece una perspectiva única del teatro romano exterior.",
    "tip_zh": "千万不要错过令人惊叹的马赛克地板和大窗户，大窗户提供了欣赏室外罗马剧院的独特视角。",
    "tip_fr": "Ne manquez pas les superbes sols en mosaïque et la grande fenêtre offrant une perspective unique sur le théâtre romain à l'extérieur.",
    "tip_de": "Verpassen Sie nicht die atemberaubenden Mosaikböden und das große Fenster, das eine einzigartige Perspektive auf das römische Theater draußen bietet.",
    "tip_nl": "Mis de prachtige mozaïekvloeren en het grote raam dat een uniek perspectief biedt op het Romeinse theater buiten niet.",

    "whyThisSpot_en": "A brilliantly designed museum that blends architecture with history, offering a deep dive into Lyon's Roman foundation.",
    "whyThisSpot_ja": "建築と歴史が融合した見事にデザインされた博物館で、リヨンのローマ時代の基礎を深く知ることができます。",
    "whyThisSpot_es": "Un museo brillantemente diseñado que combina la arquitectura con la historia, ofreciendo una inmersión profunda en la fundación romana de Lyon.",
    "whyThisSpot_zh": "这是一座设计精美的博物馆，将建筑与历史完美融合，深入了解里昂的罗马基础。",
    "whyThisSpot_fr": "Un musée brillamment conçu qui allie architecture et histoire, offrant une plongée profonde dans la fondation romaine de Lyon.",
    "whyThisSpot_de": "Ein brillant gestaltetes Museum, das Architektur mit Geschichte verbindet und einen tiefen Einblick in die römische Gründung Lyons bietet.",
    "whyThisSpot_nl": "Een briljant ontworpen museum dat architectuur en geschiedenis combineert en een diepe duik biedt in de Romeinse fundamenten van Lyon."
  },
  "lyn_lyon_19": {
    "desc_en": "A deeply moving museum housed in the former Gestapo headquarters, powerfully honoring Lyon's critical role as the Capital of the French Resistance during WWII.",
    "desc_ja": "旧ゲシュタポ本部に収容された非常に感動的な博物館。第二次世界大戦中のフランスのレジスタンスの中心地としてのリヨンの重要な役割を強力に称えています。",
    "desc_es": "Un museo profundamente conmovedor ubicado en la antigua sede de la Gestapo, que rinde un poderoso homenaje al papel fundamental de Lyon como capital de la Resistencia francesa durante la Segunda Guerra Mundial.",
    "desc_zh": "一座设在前盖世太保总部内非常感人的博物馆，有力地纪念了里昂在二战期间作为法国抵抗运动之都的关键作用。",
    "desc_fr": "Un musée profondément émouvant installé dans l'ancien siège de la Gestapo, honorant avec force le rôle essentiel de Lyon en tant que capitale de la Résistance française pendant la Seconde Guerre mondiale.",
    "desc_de": "Ein zutiefst bewegendes Museum im ehemaligen Gestapo-Hauptquartier, das Lyons entscheidende Rolle als Hauptstadt der französischen Résistance im Zweiten Weltkrieg eindrucksvoll würdigt.",
    "desc_nl": "Een diep ontroerend museum gevestigd in het voormalige hoofdkwartier van de Gestapo, dat op indrukwekkende wijze de cruciale rol van Lyon als hoofdstad van de Franse Resistance tijdens de Tweede Wereldoorlog eert.",
    
    "tip_en": "The audio guide is highly recommended to fully grasp the emotional and historical weight of the personal testimonies exhibited.",
    "tip_ja": "展示されている個人的な証言の感情的および歴史的な重みを完全に理解するために、オーディオガイドを強くお勧めします。",
    "tip_es": "La audioguía es muy recomendable para comprender plenamente el peso emocional e histórico de los testimonios personales exhibidos.",
    "tip_zh": "强烈推荐使用音频指南，以充分理解展出的个人证词的情感和历史分量。",
    "tip_fr": "L'audioguide est fortement recommandé pour saisir toute la charge émotionnelle et historique des témoignages personnels exposés.",
    "tip_de": "Der Audioguide ist sehr zu empfehlen, um das emotionale und historische Gewicht der ausgestellten persönlichen Zeugnisse vollständig zu erfassen.",
    "tip_nl": "De audiogids is een echte aanrader om de emotioneele en historische lading van de tentoongestelde persoonlijke getuigenissen volledig te begrijpen.",
    
    "whyThisSpot_en": "Essential for understanding Lyon's resilient spirit and its profound modern history.",
    "whyThisSpot_ja": "リヨンの回復力のある精神とその深遠な現代史を理解するために不可欠です。",
    "whyThisSpot_es": "Esencial para comprender el espíritu resistente de Lyon y su profunda historia moderna.",
    "whyThisSpot_zh": "对于了解里昂坚韧的精神及其深厚的现代历史至关重要。",
    "whyThisSpot_fr": "Essentiel pour comprendre l'esprit de résilience de Lyon et sa profonde histoire moderne.",
    "whyThisSpot_de": "Unerlässlich für das Verständnis von Lyons widerstandsfähigem Geist und seiner tiefgreifenden modernen Geschichte.",
    "whyThisSpot_nl": "Essentieel voor het begrijpen van de veerkrachtige geest van Lyon en zijn diepgaande moderne geschiedenis."
  },
  "lyn_lyon_22": {
    "desc_en": "An exciting aviation museum in Corbas maintained by passionate volunteers, displaying a spectacular array of vintage military aircraft, jets, and historic engines.",
    "desc_ja": "情熱的なボランティアによって維持されているコルバスのエキサイティングな航空博物館。ビンテージの軍用機、ジェット機、歴史的なエンジンの壮大な配列が展示されています。",
    "desc_es": "Un emocionante museo de aviación en Corbas mantenido por apasionados voluntarios, que exhibe una espectacular variedad de aviones militares antiguos, jets y motores históricos.",
    "desc_zh": "由热情的志愿者维护的科尔巴斯令人兴奋的航空博物馆，展示了一系列壮观的老式军用飞机、喷气式飞机和历史悠久的发动机。",
    "desc_fr": "Un musée de l'aviation passionnant à Corbas, entretenu par des bénévoles passionnés, exposant une gamme spectaculaire d'avions militaires d'époque, de jets et de moteurs historiques.",
    "desc_de": "Ein spannendes Luftfahrtmuseum in Corbas, das von leidenschaftlichen Freiwilligen gepflegt wird und eine spektakuläre Auswahl an historischen Militärflugzeugen, Jets und historischen Triebwerken zeigt.",
    "desc_nl": "Een boeiend luchtvaartmuseum in Corbas dat wordt onderhouden door gepassioneerde vrijwilligers en een spectaculaire reeks vintage militaire vliegtuigen, straaljagers en historische motoren tentoonstelt.",
    
    "tip_en": "Guided tours are often given by retired pilots whose personal anecdotes make the exhibits come alive. A truly hidden gem for aviation enthusiasts.",
    "tip_ja": "ガイド付きツアーは退役パイロットによって行われることが多く、彼らの個人的な逸話が展示品に命を吹き込みます。航空愛好家にとって本当に隠れた宝石です。",
    "tip_es": "Las visitas guiadas suelen estar a cargo de pilotos jubilados cuyas anécdotas personales dan vida a las exhibiciones. Una verdadera joya escondida para los entusiastas de la aviación.",
    "tip_zh": "导游通常由退役飞行员担任，他们的个人轶事使展品栩栩如生。对于航空爱好者来说，这里是一个真正隐藏的宝石。",
    "tip_fr": "Les visites guidées sont souvent assurées par des pilotes à la retraite dont les anecdotes personnelles font vivre les expositions. Un véritable joyau caché pour les passionnés d'aviation.",
    "tip_de": "Führungen werden oft von pensionierten Piloten durchgeführt, deren persönliche Anekdoten die Exponate zum Leben erwecken. Ein wahrer Geheimtipp für Luftfahrtbegeisterte.",
    "tip_nl": "Rondleidingen worden vaak gegeven door gepensioneerde piloten wier persoonlijke anekdotes de tentoonstellingen tot leven brengen. Een echt verborgen juweeltje voor luchtvaartliefhebbers.",
    
    "whyThisSpot_en": "Offers an up-close, authentic look at aviation history thanks to the dedication of its volunteer staff.",
    "whyThisSpot_ja": "ボランティアスタッフの献身的な取り組みにより、航空の歴史を間近で本格的に見ることができます。",
    "whyThisSpot_es": "Ofrece una mirada cercana y auténtica a la historia de la aviación gracias a la dedicación de su personal voluntario.",
    "whyThisSpot_zh": "由于志愿者工作人员的奉献，这里提供了一个近距离、真实地了解航空历史的机会。",
    "whyThisSpot_fr": "Offre un regard authentique et de près sur l'histoire de l'aviation grâce au dévouement de son personnel bénévole.",
    "whyThisSpot_de": "Bietet dank des Engagements der ehrenamtlichen Mitarbeiter einen hautnahen und authentischen Einblick in die Geschichte der Luftfahrt.",
    "whyThisSpot_nl": "Biedt een authentieke blik van dichtbij op de geschiedenis van de luchtvaart dankzij de toewijding van de vrijwilligers."
  },
  "lyn_lyon_23": {
    "desc_en": "The ultimate temple of Lyonnaise gastronomy, a vibrant indoor market featuring premium gourmet stalls selling legendary Saint-Marcellin cheese, artisanal charcuterie, and fresh oysters.",
    "desc_ja": "リヨンの美食の究極の殿堂。伝説のサン マルセラン チーズ、職人技のシャルキュトリー、新鮮なカキを販売する高級グルメ屋台が並ぶ活気ある屋内市場です。",
    "desc_es": "El templo definitivo de la gastronomía lionesa, un animado mercado interior con puestos gourmet de primera calidad que venden el legendario queso Saint-Marcellin, charcutería artesanal y ostras frescas.",
    "desc_zh": "里昂美食的终极殿堂，一个充满活力的室内市场，设有出售传奇圣马塞兰奶酪、手工熟食和新鲜牡蛎的高级美食摊位。",
    "desc_fr": "Le temple absolu de la gastronomie lyonnaise, un marché couvert animé proposant des stands gastronomiques haut de gamme vendant du légendaire fromage Saint-Marcellin, de la charcuterie artisanale et des huîtres fraîches.",
    "desc_de": "Der ultimative Tempel der Lyoner Gastronomie, ein lebhafter überdachter Markt mit erstklassigen Gourmetständen, die legendären Saint-Marcellin-Käse, handwerkliche Wurstwaren und frische Austern verkaufen.",
    "desc_nl": "De ultieme tempel van de Lyonese gastronomie, een levendige overdekte markt met hoogwaardige gastronomische kraampjes waar legendarische Saint-Marcellin-kaas, ambachtelijke vleeswaren en verse oesters worden verkocht.",
    
    "tip_en": "Go hungry! Stop by 'Mère Richard' for their famous cheese and try a praline tart from 'Sève' for dessert.",
    "tip_ja": "お腹を空かせて行きましょう！『Mère Richard』に立ち寄って有名なチーズを試し、デザートには『Sève』のプラリネタルトをお試しください。",
    "tip_es": "¡Ve con hambre! Pasa por 'Mère Richard' para probar su famoso queso y prueba una tarta de praliné de 'Sève' de postre.",
    "tip_zh": "空着肚子去吧！顺便去‘Mère Richard’尝尝他们著名的奶酪，甜点则尝尝‘Sève’的果仁糖馅饼。",
    "tip_fr": "Allez-y l'estomac vide ! Arrêtez-vous chez 'Mère Richard' pour son célèbre fromage et goûtez une tarte aux pralines de chez 'Sève' pour le dessert.",
    "tip_de": "Gehen Sie hungrig dorthin! Halten Sie bei 'Mère Richard' an, um den berühmten Käse zu probieren, und versuchen Sie ein Pralinen-Törtchen von 'Sève' zum Nachtisch.",
    "tip_nl": "Ga met honger! Stop bij 'Mère Richard' voor hun beroemde kaas en probeer als dessert een pralinétaart van 'Sève'.",
    
    "whyThisSpot_en": "A true sensory explosion that solidifies Lyon's reputation as the culinary capital of France.",
    "whyThisSpot_ja": "フランスの美食の首都としてのリヨンの名声を確固たるものにする、真の感覚的爆発。",
    "whyThisSpot_es": "Una verdadera explosión sensorial que consolida la reputación de Lyon como la capital culinaria de Francia.",
    "whyThisSpot_zh": "一场真正的感官大爆发，巩固了里昂作为法国烹饪之都的声誉。",
    "whyThisSpot_fr": "Une véritable explosion sensorielle qui consolide la réputation de Lyon en tant que capitale culinaire de la France.",
    "whyThisSpot_de": "Eine wahre sensorische Explosion, die Lyons Ruf als kulinarische Hauptstadt Frankreichs festigt.",
    "whyThisSpot_nl": "Een ware zintuiglijke explosie die de reputatie van Lyon als de culinaire hoofdstad van Frankrijk versterkt."
  },
  "lyn_lyon_30": {
    "desc_en": "The world-famous flagship temple of French gastronomy created by culinary legend Paul Bocuse, offering a luxurious and unforgettable fine-dining experience.",
    "desc_ja": "料理界のレジェンド、ポール・ボキューズが創設した、世界的に有名なフランス美食の主力殿堂。豪華で忘れられない素晴らしいダイニング体験を提供します。",
    "desc_es": "El mundialmente famoso templo de la gastronomía francesa creado por la leyenda culinaria Paul Bocuse, que ofrece una experiencia gastronómica de lujo inolvidable.",
    "desc_zh": "由烹饪传奇人物保罗·博古斯创立的世界著名法国美食旗舰圣殿，提供奢华且令人难忘的高级用餐体验。",
    "desc_fr": "Le temple mondialement célèbre de la gastronomie française créé par la légende de la cuisine Paul Bocuse, offrant une expérience gastronomique luxueuse et inoubliable.",
    "desc_de": "Der weltberühmte Flaggschiff-Tempel der französischen Gastronomie, der von der kulinarischen Legende Paul Bocuse geschaffen wurde und ein luxuriöses und unvergessliches Fine-Dining-Erlebnis bietet.",
    "desc_nl": "De wereldberoemde vlaggenschiptempel van de Franse gastronomie, gecreëerd door culinaire legende Paul Bocuse, die een luxueuze en onvergetelijke verfijnde eetervaring biedt.",
    
    "tip_en": "You absolutely must order the legendary VGE Truffle Soup, created for the French President in 1975. Reservations must be made months in advance.",
    "tip_ja": "1975年にフランス大統領のために作られた伝説のVGEトリュフスープは絶対に注文するべきです。予約は数ヶ月前にする必要があります。",
    "tip_es": "No puedes dejar de pedir la legendaria sopa de trufas VGE, creada para el presidente francés en 1975. Se debe reservar con meses de antelación.",
    "tip_zh": "您一定要点 1975 年为法国总统发明的传奇 VGE 松露汤。必须提前几个月预订。",
    "tip_fr": "Vous devez absolument commander la mythique soupe aux truffes VGE, créée pour le président de la République en 1975. Les réservations doivent être effectuées plusieurs mois à l'avance.",
    "tip_de": "Sie müssen unbedingt die legendäre VGE-Trüffelsuppe probieren, die 1975 für den französischen Präsidenten kreiert wurde. Reservierungen müssen Monate im Voraus vorgenommen werden.",
    "tip_nl": "U moet absoluut de legendarische VGE-truffelsoep bestellen, gecreëerd voor de Franse president in 1975. Reserveren moet maanden van tevoren gebeuren.",
    
    "whyThisSpot_en": "A once-in-a-lifetime pilgrimage for food lovers to taste classic, unchanged French culinary perfection.",
    "whyThisSpot_ja": "美食家にとって、古典的で変わらないフランスの完璧な料理を味わうための、一生に一度の巡礼です。",
    "whyThisSpot_es": "Un peregrinaje único en la vida para los amantes de la comida para probar la clásica e inalterada perfección culinaria francesa.",
    "whyThisSpot_zh": "对于美食爱好者来说，这是一次一生一次的朝圣之旅，品尝经典且经久不衰的法国完美烹饪艺术。",
    "whyThisSpot_fr": "Un pèlerinage incontournable pour les amateurs de gastronomie pour déguster la perfection culinaire française classique et intemporelle.",
    "whyThisSpot_de": "Eine einmalige Pilgerreise für Feinschmecker, um die klassische, unveränderte französische kulinarische Perfektion zu probieren.",
    "whyThisSpot_nl": "Een unieke pelgrimstocht voor fijnproevers om de klassieke, onveranderde Franse culinaire perfectie te proeven."
  },
  "lyn_lyon_33": {
    "desc_en": "A spectacular 6-story open-air stairwell and historic 'traboule' in the Croix-Rousse district, serving as a powerful symbol of the 19th-century Canut silk worker revolts.",
    "desc_ja": "クロワ・ルース地区にある壮観な6階建ての屋外階段と歴史的な「トラブール」。19世紀のカニュ絹織物工の反乱の強力な象徴として機能しています。",
    "desc_es": "Una espectacular escalera al aire libre de 6 pisos y un 'traboule' histórico en el distrito de Croix-Rousse, que sirve como un poderoso símbolo de las revueltas de los trabajadores de la seda Canut del siglo XIX.",
    "desc_zh": "红十字区一座壮观的 6 层露天楼梯间和历史悠久的“traboule”，是 19 世纪卡努特丝绸工人起义的有力象征。",
    "desc_fr": "Une traboule spectaculaire dotée d'un escalier à ciel ouvert de 6 étages dans le quartier de la Croix-Rousse, symbole puissant des révoltes des canuts au XIXe siècle.",
    "desc_de": "Eine spektakuläre 6-stöckige Freilufttreppe und eine historische 'Traboule' im Viertel Croix-Rousse, die als starkes Symbol für die Aufstände der Seidenweber der Canuts im 19. Jahrhundert dient.",
    "desc_nl": "Een spectaculair 6 verdiepingen tellend openlucht trappenhuis en historische 'traboule' in de wijk Croix-Rousse, dat dient als een krachtig symbool van de Canut zijdebewerkers opstanden in de 19e eeuw.",
    
    "tip_en": "Enter from 9 Place Colbert. The striking geometry of the stairs makes it one of the most photogenic and atmospheric spots in Lyon.",
    "tip_ja": "コルベール広場9番から入ります。階段の印象的な幾何学的形状により、リヨンで最も写真映えする雰囲気のあるスポットの1つになっています。",
    "tip_es": "Entra por 9 Place Colbert. La sorprendente geometría de las escaleras lo convierte en uno de los lugares más fotogénicos y evocadores de Lyon.",
    "tip_zh": "从科尔贝尔广场 9 号进入。楼梯引人注目的几何形状使其成为里昂最上镜、最有氛围的景点之一。",
    "tip_fr": "Entrez par le 9 Place Colbert. La géométrie saisissante de ses escaliers en fait l'un des lieux les plus photogéniques et atmosphériques de Lyon.",
    "tip_de": "Betreten Sie es vom 9 Place Colbert. Die auffällige Geometrie der Treppen macht es zu einem der fotogensten und stimmungsvollsten Orte in Lyon.",
    "tip_nl": "Ga naar binnen vanaf 9 Place Colbert. De opvallende geometrie van de trappen maakt het een van de meest fotogenieke en sfeervolle plekken in Lyon.",
    
    "whyThisSpot_en": "An architectural marvel and a window into the turbulent and fascinating history of Lyon's silk weaving industry.",
    "whyThisSpot_ja": "建築の驚異であり、リヨンの絹織物産業の激動の魅力的な歴史への窓です。",
    "whyThisSpot_es": "Una maravilla arquitectónica y una ventana a la turbulenta y fascinante historia de la industria tejedora de seda de Lyon.",
    "whyThisSpot_zh": "一座建筑奇迹，也是了解里昂丝绸编织业动荡而迷人历史的窗口。",
    "whyThisSpot_fr": "Une merveille architecturale et une fenêtre sur l'histoire mouvementée et fascinante de l'industrie de la soie à Lyon.",
    "whyThisSpot_de": "Ein architektonisches Wunderwerk und ein Fenster in die turbulente und faszinierende Geschichte der Lyoner Seidenweberei.",
    "whyThisSpot_nl": "Een architectonisch wonder en een venster op de turbulente en fascinerende geschiedenis van de zijdeweverij in Lyon."
  },
  "lyn_lyon_35": {
    "desc_en": "Europe's largest trompe-l'œil mural covering a massive 1,200 square meters, beautifully illustrating the everyday life and evolution of the Croix-Rousse silk district.",
    "desc_ja": "1,200平方メートルの広大な面積を誇るヨーロッパ最大のだまし絵の壁画で、クロワ・ルース絹織物地区の日常生活と進化を美しく描いています。",
    "desc_es": "El mural de trampantojo más grande de Europa que cubre unos enormes 1.200 metros cuadrados y que ilustra maravillosamente la vida cotidiana y la evolución del distrito de la seda de Croix-Rousse.",
    "desc_zh": "欧洲最大的错视壁画占地 1,200 平方米，生动展现了红十字丝绸区的日常生活和发展演变。",
    "desc_fr": "La plus grande fresque en trompe-l'œil d'Europe couvrant 1 200 mètres carrés, illustrant magnifiquement la vie quotidienne et l'évolution du quartier de la soie de la Croix-Rousse.",
    "desc_de": "Europas größtes Trompe-l'œil-Wandgemälde, das riesige 1.200 Quadratmeter umfasst und auf wunderschöne Weise das alltägliche Leben und die Entwicklung des Seidenviertels Croix-Rousse veranschaulicht.",
    "desc_nl": "De grootste trompe-l'œil-muurschildering van Europa die maar liefst 1.200 vierkante meter beslaat en het dagelijks leven en de evolutie van de zijdewijk Croix-Rousse prachtig illustreert.",
    
    "tip_en": "Notice how the mural is updated every decade to reflect changes in the neighborhood and the aging of the painted residents. A true living artwork!",
    "tip_ja": "壁画が地区の変化や描かれた住民の加齢を反映するために、10年ごとにどのように更新されるかに注目してください。真に生きている芸術作品です！",
    "tip_es": "Observa cómo el mural se actualiza cada década para reflejar los cambios en el vecindario y el envejecimiento de los residentes pintados. ¡Una verdadera obra de arte viva!",
    "tip_zh": "请注意壁画如何每十年更新一次，以反映社区的变化和所画居民的衰老。一件真正的活生生的艺术品！",
    "tip_fr": "Remarquez comment la fresque est mise à jour chaque décennie pour refléter les changements du quartier et le vieillissement des habitants peints. Une véritable œuvre d'art vivante !",
    "tip_de": "Beachten Sie, wie das Wandbild jedes Jahrzehnt aktualisiert wird, um Veränderungen in der Nachbarschaft und das Altern der gemalten Bewohner widerzuspiegeln. Ein wahres lebendiges Kunstwerk!",
    "tip_nl": "Merk op hoe de muurschildering elk decennium wordt bijgewerkt om de veranderingen in de buurt en de veroudering van de geschilderde bewoners weer te geven. Een waar levend kunstwerk!",
    
    "whyThisSpot_en": "An incredible feat of urban artistry that immerses you completely in the vibrant local community vibe.",
    "whyThisSpot_ja": "活気に満ちた地元のコミュニティの雰囲気にどっぷりと浸れる、都市芸術の信じられないほどの偉業。",
    "whyThisSpot_es": "Una increíble hazaña de arte urbano que te sumerge por completo en la vibrante atmósfera de la comunidad local.",
    "whyThisSpot_zh": "这是一项令人难以置信的城市艺术壮举，让您完全沉浸在充满活力的当地社区氛围中。",
    "whyThisSpot_fr": "Une incroyable prouesse d'art urbain qui vous plonge complètement dans l'ambiance dynamique de la communauté locale.",
    "whyThisSpot_de": "Eine unglaubliche Meisterleistung der urbanen Kunst, die Sie vollständig in die lebendige Atmosphäre der lokalen Gemeinschaft eintauchen lässt.",
    "whyThisSpot_nl": "Een ongelooflijk staaltje stedelijke kunst dat je volledig onderdompelt in de levendige sfeer van de lokale gemeenschap."
  },
  "lyn_lyon_36": {
    "desc_en": "An elegant, striking red pedestrian suspension bridge gracefully crossing the Saône river, offering picturesque panoramas of the historic Vieux Lyon and Saint-Georges church.",
    "desc_ja": "ソーヌ川に優雅に架かるエレガントで印象的な赤い歩行者用の吊り橋。歴史的な旧市街（ヴュー リヨン）とサン ジョルジュ教会の絵のように美しいパノラマの景色を楽しめます。",
    "desc_es": "Un elegante y llamativo puente colgante peatonal rojo que cruza con gracia el río Saona, ofreciendo pintorescos panoramas del histórico Vieux Lyon y la iglesia de Saint-Georges.",
    "desc_zh": "一座优雅、醒目的红色人行悬索桥优雅地横跨索恩河，提供历史悠久的里昂老城和圣乔治教堂如画般的全景。",
    "desc_fr": "Une passerelle suspendue piétonne rouge élégante et saisissante traversant gracieusement la Saône, offrant des panoramas pittoresques sur le Vieux Lyon historique et l'église Saint-Georges.",
    "desc_de": "Eine elegante, auffällige rote Fußgänger-Hängebrücke, die anmutig den Fluss Saône überquert und malerische Panoramen auf das historische Vieux Lyon und die Kirche Saint-Georges bietet.",
    "desc_nl": "Een elegante, opvallende rode voetgangershangbrug die gracieus de rivier de Saône oversteekt en een schilderachtig panorama biedt op het historische Vieux Lyon en de Saint-Georges-kerk.",
    
    "tip_en": "Visit at sunset or early evening. The vibrant red against the golden light over the river and the lit-up church makes for an unparalleled photograph.",
    "tip_ja": "日没または夕方早めに訪れてください。川越しの黄金色の光とライトアップされた教会を背景にした鮮やかな赤は、比類のない写真になります。",
    "tip_es": "Visítalo al atardecer o a primera hora de la noche. El rojo vibrante contra la luz dorada sobre el río y la iglesia iluminada hacen una fotografía inigualable.",
    "tip_zh": "在日落或傍晚时分游览。红色的桥身在河面上金色的夕阳和被灯光照亮的教堂的映衬下，是绝佳的摄影素材。",
    "tip_fr": "Visitez au coucher du soleil ou en début de soirée. Le rouge éclatant contrastant avec la lumière dorée sur le fleuve et l'église illuminée permet de réaliser une photographie sans pareille.",
    "tip_de": "Besuchen Sie uns bei Sonnenuntergang oder am frühen Abend. Das leuchtende Rot vor dem goldenen Licht über dem Fluss und der beleuchteten Kirche ist ein unvergleichliches Fotomotiv.",
    "tip_nl": "Bezoek bij zonsondergang of vroege avond. Het levendige rood tegen het gouden licht over de rivier en de verlichte kerk zorgt voor een ongeëvenaarde foto.",
    
    "whyThisSpot_en": "The perfect romantic stroll and one of the most aesthetic viewpoints connecting the modern city to its medieval heart.",
    "whyThisSpot_ja": "完璧なロマンチックな散歩であり、近代都市と中世の中心部を結ぶ最も美しい視点の1つです。",
    "whyThisSpot_es": "El paseo romántico perfecto y uno de los miradores más estéticos que conecta la ciudad moderna con su corazón medieval.",
    "whyThisSpot_zh": "这里是完美浪漫散步的好去处，也是将现代城市与其中心地带的中世纪风情连接起来的最具美感的观景点之一。",
    "whyThisSpot_fr": "La promenade romantique parfaite et l'un des points de vue les plus esthétiques reliant la ville moderne à son cœur médiéval.",
    "whyThisSpot_de": "Der perfekte romantische Spaziergang und einer der ästhetischsten Aussichtspunkte, der die moderne Stadt mit ihrem mittelalterlichen Herzen verbindet.",
    "whyThisSpot_nl": "De perfecte romantische wandeling en een van de meest esthetische uitkijkpunten die de moderne stad met het middeleeuwse hart verbindt."
  },
  "lyn_lyon_38": {
    "desc_en": "A secret hilltop garden park, a gift from the city of Montreal, offering serene and breathtaking panoramic views over Lyon's iconic terracotta rooftops and winding rivers.",
    "desc_ja": "モントリオール市からの贈り物である秘密の丘の上の庭園公園。リヨンを象徴するテラコッタの屋根と曲がりくねった川の穏やかで息をのむようなパノラマの景色を楽しめます。",
    "desc_es": "Un jardín secreto en la cima de una colina, un regalo de la ciudad de Montreal, que ofrece serenas e impresionantes vistas panorámicas de los emblemáticos tejados de terracota de Lyon y sus ríos serpenteantes.",
    "desc_zh": "一座建在山顶的秘密花园公园，是蒙特利尔市的礼物。在这里，您可以宁静地欣赏令人惊叹的里昂全景，包括标志性的红瓦屋顶和蜿蜒的河流。",
    "desc_fr": "Un parc-jardin secret au sommet d'une colline, un cadeau de la ville de Montréal, offrant une vue panoramique sereine et époustouflante sur les toits en terre cuite emblématiques de Lyon et ses fleuves sinueux.",
    "desc_de": "Ein geheimer Gartenpark auf einem Hügel, ein Geschenk der Stadt Montreal, der einen ruhigen und atemberaubenden Panoramablick über die ikonischen Terrakottadächer von Lyon und die gewundenen Flüsse bietet.",
    "desc_nl": "Een geheim tuinpark op een heuveltop, een geschenk van de stad Montreal, met een sereen en adembenemend panoramisch uitzicht over de iconische terracottadaken van Lyon en de kronkelende rivieren.",
    
    "tip_en": "It's slightly hidden away and far less crowded than Fourvière. Pack a small picnic and enjoy the absolute best, uninterrupted sunset view in the city.",
    "tip_ja": "少し隠れた場所にあり、フルヴィエールよりもはるかに混雑していません。小さなお弁当を持参して、市内でも最高で遮るもののない夕日をお楽しみください。",
    "tip_es": "Está un poco escondido y mucho menos concurrido que Fourvière. Prepara un pequeño picnic y disfruta de la mejor vista ininterrumpida de la puesta de sol en la ciudad.",
    "tip_zh": "它的位置比较隐蔽，比起富维耶，这里的人要少得多。带上简单的野餐，享受城市里绝对最佳、无遮挡的日落美景。",
    "tip_fr": "Il est légèrement caché et beaucoup moins fréquenté que Fourvière. Préparez un petit pique-nique et profitez de la meilleure vue imprenable sur le coucher de soleil de la ville.",
    "tip_de": "Es ist etwas versteckt und weit weniger überlaufen als Fourvière. Packen Sie ein kleines Picknick ein und genießen Sie den absolut besten, ungestörten Sonnenuntergangsblick der Stadt.",
    "tip_nl": "Het is een beetje verborgen en veel minder druk dan Fourvière. Neem een ​​kleine picknick mee en geniet van het absoluut beste, ononderbroken uitzicht op de zonsondergang in de stad.",
    
    "whyThisSpot_en": "The ultimate peaceful retreat for lovers and photographers wanting to capture Lyon from above without the tourist crowds.",
    "whyThisSpot_ja": "観光客の混雑なしに上空からリヨンを撮影したい恋人や写真家にとって、究極の平和な隠れ家です。",
    "whyThisSpot_es": "El último refugio tranquilo para amantes y fotógrafos que desean capturar Lyon desde arriba sin las multitudes de turistas.",
    "whyThisSpot_zh": "这是恋人们和摄影师们最理想的宁静避风港，他们可以在没有游客拥挤的情况下俯瞰里昂的美景。",
    "whyThisSpot_fr": "Le refuge paisible par excellence pour les amoureux et les photographes qui souhaitent capturer Lyon d'en haut sans la foule de touristes.",
    "whyThisSpot_de": "Der ultimative, friedliche Rückzugsort für Liebhaber und Fotografen, die Lyon von oben einfangen möchten, ohne von Touristenmassen gestört zu werden.",
    "whyThisSpot_nl": "De ultieme vredige plek voor geliefden en fotografen die Lyon van bovenaf willen vastleggen zonder de toeristische drukte."
  },
  "lyn_lyon_39": {
    "desc_en": "An ultra-modern, award-winning eco-district at the southern tip of the peninsula, famous for its avant-garde architecture, including the striking Orange Cube and revitalized docks.",
    "desc_ja": "半島南端にある超現代的で受賞歴のあるエコ地区。印象的なオレンジ キューブや再生されたドックなど、前衛的な建築で有名です。",
    "desc_es": "Un distrito ecológico ultramoderno y galardonado en el extremo sur de la península, famoso por su arquitectura vanguardista, que incluye el llamativo Orange Cube y los muelles revitalizados.",
    "desc_zh": "位于半岛南端的一个屡获殊荣的超现代生态区，以其前卫的建筑而闻名，包括引人注目的橙色立方体和重新焕发活力的码头。",
    "desc_fr": "Un écoquartier ultramoderne et primé à la pointe sud de la presqu'île, célèbre pour son architecture avant-gardiste, notamment le surprenant Cube Orange et les quais revitalisés.",
    "desc_de": "Ein hochmodernes, preisgekröntes Öko-Viertel an der Südspitze der Halbinsel, berühmt für seine avantgardistische Architektur, einschließlich des markanten Orange Cube und der revitalisierten Docks.",
    "desc_nl": "Een ultramoderne, bekroonde ecowijk op het zuidelijkste puntje van het schiereiland, beroemd om zijn avant-gardistische architectuur, waaronder de opvallende Orange Cube en gerevitaliseerde dokken.",
    
    "tip_en": "Rent a bike or take a leisurely stroll along the water basins to fully appreciate the stark, beautiful contrast between Lyon's historical center and this futuristic waterfront.",
    "tip_ja": "自転車をレンタルするか、水域に沿ってゆっくりと散歩して、リヨンの歴史的中心部とこの未来的なウォーターフロントの間の際立った美しいコントラストを十分に味わってください。",
    "tip_es": "Alquila una bicicleta o da un paseo tranquilo por los estanques de agua para apreciar plenamente el fuerte y hermoso contraste entre el centro histórico de Lyon y esta costa futurista.",
    "tip_zh": "租一辆自行车或沿着水池悠闲漫步，充分欣赏里昂历史中心与这处未来主义海滨之间鲜明而美丽的对比。",
    "tip_fr": "Louez un vélo ou promenez-vous tranquillement le long des bassins d'eau pour apprécier pleinement le contraste saisissant et magnifique entre le centre historique de Lyon et ce front de mer futuriste.",
    "tip_de": "Mieten Sie ein Fahrrad oder machen Sie einen gemütlichen Spaziergang an den Wasserbecken entlang, um den starken, schönen Kontrast zwischen dem historischen Zentrum von Lyon und diesem futuristischen Ufer zu genießen.",
    "tip_nl": "Huur een fiets of maak een ontspannende wandeling langs de waterbekkens om ten volle te genieten van het sterke, prachtige contrast tussen het historische centrum van Lyon en deze futuristische waterkant.",
    
    "whyThisSpot_en": "A visionary area that proves Lyon isn't just about ancient history—it's a pioneer of sustainable urban future.",
    "whyThisSpot_ja": "リヨンが古代の歴史だけではないことを証明する先見の明のあるエリア。持続可能な都市の未来のパイオニアです。",
    "whyThisSpot_es": "Un área visionaria que demuestra que Lyon no se trata solo de historia antigua: es pionera en el futuro urbano sostenible.",
    "whyThisSpot_zh": "这是一个具有远见的地区，它证明了里昂不仅拥有悠久的历史，而且是可持续城市未来的先驱。",
    "whyThisSpot_fr": "Un quartier visionnaire qui prouve que Lyon ne se résume pas à son histoire ancienne : c'est une pionnière de l'avenir urbain durable.",
    "whyThisSpot_de": "Ein visionäres Viertel, das beweist, dass es in Lyon nicht nur um alte Geschichte geht – es ist ein Vorreiter für eine nachhaltige städtische Zukunft.",
    "whyThisSpot_nl": "Een visionair gebied dat bewijst dat Lyon niet alleen om oude geschiedenis draait: het is een pionier op het gebied van een duurzame stedelijke toekomst."
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
