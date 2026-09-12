#!/usr/bin/env python3
"""
Zero-Margin Travel App - Database Audit & Defect Fixer (v27.0.0)
Fixes all defects identified in Deep Search Audit:
- lyon_9: Entity mismatch (La Tourette -> Fresque des Canuts, Free Entry)
- br_7: Manneken Pis height (61cm -> 55.5cm), mistranslation fix, populate tips
- b_29: Computerspielemuseum price (€11 -> €12)
- bo_17: MADD Bordeaux renovation status note in tips
- bo_30 & bo_32: Redundancy elimination between desc and tip
- b_12 & b_15: Precise location/direction info for observation deck and Holocaust underground center
- c_4: Clarify winter ice rink season (Heinzels Wintermärchen)
- lyon_32: Standardize silk workers to カニュ (Canut)
- Multilingual leakage cleanup across all foreign tip/desc fields
"""

import os
import json
import glob
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

JAPANESE_REGEX = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]')

def fix_lyon(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        if s.get('id') == 'lyon_9':
            print("  -> Fixing lyon_9: Entity mismatch to Fresque des Canuts")
            s['name'] = "Fresque des Canuts（カニュの壁画）"
            s['name_en'] = "Fresque des Canuts (Silk Weavers' Mural)"
            s['name_ja'] = "Fresque des Canuts（カニュの壁画）"
            s['name_es'] = "Fresque des Canuts (Mural de los Tejedores de Seda)"
            s['name_zh'] = "Fresque des Canuts (卡纽绢丝工匠巨幅壁画)"
            s['name_fr'] = "Fresque des Canuts (Mur des Canuts)"
            s['name_de'] = "Fresque des Canuts (Wandgemälde der Seidenweber)"
            
            s['price'] = "Free Entry"
            s['price_en'] = "Free Entry"
            s['price_ja'] = "見学無料"
            s['price_es'] = "Acceso libre"
            s['price_zh'] = "免费参观"
            s['price_fr'] = "Accès libre"
            s['price_de'] = "Frei zugänglich"
            s['free'] = True
            s['locationZone'] = "city"
            
            s['desc_en'] = "Europe's largest trompe-l'œil mural spanning 1,200 m² in Lyon's historic Croix-Rousse district."
            s['desc_ja'] = "クロワ・ルース地区にある、1,200㎡におよぶヨーロッパ最大の立体だまし絵（トロンプ・ルイユ）壁画。"
            s['desc_es'] = "El mural en trompe-l'œil más grande de Europa (1.200 m²) ubicado en el distrito histórico de Croix-Rousse."
            s['desc_zh'] = "位于里昂历史悠久的克洛瓦-鲁斯区、占地1200平方米的欧洲最大立体错视画墙面。"
            s['desc_fr'] = "La plus grande fresque murale en trompe-l'œil d'Europe (1 200 m²) située dans le quartier historique de la Croix-Rousse."
            s['desc_de'] = "Europas größtes Trompe-l'œil-Wandgemälde (1.200 m²) im historischen Viertel Croix-Rousse."

            s['tip_en'] = "🖼️ The mural is updated every decade to reflect neighborhood changes. Step close to inspect the 3D optical illusion stairs and painted figures!"
            s['tip_ja'] = "🖼️ 壁画は10年ごとに地区の実際の変化に合わせて描き直されます。立体的に見える階段や人々のグラフィティとの記念撮影が楽しめます。"
            s['tip_es'] = "🖼️ El mural se actualiza cada década para reflejar la evolución del barrio. ¡Acércate para tomarte fotos con las escaleras y figuras en 3D!"
            s['tip_zh'] = "🖼️ 壁画每十年根据街区的真实变迁重新临摹更新。非常适合贴近画面与逼真立体的3D阶梯及人偶合影留念。"
            s['tip_fr'] = "🖼️ La fresque est actualisée tous les dix ans pour suivre l'évolution du quartier. Approchez-vous pour vous photographier avec les trompe-l'œil !"
            s['tip_de'] = "🖼️ Das Kunstwerk wird alle zehn Jahre an die reale Entwicklung des Viertels angepasst. Perfekter Fotospot für optische 3D-Täuschungen!"

        if s.get('id') == 'lyon_32':
            # Standardize silk workers to カニュ
            s['desc_ja'] = s.get('desc_ja', '').replace('カヌーツ', 'カニュ')
            s['tip_ja'] = s.get('tip_ja', '').replace('カヌーツ', 'カニュ')

def fix_brussels(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        if s.get('id') == 'br_7':
            print("  -> Fixing br_7: Manneken Pis height & description & tips")
            s['desc_en'] = "Famous 55.5cm bronze fountain statue of a peeing boy in central Brussels."
            s['desc_ja'] = "ブリュッセル中心部に立つ、小便を放つ少年の有名な高さ55.5cmのブロンズ製噴水像。"
            s['desc_es'] = "Famosa estatua de fuente de bronce de 55,5 cm de un niño orinando en el centro de Bruselas."
            s['desc_fr'] = "Célèbre statue fontaine en bronze de 55,5 cm représentant un garçon qui fait pipi au centre de Bruxelles."
            s['desc_de'] = "Berühmte 55,5 cm große bronzene Brunnenstatue eines pinkelnden Jungen im Zentrum von Brüssel."

            s['tip_en'] = "👦 Visit the nearby GardeRobe MannekenPis museum to view over 1,000 historic costumes worn by the statue during official festivals!"
            s['tip_ja'] = "👦 近くの衣装博物館（GardeRobe MannekenPis）では1,000着を超える歴代の着せ替え衣装を鑑賞できます。公式行事の日には実際に衣装が着用されます。"
            s['tip_es'] = "👦 ¡Visita el cercano museo GardeRobe MannekenPis para ver más de 1.000 trajes históricos que viste la estatua durante festivales!"
            s['tip_zh'] = "👦 推荐顺道参观附近的服装博物馆（GardeRobe MannekenPis），欣赏为小童定制的千余套节日华服；逢重大节庆更会穿上特定服饰。"
            s['tip_fr'] = "👦 Visitez le musée GardeRobe MannekenPis tout proche pour admirer plus de 1 000 costumes historiques portés par la statue !"
            s['tip_de'] = "👦 Besuchen Sie das nahegelegene Museum GardeRobe MannekenPis mit über 1.000 historischen Kostümen für die Statue!"

def fix_berlin(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'b_12':
            print("  -> Fixing b_12: Berliner Mauer tip precision")
            s['tip_en'] = "🧱 Visit the free observation deck inside the Documentation Center across Bernauer Straße to view the intact border strip and watchtower from above."
            s['tip_ja'] = "🧱 通りの反対側にあるドキュメンテーションセンター屋上展望台（入場無料）へ登ると、かつての無人地帯（死亡地帯）と監視塔の構造を一目で俯瞰できます。"
            s['tip_es'] = "🧱 Sube al mirador gratuito dentro del Centro de Documentación al otro lado de Bernauer Straße para contemplar la franja de frontera e histórica torre."
            s['tip_zh'] = "🧱 推荐登上一街之隔的档案中心免费屋顶观景台，可居高临下俯瞰完整的原防空警戒死角无人区与监视塔结构。"
            s['tip_fr'] = "🧱 Montez sur la plateforme d'observation gratuite du centre de documentation pour observer la bande de frontière et le mirador conservés."
            s['tip_de'] = "🧱 Die kostenlose Aussichtsplattform im Dokumentationszentrum auf der gegenüberliegenden Straßenseite nutzen für den Blick auf den Grenzstreifen."

        elif sid == 'b_15':
            print("  -> Fixing b_15: Holocaust Memorial underground entrance location")
            s['tip_en'] = "🕯️ Access the underground Information Center (Ort der Information) via the stairs at the southeast corner of the field (Cora-Berliner-Straße side)."
            s['tip_ja'] = "🕯️ 敷地南東角（コーラ・ベルリナー通り側）の階段から地下情報センター（Ort der Information）へ。犠牲者の手紙や遺書などの無料展示がご覧いただけます。"
            s['tip_es'] = "🕯️ Accede al Centro de Información subterráneo por la escalera de la esquina sudeste (lado Cora-Berliner-Straße)."
            s['tip_zh'] = "🕯️ 地下信息中心（Ort der Information）的免费入口位于纪念碑群东南角（Cora-Berliner-Straße街一侧）的下行阶梯处。"
            s['tip_fr'] = "🕯️ Accédez au centre d'information souterrain par l'escalier situé au coin sud-est (côté Cora-Berliner-Straße)."
            s['tip_de'] = "🕯️ Zugang zum unterirdischen Ort der Information über die Treppe an der Südost-Ecke des Stelenfeldes (Seite Cora-Berliner-Straße)."

        elif sid == 'b_29':
            print("  -> Fixing b_29: Computerspielemuseum price (€11 -> €12)")
            s['price'] = "Entry: €12"
            s['price_en'] = "Entry: €12"
            s['price_ja'] = "入場料: 12 ユーロ"
            s['price_es'] = "Entrada: 12€"
            s['price_zh'] = "门票：12 欧元"
            s['price_fr'] = "Entrée : 12 €"
            s['price_de'] = "Eintritt: 12 €"

def fix_bordeaux(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        sid = s.get('id')
        if sid == 'bo_17':
            print("  -> Fixing bo_17: MADD Bordeaux renovation notice")
            s['tip_en'] = "🏛️ The main 18th-century mansion is currently undergoing long-term restoration. Check the official website for off-site temporary exhibits."
            s['tip_ja'] = "🏛️ 現在本館（18世紀貴族館）は大改修工事のため休館中です。訪問前に公式サイトで仮設会場での企画展の開催状況をご確認ください。"
            s['tip_es'] = "🏛️ El edificio principal está en restauración. Consulta la web oficial para ver las exposiciones temporales fuera de su sede habitual."
            s['tip_zh'] = "🏛️ 主楼目前正在进行大规模长期的修缮改造；前往前请务必登录官网确认临展场馆与开放日程。"
            s['tip_fr'] = "🏛️ Le bâtiment principal fait l'objet de travaux de rénovation. Consultez le site officiel pour les expositions temporaires hors les murs."
            s['tip_de'] = "🏛️ Das Hauptgebäude wird derzeit umfassend saniert. Aktuelle Ausweichausstellungen vorab auf der Website prüfen."

        elif sid == 'bo_30':
            print("  -> Fixing bo_30: Rue Sainte-Catherine redundancy cleanup")
            s['desc_ja'] = "コメディ広場からヴィクトワール広場まで歴史的中心部を南北に貫く、全長1.2kmの歩行者専用ショッピング街。"
            s['tip_ja'] = "🛍️ 混雑を避けるなら平日の午前中の散策がおすすめ！大劇場の美しいファサードを背にスタートし、ブティックや老舗パティスリー巡りを楽しめます。"

        elif sid == 'bo_32':
            print("  -> Fixing bo_32: Darwin Eco-Système redundancy cleanup")
            s['desc_ja'] = "ガロンヌ川右岸の旧軍兵舎（ニエル軍営）を再利用した、文化とエコ活動が融合するオルタナティブ・カルチャーハブ。"
            s['tip_ja'] = "🌿 施設内の「Le Magasin Général」はヨーロッパ最大級のオーガニックレストラン！インドアスケートパークのウォールアートと共にクラフトビールが楽しめます。"

def fix_cologne(data):
    spots = data.get('spots', []) if isinstance(data, dict) else data
    for s in spots:
        if s.get('id') == 'c_4':
            print("  -> Fixing c_4: Heumarkt ice rink seasonality")
            s['tip_ja'] = "⛸️ 11月下旬〜1月初旬のクリスマス市（Heinzels Wintermärchen）期間中、フリードリヒ・ヴィルヘルム3世騎馬像を囲む特設アイススケートリンクが登場します。"

def clean_all_multilingual_leaks():
    print("🚀 Cleaning all Japanese leakage from foreign fields across all city JSON files...")
    city_files = sorted(glob.glob(os.path.join(cities_dir, '*.json')))
    for fpath in city_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        fname = os.path.basename(fpath)
        if fname == 'lyon.json':
            fix_lyon(data)
        elif fname == 'brussels.json':
            fix_brussels(data)
        elif fname == 'berlin.json':
            fix_berlin(data)
        elif fname == 'bordeaux.json':
            fix_bordeaux(data)
        elif fname == 'cologne.json':
            fix_cologne(data)
            
        spots = data.get('spots', []) if isinstance(data, dict) else data
        cleaned_count = 0
        for s in spots:
            # Check foreign fields for Japanese text leaks
            tip_ja = s.get('tip_ja', '')
            desc_ja = s.get('desc_ja', '')

            for field in ['tip_en', 'tip_de', 'tip_fr', 'tip_es', 'tip_zh']:
                val = s.get(field, '')
                if JAPANESE_REGEX.search(val):
                    # Leak detected! If field is tip, replace with tip_en fallback or clean English
                    if field == 'tip_en':
                        s['tip_en'] = s.get('tip', '💡 Great spot to visit for memorable photos and local atmosphere.')
                    elif field == 'tip_de':
                        s['tip_de'] = '💡 Empfehlenswerter Ort für schöne Fotos und authentische Atmosphäre.'
                    elif field == 'tip_fr':
                        s['tip_fr'] = '💡 Superbe endroit à visiter pour des photos mémorables et une ambiance locale.'
                    elif field == 'tip_es':
                        s['tip_es'] = '💡 Gran lugar para visitar y tomar fotos memorables con ambiente local.'
                    elif field == 'tip_zh':
                        s['tip_zh'] = '💡 非常值得打卡游览的最佳地点，适合合影留念与感受在地氛围。'
                    cleaned_count += 1

            for field in ['desc_en', 'desc_de', 'desc_fr', 'desc_es', 'desc_zh']:
                val = s.get(field, '')
                if JAPANESE_REGEX.search(val):
                    if field == 'desc_en':
                        s['desc_en'] = s.get('desc', 'Popular landmark in the city center.')
                    elif field == 'desc_de':
                        s['desc_de'] = 'Beliebte Sehenswürdigkeit im Stadtzentrum.'
                    elif field == 'desc_fr':
                        s['desc_fr'] = 'Monument célèbre situé au cœur de la ville.'
                    elif field == 'desc_es':
                        s['desc_es'] = 'Punto de interés popular en el centro de la ciudad.'
                    elif field == 'desc_zh': "位于市中心的知名观光地标。"
                    cleaned_count += 1

        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  - Refined {fname} (Cleaned {cleaned_count} foreign language text leaks)")

if __name__ == '__main__':
    clean_all_multilingual_leaks()
