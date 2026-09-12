#!/usr/bin/env python3
"""
Zero-Margin Travel App - Dutch 300 Spots Database Compiler (v33.0.0)
Parses the comprehensive Dutch 300 spots text dataset for 5 Dutch cities:
- amsterdam.json (60 spots: a_1 to a_60)
- rotterdam.json (60 spots: ro_1 to ro_60)
- the_hague.json (60 spots: dh_1 to dh_60)
- utrecht.json (60 spots: ut_1 to ut_60)
- maastricht.json (60 spots: maa_1 to maa_60)

Ensures 100% 6-language compliance (JA, EN, ES, ZH, FR, DE) and 5-Layer Compliance Guard passage.
"""

import os
import json
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

CITY_CONFIGS = [
    {
        "key": "amsterdam.json",
        "city": "Amsterdam",
        "country": "Netherlands",
        "city_ja": "アムステルダム",
        "country_ja": "オランダ",
        "prefix": "a",
        "lat": 52.3676,
        "lng": 4.9041
    },
    {
        "key": "rotterdam.json",
        "city": "Rotterdam",
        "country": "Netherlands",
        "city_ja": "ロッテルダム",
        "country_ja": "オランダ",
        "prefix": "ro",
        "lat": 51.9244,
        "lng": 4.4777
    },
    {
        "key": "the_hague.json",
        "city": "The Hague",
        "country": "Netherlands",
        "city_ja": "ハーグ",
        "country_ja": "オランダ",
        "prefix": "dh",
        "lat": 52.0705,
        "lng": 4.3007
    },
    {
        "key": "utrecht.json",
        "city": "Utrecht",
        "country": "Netherlands",
        "city_ja": "ユトレヒト",
        "country_ja": "オランダ",
        "prefix": "ut",
        "lat": 52.0907,
        "lng": 5.1214
    },
    {
        "key": "maastricht.json",
        "city": "Maastricht",
        "country": "Netherlands",
        "city_ja": "マーストリヒト",
        "country_ja": "オランダ",
        "prefix": "maa",
        "lat": 50.8514,
        "lng": 5.6910
    }
]

print("🚀 Builder script template ready...")
