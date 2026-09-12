#!/usr/bin/env python3
"""
Zero-Margin Travel App - Dutch 300 Text Extractor and Compiler (v33.0.0)
Extracts all 300 spots from the user's prompt text and populates:
- amsterdam.json (60 spots: a_1 to a_60)
- rotterdam.json (60 spots: ro_1 to ro_60)
- the_hague.json (60 spots: dh_1 to dh_60)
- utrecht.json (60 spots: ut_1 to ut_60)
- maastricht.json (60 spots: maa_1 to maa_60)
"""

import os
import json
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
cities_dir = os.path.join(base_dir, '..', 'data', 'cities')

# Let's inspect existing city JSONs if needed
print("Compiler script created...")
