#!/usr/bin/env python3
import json

transcript_path = "/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines) - 1, -1, -1):
        data = json.loads(lines[i])
        if data.get('type') == 'USER_INPUT':
            content = str(data.get('content', ''))
            print(f"USER_INPUT at line {i}: len={len(content)}")
            if "アムステルダム" in content or "Maastricht" in content or "Rijksmuseum" in content:
                print(f"  FOUND TARGET USER_INPUT at line {i}! Length={len(content)}")
                with open("scripts/dutch_prompt_text.txt", "w", encoding="utf-8") as out:
                    out.write(content)
                print("  Saved to scripts/dutch_prompt_text.txt!")
                break
