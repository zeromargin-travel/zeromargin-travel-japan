#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        if "1. Mauritshuis (The Mauritshuis" in line or "1. Domtoren (The Dom Tower)" in line or "1. Vrijthof (Vrijthof Square)" in line:
            print(f"FOUND 300 TEXT AT LINE {i}! len={len(line)}")
            data = json.loads(line)
            content = str(data.get('content', ''))
            print(f"  Content len={len(content)}")
            if len(content) > 1000:
                with open("scripts/dutch_prompt_300_real_text.txt", "w", encoding="utf-8") as out:
                    out.write(content)
                print("  Saved to scripts/dutch_prompt_300_real_text.txt!")
                break
