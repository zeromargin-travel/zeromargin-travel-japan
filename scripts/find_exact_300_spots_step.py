#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        if "1. Erasmusbrug (Erasmus Bridge" in line or "1. Domtoren (The Dom Tower" in line or "1. Vrijthof (Vrijthof Square" in line:
            print(f"FOUND EXACT 300 TEXT AT LINE {i}! len={len(line)}")
            data = json.loads(line)
            # Search for longest string
            strings = []
            def search_str(d):
                if isinstance(d, str): strings.append(d)
                elif isinstance(d, dict):
                    for v in d.values(): search_str(v)
                elif isinstance(d, list):
                    for v in d: search_str(v)
            search_str(data)
            longest = max(strings, key=len)
            print(f"  Longest string len: {len(longest)}")
            with open("scripts/dutch_prompt_300_TRUE_RAW.txt", "w", encoding="utf-8") as out:
                out.write(longest)
            print("  Saved to scripts/dutch_prompt_300_TRUE_RAW.txt!")
            break
