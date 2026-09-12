#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        if "Geuldal & Epen Bronnenwandeling" in line or "Dominicanen Bookshop" in line or "Vrijthof Square" in line:
            print(f"Line {i}: len={len(line)}")
            data = json.loads(line)
            # Find longest string in data
            strings = []
            def get_strings(d):
                if isinstance(d, str):
                    strings.append(d)
                elif isinstance(d, dict):
                    for v in d.values(): get_strings(v)
                elif isinstance(d, list):
                    for v in d: get_strings(v)
            get_strings(data)
            longest = max(strings, key=len) if strings else ""
            print(f"  Longest string len: {len(longest)}")
            if len(longest) > 5000:
                with open("scripts/dutch_raw_300_full.txt", "w", encoding="utf-8") as out:
                    out.write(longest)
                print("  Saved full text to scripts/dutch_raw_300_full.txt!")
                break
