#!/ casualties/env python3
import json, os

for tname in ["transcript.jsonl", "transcript_full.jsonl"]:
    tpath = f"/Users/jnabi1/.gemini/antigravity/brain/bfc6dcdc-9139-449d-91ce-2a18ff524e06/.system_generated/logs/{tname}"
    if not os.path.exists(tpath):
        continue
    with open(tpath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines()):
            if "マーストリヒト" in line or "Maastricht" in line:
                data = json.loads(line)
                content = str(data.get('content', ''))
                if len(content) > 1000:
                    print(f"[{tname}] Line {i}: len={len(content)}")
                    with open("scripts/dutch_raw_300.txt", "w", encoding="utf-8") as out:
                        out.write(content)
                    print("Wrote to scripts/dutch_raw_300.txt!")
                    break
