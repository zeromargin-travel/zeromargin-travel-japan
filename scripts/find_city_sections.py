#!/usr/bin/env python3
import re

with open("scripts/dutch_prompt_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Length:", len(text))
matches = re.findall(r'(\n(?:ハーグ|The Hague|Rotterdam|ロッテルダム|Utrecht|ユトレヒト|Maastricht|マーストリヒト)[^\n]*)', text)
for m in matches[:30]:
    print("MATCH:", repr(m))
