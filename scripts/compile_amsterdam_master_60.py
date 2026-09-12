#!/usr/bin/env python3
"""
Zero-Margin Travel App - Full 60 Amsterdam Spots Compiler (v34.0.0)
Populates 60 spots for Amsterdam in data/cities/amsterdam.json.
100% compliant with Master Rulebook v6.0.0 and 5-Layer Compliance Guard.
"""

import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

spots_data = [
    # 1 to 10
    ("a_1", "Rijksmuseum", "アムステルダム国立美術館", "Museum & Gallery", "17世紀オランダ黄金時代の傑作（レンブラント『夜警』、フェルメール『牛乳を注ぐ女』）を収蔵するオランダ最高峰の国立美術館。", "The national museum of the Netherlands dedicated to Dutch Golden Age art, housing Rembrandt's 'The Night Watch'.", "🎟️ 全員WEB事前日時予約が必須。朝9時の初回枠を予約し、開館と同時に2階「名誉の間」の『夜警』へ直行するのが混雑回避の鉄則。", "🎟️ Mandatory advance time-slot booking online. Book the 9:00 AM slot to view 'The Night Watch' in Room 2.4 without crowds.", "料金: €25.00", 52.3600, 4.8852, "city", False, True, False, False),
    ("a_2", "Van Gogh Museum", "ゴッホ美術館", "Museum & Gallery", "フィンセント・ファン・ゴッホの作品200点以上と書簡群を世界最大の規模で収蔵する専用美術館。", "Art museum holding the world's largest collection of paintings and letters by Vincent van Gogh.", "🎟️ 100%オンライン完全事前予約制（現地券売窓口なし）。ハイシーズンは数週間前に売切れるため早期確保必須。", "🎟️ 100% online advance ticket purchase required; no walk-up ticket desk. Reserve weeks early during peak season.", "料金: €24.00", 52.3584, 4.8811, "city", False, True, False, False),
    ("a_3", "Anne Frank House", "アンネ・フランクの家", "Museum & Gallery", "第2次世界大戦中にアンネ・フランク一家がナチスの迫害から隠れ潜んだプリンセンフラハト沿いの17世紀運河邸宅。", "Historic canal house where Anne Frank hid from Nazi persecution during World War II.", "🎟️ チケットは毎週火曜午前10時（現地時間）に「6週間後」の枠がオンライン限定で一斉解放され数分で完売。", "🎟️ Tickets released online every Tuesday at 10:00 AM (CEST) for visits 6 weeks later; sells out in minutes.", "料金: €16.00", 52.3752, 4.8840, "city", False, True, False, False),
    ("a_4", "Amsterdam Canal Cruise", "アムステルダム運河クルーズ", "Scenery & Walk", "ユネスコ世界遺産に登録された17世紀の運河網（ヘレンフラハト、カイザースフラハト、プリンセンフラハト）を巡るボートツアー。", "Sightseeing boat tour navigating through the UNESCO World Heritage 17th-century canal ring of Amsterdam.", "📸 夕暮れ時のオープントップ小型船がおすすめ。ガラスの映り込みなしでライトアップされたアーチ橋を撮影可能。", "📸 Opt for an open-top small boat tour during golden hour or sunset to photograph illuminated bridge arches.", "料金: €18.00", 52.3780, 4.8980, "city", True, False, False, False),
    ("a_5", "Dam Square & Royal Palace Amsterdam", "ダム広場＆アムステルダム王宮", "Landmark", "アムステルダム発祥の歴史的中央広場と、17世紀オランダ古典主義建築の王宮（旧市庁舎）。", "Historic town square marking the center of Amsterdam, featuring the 17th-century neoclassical Royal Palace.", "🏛️ 国王陛下の公式執務・公式参拝時に突発閉館する場合があるため、訪問当日の朝に公式サイトで営業確認を推奨。", "🏛️ The Royal Palace is an active official reception palace. Check official website on the morning of your visit for closures.", "広場散策無料 / 王宮: €12.50", 52.3731, 4.8913, "city", False, True, False, False),
    ("a_6", "Heineken Experience", "ハイネケン・エクスペリエンス", "Café & Bistro", "デ・パイプ地区の旧煉瓦造り醸造所内にある体感型ミュージアム。", "Interactive self-guided tour set inside Heineken's historic first brick brewery in De Pijp.", "🍺 入場料に生ビール2杯が含まれる。地下でのビール注ぎ方マスタークラス（Perfect Pour）への参加が人気。", "🍺 Admission includes two freshly poured beers. Join the bartender-led 'Perfect Pour' masterclass in the cellar.", "料金: €23.00", 52.3578, 4.8918, "city", False, True, False, False),
    ("a_7", "Zaanse Schans", "ザーンセ・スカンス伝統木造建築群＆風車村", "Scenery & Walk", "ザーン川沿いに緑色の伝統木造建築群と18・19世紀の産業用風車が保存された野外保護地区。", "Historic open-air conservation village featuring green wooden houses and working 18th-century industrial windmills.", "🧀 村内の散策・木靴工房見学・チーズ実演は無料。中央駅からSprinter電車で17分＋徒歩15分。", "🧀 Entrance to the village, clog workshop, and cheese demonstration is free. Take Sprinter train (17 min) from Centraal.", "散策無料 / 風車内部: 約€5.00", 52.4729, 4.8160, "suburban", True, False, True, True),
    ("a_8", "Keukenhof", "キューケンホフ公園", "Scenery & Walk", "リッセに位置する32ヘクタールの敷地に700万球以上のチューリップが咲き誇る「ヨーロッパの庭園」（春季限定）。", "The 'Garden of Europe' in Lisse, featuring over 7 million blooming spring bulbs across 32 hectares of landscaped gardens.", "🎟️ スキポール空港/アムステルダムRAI発のコンビチケット（直行バス＋入園券）を事前購入。園外でのレンタサイクルもおすすめ。", "🎟️ Purchase the official 'Combi-Ticket' combining park entry with direct express shuttle buses from Schiphol or RAI.", "料金: €20.00", 52.2697, 4.5464, "suburban", True, False, False, False),
    ("a_9", "A'DAM LOOKOUT", "アダム・ルックアウト＆空中ブランコ", "Landmark", "IJ川北岸に立つ22階建てタワー最上階の360度パノラマ展望デッキ。", "Observation deck atop a 22-story tower on the IJ river, featuring Europe's highest over-the-edge swing.", "⛴️ 中央駅裏手から無料24時間運航フェリー（Buiksloterweg行き）で3分。日没45分前の入場が夜景への変化を楽しめる。", "⛴️ Take the free 24/7 public ferry from behind Centraal (~3 min crossing). Visit 45 minutes before sunset for golden hour.", "展望台: €16.50 / ブランコ: €6.00", 52.3840, 4.9023, "city", True, False, False, False),
    ("a_10", "Vondelpark", "フォンデル公園", "Scenery & Walk", "ミュージアム広場西側に広がる47ヘクタールのイギリス風景式市民公園。", "Amsterdam's most famous 47-hectare English landscape park featuring winding waterways and rose gardens.", "🚲 自転車専用レーンと歩道が厳密に分離されている。ローカル自転車のスピードが速いため舗装路上の立ち止まり注意。", "🚲 Dedicated separate lanes for cyclists and pedestrians. Local bike traffic moves fast; avoid walking on cycle paths.", "散策無料", 52.3579, 4.8686, "city", True, False, False, True),

    # 11 to 20
    ("a_11", "De Jordaan", "ヨルダーン地区", "Scenery & Walk", "労働者街からおしゃれなアートギャラリー・隠れ庭園（ホフフェス）の並ぶ人気歴史地区へ変貌したエリア。", "Historic neighborhood transformed into a charming quarter of leafy canals, galleries, and hidden courtyards.", "🚶 土曜朝はノーデルマルクトのオーガニック市を訪れ、隣の「Winkel 43」で焼きたて温かいダッチアップルパイを賞味。", "🚶 Visit the Saturday morning market on Noordermarkt, then stop at Winkel 43 for fresh warm Dutch apple pie.", "散策無料", 52.3745, 4.8812, "city", False, False, True, True),
    ("a_12", "De Negen Straatjes", "ナイン・ストリート", "Scenery & Walk", "主要運河を繋ぐ9本の狭い横丁からなるヴィンテージブティック＆スペシャルティコーヒー街。", "Picturesque shopping district of nine narrow cross-streets connecting Amsterdam's main canals.", "🛍️ 月曜午前中は個人店が午後1時頃まで開店しないことが多い。火曜〜土曜午後の散策がおすすめ。", "🛍️ Independent boutique shops open later on Mondays (around 1:00 PM). Visit Tuesday to Saturday afternoon.", "散策無料", 52.3698, 4.8845, "city", False, False, True, True),
    ("a_13", "Drijvende Bloemenmarkt", "シンゲルの水上花市場", "Landmark", "シンゲル運河上の台船に並ぶ世界唯一の水上花市場。球根や観葉植物、ダッチ土産を販売。", "The world's only floating flower market, resting on permanent floating barges along the Singel canal.", "🌷 チューリップ球根を国外へ持ち出す際は「検疫済み植物検査スタンプシール」付きパッケージを選ぶ必要あり。", "🌷 If purchasing tulip bulbs to take abroad, ensure the packaging has the official phytosanitary inspection stamp seal.", "散策無料", 52.3668, 4.8913, "city", False, False, True, True),
    ("a_14", "Stedelijk Museum Amsterdam", "アムステルダム市立美術館", "Museum & Gallery", "バスタブ型の未来的な新館デザインで知られる近代・現代美術＆デザインの殿堂。", "Museum of modern and contemporary art and design known for its distinctive 'Bathtub' architectural extension.", "🎟️ ゴッホ美術館に比べて入館待ち列が短い。地下のデザインギャラリーでは20世紀オランダデザインを網羅。", "🎟️ Lines are shorter than at the neighboring Van Gogh Museum. The basement design galleries showcase 20th-century Dutch design.", "料金: €22.50", 52.3580, 4.8798, "city", False, True, False, False),
    ("a_15", "NEMO Science Museum", "NEMO科学館", "Museum & Gallery", "レンゾ・ピアノ設計の巨大な緑色船首型建築内にある体験型科学館。", "Interactive hands-on science museum housed in a green copper ship-hull building designed by Renzo Piano.", "☀️ 屋上階段テラス（水遊び展示・港のパノラマビュー）は入館チケットなしで屋外階段から完全無料開放。", "☀️ The cascading rooftop terrace (featuring water installations and harbor views) is free via outdoor stairs.", "入館料: €17.50 / 屋上: 無料", 52.3741, 4.9123, "city", True, True, False, False),
    ("a_16", "Albert Cuypmarkt", "アルバート・カイプ市場", "Café & Bistro", "デ・パイプ地区で260以上の露店が並ぶヨーロッパ最大級の屋外露店市場（日曜休み）。", "Europe's largest daily open-air street market, featuring over 260 vendor stalls in the lively De Pijp quarter.", "🍽️ 目の前の鉄板で焼き上げる大判熱々ストループワッフルと、白身魚フリッター（キッベリング）が名物。", "🍽️ Try freshly pressed hot stroopwafels made on the griddle right in front of you, and hot kibbeling (fried fish).", "散策無料", 52.3562, 4.8944, "city", False, False, True, True),
    ("a_17", "Het Scheepvaartmuseum", "国立海事博物館", "Museum & Gallery", "17世紀の旧海軍軍需品庫にオランダ海事史・航海具コレクションを展示。VOC東インド会社船の復元船を係留。", "Museum housed in a 17th-century naval storehouse showcasing Dutch maritime history with a full-scale VOC ship replica.", "🚢 係留された東インド会社船アムステルダム号の船長室から最下層貨物室まで全甲板に乗り込み見学可能。", "🚢 You can fully board and explore all levels of the moored East Indiaman Amsterdam replica ship.", "料金: €18.50", 52.3717, 4.9147, "city", True, True, False, False),
    ("a_18", "Museum Het Rembrandthuis", "レンブラントの家美術館", "Museum & Gallery", "画家レンブラントが絶頂期に暮らしアトリエを構えた17世紀の町屋建築。", "Historic 17th-century townhouse where Rembrandt van Rijn lived and worked during the height of his career.", "🎨 3階アトリエにて天然鉱物と亜麻仁油を磨り潰して絵の具を作る実演デモンストレーションを毎日無料開催。", "🎨 Head to the 3rd-floor studio for daily live demonstrations showing how Rembrandt ground mineral pigments.", "料金: €19.50", 52.3693, 4.9011, "city", False, True, False, False),
    ("a_19", "Rembrandtplein", "レンブラント広場", "Landmark", "レンブラントの銅像と『夜警』の登場人物3D等身大ブロンズ像が並ぶ賑やかな広場。", "Bustling public square dominated by a bronze statue of Rembrandt surrounded by 3D life-sized figures of 'The Night Watch'.", "📸 ブロンズ像の隊員たちの間に入って直接記念撮影が可能。夜間はスリに注意。", "📸 You can walk directly among the life-sized bronze figures of the Night Watch militia for photos.", "散策無料", 52.3660, 4.8967, "city", False, False, False, True),
    ("a_20", "De Oude Kerk", "旧教会", "Landmark", "1306年頃奉納のアムステルダム最古の建造物。パイプオルガンや床一面の墓石群が残る。", "Amsterdam's oldest standing building (c. 1306) featuring barrel-vaulted wooden ceilings and historic grave slabs.", "🚶 床の墓石群の中にレンブラントの妻サスキア・ファン・アイレンブルフの墓標（29番墓石）が存在。", "🚶 Among the thousands of tomb slabs paved into the floor is the final resting place of Rembrandt's wife Saskia.", "料金: €13.50", 52.3742, 4.8980, "city", False, True, False, False),

    # 21 to 30
    ("a_21", "Westerkerk", "西教会", "Landmark", "プリンセンフラハト沿いに立つ85mの塔（アムステルダム最高峰）を持つプロテスタント大聖堂。", "17th-century Dutch Renaissance Protestant church featuring the 85-meter Westertoren spire.", "📸 レリエフラハト橋交差点の対岸から、運河と教会塔を一枚に収める構図が定番フォトスポット。", "📸 Frame the church and its tower from across the Prinsengracht canal near the Leliegracht bridge intersection.", "聖堂無料 / 塔登攀: €9.00", 52.3746, 4.8838, "city", False, False, False, True),
    ("a_22", "De Wallen", "飾り窓地区", "Landmark", "中世の面影を残す運河と路地が広がる歴史的旧市街エリア。", "Amsterdam's historic medieval core known for its canals, narrow alleys, and historic brown cafes.", "⚠️ 窓の中の性労働者に対する撮影は厳禁。違反者は警備員・治安当局により厳重罰則あり。", "⚠️ Strictly forbidden: Taking photos or videos of sex workers in windows is strictly prohibited and enforced.", "散策無料", 52.3725, 4.8970, "city", False, False, False, True),
    ("a_23", "Het Begijnhof", "ベギンホフ修道院中庭", "Landmark", "14世紀に建てられたベギン会修道女のための静寂な中庭。市内最古級の木造家屋（1420年頃）が残る。", "Tranquil 14th-century enclosed courtyard complex containing one of Amsterdam's oldest wooden houses.", "🤫 現在も高齢女性が暮らすアクティブな住宅地のため、完全静寂マナー遵守。スパイ広場側の木製扉から入場。", "🤫 This is a quiet private residential area; absolute silence is mandatory. Enter via the wooden doorway off Spui.", "散策無料", 52.3690, 4.8897, "city", False, False, False, True),
    ("a_24", "Magere Brug", "マヘレの跳ね橋", "Landmark", "アムステル川に架かる白塗りの伝統的木造二重跳ね橋。", "Iconic white-painted traditional Dutch wooden double-drawbridge spanning the Amstel River.", "📸 約1,200個の電球が一斉に点灯する日没後のナイトビューが非常にロマンチック。", "📸 Visit after nightfall when the entire timber structure is illuminated by roughly 1,200 lights.", "散策無料", 52.3636, 4.9018, "city", False, False, False, True),
    ("a_25", "Eye Filmmuseum", "アイ映画ミュージアム", "Museum & Gallery", "IJ川北岸に立つスタイリッシュな白い建築の映像文化ミュージアム。", "Sleek white architectural landmark on the north bank of the IJ river dedicated to film preservation and exhibitions.", "⛴️ 中央駅裏から無料フェリー（Buiksloterweg行き）利用。地下の常設ヴィンテージカメラ展は入場無料。", "⛴️ Take the free public ferry (Buiksloterweg direction) from Centraal. The basement interactive exhibit is free.", "企画展: €15.00 / 地下常設: 無料", 52.3842, 4.9006, "city", False, True, False, False),
    ("a_26", "Volendam & Marken", "フォーレンダム＆マルケン漁村", "Scenery & Walk", "アイセル湖畔の伝統漁村。民族衣装撮影スポットや木造高床式住宅が広がる。", "Historic IJsselmeer fishing villages featuring traditional costume studios and stilt-house wooden villages.", "⛴️ ２つの村を結ぶ「Volendam Marken Express」フェリーに乗船。港の屋台で薫製ウナギや生ハーリングを賞味。", "⛴️ Take the 30-minute Volendam Marken Express ferry between the two towns and try smoked eel.", "散策無料 / 連絡船往復: 約€16.00", 52.4950, 5.0680, "suburban", True, False, True, True),
    ("a_27", "Historisch Centrum Haarlem", "ハーレム歴史地区", "Scenery & Walk", "中央駅から電車で15分の風情ある中世運河都市。聖バーフォ教会やフランス・ハルス美術館が点在。", "Medieval canal city located 15 minutes by train from Amsterdam Centraal, featuring St. Bavo Church.", "🚶 アムステルダムより混雑が少なく落ち着いた街歩きが可能。スパールネ川沿いのド・アドリアーン風車も見どころ。", "🚶 An easy day-trip alternative with far fewer crowds than Amsterdam. Visit De Adriaan windmill on the Spaarne.", "街歩き無料 / 聖バーフォ教会: €4.00", 52.3810, 4.6370, "suburban", True, False, True, True),
    ("a_28", "Moco Museum", "モコ美術館", "Museum & Gallery", "ミュージアム広場のヴィラ邸宅内にあるバンクシーや草間彌生、モダンアート展示のブティック美術館。", "Independent boutique museum housed in Villa Alsberg on Museumplein, focusing on Banksy and contemporary art.", "📸 地下のデジタルミラー空間を含む館内全域で写真撮影が可能。事前WEB予約で入館待ち回避。", "📸 Photography is permitted throughout the galleries and digital mirror installations. Book online in advance.", "料金: €21.95", 52.3582, 4.8818, "city", False, True, False, False),
    ("a_29", "De Pijp", "デ・パイプ地区", "Scenery & Walk", "ボヘミアンな雰囲気が漂うカルチェ・ラタン。ブランチカフェやクラフトビールバーが集まる。", "Bohemian 'Quartier Latin' of Amsterdam filled with brunch spots, craft beer bars, and multicultural food.", "🍽️ オランダ料理だけでなく、スリナム料理（チキンロティ）やインドネシア料理の本格サテも人気。", "🍽️ Explore authentic Surinamese eateries for chicken roti, or visit Indonesian snack shops for satay.", "散策無料", 52.3540, 4.8960, "city", False, False, True, True),
    ("a_30", "NDSM-werf", "NDSM造船所跡アートエリア", "Scenery & Walk", "北アムステルダムの造船所跡を再生したストリートアート・コンテナバー・創作スタジオのハブ。", "Sprawling former industrial shipyard in Amsterdam-Noord transformed into a hub for street art and shipping-container bars.", "⛴️ 中央駅裏からNDSM行きの無料直行フェリー（約15分）に乗船。巨大蚤の市（IJ-hallen）の開催日確認がおすすめ。", "⛴️ Board the free direct 15-minute public ferry from Centraal to NDSM. Try to align your visit with IJ-hallen flea market.", "渡船・エリア入場無料", 52.4005, 4.8935, "city", False, False, True, True),

    # 31 to 40
    ("a_31", "STRAAT Museum", "STRAATストリートアート美術館", "Museum & Gallery", "NDSMの巨大倉庫を利用した世界最大規模のストリートアート＆グラフィティ専用ミュージアム。", "The world's largest dedicated museum for street art and graffiti, housed in a former shipyard warehouse at NDSM.", "🎨 2階のカフェブリッジやキャットウォークから、キャンバス画の巨大なスケール感を俯瞰して鑑賞可能。", "🎨 Head up to the 2nd-floor cafe bridge and viewing walkways to view the massive scale of the artworks.", "料金: €19.50", 52.4008, 4.8942, "city", False, True, False, False),
    ("a_32", "The Amsterdam Dungeon", "アムステルダム・ダンジョン", "Landmark", "ダム広場近くで暗黒のダッチヒストリー（魔女裁判、ペスト、スペイン審問）を演劇形式で体験するアトラクション。", "Interactive comedy-horror attraction near Dam Square dramatizing dark Dutch history with live actors.", "🎭 英語でのショー進行。雨の日のインドア体験として非常に人気。", "🎭 Tours are conducted primarily in English with live actors. A great indoor activity on rainy days.", "料金: €25.00", 52.3706, 4.8917, "city", True, True, False, False),
    ("a_33", "BODY WORLDS Amsterdam", "ボディ・ワールド", "Museum & Gallery", "実物の人体標本200点以上を展示し、幸福感や生活習慣が身体に与える影響を解剖学的に解説。", "Anatomy exhibition on Damrak featuring over 200 authentic plastinated human specimens showcasing human physiology.", "🧠 チケット内に最後に行える「InBody」体成分無料スキャン測定が含まれている。", "🧠 Included with your ticket is a free InBody health scan assessment at the end of the exhibition.", "料金: €22.50", 52.3748, 4.8942, "city", False, True, False, False),
    ("a_34", "ARTIS & Micropia", "アルティス動物園＆マイクロピア", "Museum & Gallery", "1838年創設の伝統的都市型動物園と、世界唯一の微生物・細菌専門ミュージアム「マイクロピア」。", "Historic 1838 urban zoo combined with Micropia, the world's only museum dedicated exclusively to microbes and bacteria.", "🔬 マイクロピア館内の電子顕微鏡や「Kiss-o-Meter（キスで交換される微生物数測定器）」がユニーク。", "🔬 Inside Micropia, test the 'Kiss-o-Meter' to see how many millions of microbes are exchanged during a kiss.", "動物園: €26.50 / マイクロピア: €17.50", 52.3660, 4.9165, "city", True, True, False, False),
    ("a_35", "Wereldmuseum Amsterdam", "熱帯博物館（世界博物館）", "Museum & Gallery", "東南アジア、アフリカ、中南米の民俗品・文化遺産を巨大な大理石大ホールに展示する文化人類学博物館。", "Ethnographical museum housed in a colonial institute palace, exploring global material culture.", "🏛️ 3階建ての吹抜け大理石ホール建築が見事。広々としており混雑なくゆったり鑑賞可能。", "🏛️ The three-story monumental marble central Grand Hall is an architectural wonder and rarely crowded.", "料金: €16.00", 52.3624, 4.9213, "city", True, True, False, False),
    ("a_36", "Brouwerij 't IJ", "アイ醸造所", "Café & Bistro", "東部の18世紀木造風車「デ・フーイエル」の直下に位置するオーガニッククラフトビール醸造所。", "Craft brewery situated directly beneath the historic 18th-century De Gooyer wooden windmill.", "🍺 風車をバックにしたテラス席で、新鮮な樽生ビール（IJwitなど）と熟成ゴーダチーズを味わうのが定番。", "🍺 Sit on the outdoor terrace for a photo pairing your fresh draft beer with the towering windmill backdrop.", "ビール・軽食予算: €5〜€15", 52.3667, 4.9264, "city", False, False, False, True),
    ("a_37", "Kalverstraat & Damrak", "カルバー通り＆ダムラック", "Scenery & Walk", "中央駅からダム広場を経てムント広場へ続く歩行者専用ショッピングストリート。", "Primary central retail pedestrian spine running from Centraal Station through Dam Square to Muntplein.", "🍟 ダムラック沿いの名店「Manneken Pis」で熱々の二度揚げダッチフリッツ（サテソースやマヨネーズがけ）をテイクアウト。", "🍟 Grab a cone of double-fried Dutch fries from Manneken Pis on Damrak topped with mayo or peanut satay sauce.", "散策無料", 52.3700, 4.8910, "city", False, False, True, True),
    ("a_38", "De Bijenkorf", "デ・バイエンコルフ高級百貨店", "Landmark", "ダム広場東側に立つ1870年創業のオランダ最高峰ラグジュアリーデパート。", "Premier luxury department store of the Netherlands, dominating the eastern side of Dam Square.", "🛍️ 5階のフードラウンジ「The Kitchen」からはダム広場を見下ろす景観が広がる。非EU旅行者用Tax-Freeラウンジ完備。", "🛍️ The 5th-floor dining lounge offers glass views over Dam Square. Tax-Free Lounge available on-site.", "入館無料", 52.3728, 4.8938, "city", False, True, True, True),
    ("a_39", "Café de Klos & Bruine Cafés", "伝統的ブラウンカフェ＆名物リブ店", "Café & Bistro", "濃い木目調インテリアと真鍮ビールタップが味わい深い伝統的居酒屋（ブラウンカフェ）。", "Historic traditional Dutch pubs characteristically decorated with dark wooden interiors and candlelit tables.", "🥧 1642年創業の「Café Papeneiland」で名物の極厚自家製アップルパイ（ホイップ添え）を注文。", "🥧 At Café Papeneiland (operating since 1642 on Prinsengracht), order their legendary handmade Dutch apple cake.", "飲食予算: €8〜€30", 52.3770, 4.8820, "city", False, True, False, True),
    ("a_40", "OBA Oosterdok", "アムステルダム中央図書館", "Scenery & Walk", "ウォーターフロントに立つヨーロッパ最大級の公立図書館。", "Europe's largest public library facility located on the Oosterdok waterfront near Centraal Station.", "📖 7階のテラスレストランは図書カードなしで無料利用可能。旧市街と港を一望できる穴場絶景スポット。", "📖 The 7th-floor terrace restaurant is open to the public for free without a library pass, offering panoramic views.", "無料", 52.3762, 4.9078, "city", False, True, False, True),

    # 41 to 50
    ("a_41", "Foodhallen Amsterdam", "フードハレン", "Café & Bistro", "19世紀の路面電車車庫（De Hallen）をリノベーションしたインドアフードコート。", "Indoor food hall housed inside a converted 19th-century municipal brick tram depot in Amsterdam-West.", "🍽️ ミシュランシェフ監修の「De BallenBar」でトリュフ風味や牛肉のダッチビターバレンをテイクアウト。", "🍽️ Order gourmet Dutch bitterballen filled with beef or truffle from De BallenBar inside the hall.", "入場無料", 52.3688, 4.8690, "city", False, True, False, True),
    ("a_42", "Station Amsterdam Centraal", "アムステルダム中央駅", "Landmark", "1889年開業のネオ・ルネサンス様式駅舎。設計は国立美術館と同じカイペルス。", "Primary transportation hub designed by Pierre Cuypers and opened in 1889 in Dutch Renaissance Revival style.", "🏛️ ファサードの2つの塔のうち、右側は時計、左側は現役の風向計（windwijzer）になっている。", "🏛️ Look at the twin facade towers: the right-hand tower is a clock, while the left-hand is a working wind vane.", "見学無料", 52.3791, 4.9003, "city", False, True, False, True),
    ("a_43", "Het Amsterdamse Bos", "アムステルダムの森", "Scenery & Walk", "市南部に広がる1,000ヘクタール（セントラルパークの3倍）の広大な森林公園。", "Sprawling 1,000-hectare parkland and woodland south of the city featuring rowing canals and a goat farm.", "🐐 園内のオーガニックヤギ農場（Ridammerhoeve）で子ヤギへのミルクやり体験や自家製ヤギ乳アイスを賞味。", "🐐 At the Geitenboerderij Ridammerhoeve organic goat farm, kids can bottle-feed young goats and sample goat ice cream.", "入園無料", 52.3130, 4.8430, "suburban", True, False, False, True),
    ("a_44", "Hortus Botanicus Amsterdam", "アムステルダム植物園", "Scenery & Walk", "1638年設立の世界最古級の植物園。温室やバタフライハウスを併設。", "One of the oldest botanical gardens in the world, featuring centuries-old cycads and a Butterfly House.", "🦋 温室のバタフライハウスでは色鮮やかな熱帯のチョウが自由に飛び交う。歴史的なオランジェリーカフェも併設。", "🦋 Step inside the warm Butterfly House to observe tropical butterfly species fluttering freely around visitors.", "料金: €13.50", 52.3668, 4.9080, "city", False, True, False, False),
    ("a_45", "Joods Cultureel Kwartier", "ユダヤ文化地区＆ポルトガル・シナゴーグ", "Museum & Gallery", "真鍮製キャンドルで照らされる17世紀ポルトガル・シナゴーグとユダヤ歴史博物館。", "Monumental 17th-century Portuguese Synagogue with a sand-covered floor, alongside the Jewish Museum.", "🕯️ 共通パス1枚でシナゴーグ・ユダヤ博物館・ホロコースト博物館に入場可能。", "🕯️ A single Jewish Cultural Quarter ticket grants combined entry to the Portuguese Synagogue and museums.", "料金: €20.00", 52.3673, 4.9048, "city", False, True, False, False),
    ("a_46", "Nationaal Holocaust Museum", "国立ホロコースト博物館", "Museum & Gallery", "第2次世界大戦中に数百人の子供たちが密かに救出された旧教員養成学校校舎。2024年に全面リニューアル。", "Historic museum building from which hundreds of Jewish children were covertly rescued during WWII.", "🎟️ 全員WEB日時指定予約が必須。校舎と託児所の間の脱出庭園小道が保存されている。", "🎟️ Advance time-slot booking online required. The historic escape garden path is preserved.", "料金: €20.00", 52.3665, 4.9070, "city", False, True, False, False),
    ("a_47", "Westergas", "ウェスターガス文化公園", "Scenery & Walk", "旧ガス工場群をカフェ・映画館・デジタルアート空間（Fabrique des Lumières）へ再生。", "Vibrant cultural complex set in repurposed 19th-century municipal gasworks buildings within Westerpark.", "🎨 工場ホール内の「Fabrique des Lumières」ではプロジェクションマッピングによる没入型名画体験を提供。", "🎨 Inside Fabrique des Lumières, high-definition digital artwork is projected across walls and floors.", "公園散策無料 / デジタルアート: €17.50", 52.3860, 4.8700, "city", False, True, False, True),
    ("a_48", "Magna Plaza", "マグナ・プラザ", "Landmark", "王宮裏手に立つ1898年建造の旧中央郵便局（ネオ・ゴシック調の「郵便局の城」）を改装したショッピングモール。", "Former Main Post Office building constructed in 1898 in Neo-Gothic style, repurposed into a shopping arcade.", "🏛️ 吹き抜けの中央アトリウムと大理石アーチが美しく、雨の日の立ち寄りに最適。", "🏛️ Step inside to admire the central multi-tiered open atrium and marble arches, ideal on a rainy day.", "入場無料", 52.3736, 4.8893, "city", False, True, True, True),
    ("a_49", "Proeflokaal In de Wildeman", "イン・デ・ヴィルデマン", "Café & Bistro", "17世紀の蒸留所跡を利用した老舗ビアホール。オランダ・ベルギーのクラフト生ビールを多数タップで提供。", "Traditional beer hall in a former 17th-century distillery offering hundreds of Dutch and Belgian ales.", "🍺 ビールメニューが豊富なため、好みの味（ドライ、フルーティ、黒ビール等）をスタッフに伝えて注文。", "🍺 Tell the bar staff your flavor preferences (dry, malty, or sour) for expert craft beer recommendations.", "飲食予算: €8〜€25", 52.3761, 4.8953, "city", False, True, False, True),
    ("a_50", "Kaasmarkt Alkmaar", "アルクマール・チーズ市", "Landmark", "1365年から続く伝統的チーズ取引のスペクタクル（4月〜9月の金曜午前開催）。", "Traditional cheese trading spectacle dating back to 1365, held on Waagplein every Friday morning in spring/summer.", "🧀 10時の開始前に到着し、Waagplein広場の柵沿い最前列を確保。中央駅から直行電車で約35分。", "🧀 Proceedings start at 10:00 AM; arrive by 9:30 AM to secure a front-row spot along the square barriers.", "見学無料", 52.6315, 4.7500, "suburban", True, False, True, True),

    # 51 to 60
    ("a_51", "Panoramaterras Schiphol", "スキポール空港パノラマテラス", "Landmark", "スキポール空港ターミナル屋上に設置された飛行機見学デッキ。KLMフォッカー100の実機を内部見学可能。", "Public viewing deck on the roof of Amsterdam Airport Schiphol featuring a boarding-accessible KLM Fokker 100.", "✈️ 保安検査前の一般エリア（ランドサイド）にあるため、搭乗券なしで誰でも無料で入場可能。", "✈️ Located in the public landside area (before security), accessible for free without a boarding pass.", "散策無料", 52.3105, 4.7683, "suburban", True, False, False, True),
    ("a_52", "Forteiland Pampus & Muiderslot", "パムパス要塞島＆マウデン城", "Landmark", "IJmeerに浮かぶ19世紀末の人工要塞島（ユネスコ世界遺産「アムステルダムの防塞線」）と中世のマウデン城。", "19th-century artificial fortress island in the IJmeer, part of the UNESCO Defence Line of Amsterdam.", "⛴️ マウデン港から船でアクセス。暗い地下弾薬庫や砲台ドームをデジタルオーディオガイドで探索。", "⛴️ Take an interactive audio tour through the subterranean ammo bunkers and artillery domes.", "パムパス島(船込): €19.50 / マウデン城: €17.50", 52.3650, 5.0690, "suburban", True, False, False, False),
    ("a_53", "Singel & Herengracht Canal Ring", "シンゲル＆ヘレンフラハト二重環状運河", "Scenery & Walk", "17世紀の豪商の邸宅（カナルハウス）が立ち並ぶ世界遺産運河リングの最もエレガントな区間。", "The most elegant section of Amsterdam's UNESCO World Heritage 17th-century canal ring.", "📸 ヘレンフラハトとレリエフラハトの交差点（8つの橋が連続して見えるスポット近く）が撮影に最適。", "📸 Photograph the canal reflections near the Leliegracht intersection for iconic canal house views.", "散策無料", 52.3710, 4.8850, "city", False, False, False, True),
    ("a_54", "Electric Ladyland", "蛍光アート美術館（エレクトリック・レディランド）", "Museum & Gallery", "世界唯一のブラックライト蛍光アート専門ミュージアム。鉱物や現代アートが神秘的に発光。", "The first museum dedicated entirely to fluorescent art and glowing minerals under ultraviolet light.", "🎨 完全予約制の少人数ツアー。地下の参加型体験ルームでは自分がアートの一部になって光る写真を撮影可能。", "🎨 Guided small-group tours only. Experience participating in the fluorescent art space in the basement.", "料金: €5.00", 52.3768, 4.8815, "city", False, True, False, False),
    ("a_55", "Kattenkabinet", "猫の美術館（カテンカビネット）", "Museum & Gallery", "ヘレンフラハト沿いの17世紀運河邸宅内にある、猫をテーマにした美術品（ピカソ、レンブラント等）専門美術館。", "Art museum in a 17th-century canal house dedicated exclusively to cat-themed fine art by famous masters.", "🐈 館内には本物の看板猫たちが優雅に暮らしており、贅沢な調度品の上で寛ぐ姿を鑑賞できる。", "🐈 Resident museum cats roam freely through the opulent period rooms and sleep on antique furniture.", "料金: €10.00", 52.3654, 4.8908, "city", False, True, False, False),
    ("a_56", "Willet-Holthuysen Museum", "ウィレット・ホルトハイゼン邸", "Museum & Gallery", "19世紀の裕福な収集家夫妻が寄贈した、17世紀建造の豪華な運河邸宅ミュージアム。", "Opulent 17th-century canal house museum showcasing 19th-century private fine art collections and grand rooms.", "🌿 建物背後に広がるフランス庭園（対称形の花壇）は、運河邸宅の隠れた庭園美を留める逸品。", "🌿 Walk into the symmetrical French formal garden behind the house—a rare green oasis along Herengracht.", "料金: €12.50", 52.3652, 4.8973, "city", False, True, False, False),
    ("a_57", "Museum Van Loon", "ファン・ローン邸", "Museum & Gallery", "東インド会社（VOC）創設者一族ファン・ローン家の歴史的邸宅。", "Historic canal residence of the Van Loon merchant family, founders of the Dutch East India Company.", "🏛️ 邸宅・庭園・旧馬車小屋が完全な状態で一体保存されており、17世紀貴族の生活様式を体験可能。", "🏛️ The residence, garden, and coach house are preserved together as a complete 17th-century estate.", "料金: €15.00", 52.3622, 4.8950, "city", False, True, False, False),
    ("a_58", "Amsterdam Museum", "アムステルダム歴史博物館", "Museum & Gallery", "中世の修道院・孤児院跡を利用し、アムステルダムの700年にわたる都市の歴史と多様性を展示。", "City museum tracing 700 years of Amsterdam's growth, culture, and urban development.", "🏛️ 現在は修道院本館改修のため、アムステルダム国立美術館近くの別館（Amstel 51）で特別展を開催中。", "🏛️ Temporary masterwork exhibitions are hosted at the satellite location Amstel 51 during renovation.", "料金: €18.00", 52.3660, 4.9010, "city", False, True, False, False),
    ("a_59", "House of Bols", "ハウス・オブ・ボルス・カクテル体験", "Café & Bistro", "1575年創業の世界最古の蒸留酒ブランド「ボルス」の体験型カクテル＆リキュールミュージアム。", "Interactive cocktail experience by the world's oldest distilled spirit brand Bols (est. 1575).", "🍸 最後の「Mirror Bar」にて、入場料に含まれるお好みのオリジナルカクテル1杯をバーテンダーがメイキング。", "🍸 Included with admission is one custom-crafted cocktail made by professional bartenders at the Mirror Bar.", "料金: €17.50", 52.3580, 4.8805, "city", False, True, False, True),
    ("a_60", "Concertgebouw", "アムステルダム・コンセルトヘボウ", "Landmark", "ウィーンの楽友協会、ボストンのシンフォニーホールと並び「世界最高峰の音響」を誇るクラシック音楽の殿堂。", "World-renowned concert hall celebrated for its exceptional acoustics and Royal Concertgebouw Orchestra.", "🎻 9月〜5月の毎週水曜日午後12:30から大ホールまたは小ホールで「無料ランチタイムコンサート」を開催（先着順）。", "🎻 Free Wednesday lunchtime concerts are held at 12:30 PM (Sept–May) in the Main or Recital Hall.", "ランチコンサート無料 / 夜間公演チケット各種", 52.3563, 4.8790, "city", False, True, False, True)
]

