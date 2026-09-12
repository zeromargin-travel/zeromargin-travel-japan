#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        if "Van Gogh Museum" in line and "Erasmusbrug" in line and "Vrijthof" in line:
            print(f"FOUND 300 text at line {i}! Length={len(line)}")
            data = json.loads(line)
            # Find longest string in data
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
            with open("scripts/dutch_prompt_300_real.txt", "w", encoding="utf-8") as out:
                out.write(longest)
            print("  Saved to scripts/dutch_prompt_300_real.txt!")
            break
