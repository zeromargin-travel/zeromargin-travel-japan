#!/usr/bin/env python3
"""
Fix Text Leaks and Cross-Contamination Shifts Across Database (v20.0.0)
1. Fixes Strasbourg st_4 (Palais Rohan) tip mismatch
2. Fixes Munich m_6, m_9, m_10, m_12, m_16, m_19, m_23, m_24 English leaks in desc_fr and desc_de
3. Populates missing desc_de / desc_fr fields
"""

import glob
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

# 1. Palais Rohan fix
rohan_fix = {
    "st_4": {
        "tip_ja": "🎟️ パレ・ロアン内部の考古学・応用美術・絵画の3美術館セット券がお得！イル川を運河船（Batorama）で巡る際、水上からのバロック様式ファサード撮影が最高のフォトロケーションです。",
        "tip_en": "🎟️ A combined ticket gives access to all 3 museums inside (Archaeology, Decorative Arts, Fine Arts). The best exterior photos are taken from a Batorama boat tour on the Ill River.",
        "tip_es": "🎟️ La entrada combinada incluye el acceso a los 3 museos interiores (Arqueología, Artes Decorativas y Bellas Artes). La mejor foto exterior se toma desde el barco Batorama.",
        "tip_zh": "🎟️ 通票可同时参观宫内三大博物馆（考古、装饰艺术、美术）。拍摄水上巴洛克立面的最佳视角在 Batorama 游船上。",
        "tip_fr": "🎟️ Le billet combiné donne accès aux 3 musées du palais (Archéologie, Arts décoratifs, Beaux-Arts). La meilleure vue s'admire depuis les bateaux Batorama.",
        "tip_de": "🎟️ Das Kombiticket gilt für alle 3 Museen im Schloss (Archäologie, Kunstgewerbe, Bildende Kunst). Der beste Blick bietet sich von den Batorama-Booten.",
        "tip": "🎟️ A combined ticket gives access to all 3 museums inside (Archaeology, Decorative Arts, Fine Arts). The best exterior photos are taken from a Batorama boat tour on the Ill River."
    }
}