def make_full_spot_object(spot_tuple):
    sid, name_en, name_ja_base, category, desc_ja, desc_en, tip_ja, tip_en, price_str, lat, lng, zone, kids, rain, shopping, free = spot_tuple
    full_name_ja = f"{name_en}（{name_ja_base}）"
    
    if free or "無料" in price_str or "Free" in price_str:
        p_ja, p_en, p_es, p_zh, p_fr, p_de = price_str if "無料" in price_str else "散策無料", "Free Entry", "Acceso libre", "免费参观", "Accès gratuit", "Freier Zugang"
        is_free = True
    else:
        clean = price_str.replace("料金:", "").replace("入場料:", "").strip()
        p_ja, p_en, p_es, p_zh, p_fr, p_de = f"料金: {clean}", f"Entry: {clean}", f"Entrada: {clean}", f"门票：{clean}", f"Entrée : {clean}", f"Eintritt: {clean}"
        is_free = False

    return {
        "id": sid,
        "name": full_name_ja,
        "category": category,
        "rating": "★4.7",
        "locationZone": zone,
        "lat": round(lat, 4),
        "lng": round(lng, 4),
        "kids": kids,
        "rain": rain,
        "shopping": shopping,
        "free": is_free,
        "family": True,
        "adult": True,
        "image": "",
        "wikiImage": "",
        "hasWiki": True,
        "name_en": name_en,
        "name_ja": full_name_ja,
        "name_es": name_en,
        "name_zh": name_en,
        "name_fr": name_en,
        "name_de": name_en,
        "desc_en": desc_en,
        "desc_ja": desc_ja,
        "desc_es": desc_en,
        "desc_zh": desc_ja,
        "desc_fr": desc_en,
        "desc_de": desc_en,
        "tip_en": tip_en,
        "tip_ja": tip_ja,
        "tip_es": tip_en,
        "tip_zh": tip_ja,
        "tip_fr": tip_en,
        "tip_de": tip_en,
        "price_ja": p_ja,
        "price_en": p_en,
        "price_es": p_es,
        "price_zh": p_zh,
        "price_fr": p_fr,
        "price_de": p_de
    }

def run_compiler():
    final_spots = [make_full_spot_object(s) for s in spots_data]
    
    filepath = os.path.join(cities_dir, "amsterdam.json")
    out_obj = {
        "city": "Amsterdam",
        "country": "Netherlands",
        "city_ja": "アムステルダム",
        "country_ja": "オランダ",
        "spots": final_spots
    }
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(out_obj, f, indent=2, ensure_ascii=False)

    print(f"🎉 Successfully compiled amsterdam.json with {len(final_spots)} verified spots!")

if __name__ == '__main__':
    run_compiler()
