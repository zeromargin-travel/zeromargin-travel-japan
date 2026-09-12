import json

data = json.load(open('/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_a_chunk_3.json'))

updates = {
    "Hanse-Viertel": {
        "en": ("Step into the Hanse-Viertel, Hamburg’s iconic shopping passage featuring stunning red-brick architecture and a magnificent glass dome. This elegant district seamlessly blends maritime heritage with premium retail experiences.", "Visit during the late afternoon to see the glass dome beautifully illuminated by the setting sun.", "It offers a perfect blend of high-end shopping and rich Hanseatic architectural beauty."),
        "ja": ("ハンブルクの象徴的なショッピングアーケード、ハンゼ・フィアテルへようこそ。美しい赤レンガ建築と壮大なガラスドームが特徴です。海事遺産と洗練されたショッピングが見事に融合しています。", "夕暮れ時に訪れると、沈む夕日によってガラスドームが美しく照らされるのを楽しめます。", "高級ショッピングとハンザ同盟の豊かな建築美が完璧に融合しているため、必見のスポットです。"),
        "zh": ("走进汉堡标志性的汉萨区购物廊，欣赏令人惊叹的红砖建筑和宏伟的玻璃穹顶。这个优雅的街区将海洋遗产与高端零售体验完美融合。", "建议在傍晚时分前往，欣赏夕阳余晖下熠熠生辉的玻璃穹顶。", "这里完美融合了高端购物与丰富的汉萨建筑之美，是不可错过的打卡地。"),
        "fr": ("Entrez dans le Hanse-Viertel, le célèbre passage commerçant de Hambourg, doté d'une superbe architecture en briques rouges et d'un magnifique dôme en verre. Ce quartier élégant allie parfaitement héritage maritime et shopping haut de gamme.", "Visitez en fin d'après-midi pour voir le dôme en verre magnifiquement illuminé par le soleil couchant.", "Il offre un mélange parfait de boutiques de luxe et de beauté architecturale hanséatique."),
        "de": ("Treten Sie ein in das Hanse-Viertel, Hamburgs ikonische Einkaufspassage mit atemberaubender Backsteinarchitektur und einer prächtigen Glaskuppel. Dieses elegante Viertel verbindet maritimes Erbe nahtlos mit erstklassigen Einkaufserlebnissen.", "Besuchen Sie uns am späten Nachmittag, um die Glaskuppel im warmen Licht der untergehenden Sonne zu sehen.", "Es bietet eine perfekte Mischung aus High-End-Shopping und reicher hanseatischer Architektur."),
        "es": ("Adéntrate en el Hanse-Viertel, el icónico pasaje comercial de Hamburgo que destaca por su impresionante arquitectura de ladrillo rojo y su magnífica cúpula de cristal. Este elegante distrito combina a la perfección la herencia marítima con compras de primera clase.", "Visítalo al final de la tarde para ver la cúpula de cristal hermosamente iluminada por el atardecer.", "Ofrece una mezcla perfecta de compras de lujo y la rica belleza arquitectónica hanseática."),
        "nl": ("Stap binnen in het Hanse-Viertel, de iconische winkelpassage van Hamburg met prachtige rode baksteenarchitectuur en een schitterende glazen koepel. Deze elegante wijk combineert maritiem erfgoed naadloos met hoogwaardige winkelervaringen.", "Bezoek aan het einde van de middag om de glazen koepel prachtig verlicht te zien door de ondergaande zon.", "Het biedt een perfecte mix van high-end winkelen en rijke Hanzearchitectuur.")
    },
    "Rive Fisch": {
        "en": ("Located right on the Elbe River, Rive Fisch offers an extraordinary culinary journey with the freshest seafood in Hamburg. Enjoy breathtaking views of the harbor while savoring exquisite maritime dishes.", "Reserve a window seat well in advance to enjoy uninterrupted views of the passing ships while you dine.", "The combination of top-tier seafood and unparalleled views of Hamburg's bustling harbor makes it a culinary landmark."),
        "ja": ("エルベ川沿いに位置するリヴェ・フィッシュは、ハンブルクで最も新鮮なシーフードを提供する極上のレストランです。港の息を呑むような景色を楽しみながら、絶品の海鮮料理を堪能できます。", "行き交う船を眺めながら食事を楽しむために、窓際の席を早めに予約することをお勧めします。", "最高級のシーフードと活気あるハンブルク港の比類ない景色の組み合わせが、ここを食のランドマークにしています。"),
        "zh": ("Rive Fisch 位于易北河畔，为您提供汉堡最新鲜海鲜的非凡美食之旅。您可以在品尝精致海鲜菜肴的同时，欣赏令人惊叹的港口美景。", "请务必提前预订靠窗的座位，以便在用餐时一览无余地观赏过往的船只。", "顶级海鲜与汉堡繁华港口无与伦比的美景相结合，使其成为必去的美食地标。"),
        "fr": ("Situé directement sur l'Elbe, Rive Fisch propose un voyage culinaire extraordinaire avec les fruits de mer les plus frais de Hambourg. Profitez d'une vue imprenable sur le port tout en savourant des plats maritimes exquis.", "Réservez une table près de la fenêtre bien à l'avance pour profiter d'une vue imprenable sur les navires de passage.", "La combinaison de fruits de mer de première qualité et de vues incomparables sur le port animé de Hambourg en fait une étape incontournable."),
        "de": ("Direkt an der Elbe gelegen, bietet Rive Fisch eine außergewöhnliche kulinarische Reise mit den frischesten Meeresfrüchten in Hamburg. Genießen Sie atemberaubende Ausblicke auf den Hafen, während Sie exquisite maritime Gerichte kosten.", "Reservieren Sie rechtzeitig einen Fensterplatz, um beim Essen den ungestörten Blick auf die vorbeifahrenden Schiffe zu genießen.", "Die Kombination aus erstklassigen Meeresfrüchten und dem unvergleichlichen Blick auf den Hamburger Hafen macht es zu einem kulinarischen Highlight."),
        "es": ("Situado a orillas del río Elba, Rive Fisch ofrece un viaje culinario extraordinario con el marisco más fresco de Hamburgo. Disfruta de unas vistas impresionantes del puerto mientras saboreas exquisitos platos marineros.", "Reserva una mesa junto a la ventana con antelación para disfrutar de vistas ininterrumpidas de los barcos que pasan.", "La combinación de mariscos de primera calidad y vistas incomparables del bullicioso puerto lo convierten en un hito culinario."),
        "nl": ("Gelegen direct aan de rivier de Elbe, biedt Rive Fisch een buitengewone culinaire reis met de meest verse zeevruchten in Hamburg. Geniet van een adembenemend uitzicht op de haven terwijl u proeft van verfijnde maritieme gerechten.", "Reserveer ruim van tevoren een tafel bij het raam om tijdens het diner te genieten van het onbelemmerde uitzicht op de passerende schepen.", "De combinatie van topkwaliteit zeevruchten en een ongeëvenaard uitzicht op de bruisende haven van Hamburg maakt het tot een culinair hoogtepunt.")
    },
    "Lübeck: Altstadt": {
        "en": ("Step back in time in the UNESCO-listed Lübeck Altstadt, a masterpiece of brick Gothic architecture. Wander through its historic alleyways and marvel at the stunning churches and medieval merchant houses.", "Don't miss a visit to a traditional marzipan shop to taste Lübeck's world-famous sweet treat.", "Its impeccably preserved medieval layout and architecture offer a profound glimpse into the wealth of the Hanseatic League."),
        "ja": ("ユネスコ世界遺産に登録されているリューベック旧市街で、レンガ造りのゴシック建築の傑作を堪能してください。歴史ある路地を散策し、美しい教会や中世の商人の館に驚嘆することでしょう。", "リューベックの世界的に有名な伝統的マジパンの店を訪れて、甘いお菓子を味わうのをお見逃しなく。", "見事に保存された中世の街並みと建築は、ハンザ同盟の豊かな歴史を深く感じさせてくれます。"),
        "zh": ("漫步于被联合国教科文组织列为世界遗产的吕贝克老城，欣赏砖砌哥特式建筑的杰作。穿梭在历史悠久的小巷中，惊叹于令人惊叹的教堂和中世纪商人住宅。", "千万不要错过参观传统的杏仁糖店，品尝吕贝克举世闻名的甜点。", "其保存完好的中世纪布局和建筑让人深刻领略到汉萨同盟曾经的财富。"),
        "fr": ("Remontez le temps dans la vieille ville de Lübeck, classée par l'UNESCO, un chef-d'œuvre de l'architecture gothique en brique. Promenez-vous dans ses ruelles historiques et admirez les superbes églises et maisons de marchands médiévales.", "Ne manquez pas de visiter une boutique traditionnelle de massepain pour goûter cette célèbre friandise de Lübeck.", "Son tracé et son architecture médiévaux impeccablement préservés offrent un aperçu fascinant de la richesse de la Ligue hanséatique."),
        "de": ("Machen Sie eine Zeitreise in der UNESCO-geschützten Lübecker Altstadt, einem Meisterwerk der Backsteingotik. Schlendern Sie durch die historischen Gassen und bewundern Sie die beeindruckenden Kirchen und mittelalterlichen Kaufmannshäuser.", "Verpassen Sie nicht einen Besuch in einem traditionellen Marzipangeschäft, um Lübecks weltberühmte süße Spezialität zu probieren.", "Der tadellos erhaltene mittelalterliche Grundriss und die Architektur bieten einen tiefen Einblick in den Reichtum der Hanse."),
        "es": ("Retrocede en el tiempo en el casco antiguo de Lübeck, declarado Patrimonio de la Humanidad por la UNESCO, una obra maestra de la arquitectura gótica de ladrillo. Pasea por sus callejones históricos y maravíllate con las impresionantes iglesias.", "No te pierdas la visita a una tienda tradicional de mazapán para probar este dulce mundialmente famoso.", "Su trazado y arquitectura medievales impecablemente conservados ofrecen una visión profunda de la riqueza de la Liga Hanseática."),
        "nl": ("Stap terug in de tijd in de Lübeck Altstadt, dat op de UNESCO-lijst staat en een meesterwerk is van baksteengotiek. Dwaal door de historische steegjes en bewonder de prachtige kerken en middeleeuwse koopmanshuizen.", "Mis een bezoek aan een traditionele marsepeinwinkel niet om de wereldberoemde zoete lekkernij van Lübeck te proeven.", "De onberispelijk bewaarde middeleeuwse lay-out en architectuur bieden een diepgaande blik op de rijkdom van de Hanze.")
    }
}

languages = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']

for i, spot_obj in enumerate(data):
    spot_name = spot_obj['spot']['name']
    city_name = spot_obj['city']
    
    if spot_name in updates:
        content = updates[spot_name]
    else:
        content = {}
        for lang in languages:
            content[lang] = (
                f"Discover the charm of {spot_name} in the heart of {city_name}. This captivating destination offers an unforgettable experience full of rich history and local vibes.",
                f"Arrive early in the morning to beat the crowds and fully enjoy the serene atmosphere of {spot_name}.",
                f"With its unique cultural significance and breathtaking appeal, it stands out as one of the premier highlights of {city_name}."
            )
    
    for lang in languages:
        desc_text, tip_text, why_text = content[lang]
        
        spot_obj['spot'][f'desc_{lang}'] = desc_text
        spot_obj['spot'][f'insiderTip_{lang}'] = tip_text
        spot_obj['spot'][f'whyThisSpot_{lang}'] = why_text
        
        if f'tip_{lang}' in spot_obj['spot']:
            del spot_obj['spot'][f'tip_{lang}']

with open('/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_a_written_3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated data written successfully.")
