#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    data = json.loads(lines[6899])
    content = data.get('content', '')
    print(f"Line 6899 content length: {len(content)}")
    with open("scripts/full_user_300_prompt.txt", "w", encoding="utf-8") as out:
        out.write(content)
    print("Saved to scripts/full_user_300_prompt.txt!")
