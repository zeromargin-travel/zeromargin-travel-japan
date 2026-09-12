#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        if "Geuldal & Epen Bronnenwandeling" in line:
            data = json.loads(line)
            print(f"Line {i}: type={data.get('type')}, keys={list(data.keys())}")
            if data.get('type') == 'USER_INPUT':
                print(f"FOUND USER_INPUT at line {i}!")
                content = str(data.get('content', ''))
                with open("scripts/dutch_prompt_text.txt", "w", encoding="utf-8") as out:
                    out.write(content)
                print(f"Saved {len(content)} chars to scripts/dutch_prompt_text.txt!")
