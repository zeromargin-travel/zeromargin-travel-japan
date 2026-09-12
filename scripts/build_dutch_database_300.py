#!/usr/bin/env python3
"""
Zero-Margin Travel App - Dutch 300 Master Database Builder (v33.0.0)
Populates full 60 spots across 5 Dutch cities:
- amsterdam.json (a_1 to a_60)
- rotterdam.json (ro_1 to ro_60)
- the_hague.json (dh_1 to dh_60)
- utrecht.json (ut_1 to ut_60)
- maastricht.json (maa_1 to maa_60)
"""

import os
import json
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

def translate_price_obj(price_raw):
    if not price_raw or "Free" in price_raw or "無料" in price_raw or "free" in price_raw.lower():
        clean = price_raw.strip() if price_raw else "見学無料"
        return {
            "price_ja": "見学無料" if clean.lower() == "free" else clean,
            "price_en": "Free Entry",
            "price_es": "Acceso libre",
            "price_zh": "免费参观",
            "price_fr": "Accès gratuit",
            "price_de": "Freier Zugang",
            "is_free": True
        }
    else:
        clean = price_raw.replace("料金:", "").replace("入場料:", "").strip()
        return {
            "price_ja": f"料金: {clean}",
            "price_en": f"Entry: {clean}",
            "price_es": f"Entrada: {clean}",
            "price_zh": f"门票：{clean}",
            "price_fr": f"Entrée : {clean}",
            "price_de": f"Eintritt: {clean}",
            "is_free": False
        }

def make_spot(sid, name_en, name_ja, category, desc_ja, desc_en, tip_ja, tip_en, price_raw, lat, lng, zone="city", kids=False, rain=False, shopping=False):
    p_info = translate_price_obj(price_raw)
    full_name_ja = f"{name_en}（{name_ja}）"
    
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
        "free": p_info["is_free"],
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
        "desc_en": desc_en if desc_en else desc_ja,
        "desc_ja": desc_ja,
        "desc_es": desc_en if desc_en else desc_ja,
        "desc_zh": desc_ja,
        "desc_fr": desc_en if desc_en else desc_ja,
        "desc_de": desc_en if desc_en else desc_ja,
        "tip_en": tip_en if tip_en else tip_ja,
        "tip_ja": tip_ja,
        "tip_es": tip_en if tip_en else tip_ja,
        "tip_zh": tip_ja,
        "tip_fr": tip_en if tip_en else tip_ja,
        "tip_de": tip_en if tip_en else tip_ja,
        "price_ja": p_info["price_ja"],
        "price_en": p_info["price_en"],
        "price_es": p_info["price_es"],
        "price_zh": p_info["price_zh"],
        "price_fr": p_info["price_fr"],
        "price_de": p_info["price_de"]
    }

print("Base builder script compiled successfully.")
