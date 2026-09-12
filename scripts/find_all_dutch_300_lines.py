#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"Total lines in transcript_full.jsonl: {len(lines)}")
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i]
        if "Mauritshuis" in line and "60. Geuldal" in line:
            print(f"Line {i} has BOTH Mauritshuis and Geuldal! Length={len(line)}")
            # Extract text
            strings = []
            def search_str(d):
                if isinstance(d, str): strings.append(d)
                elif isinstance(d, dict): [search_str(v) for v in d.values()]
                elif isinstance(d, list): [search_str(v) for v in d]
            search_str(json.loads(line))
            longest = max(strings, key=len)
            print(f"  Longest string len: {len(longest)}")
            with open("scripts/dutch_prompt_300_TRUE_ALL.txt", "w", encoding="utf-8") as out:
                out.write(longest)
            print("  🎉 Saved to scripts/dutch_prompt_300_TRUE_ALL.txt!")
            break
