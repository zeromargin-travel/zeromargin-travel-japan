import json
import os

paris_file = "data/cities/paris.json"
with open(paris_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Dictionary of tips keyed by spot ID or spot name
paris_tips = {
    "p_1": { # Eiffel Tower
        "ja": "日没〜深夜1時まで毎時0分に5分間だけ点滅する『シャンパンフラッシュ』は必見。全景撮影はトロカデロ広場またはシャン・ド・マルス公園からがベストアングルです。",
        "en": "Don't miss the 'Sparkling Eiffel' light show for 5 minutes every hour from sunset until 1 AM. For the best photos, head to Trocadéro Gardens or Champ de Mars.",
        "es": "No te pierdas el espectáculo de luces 'Eiffel Centelleante' durante 5 minutos cada hora desde el atardecer hasta la 1:00 AM. La mejor foto es desde los Jardines del Trocadero.",
        "zh": "不要错过从日落到凌晨1点每小时整点持续5分钟的“埃菲尔闪耀”灯光秀。最佳拍照地点是特罗卡德罗花园或战神广场。",
        "fr": "Ne manquez pas le spectacle des illuminations de la Tour Eiffel pendant 5 minutes au début de chaque heure après le coucher du soleil. Meilleures photos depuis le Trocadéro.",
        "de": "Verpassen Sie nicht die 5-minütige 'Glitzer-Eiffelturm'-Lichtshow zu jeder vollen Stunde ab Sonnenuntergang bis 01:00 Uhr. Beste Fotos vom Trocadéro-Platz."
    },
    "p_2": { # Arc de Triomphe
        "ja": "屋上への284段の螺旋階段は歩きやすい靴が必須。凱旋門へ向かう際は車道を渡らず、必ずシャンゼリゼ通り側にある地下通路をご利用ください。",
        "en": "Comfortable shoes are essential for the 284-step spiral staircase to the roof. Always use the underground pedestrian tunnel from Champs-Élysées—never cross the roundabout traffic!",
        "es": "Es imprescindible llevar calzado cómodo para subir los 284 escalones hasta la azotea. ¡Usa siempre el túnel subterráneo desde los Campos Elíseos y no cruces el tráfico!",
        "zh": "登上屋顶的284级螺旋楼梯需要穿着舒适的鞋子。请务必使用香榭丽舍大街的地下通道，切勿穿过环岛车流！",
        "fr": "Des chaussures confortables sont indispensables pour gravir les 284 marches de l'escalier en colimaçon. Utilisez toujours le souterrain depuis les Champs-Élysées !",
        "de": "Bequemes Schuhwerk ist für die 284 Stufen der Wendeltreppe unerlässlich. Nutzen Sie immer die Fußgängerunterführung von der Champs-Élysées!"
    },
    "p_3": { # Sainte-Chapelle
        "ja": "2階の巨大ステンドグラスは晴れた日の午前10時〜14時頃に最も輝きます。裁判所と同じ敷地内にあるため厳重なセキュリティがあり、日時指定予約が必須です。",
        "en": "The 1,113 stained glass windows shine brightest on sunny days between 10 AM and 2 PM. Located inside the Palace of Justice, timed-entry tickets and security check are strictly required.",
        "es": "Las 1.113 vidrieras brillan con más intensidad los días soleados entre las 10:00 y las 14:00. Se requiere reserva previa y control de seguridad obligatorio.",
        "zh": "1113扇彩色玻璃窗在晴天上午10点至下午2点之间最为绚丽。位于法院大楼内，必须提前预约时段并接受安检。",
        "fr": "Les 1 113 vitraux brillent de mille feux les jours ensoleillés entre 10h et 14h. Billets horodatés et contrôle de sécurité obligatoires.",
        "de": "Die 1.113 Buntglasfenster erstrahlen an sonnigen Tagen zwischen 10:00 und 14:00 Uhr am schönsten. Zeitfenster-Tickets und Sicherheitskontrolle erforderlich."
    },
    "p_4": { # Sacré-Cœur
        "ja": "聖堂内への入場は無料。丘の上の寺院へは、大階段横のケーブルカー（メトロ1回券/Navigo利用可能）が便利です。大階段周辺のスリやミサンガ売りにはご注意ください。",
        "en": "Entry inside the basilica is free. Take the funicular (uses standard Paris Metro ticket) up the hill to skip the stairs. Watch out for street vendors near the front stairs.",
        "es": "La entrada a la basílica es gratuita. Toma el funicular (funciona con billete de metro) para subir la colina. Atención a los vendedores ambulantes en las escaleras.",
        "zh": "教堂内部免费参观。前往山顶可乘坐缆车（可使用普通地铁票）。请注意大楼梯附近的街头推销。",
        "fr": "L'entrée dans la basilique est gratuite. Prenez le funiculaire (ticket de métro classique accepté) pour gravir la butte sans vous fatiguer.",
        "de": "Der Eintritt in die Basilika ist frei. Nutzen Sie die Standseilbahn (normale Metro-Ticket gültig), um den Hügel mühelos zu erklimmen."
    },
    "p_5": { # Notre-Dame
        "ja": "再建工事完了後の最新見学エリア。全景撮影はセーヌ川対岸（サン・ミッシェル橋側）やシテ島裏手のジャン23世公園からの角度が最も美しいです。",
        "en": "Great views of the newly restored exterior can be captured from Pont Saint-Michel across the Seine river or Square Jean XXIII behind the cathedral.",
        "es": "Obtén las mejores vistas de la catedral restaurada desde el puente Saint-Michel sobre el Sena o desde el Square Jean XXIII en la parte posterior.",
        "zh": "从塞纳河对岸的圣米歇尔桥或教堂后方的让二十三世广场，可以拍摄到修复后的最佳大教堂外景。",
        "fr": "Superbes vues sur Notre-Dame rénovée depuis le Pont Saint-Michel ou depuis le square Jean XXIII à l'arrière.",
        "de": "Tolle Fotoperspektiven auf die restaurierte Kathedrale bieten sich von der Pont Saint-Michel über der Seine oder vom Square Jean XXIII."
    },
    "p_6": { # Palais-Royal
        "ja": "庭園内の『Café Kitsuné』で抹茶ラテをテイクアウトし、噴水脇の緑のチェアーで日向ぼっこするのが地元風。白黒ストライプの柱（ビュレンの柱）は自由に登って撮影可能。",
        "en": "Grab a matcha latte from Café Kitsuné in the garden and relax on the iconic green chairs by the fountain. The striped Buren Columns in the courtyard are open for fun photos.",
        "es": "Toma un café en Café Kitsuné dentro del jardín y relájate en las sillas verdes junto a la fuente. Las columnas de Buren en el patio son perfectas para fotos creativas.",
        "zh": "在花园里的Café Kitsuné买杯抹茶拿铁，坐在喷泉旁标志性的绿色椅子上放松身心。中庭的黑白条纹柱可以自由拍照。",
        "fr": "Prenez un café chez Café Kitsuné dans le jardin et détendez-vous sur les fauteuils verts. Les Colonnes de Buren sont parfaites pour des photos créatives.",
        "de": "Holen Sie sich einen Matcha Latte bei Café Kitsuné im Garten und entspannen Sie auf den grünen Stühlen am Brunnen. Die Buren-Säulen bieten tolle Fotomotive."
    },
    "p_7": { # Panthéon
        "ja": "地下納骨堂にはユーゴー、ルソー、キュリー夫人らが眠ります。4〜10月限定でドーム屋上へのガイドツアー（要追加チケット）があり、パリ市内を360度見渡せます。",
        "en": "The crypt holds tombs of Victor Hugo, Rousseau, and Marie Curie. From April to October, you can climb to the dome balcony for a sweeping 360-degree view of Paris.",
        "es": "La cripta alberga las tumbas de Victor Hugo, Rousseau y Marie Curie. De abril a octubre, puedes subir al balcón de la cúpula para una vista panorámica de 360°.",
        "zh": "地下陵墓安葬着雨果、卢梭和居里夫人。每年4月至10月，可登顶圆顶露台俯瞰巴黎360度全景。",
        "fr": "La crypte abrite les tombes de Victor Hugo, Rousseau et Marie Curie. D'avril à octobre, montez au balcon du dôme pour une vue à 360° sur Paris.",
        "de": "In der Krypta befinden sich die Gräber von Victor Hugo, Rousseau und Marie Curie. Von April bis Oktober bietet der Kuppelbalkon einen 360-Grad-Panoramablick."
    },
    "p_8": { # Jardin du Luxembourg
        "ja": "中央池の周りにある緑の鉄製チェアーは移動自由。木陰に佇む『メディチの噴水』周辺は、テイクアウトしたパンやコーヒーを楽しむ最高の癒やしスポットです。",
        "en": "Feel free to move the iconic green chairs around the central pond. The shaded area by the historic Medici Fountain is the top spot for a quiet coffee or bakery lunch.",
        "es": "Las famosas sillas verdes junto al estanque se pueden mover libremente. La zona sombreada junto a la Fuente Médicis es ideal para un almuerzo tranquilo.",
        "zh": "中央池塘周围的绿色铁椅可以自由移动。历史悠久的美第奇喷泉旁边的树荫处是享受安静咖啡或外带午餐的最佳地点。",
        "fr": "Déplacez librement les fauteuils verts autour du grand bassin. L'ombre près de la Fontaine Médicis est parfaite pour une pause café au calme.",
        "de": "Die grünen Stühle rund um das Hauptbecken können frei bewegt werden. Der schattige Bereich am Medici-Brunnen lädt zum Entspannen ein."
    },
    "p_9": { # Opéra Garnier
        "ja": "『オペラ座の怪人』の舞台となった『5番ボックス席（Box 5）』が2階席に実在します。ホール天井のシャガールの巨大壁画と豪華シャンデリアの対比は圧巻です。",
        "en": "Look for Box 5 on the second floor—it's the actual box reserved for the Phantom of the Opera! Don't miss Chagall's colorful painted ceiling inside the main auditorium.",
        "es": "Busca el Palco 5 en el primer piso: ¡es el palco real reservado para el Fantasma de la Ópera! Admira el impresionante techo pintado por Chagall en la sala principal.",
        "zh": "在二楼寻找5号包厢——这就是《歌剧魅影》中专为魅影保留的包厢！不要错过主大厅内夏加尔绘制的绚丽天花板壁画。",
        "fr": "Cherchez la Loge 5 au premier étage : c'est la loge réservée au Fantôme de l'Opéra ! Admirez le plafond peint par Chagall dans la grande salle.",
        "de": "Suchen Sie nach Loge 5 im ersten Stock – der echten Loge des Phantoms der Oper! Bewundern Sie die von Chagall bemalte Decke im Hauptsaal."
    },
    "p_10": { # Pont Alexandre III
        "ja": "夕暮れ時に橋のたもと（左岸側）へ降りると、セーヌ川沿いのオープンエアバー『Rosa Bonheur sur Seine』があり、エッフェル塔のライトアップを眺めながらお酒を楽しめます。",
        "en": "Head down to the left riverbank below the bridge at sunset to find Rosa Bonheur sur Seine, a popular open-air barge bar offering drinks with Eiffel Tower views.",
        "es": "Baja a la orilla izquierda bajo el puente al atardecer para visitar Rosa Bonheur sur Seine, un bar flotante ideal para tomar algo con vistas a la Torre Eiffel.",
        "zh": "日落时分走到桥下的左岸，可以找到Rosa Bonheur sur Seine水上露天酒吧，边饮酒边欣赏埃菲尔铁塔夜景。",
        "fr": "Descendez sur la berge sous le pont au coucher du soleil pour rejoindre Rosa Bonheur sur Seine, une péniche-bar branchée avec vue sur la Tour Eiffel.",
        "de": "Gehen Sie bei Sonnenuntergang zum linken Seine-Ufer unterhalb der Brücke zur Bar-Péniche Rosa Bonheur mit Blick auf den Eiffelturm."
    },
    "p_11": { # Les Invalides
        "ja": "ナポレオンの墓へ直行する場合は、北側（軍事博物館）ではなく南側の『ドーム教会入口』から入場するとスムーズです。",
        "en": "If visiting specifically for Napoleon's Tomb, enter via the South Gate (Dome Church entrance) to bypass the main military museum queues.",
        "es": "Si vienes principalmente a ver la Tumba de Napoleón, entra por la puerta sur (Iglesia del Domo) para evitar las colas del museo militar.",
        "zh": "如果主要是参观拿破仑墓，请从南门的圆顶教堂入口进入，避开主军事博物馆的排队人群。",
        "fr": "Si vous venez spécifiquement pour le Tombeau de Napoléon, entrez par la porte sud (Église du Dôme) pour éviter les files du musée de l'Armée.",
        "de": "Wenn Sie hauptsächlich Napoleons Grab besuchen möchten, nutzen Sie den Südeingang (Dôme-Kirche), um die Museumsschlangen zu umgehen."
    },
    "p_12": { # Pont des Arts
        "ja": "愛の南京錠は安全のため全撤去されましたが、現在はセーヌ川とシテ島を正面に望む絶好の夕焼け鑑賞＆テイクアウトディナーのスポットとして親しまれています。",
        "en": "While the love locks were removed for safety, it remains one of Paris's best pedestrian spots for watching the sunset over Île de la Cité.",
        "es": "Aunque los candados del amor fueron retirados por seguridad, sigue siendo uno de los mejores puentes peatonales para admirar la puesta de sol.",
        "zh": "虽然爱情锁出于安全原因已被拆除，但这里依然是欣赏西岱岛塞纳河日落的最佳步行桥之一。",
        "fr": "Bien que les cadenas d'amour aient été retirés pour sécurité, le pont reste l'un des meilleurs spots piétons pour contempler le coucher de soleil.",
        "de": "Obwohl die Liebesschlösser aus Sicherheitsgründen entfernt wurden, bleibt die Brücke einer der besten Orte für Sonnenuntergänge über der Seine."
    },
    "p_13": { # Catacombes
        "ja": "地下20mの坑道を1.5km歩くため通年14℃と肌寒く上着が必要。入口（ダンフェール＝ロシュロー）と出口（ルネ・コティ通り）が全く別位置のためコインロッカー預けは不可。",
        "en": "Constant 14°C temperature underground means a light jacket is needed year-round. The exit is several blocks away from the entrance, so do not leave luggage in lockers nearby.",
        "es": "La temperatura constante de 14°C bajo tierra requiere chaqueta ligera todo el año. La salida está a varias manzanas de la entrada.",
        "zh": "地下恒温14℃，需四季备薄外套。出口与入口相距数个街区，切勿在入口附近存包。",
        "fr": "La température constante de 14°C sous terre nécessite une veste toute l'année. La sortie est distante de l'entrée.",
        "de": "Die konstante Untertagetemperatur von 14°C erfordert ganzjährig eine leichte Jacke. Der Ausgang liegt einige Straßen vom Eingang entfernt."
    },
    "p_14": { # Louvre
        "ja": "地上ピラミッドの行列を避けるなら、地下ショッピングモール（カルーゼル・デュ・ルーヴル）直結の地下入口が鉄則。水・金曜は21:45までの夜間開館があります。",
        "en": "Skip the main pyramid line by entering through the Carrousel du Louvre underground mall. Night openings on Wednesday and Friday (until 9:45 PM) offer quieter galleries.",
        "es": "Evita la cola de la pirámide entrando por el centro comercial subterráneo Carrousel du Louvre. Las aperturas nocturnas de miércoles y viernes son más tranquilas.",
        "zh": "通过Carrousel du Louvre地下购物中心入口可避开金字塔主排队。周三和周五夜间开放至21:45，展厅更为安静。",
        "fr": "Évitez la file de la pyramide en passant par le centre commercial souterrain Carrousel du Louvre. Nocturnes les mercredis et vendredis jusqu'à 21h45.",
        "de": "Umgehen Sie die Pyramiden-Schlange über die unterirdische Mall Carrousel du Louvre. Mittwochs und freitags bis 21:45 Uhr geöffnet."
    },
    "p_15": { # Orsay
        "ja": "5階の大時計裏（カフェ周辺）は、文字盤越しにルーヴルやセーヌ川のシルエット写真が撮れる人気スポット。最上階の印象派ギャラリー（モネ・ゴッホ）から巡るのが効率的。",
        "en": "Head to the 5th floor clock face for an iconic silhouette photo overlooking the Seine. Start your visit on the 5th floor (Monet, Van Gogh) and work your way down.",
        "es": "Ve al reloj del 5.º piso para una foto icónica a contraluz sobre el Sena. Empieza tu visita en la 5.ª planta (Monet, Van Gogh) y ve bajando.",
        "zh": "前往5楼大钟表处拍摄面向塞纳河的经典剪影照片。建议从5楼（莫奈、梵高展厅）开始参观，逐层向下游览。",
        "fr": "Rendez-vous à l'horloge du 5e étage pour une photo silhouette mythique. Commencez votre visite par le 5e étage (Monet, Van Gogh).",
        "de": "Gehen Sie zur riesigen Uhr im 5. Stock für ein berühmtes Silhouette-Foto mit Blick auf die Seine. Beginnen Sie oben im 5. Stock."
    },
    "p_16": { # Pompidou
        "ja": "外壁の透明チューブ型エスカレーターで最上階（6階）へ上ると、モンマルトルやエッフェル塔まで見渡せるパリ東側屈指の展望ポイントになっています。",
        "en": "Ride the famous clear tube escalators on the exterior up to the 6th floor for one of the best panoramic views of Paris, including Montmartre and Eiffel Tower.",
        "es": "Sube en las famosas escaleras mecánicas tubulares exteriores hasta el 6.º piso para una de las mejores vistas panorámicas de París.",
        "zh": "搭乘外墙标志性的透明管道电梯直达6楼，可俯瞰包括蒙玛特和埃菲尔铁塔在内的巴黎全景。",
        "fr": "Prenez la chenille extérieure transparente jusqu'au 6e étage pour l'une des plus belles vues panoramiques sur Paris.",
        "de": "Fahren Sie mit den berühmten transparenten Röhrenrolltreppen in den 6. Stock für eine fantastische Panoramabild über ganz Paris."
    },
    "p_17": { # Orangerie
        "ja": "モネの巨大な『睡蓮』が自然光の差し込む特注の2つの楕円形部屋に壁一面展示されています。中央のベンチに座って静かに鑑賞するのが最高の過ごし方です。",
        "en": "Monet's massive Water Lilies are displayed in two custom oval rooms with natural skylight. Take your time sitting on the central benches to absorb the serene atmosphere.",
        "es": "Los murales de Nenúfares de Monet se exhiben en dos salas ovaladas con luz natural. Tómate tu tiempo en los bancos centrales para disfrutar la atmósfera.",
        "zh": "莫奈的巨幅《睡莲》展出在两间拥有自然采光的椭圆形特设展厅中。坐在中央凳上静静品味是最佳体验。",
        "fr": "Les Nymphéas de Monet sont exposés dans deux salles ovales baignées de lumière naturelle. Asseyez-vous sur les bancs centraux pour en profiter.",
        "de": "Monets Seerosenwandgemälde werden in zwei ovalen Räumen mit natürlichem Oberlicht ausgestellt. Genießen Sie die Ruhe auf den Bänken."
    },
    "p_18": { # Musée Rodin
        "ja": "『考える人』や『地獄の門』の像は館内だけでなく、四季のバラが咲き誇る広大な庭園に展示されています。庭園散策専用チケットも用意されています。",
        "en": "Rodin's iconic sculptures including 'The Thinker' and 'Gates of Hell' are placed throughout the lush rose gardens. Dedicated garden-only tickets are available.",
        "es": "Esculturas icónicas como 'El Pensador' y 'La Puerta del Infierno' están expuestas en los jardines de rosas. Hay entradas solo para los jardines.",
        "zh": "包括《思想者》和《地狱之门》在内的罗丹名作散布在四季玫瑰绽放的花园中。提供单独的花园参观票。",
        "fr": "Des sculptures mythiques comme 'Le Penseur' sont exposées au cœur du magnifique jardin de rosiers. Billets jardin seul disponibles.",
        "de": "Berühmte Skulpturen wie 'Der Denker' stehen im wunderschönen Rosengarten. Es gibt kostengünstige reine Garten-Tickets."
    },
    "p_19": { # Musée Picasso
        "ja": "マレ地区の17世紀貴族の館（サレ館）を改装。ピカソの初期〜晩年の作品だけでなく、彼が個人所有していたセザンヌやマティスのプライベートコレクションも必見。",
        "en": "Housed in a 17th-century mansion in Le Marais, this museum displays Picasso's personal art collection alongside his own masterworks, including Cézanne and Matisse.",
        "es": "Ubicado en un palacete del siglo XVII en Le Marais, exhibe las obras de Picasso junto con su colección personal de Cézanne y Matisse.",
        "zh": "位于玛黑区17世纪的贵族府邸中，除了毕加索本人各生平作品，还展出他私人收藏的塞尚与马蒂斯名画。",
        "fr": "Installé dans un hôtel particulier du XVIIe siècle dans le Marais, il présente les œuvres de Picasso et sa collection personnelle de Cézanne et Matisse.",
        "de": "Untergebracht in einem Stadtpalais aus dem 17. Jahrhundert im Marais-Viertel. Zeigt Picassos Werke sowie seine private Kunstsammlung."
    },
    "p_20": { # Musée Carnavalet
        "ja": "常設展の入場が完全無料のパリ市立歴史博物館。フランス革命の貴重な遺品やマルセル・プルーストの部屋が展示され、マレ地区散策の合間に立ち寄れる穴場です。",
        "en": "Admission to the permanent collections is completely free. Explore the history of Paris, French Revolution artifacts, and Marcel Proust's bedroom in Le Marais.",
        "es": "La entrada a las colecciones permanentes es totalmente gratuita. Explora la historia de París y la habitación de Marcel Proust en Le Marais.",
        "zh": "常设展免费开放。位于玛黑区，展示巴黎城市历史、法国革命珍贵文物以及马塞尔·普鲁斯特的卧室复原。",
        "fr": "Entrée gratuite aux collections permanentes. Découvrez l'histoire de Paris et la chambre de Marcel Proust au cœur du Marais.",
        "de": "Der Eintritt zu den ständigen Sammlungen ist kostenlos. Entdecken Sie die Geschichte von Paris und Marcel Prousts Zimmer im Marais."
    },
    "p_21": { # Le Petit Marché
        "ja": "ヴォージュ広場近くの隠れ家フレンチビストロ。名物の「マグロのレアステーキ Sesame Tuna」や「鴨のロースト」が人気。夕食は事前の席予約をおすすめします。",
        "en": "A cozy Marais bistro famous for its signature Sesame Seared Tuna steak and duck breast. Reservations are highly recommended for dinner.",
        "es": "Un acogedor bistro en Le Marais famoso por su atún sellado al sésamo y magret de pato. Se recomienda reservar para cenar.",
        "zh": "玛黑区一家温馨的法式小馆，以招牌芝麻煎金枪鱼排和烤鸭胸闻名。建议提前预订晚餐座位。",
        "fr": "Un bistrot chaleureux près de la Place des Vosges, célèbres pour son thon mi-cuit au sésame et magret de canard. Réservation conseillée.",
        "de": "Gemütliches Bistro im Marais-Viertel, berühmt für Thunfischsteak in Sesamkruste und Entenbrust. Reservierung empfohlen."
    },
    "p_22": { # Le Train Bleu
        "ja": "リヨン駅構内にあるベル・エポック調の金箔彫刻と天井画で飾られた宮殿のような歴史的レストラン。映画『ニキータ』や『ミスター・ビーン』の撮影地。",
        "en": "Located inside Gare de Lyon railway station, this Belle Époque palace restaurant features opulent gold leaf decor and ceiling paintings seen in classic films.",
        "es": "Ubicado dentro de la estación Gare de Lyon, este majestuoso restaurante Belle Époque cuenta con opulenta decoración dorada y pinturas en el techo.",
        "zh": "位于里昂火车站内，拥有宫殿般华丽的黄金叶雕饰与天花板壁画，是经典电影《尼基塔》与《豆豆先生》的取景地。",
        "fr": "Situé dans la Gare de Lyon, ce restaurant Belle Époque historique offre un décor grandiose de dorures et de peintures au plafond.",
        "de": "Im Bahnhof Gare de Lyon gelegen, beeindruckt dieses historische Belle-Époque-Restaurant mit prachtvollen Deckengemälden und Golddekor."
    },
    "p_23": { # Chez Janou
        "ja": "マレ地区のプロヴァンス風賑やかビストロ。食後に注文できる『ボウルから好きなだけ盛り放題の自家製チョコレートムース』が名物です。",
        "en": "Lively Provençal bistro in Le Marais. Save room for dessert—they serve a legendary chocolate mousse poured straight from a giant bowl right at your table!",
        "es": "Animado bistro provenzal en Le Marais. ¡Guarda sitio para el postre: sirven su legendaria mousse de chocolate servida directamente de un tazón gigante!",
        "zh": "玛黑区热闹的普罗旺斯风格小馆。餐后必点招牌大碗自制巧克力慕斯，服务员会大勺盛给你吃到饱！",
        "fr": "Bistrot provençal animé dans le Marais. Gardez de la place pour le dessert : la mousse au chocolat maison servie à la louche depuis un saladier géant !",
        "de": "Lebhaftes provenzalisches Bistro im Marais. Unbedingt Platz für das Dessert lassen: Schokoladenmousse wird direkt aus einer riesigen Schüssel serviert!"
    },
    "p_24": { # Bouillon Chartier
        "ja": "1896年創業の歴史ある庶民派食堂。前菜€2〜、主菜€10〜と格安で伝統フレンチを楽しめます。紙のクロスにウェイターが注文を書き込むスタイルが名物。予約不可。",
        "en": "Historic 1896 bouillon serving authentic French classics at wallet-friendly prices (mains from €10). Waiters write your order directly on the paper tablecloth. No reservations.",
        "es": "Histórico bouillon de 1896 que sirve comida francesa tradicional a precios populares. Los camareros anotan el pedido en el mantel de papel. Sin reservas.",
        "zh": "始于1896年的百年平民食堂，提供价格极为亲民的传统法餐（主菜仅€10起）。侍应生会在纸桌布上直接手写点单。不可预约，建议早去。",
        "fr": "Bouillon historique de 1896 proposant des classiques français à prix doux. Les serveurs écrivent l'addition directement sur la nappe en papier. Sans réservation.",
        "de": "Historisches Speiselokal von 1896 mit traditioneller französischer Küche zu sehr günstigen Preisen. Der Kellner schreibt die Bestellung auf die Papiertischdecke."
    },
    "p_25": { # Frenchie Bar à Vins
        "ja": "予約困難なミシュラン店『Frenchie』の向かいにあるカジュアルワインバー。予約不可の先着順のため、開店15分前（18:15頃）に並ぶと1巡目で入店できます。",
        "en": "Casual walk-in wine bar across from the Michelin-starred Frenchie. Arrive 15 minutes before opening at 6:30 PM to secure a table in the first seating without reservation.",
        "es": "Bar de vinos de ambiente relajado frente al galardonado Frenchie. Llega 15 minutos antes de la apertura (18:30) para asegurar mesa sin reserva.",
        "zh": "位于米其林餐厅Frenchie对面的休闲葡萄酒酒吧。无需预约，建议在18:15（开门前15分钟）前往排队，可第一批入座。",
        "fr": "Bar à vin convivial situé en face du restaurant étoilé Frenchie. Arrivez 15 minutes avant l'ouverture à 18h30 pour avoir una table au premier service.",
        "de": "Gemütliche Weinbar gegenüber dem Michelin-Restaurant Frenchie. Ohne Reservierung – kommen Sie 15 Minuten vor Öffnung um 18:30 Uhr."
    },
    "p_26": { # Les Deux Magots
        "ja": "ピカソやヘミングウェイが集ったサンジェルマンの伝説的カフェ。濃厚な『伝統の手立てホットチョコレート』をテラス席で味わうのが真骨頂です。",
        "en": "Legendary Saint-Germain café frequented by Picasso and Hemingway. Enjoy their rich thick hot chocolate served in porcelain pots on the outdoor terrace.",
        "es": "Café legendario de Saint-Germain frecuentado por Picasso y Hemingway. Disfruta de su espeso chocolate caliente tradicional en la terraza exterior.",
        "zh": "毕加索与海明威曾常光顾的圣日耳曼传奇咖啡馆。在露天座位点一杯用瓷壶盛装的浓郁传统热巧克力是最佳体验。",
        "fr": "Café mythique de Saint-Germain-des-Prés fréquenté par Picasso et Hemingway. Savourez leur chocolat chaud à l'ancienne en terrasse.",
        "de": "Legendäres Café in Saint-Germain, das von Picasso und Hemingway besucht wurde. Genießen Sie die dicke heiße Schokolade auf der Terrasse."
    },
    "p_27": { # L'As du Fallafel
        "ja": "マレ地区のユダヤ人街にあるパリ一番人気のファラフェル店。テイクアウト（Emporter）の行列に並ぶと自家製ピタパンサンドが素早く買えます（火曜定休）。",
        "en": "The undisputed king of falafel pita sandwiches in Le Marais. The takeaway line (Emporter) moves very quickly even when long. Closed Saturdays.",
        "es": "El rey indiscutible de los sándwiches de falafel en Le Marais. La cola para llevar (Emporter) avanza muy rápido. Cerrado los sábados.",
        "zh": "玛黑区犹太街最受欢迎的法拉费（中东中空饼）店。外带（Emporter）队列虽然长但移动极快。周六休息。",
        "fr": "Le roi incontesté du sandwich falafel dans le Marais. La file a emporter avance très vite. Fermé le samedi.",
        "de": "Der unangefochtene König der Falafel-Sourdough-Taschen im Marais. Die Mitnahmeschlange geht trotz der Länge sehr schnell voran. Samstags geschlossen."
    },
    "p_28": { # Pink Mamma
        "ja": "ピガール地区にある4階建てのお洒落イタリアン。最上階の天窓から光が注ぐサンルーム席が人気。事前ウェブ予約が必須です。",
        "en": "Stunning 4-story Italian trattoria in Pigalle. The top floor glass greenhouse room is the most sought-after dining spot. Book weeks ahead online!",
        "es": "Espectacular trattoria italiana de 4 plantas en Pigalle. La última planta con invernadero de cristal es la más cotizada. ¡Reserva online con semanas de antelación!",
        "zh": "皮加勒区几高人气的4层楼意式餐厅。顶层的玻璃玻璃阳光房座位最受欢迎。务必提前数周在官网预约！",
        "fr": "Superbe trattoria italienne sur 4 étages à Pigalle. La verrière au dernier étage est la salle la plus prisée. Réservation en ligne indispensable !",
        "de": "Spektakuläre 4-stöckige italienische Trattoria in Pigalle. Der Glas-Wintergarten im obersten Stockwerk ist extrem begehrt. Wochen voraus buchen!"
    },
    "p_29": { # Marché des Enfants Rouges
        "ja": "1615年開設のパリ最古の屋根付き市場。クスクス、モロッコ料理、クレープ、日本風お弁当など世界各国の屋台が集まるカジュアルランチスポット。",
        "en": "Paris's oldest covered market (1615) filled with vibrant food stalls serving Moroccan couscous, savory crepes, Lebanese, and Asian street food.",
        "es": "El mercado cubierto más antiguo de París (1615), repleto de puestos de comida internacional: cuscús marroquí, crepes, comida libanesa y asiática.",
        "zh": "建立于1615年的巴黎最古老有顶市场。汇聚摩洛哥库斯库斯、咸煎饼、黎巴嫩及亚洲美食等世界各国风味小吃摊。",
        "fr": "Le plus ancien marché couvert de Paris (1615), plein de comptoirs gourmands : couscous marocain, crêpes, cuisine libanaise et asiatique.",
        "de": "Der älteste überdachte Markt in Paris (1615) mit lebhaften Essensständen für marokkanischen Couscous, Crêpes und internationale Küche."
    },
    "p_30": { # Cédric Grolet Le Meurice
        "ja": "世界一のパティシエに選ばれたセドリック・グロレの店。本物のフルーツと見紛う芸術的な『トロンプ・ルイユ（騙し絵菓子）』が看板商品。事前のWeb予約が確実。",
        "en": "World-famous pastry chef Cédric Grolet's shop known for hyper-realistic fruit-shaped sculpted desserts. Pre-order online to skip hours of waiting.",
        "es": "La pastelería del afamado chef Cédric Grolet, conocida por sus postres hiperrealistas con forma de frutas. Pide online para evitar colas.",
        "zh": "屡获殊荣的世界顶尖甜品师Cédric Grolet的店铺，以高度逼真的拟真水果造型甜品（Trompe-l'œil）闻名。建议官网提前预约订购。",
        "fr": "La boutique du chef pâtissier Cédric Grolet, célèbre pour ses desserts trompe-l'œil en forme de fruits. Précommandez en ligne pour éviter l'attente.",
        "de": "Die Boutique des Weltklasse-Patissiers Cédric Grolet, bekannt für seine täuschend echten Dessert-Skulpturen in Fruchtform. Online vorbestellen!"
    },
    "p_31": { # Angelina Paris
        "ja": "ココ・シャネルも通った名店。超濃密な熱々ホットチョコレート『ショコラ・ショー』と濃密栗ペーストの『モンブラン』の組み合わせが看板メニュー。",
        "en": "Famous Belle Époque tearoom once frequented by Coco Chanel. Order their thick signature hot chocolate ('L'Africain') paired with a Mont-Blanc pastry.",
        "es": "Famoso salón de té de la Belle Époque frecuentado por Coco Chanel. Pide su espeso chocolate caliente 'L'Africain' y su famoso pastel Mont-Blanc.",
        "zh": "可可·香奈儿曾常光顾的著名法式茶室。必点极其浓郁的非洲款热巧克力（L'Africain）与经典蒙布朗栗子蛋糕。",
        "fr": "Salon de thé historique fréquenté en son temps par Coco Chanel. Dégustez leur traditionnel chocolat chaud l'Africain et le Mont-Blanc.",
        "de": "Berühmter Belle-Époque-Teesalon, in dem einst Coco Chanel verkehrte. Bestellen Sie die dicke heiße Schokolade 'L'Africain' und den Mont-Blanc."
    },
    "p_32": { # Du Pain et des Idées
        "ja": "サン・マルタン運河近くの伝説的パン屋。看板商品『ル・ショコラ・ピスターシュ（ピスタチオとチョコの渦巻きパン）』はパリで絶対に食べたい絶品クロワッサン生地菓子。",
        "en": "Artisanal bakery near Canal Saint-Martin. Try their iconic 'Escargot Chocolat Pistache' (pistachio and chocolate spiral pastry) baked fresh daily.",
        "es": "Panadería artesanal cerca del Canal Saint-Martin. Prueba su famoso 'Escargot Chocolat Pistache' (hojaldre en espiral de pistacho y chocolate).",
        "zh": "圣马丁运河附近的传奇手工面包店。必尝招牌“开心果巧克力蜗牛卷”（Escargot Chocolat Pistache），金黄酥脆极其美味。",
        "fr": "Boulangerie artisanale emblématique près du Canal Saint-Martin. Goûtez leur fameux Escargot Chocolat Pistache cuit sur place.",
        "de": "Handwerkliche Boulangerie nahe dem Canal Saint-Martin. Probieren Sie den berühmten 'Escargot Chocolat Pistache' (Schnecke mit Pistazie & Schokolade)."
    },
    "p_33": { # Carette Trocadéro
        "ja": "トロカデロ広場に面した有名サロン・ド・テ。自家製ホイップクリーム（シャンティイ）を贅沢に添えて飲む濃厚生チョコレートドリンクがSNSで大人気。",
        "en": "Chic tearoom at Place du Trocadéro famous for its velvety rich hot chocolate served with a giant bowl of homemade chantilly whipped cream.",
        "es": "Elegante salón de té en la Plaza del Trocadero famoso por su chocolate caliente servido con una generosa copa de nata montada casera.",
        "zh": "特罗卡德罗广场旁的时髦茶室，以特制浓郁热巧克力配巨碗手打鲜奶油（Chantilly）在社交媒体爆火。",
        "fr": "Salon de thé chic au Trocadéro célèbre pour son chocolat chaud très onctueux servi avec un grand pot de crème chantilly maison.",
        "de": "Schicker Teesalon am Trocadéro, bekannt für samtige heiße Schokolade mit einer großen Schale hausgemachter Schlagsahne."
    },
    "p_34": { # Musée du Quai Branly
        "ja": "エッフェル塔の足元にあるアフリカ・オセアニア美術の博物館。壁面一面が緑の植物で覆われた建築と、庭園から見上げるエッフェル塔の絶景が隠れた見どころ。",
        "en": "Indigenous art museum right next to the Eiffel Tower. Features a striking vertical living plant wall and peaceful gardens with unique Eiffel Tower views.",
        "es": "Museo de arte indígena junto a la Torre Eiffel. Destaca por su muro vegetal vertical y sus tranquilos jardines con vistas a la Torre Eiffel.",
        "zh": "埃菲尔铁塔旁的非西洋土著艺术博物馆。独特的绿植外墙建筑与花园内仰望埃菲尔铁塔的角度是一大亮点。",
        "fr": "Musée des arts premiers au pied de la Tour Eiffel. Il se distingue par son mur végétal et ses jardins calmes offrant une belle vue sur la tour.",
        "de": "Museum für aussereuropäische Kunst neben dem Eiffelturm. Beeindruckt mit vertikaler Pflanzenwand und Gartenblick auf den Eiffelturm."
    },
    "p_35": { # Galerie Vivienne
        "ja": "1823年建設のパリで最も美しいモザイク床を持つアーケード街。静かな古書店やアパレルショップが並び、雨の日の落ち着いた散策に最適です。",
        "en": "Paris's most elegant covered passage (1823) featuring intricate floor mosaics, glass roofs, vintage bookstores, and quiet tearooms.",
        "es": "El pasaje cubierto más elegante de París (1823) con mosaicos en el suelo, cúpula de cristal, librerías antiguas y tranquilos salones de té.",
        "zh": "建造于1823年的巴黎最典雅拱廊街，拥有精致的马赛克地板、古董书店与静谧茶室，是雨天优雅散步的最佳选择。",
        "fr": "Le plus élégant passage couvert de Paris (1823) avec ses mosaïques au sol, sa verrière et ses librairies anciennes. Parfait les jours de pluie.",
        "de": "Pariser eleganteste überdachte Passage (1823) mit kunstvollen Bodenmosaiken, Glasdach und Antiquariaten. Ideal bei Regen."
    },
    "p_36": { # Galeries Lafayette
        "ja": "本館中央の100年の歴史を持つステンドグラスドームと、8階の無料開放屋上テラスからのオペラ座＆エッフェル塔のパノラマ夜景が最大のハイライトです。",
        "en": "Don't miss the 100-year-old stained glass dome inside the main store and head up to the free 8th-floor rooftop terrace for sweeping views of the Opera and Eiffel Tower.",
        "es": "No te pierdas la cúpula de cristal de 100 años en la tienda principal y sube a la terraza gratuita del piso 8 para admirar la Ópera y la Torre Eiffel.",
        "zh": "不要错过主馆内拥有百年历史的炫彩玻璃圆顶，并务必登顶8楼免费屋顶露台，俯瞰歌剧院与埃菲尔铁塔全景。",
        "fr": "Ne manquez pas la coupole centenaire en vitrail et montez au 8e étage sur le toit-terrasse gratuit pour la vue sur l'Opéra et la Tour Eiffel.",
        "de": "Bewundern Sie die 100 Jahre alte Glaskuppel im Hauptgebäude und besuchen Sie die kostenlose Dachterrasse im 8. Stock mit Blick auf die Oper."
    },
    "p_37": { # Bateaux-Mouches
        "ja": "日没直前の便に乗ると、行きは夕焼けに染まるセーヌ川の街並み、帰りはライトアップされた夜景とエッフェル塔のシャンパンフラッシュを両方楽しめます。",
        "en": "Board a cruise right around sunset to experience Paris bathed in golden light on the way out and fully illuminated with the sparkling Eiffel Tower on the way back.",
        "es": "Embarca en un crucero justo al atardecer para ver París bañado en luz dorada a la ida y completamente iluminado a la vuelta.",
        "zh": "建议在日落前夕登船，去程可欣赏落日余晖下的塞纳河，回程可饱和观看夜景及埃菲尔铁塔闪耀灯光秀。",
        "fr": "Embarquez juste avant le coucher du soleil pour profiter des couleurs dorées à l'aller et des illuminations de la Tour Eiffel au retour.",
        "de": "Gehen Sie kurz vor Sonnenuntergang an Bord, um Paris im goldenen Abendlicht zu erleben und auf dem Rückweg die Beleuchtung zu genießen."
    },
    "p_38": { # Canal Saint-Martin
        "ja": "映画『アメリ』で水切りをしたロケ地。お洒落な太鼓橋や水門の開閉を眺めながら、沿道のインディーズカフェや古着屋を巡るローカル感あふれる散策エリア。",
        "en": "Filming location from 'Amélie'. Stroll along the iron footbridges, watch lock gates open for boats, and visit independent coffee shops and vintage boutiques.",
        "es": "Escenario de la película 'Amélie'. Pasea por sus puentes de hierro, observa cómo se abren las esclusas y visita sus cafeterías independientes.",
        "zh": "电影《天使爱美丽》打水漂的取景地。漫步于铁艺拱桥旁，观看水门开合，逛逛两旁独立咖啡馆与复古古着店。",
        "fr": "Lieu de tournage du film 'Amélie Poulain'. Flânez le long des passerelles en fonte, observez le jeu des écluses et découvrez les cafés tendance.",
        "de": "Drehort des Films 'Amélie'. Schlendern Sie über die Eisenbrücken, beobachten Sie die Schleusen und besuchen Sie kleine Vintage-Boutiquen."
    },
    "p_31_sub": { # Musée Marmottan Monet
        "ja": "「印象派」の由来となったモネの名作『印象・日の出』を所蔵。ブローニュの森に近く、団体客が少ないため静かにモネの世界に浸れる隠れた名美術館。",
        "en": "Home to Monet's groundbreaking painting 'Impression, Sunrise' which gave Impressionism its name. A tranquil museum far from large tour group crowds.",
        "es": "Alberga la obra maestra de Monet 'Impresión, sol naciente', que dio nombre al Impresionismo. Un museo tranquilo lejos de las grandes multitudes.",
        "zh": "收藏莫奈开创印象派先河的名作《印象·日出》。靠近布洛涅森林，游人较少，可沉浸式静静欣赏莫奈画作。",
        "fr": "Abrite l'œuvre fondatrice de Monet 'Impression, soleil levant'. Un musée paisible, à l'écart des grandes foules touristiques.",
        "de": "Beherbergt Monets meisterhaftes Gemälde 'Impression, Sonnenaufgang'. Ein ruhiges Museum abseits der großen Touristenmassen."
    },
    "p_32_sub": { # Fondation Louis Vuitton
        "ja": "建築家フランク・ゲーリーによる未来的な巨大ガラス船建築。屋上テラスからのブローニュの森の眺めが素晴らしく、凱旋門近くからの専用シャトルバスが便利。",
        "en": "Frank Gehry's futuristic glass vessel architecture in Bois de Boulogne. The rooftop terraces offer great forest views. Take the official shuttle bus from Arc de Triomphe.",
        "es": "Espectacular edificio en forma de barco de cristal diseñado por Frank Gehry. Las terrazas de la azotea ofrecen vistas al bosque. Autobús desde el Arco de Triunfo.",
        "zh": "建筑大师弗兰克·盖里设计的未来派玻璃巨舰建筑。顶层露台可俯瞰布洛涅森林。凯旋门旁有官方接驳巴士直达。",
        "fr": "Étonnante architecture en forme de voilier de verre signée Frank Gehry. Les terrasses offrent une vue magnifique sur le Bois de Boulogne.",
        "de": "Frank Gehrys futuristische Glas-Segelschiff-Architektur im Bois de Boulogne. Die Dachterrassen bieten einen herrlichen Blick über den Wald."
    },
    "p_33_sub": { # Musée de Cluny
        "ja": "中世の公浴場跡に建てられた美術館。世界的に有名な連作タペストリー『貴婦人と一角獣（La Dame à la licorne）』の幻想的な空間は必見です。",
        "en": "Built on ancient Roman baths in the Latin Quarter, this medieval museum displays the world-famous tapestry series 'The Lady and the Unicorn'.",
        "es": "Construido sobre antiguas termas romanas en el Barrio Latino, este museo medieval alberga el famoso tapiz 'La Dama y el Unicornio'.",
        "zh": "建于拉丁区古罗马浴场遗址之上的中世博物馆，展出举世闻名的连作织锦画《贵妇人与独角兽》。",
        "fr": "Bâti sur des thermes gallo-romains dans le Quartier Latin, ce musée médiéval abrite la célèbre tapisserie 'La Dame à la licorne'.",
        "de": "Erbaut auf antiken römischen Thermen im Quartier Latin. Zeigt die weltberühmte Wandteppich-Serie 'Die Dame mit dem Einhorn'."
    },
    "p_46": { # Disneyland Paris
        "ja": "『ディズニーランド』と『ウォルト・ディズニー・スタジオ』の2パーク構成。ピンク色の眠れる森の美女の城は世界一美しいと高評価。パリ中心部からRER A線で直結40分。",
        "en": "Features two parks: Disneyland Park and Walt Disney Studios. The pink Sleeping Beauty Castle is considered the most romantic Disney castle worldwide. 40 min via RER A train.",
        "es": "Cuenta con dos parques: Disneyland Park y Walt Disney Studios. El castillo rosa de la Bella Durmiente es considerado uno de los más bonitos del mundo. 40 min en RER A.",
        "zh": "包含迪士尼乐园与华特迪士尼影城两园。粉红色的睡美人城堡被公认为全球最浪漫的迪士尼城堡。搭乘RER A线直达仅40分钟。",
        "fr": "Comprend deux parcs : Disneyland et Walt Disney Studios. Le Château de la Belle au Bois Dormant est considéré comme le plus beau du monde. 40 min en RER A.",
        "de": "Besteht aus zwei Parks: Disneyland Park und Walt Disney Studios. Das rosa Dornröschenschloss gilt als das romantischste Disney-Schloss weltweit."
    },
    "p_47": { # Grande Galerie de l'Évolution
        "ja": "パリ植物園内にある自然史博物館。吹き抜けの大空間に剥製のアフリカゾウやキリンの大行進がドラマチックな照明で展示され、大人も子供も圧倒される隠れた傑作。",
        "en": "Located inside the Jardin des Plantes, this museum features a dramatic procession of taxidermy African savanna animals under a soaring glass roof.",
        "es": "Ubicado en el Jardin des Plantes, presenta una dramática procesión de animales disecados de la sabana africana bajo un gran techo de cristal.",
        "zh": "位于巴黎植物园内，挑高大厅在戏剧性灯光下展示着非洲野生动物标本大行进，令人震撼，是亲子游的隐秘宝藏。",
        "fr": "Situé dans le Jardin des Plantes, ce musée présente une défilé spectaculaire d'animaux naturalisés sous une grande verrière.",
        "de": "Im Jardin des Plantes gelegen, begeistert das Museum mit einer spektakulären Parade präparierter afrikanischer Wildtiere."
    },
    "p_48": { # Cité des Sciences
        "ja": "ヨーロッパ最大の科学館。体感型の実験コーナー、球形映画館『ラ・ジェオード』、プラネタリウムがあり、雨の日のファミリー体験に最適な施設。",
        "en": "Europe's largest science museum packed with interactive hands-on exhibits, a planetarium, and the iconic La Géode giant spherical IMAX theater.",
        "es": "El museo de ciencia más grande de Europa con exposiciones interactivas, un planetario y el teatro esférico gigante La Géode.",
        "zh": "欧洲最大的科学馆，充满互动动手实验区、天文馆与标志性的巨大球形影院La Géode，极其适合雨天亲子体验。",
        "fr": "Le plus grand musée des sciences d'Europe avec des expositions interactives, un planétarium et la célèbre salle sphérique La Géode.",
        "de": "Europas größtes Wissenschaftsmuseum mit interaktiven Experimenten, Planetarium und dem riesigen Kugeltheater La Géode."
    },
    "p_52": { # Musée Grévin
        "ja": "1882年創業の歴史ある蝋人形館。マリー・アントワネットやナポレオンから、現代の映画スターやスポーツ選手まで200体以上のリアルな人形と写真撮影が可能。",
        "en": "Historic wax museum operating since 1882. Take photos next to over 200 lifelike wax figures ranging from Marie Antoinette and Napoleon to modern pop stars.",
        "es": "Histórico museo de cera inaugurado en 1882. Hazte fotos con más de 200 figuras de cera de personajes desde María Antonieta hasta estrellas de cine.",
        "zh": "始于1882年的百年蜡像馆。可与从玛丽·安托瓦内特、拿破仑到现代知名影星球星在内的200多尊逼真蜡像合影。",
        "fr": "Musée de cire historique depuis 1882. Prenez des photos aux côtés de plus de 200 personnages en cire de Marie-Antoinette aux stars actuelles.",
        "de": "Historisches Wachsfigurenkabinett seit 1882. Machen Sie Fotos mit über 200 lebensgroßen Wachsfiguren von Marie Antoinette bis zu Stars."
    },
    "p_53": { # Jardin des Tuileries
        "ja": "ルーヴルとコンコルド広場を結ぶ歴史庭園。夏期（6〜8月）には大観覧車やレトロな移動遊園地（Fête Foraine）が登場し、お祭り気分が味わえます。",
        "en": "Stretching between the Louvre and Place de la Concorde. In summer (June–August), a funfair with a giant Ferris wheel operates inside the park.",
        "es": "Se extiende entre el Louvre y la Plaza de la Concordia. En verano (junio-agosto), se instala una gran feria con una gran noria.",
        "zh": "连接卢浮宫与协和广场的历史悠久花园。每年夏季（6月-8月）园内会举办包含摩天轮在内的复古移动游乐场（Fête Foraine）。",
        "fr": "S'étend entre le Louvre et la Place de la Concorde. En été (juin-août), une fête foraine avec grande roue s'installe dans le jardin.",
        "de": "Erstreckt sich zwischen dem Louvre und dem Place de la Concorde. Im Sommer (Juni–August) findet im Park ein Jahrmarkt mit Riesenrad statt."
    },
    "p_54": { # Musée de l'Air et de l'Espace
        "ja": "ル・ブルジェ空港にある最古の航空博物館。超音速旅客機『コンコルド』の実機2機（試作機と量産機）の機内に入って見学できる世界唯一の場所です。",
        "en": "Located at Le Bourget Airport, this is the only place in the world where you can step inside two actual supersonic Concorde aircraft side by side.",
        "es": "Ubicado en el aeropuerto de Le Bourget, es el único lugar del mundo donde puedes subir a bordo de dos aviones supersónicos Concorde reales.",
        "zh": "位于勒布尔热机场，是全球唯一一处可以踏入两架真实协和号（Concorde）超音速客机内部进行参观的场所。",
        "fr": "Situé à l'aéroport du Bourget, c'est le seul endroit au monde où vous pouvez visiter l'intérieur de deux véritables Concorde.",
        "de": "Am Flughafen Le Bourget gelegen – der einzige Ort der Welt, an dem Sie das Innere von zwei echten Concorde-Supersonic-Flugzeugen betreten können."
    },
    "p_55": { # Choco-Story Paris
        "ja": "チョコの4000年の歴史を学ぶ体験型博物館。プロのショコラティエによるリアルタイムの実演見学と本格チョコレートの試食が楽しめるチョコ好き必見スポット。",
        "en": "Gourmet chocolate museum featuring live chocolate-making demonstrations by master chocolatiers and unlimited tastings throughout the tour.",
        "es": "Museo del chocolate gourmet con demostraciones en vivo de maestros chocolateros y degustaciones durante todo el recorrido.",
        "zh": "美食巧克力博物馆，提供专业巧克力师现场实演与全程高品质巧克力试吃体验，巧克力爱好者必去。",
        "fr": "Musée gourmand du chocolat proposant des démonstrations en direct par des maîtres chocolatiers et des dégustations.",
        "de": "Schokoladenmuseum mit Live-Demonstrationen von Chocolatiers und Verkostungen während des gesamten Rundgangs."
    }
}

updated_count = 0
for spot in data["spots"]:
    sid = spot["id"]

    tip_data = None
    if sid in paris_tips:
        tip_data = paris_tips[sid]
    else:
        name_lower = spot["name"].lower()
        if "marmottan" in name_lower:
            tip_data = paris_tips["p_31_sub"]
        elif "louis vuitton" in name_lower:
            tip_data = paris_tips["p_32_sub"]
        elif "cluny" in name_lower:
            tip_data = paris_tips["p_33_sub"]

    if tip_data:
        spot["tip_ja"] = tip_data["ja"]
        spot["tip_en"] = tip_data["en"]
        spot["tip_es"] = tip_data["es"]
        spot["tip_zh"] = tip_data["zh"]
        spot["tip_fr"] = tip_data["fr"]
        spot["tip_de"] = tip_data["de"]
        spot["tip"] = tip_data["en"]
        updated_count += 1
    else:
        spot["tip_ja"] = ""
        spot["tip_en"] = ""
        spot["tip_es"] = ""
        spot["tip_zh"] = ""
        spot["tip_fr"] = ""
        spot["tip_de"] = ""
        spot["tip"] = ""

with open(paris_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {updated_count} Paris spots with fresh insider tips in 6 languages!")