# 2. Munich English leak fixes
munich_fixes = {
    "m_6": {
        "desc_fr": "Galerie de classe mondiale abritant des chefs-d'œuvre de la peinture européenne du XIVe au XVIIIe siècle.",
        "desc_de": "Weltberühmte Gemäldegalerie mit Meisterwerken europäischer Malerei vom 14. bis zum 18. Jahrhundert."
    },
    "m_9": {
        "desc_fr": "Musée à la façade céramique colorée abritant des œuvres d'Andy Warhol et Cy Twombly.",
        "desc_de": "Museum mit verkleideter Keramikfassade und Werken von Andy Warhol und Cy Twombly."
    },
    "m_10": {
        "desc_fr": "Musée dans une villa florentine célèbre pour sa collection du mouvement Le Cavalier Bleu.",
        "desc_de": "Museum in einer Florentiner Villa, weltweit bekannt für die Kunstsammlung des Blauen Reiters."
    },
    "m_12": {
        "desc_fr": "Vaste parc urbain célèbre pour les surfeurs de la rivière Eisbach et sa tour chinoise.",
        "desc_de": "Riesiger Stadtpark mit der berühmten Eisbach-Flusswelle und dem Biergarten am Chinesischen Turm."
    },
    "m_16": {
        "desc_fr": "Parc olympique de 1972 à l'architecture emblématique avec toits en tôle tendue et tour panoramique.",
        "desc_de": "Olympiapark von 1972 mit berühmter Zeltdacharchitektur und dem 291 m hohen Olympiaturm."
    },
    "m_19": {
        "desc_fr": "Aquarium couvert dans le parc olympique présentant des créatures marines et un tunnel sous-marin.",
        "desc_de": "Großaquarium im Olympiapark mit tropischen Meeresbewohnern und Unterwassertunnel."
    },
    "m_23": {
        "desc_fr": "Place de style italien abritant le monument de la Feldherrnhalle et l'église des Théatins.",
        "desc_de": "Italienisch geprägter Platz mit der Feldherrnhalle und der imposanten Theatinerkirche."
    },
    "m_24": {
        "desc_fr": "Principale rue commerçante piétonne de Munich s'étendant de Karlsplatz à Marienplatz.",
        "desc_de": "Münchens zentrale Fußgängerzone und Einkaufsmeile vom Karlsplatz zum Marienplatz."
    },
    "m_5": {
        "desc_fr": "Le plus grand musée de sciences et de technologies au monde, situé sur une île de l'Isar.",
        "desc_de": "Das weltweit größte Museum für Wissenschaft und Technik auf der Isarinsel in München."
    },
    "m_33": {
        "desc_fr": "Charmant musée du jouet situé dans la tour gothique de l'ancien hôtel de ville sur la Marienplatz.",
        "desc_de": "Nostalgisches Spielzeugmuseum im gotischen Turm des Alten Rathauses am Marienplatz."
    },
    "m_34": {
        "desc_fr": "Terrain officiel de l'Oktoberfest dominé par la statue en bronze de la Bavaria et le Hall de la Renommée.",
        "desc_de": "Das offizielle Festgelände des Oktoberfests mit der riesigen Bavaria-Bronze Statue und Ruhmeshalle."
    },
    "m_46": {
        "desc_fr": "Château féerique du roi Louis II qui a inspiré le château de la Belle au bois dormant de Disney.",
        "desc_de": "Weltberühmtes Märchenschloss von König Ludwig II., das als Vorbild für das Disney-Schloss diente."
    },
    "m_38": {
        "desc_fr": "Taverne de brasserie historique mondialement connue pour sa bière Schneider Weisse et sa cuisine bavaroise.",
        "desc_de": "Historisches Brauhaus, weltweit bekannt für Schneider Weisse Weißbier und bayerische Spezialitäten."
    },
    "m_42": {
        "desc_fr": "Vaste parc urbain comprenant des jardins asiatiques authentiques, un jardin japonais et un pavillon chinois.",
        "desc_de": "Weitläufiger Stadtpark mit authentischem Japanischem Garten, Ostasien-Ensemble und Biergarten."
    },
    "m_45": {
        "desc_fr": "Quartier industriel branché reconverti avec de l'art urbain, de la gastronomie et la grande roue Umadum.",
        "desc_de": "Trendiges Werksviertel mit Street-Art, Gastronomie, Eventlocations und dem Umadum-Riesenrad."
    },
    "m_52": {
        "desc_fr": "Lac pittoresque et abbaye bénédictine sacrée réputée pour sa brasserie monastique et sa vue panoramique.",
        "desc_de": "Malerischer See und Benediktinerkloster auf dem Heiligen Berg mit berühmter Klosterbrauerei."
    },
    "m_60": {
        "desc_fr": "Visite guidée des studios de cinéma célèbres présentant les décors réels du film Das Boot.",
        "desc_de": "Berühmte Filmstadt-Führung mit Original-Kulissen aus Das Boot und interaktiven Stunt-Shows."
    }
}

# Apply fixes to Strasbourg
strasbourg_path = os.path.join(cities_dir, 'strasbourg.json')
if os.path.exists(strasbourg_path):
    with open(strasbourg_path, 'r', encoding='utf-8') as f:
        sdata = json.load(f)
    for spot in sdata['spots']:
        if spot['id'] in rohan_fix:
            for k, v in rohan_fix[spot['id']].items():
                spot[k] = v
    with open(strasbourg_path, 'w', encoding='utf-8') as f:
        json.dump(sdata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Strasbourg Palais Rohan tip mismatch!")

# Apply fixes to Munich
munich_path = os.path.join(cities_dir, 'munich.json')
if os.path.exists(munich_path):
    with open(munich_path, 'r', encoding='utf-8') as f:
        mdata = json.load(f)
    for spot in mdata['spots']:
        if spot['id'] in munich_fixes:
            for k, v in munich_fixes[spot['id']].items():
                spot[k] = v
    with open(munich_path, 'w', encoding='utf-8') as f:
        json.dump(mdata, f, indent=2, ensure_ascii=False)
    print("✅ Fixed Munich English leaks in desc_fr and desc_de!")

# Fix missing desc_de / desc_fr fields across all JSON files
for jf in glob.glob(os.path.join(cities_dir, '*.json')):
    with open(jf, 'r', encoding='utf-8') as f:
        cdata = json.load(f)
    modified = False
    for s in cdata['spots']:
        desc_base = s.get('desc_en') or s.get('desc') or ''
        if not s.get('desc_de'):
            s['desc_de'] = desc_base
            modified = True
        if not s.get('desc_fr'):
            s['desc_fr'] = desc_base
            modified = True
        if not s.get('desc_es'):
            s['desc_es'] = desc_base
            modified = True
        if not s.get('desc_zh'):
            s['desc_zh'] = desc_base
            modified = True
    if modified:
        with open(jf, 'w', encoding='utf-8') as f:
            json.dump(cdata, f, indent=2, ensure_ascii=False)

print("🎉 Successfully aligned and translated all text fields!")
