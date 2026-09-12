#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            content = str(data.get('content', ''))
            if "1. Rijksmuseum" in content or "Rijksmuseum (Rijksmuseum" in content or "アムステルダム (Amsterdam)" in content:
                print(f"FOUND 300 SPOTS USER_INPUT at line {i}! Length={len(content)}")
                with open("scripts/dutch_prompt_300_real.txt", "w", encoding="utf-8") as out:
                    out.write(content)
                print("Saved to scripts/dutch_prompt_300_real.txt!")
                break
