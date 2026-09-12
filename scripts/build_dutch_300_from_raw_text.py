#!/usr/bin/env python3
"""
Zero-Margin Travel App - Universal Dutch 300 Parser (v33.0.0)
Extracts 60 spots for Amsterdam, 60 for Rotterdam, 60 for The Hague, 60 for Utrecht, 60 for Maastricht.
"""

import os
import json
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

def translate_price_struct(price_str):
    clean = price_str.strip() if price_str else "Free"
    if "Free" in clean or "無料" in clean or "free" in clean.lower():
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
        clean_p = clean.replace("料金:", "").replace("入場料:", "").replace("見学:", "").strip()
        return {
            "price_ja": f"料金: {clean_p}",
            "price_en": f"Entry: {clean_p}",
            "price_es": f"Entrada: {clean_p}",
            "price_zh": f"门票：{clean_p}",
            "price_fr": f"Entrée : {clean_p}",
            "price_de": f"Eintritt: {clean_p}",
            "is_free": False
        }

print("Raw text builder module compiled successfully...")
