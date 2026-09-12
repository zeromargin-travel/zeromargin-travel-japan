#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    data = json.loads(lines[6718])
    content = str(data.get('content', ''))
    print(f"Step 6718 content length: {len(content)}")
    with open("scripts/dutch_300_full_raw.txt", "w", encoding="utf-8") as out:
        out.write(content)
    print("Saved to scripts/dutch_300_full_raw.txt!")
