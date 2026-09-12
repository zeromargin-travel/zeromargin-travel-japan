import json
import os

# Fix bo_13 and any overlapping tips
city_updates = {
    "bordeaux.json": {
        "bo_13": {
            "tip_en": "Book time-slot tickets online in advance! The unheated concrete submarine bunker can get chilly inside even during summer, so bring a light jacket.",
            "tip_ja": "【見学のコツ】公式サイトでの日時指定チケット事前予約が必須！無暖房のコンクリート潜水艦ドック内は夏でもひんやり冷え込むため、羽織る上着を持参するのがおすすめです。",
            "tip_es": "¡Imprescindible reservar entrada con hora en línea! El búnker de hormigón no tiene calefacción y hace frío incluso en verano: lleva una chaqueta ligera.",
            "tip_zh": "必看提示：请务必提前在官网预约入场时段！潜艇混凝土要塞内部无暖气，即便是夏季也十分凉爽甚至发凉，建议带一件薄外套。",
            "tip_fr": "Réservation en ligne à l'avance obligatoire ! Le bunker sous-marin en béton n'est pas chauffé et reste frais même en été : prévoyez une veste légère.",
            "tip_de": "Zeitfenster-Tickets unbedingt vorab online buchen! Der ungeheizte Betonbunker ist auch im Sommer recht kühl – unbedingt eine Leichte Jacke mitnehmen."
        }
    },
    "strasbourg.json": {
        "st_10": {
            "tip_en": "Mozart played the 1741 Silbermann organ here in 1778. Step inside for free to admire the magnificent baroque marble mausoleum of Marshal de Saxe.",
            "tip_ja": "1778年にモーツァルトが試奏した1741年製の名器ジルバーマン・オルガンを所蔵。サックス元帥の壮麗なロココ調バロック大理石墓碑彫刻も見どころ（入場無料）。",
            "tip_es": "Mozart tocó el órgano Silbermann de 1741 en 1778. Entra gratis para admirar el mausoleo de mármol barroco del Mariscal de Saxe.",
            "tip_zh": "莫扎特于1778年曾倾情演奏1741年Silbermann名管风琴。免费入内观赏萨克森伯爵壮丽的大理石巴洛克陵墓雕塑。",
            "tip_fr": "Mozart a joué sur l'orgue Silbermann de 1741 en 1778. Entrée libre pour admirer el mausolée en marbre du Maréchal de Saxe.",
            "tip_de": "Mozart spielte 1778 auf der Silbermann-Orgel von 1741. Freier Eintritt zur Besichtigung des Barock-Mausoleums."
        },
        "st_32": {
            "tip_en": "Cars are banned on most bridges entering the island. Explore the medieval cobblestone paths on foot or take the Batorama glass boat around the perimeter.",
            "tip_ja": "旧市街島（Grande Île）へ渡る橋の多くは車両進入禁止。徒歩での石畳散策か、周遊するバトーラマ観光船での水上からの見学が一番快適です。",
            "tip_es": "La mayoría de los puentes de acceso son peatonales. Recorre las calles empedradas a pie o en el barco panorámico Batorama.",
            "tip_zh": "多数进入岛屿的桥梁均禁止汽车通行。最推荐徒步穿行于石板步道，或乘坐Batorama全景水上游船环岛。",
            "tip_fr": "La plupart des ponts menant à l'île sont piétons. Explorez les ruelles pavées à pied ou en bateau panoramique Batorama.",
            "tip_de": "Die meisten Brücken zur Insel sind für Autos gesperrt. Erkunden Sie die Gassen zu Fuß oder mit dem Batorama-Boot."
        }
    },
    "toulouse.json": {
        "to_13": {
            "tip_en": "Housed inside a former 1820 brick slaughterhouse. Don't miss Picasso's giant 1936 theatre curtain 'The Remains of Minotaur' displayed in the basement!",
            "tip_ja": "1820年の赤レンガ屠殺場リノベ美術館。地下展示室にあるピカソ作の巨大な舞台幕『ミノタウロスの死骸』は絶対に見逃せません！",
            "tip_es": "Ubicado en un antiguo matadero de 1820. ¡No te pierdas el telón gigante de Picasso 'El despojo del Minotauro' en el sótano!",
            "tip_zh": "位于1820年旧红砖屠宰场内部。切勿错过地下展厅陈列的毕加索1936年巨幅舞台幕布画《米诺陶洛斯的遗骨》！",
            "tip_fr": "Installé dans un ancien abattoir de 1820. Ne manquez pas le rideau de scène géant de Picasso dans la salle en sous-sol !",
            "de": "Im historischen Backstein-Schlachthof von 1820. Der riesige Picasso-Theatervorhang im Untergeschoss ist ein Highlight!"
        },
        "to_15": {
            "tip_en": "Buy a combined ticket with the adjacent Botanical Garden greenhouses. The giant T-Rex skeleton and interactive prehistory labs are hit with kids!",
            "tip_ja": "隣接する植物園の大温室との共通チケットが便利。ティラノサウルスの全身化石標本や触れるハンズオン実験コーナーは子供に大人気！",
            "tip_es": "Compra una entrada combinada con el Jardín Botánico. El esqueleto gigante de T-Rex y los laboratorios interactivos encantan a los niños.",
            "tip_zh": "可购买与相邻植物园温室的套票。巨型暴龙（T-Rex）骨架化石与动手触摸实验室深受小朋友喜爱！",
            "tip_fr": "Achetez un billet combiné avec les serres du Jardin des Plantes. Le squelette de T-Rex et les ateliers interactifs sont passionnants.",
            "de": "Kombiticket mit den Gewächshäusern des Botanischen Gartens nutzen. Das T-Rex-Skelett begeistert Kinder!"
        },
        "to_34": {
            "tip_en": "Arrive early to book the Moonwalk simulator experience and catch the IMAX 3D astronomy film included in your day pass!",
            "tip_ja": "開館直後に月面歩行シミュレーター（Moonwalk）の予約枠を確保するのがコツ！チケットにはIMAX 3Dプラネタリウムの鑑賞も含まれています。",
            "tip_es": "¡Llega temprano para reservar el simulador de Moonwalk y disfrutar de la película IMAX 3D incluida en tu entrada!",
            "tip_zh": "开门入园后建议直奔月面行走模拟器（Moonwalk）预约时段！通票已包含IMAX 3D天文馆电影场次。",
            "tip_fr": "Arrivez tôt pour réserver votre passage sur le simulateur Moonwalk et profiter du grand film IMAX 3D inclus !",
            "de": "Früh kommen, um den Moonwalk-Simulator zu buchen und den IMAX-3D-Film im Planetarium zu sehen!"
        }
    },
    "paris.json": {
        "p_29": {
            "tip_en": "Head straight to Chez Alain Miam Miam for towering custom sandwiches, or the Moroccan stall for authentic couscous on weekend lunches!",
            "tip_ja": "週末のランチは激ウマ巨大サンドイッチ屋『Chez Alain Miam Miam』か、クスクスが味わえるモロッコ屋台に直行するのが地元流！",
            "tip_es": "Ve directo a Chez Alain Miam Miam para sándwiches gigantes o al puesto marroquí para cuscús en los almuerzos de fin de semana.",
            "tip_zh": "周末午餐推荐直奔 Chez Alain Miam Miam 尝尝现做巨大三明治，或前往摩洛哥档口品尝地道库斯库斯米饭！",
            "tip_fr": "Foncez chez Alain Miam Miam pour ses sandwichs gargantuesques ou au traiteur marocain pour un couscous gourmand !",
            "de": "Steuern Sie am Wochenende direkt Chez Alain Miam Miam für riesige Sandwiches oder den marokkanischen Stand an!"
        },
        "p_48": {
            "tip_en": "Reserve time slots for the Cité des Enfants interactive zone for kids online in advance. The Argonaut submarine tour is included!",
            "tip_ja": "体験型体験エリア『Cité des Enfants』の入場は事前予約が必須！本物の潜水艦アルゴノート号（Argonaute）の内部見学もセットでどうぞ。",
            "tip_es": "Reserva con antelación las horas para la Cité des Enfants. ¡La visita al submarino real Argonaute está incluida!",
            "tip_zh": "亲子互动区 Cité des Enfants 务必提前在官网定场次！门票内已包含真实的古修潜艇阿尔戈号（Argonaute）内部参观。",
            "tip_fr": "Réservez vos créneaux en ligne pour la Cité des Enfants. La visite du sous-marin Argonaute est incluse !",
            "de": "Zeitfenster für die Cité des Enfants vorab online buchen. Die Besichtigung des echten U-Boots Argonaute ist inklusive!"
        }
    }
}

for fname, updates in city_updates.items():
    fpath = f"data/cities/{fname}"
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    count = 0
    for s in data['spots']:
        sid = s['id']
        if sid in updates:
            up = updates[sid]
            for k, v in up.items():
                s[k] = v
            s['tip'] = up.get('tip_en', s.get('tip', ''))
            count += 1
            
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Refined tips for {count} spots in {fname}")

print("🎉 Overlapping tips fix script finished successfully!")
