#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        if "Geuldal & Epen Bronnenwandeling" in line:
            data = json.loads(line)
            print(f"Line {i}: type={data.get('type')}")
            # Find any text block in data containing Geuldal
            def find_text(obj):
                if isinstance(obj, str) and "Geuldal & Epen Bronnenwandeling" in obj:
                    return obj
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        res = find_text(v)
                        if res: return res
                if isinstance(obj, list):
                    for item in obj:
                        res = find_text(item)
                        if res: return res
                return None
            
            res = find_text(data)
            if res:
                print(f"Found text len: {len(res)}")
                with open("scripts/dutch_prompt_text.txt", "w", encoding="utf-8") as out:
                    out.write(res)
                print("Saved to scripts/dutch_prompt_text.txt!")
                break
