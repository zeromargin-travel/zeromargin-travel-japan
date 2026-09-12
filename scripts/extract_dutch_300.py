#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        if "Geuldal & Epen Bronnenwandeling" in line:
            data = json.loads(line)
            content = str(data.get('content', ''))
            print(f"Found line {i}: len={len(content)}")
            with open("scripts/dutch_raw_300_full.txt", "w", encoding="utf-8") as out:
                out.write(content)
            print("Wrote to scripts/dutch_raw_300_full.txt!")
            break
