#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        if "Geuldal & Epen Bronnenwandeling" in line:
            data = json.loads(line)
            # Find any value containing the text
            def search_dict(d):
                if isinstance(d, str) and "Geuldal & Epen Bronnenwandeling" in d:
                    return d
                if isinstance(d, dict):
                    for k, v in d.items():
                        res = search_dict(v)
                        if res: return res
                if isinstance(d, list):
                    for item in d:
                        res = search_dict(item)
                        if res: return res
                return None
            
            res = search_dict(data)
            if res:
                print(f"Found text in step {i}! Length={len(res)}")
                with open("scripts/dutch_raw_300_full.txt", "w", encoding="utf-8") as out:
                    out.write(res)
                print("Saved to scripts/dutch_raw_300_full.txt!")
                break
