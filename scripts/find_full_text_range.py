#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(6990, len(lines)):
        line = lines[i]
        d = json.loads(line)
        print(f"Line {i}: type={d.get('type')}, len={len(line)}")
        if "アムステルダム" in line or "Maastricht" in line or "Rijksmuseum" in line:
            strings = []
            def search_str(obj):
                if isinstance(obj, str): strings.append(obj)
                elif isinstance(obj, dict): [search_str(v) for v in obj.values()]
                elif isinstance(obj, list): [search_str(v) for v in obj]
            search_str(d)
            if strings:
                longest = max(strings, key=len)
                print(f"  --> Found candidate string len={len(longest)} in line {i}")
                if len(longest) > 10000:
                    with open(f"scripts/dutch_300_full_extracted.txt", "w", encoding="utf-8") as out:
                        out.write(longest)
                    print(f"  🎉 SAVED FULL TEXT from line {i} to scripts/dutch_300_full_extracted.txt!")
                    break
