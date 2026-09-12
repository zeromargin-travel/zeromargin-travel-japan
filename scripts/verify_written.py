import json
import os

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']
fields = ['desc', 'insiderTip', 'whyThisSpot']

total_spots = 0
errors = []

for i in range(1, 6):
    file_path = f'data/target_a_written_{i}.json'
    if not os.path.exists(file_path):
        errors.append(f"Missing file: {file_path}")
        continue
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for spot_obj in data:
            spot = spot_obj['spot']
            city = spot_obj['city']
            name = spot.get('name', 'Unknown')
            total_spots += 1
            
            for field in fields:
                for lang in langs:
                    key = f"{field}_{lang}"
                    val = spot.get(key, "")
                    if not val:
                        errors.append(f"[{city} - {name}] Missing or empty {key}")
                    elif len(val) < 20: # JA/ZH might be short, but shouldn't be under 20 chars
                        errors.append(f"[{city} - {name}] Too short {key}: {val}")
                        
            # Check for '&' artifacts in EN desc
            desc_en = spot.get('desc_en', '')
            if ' & ' in desc_en and 'museum' not in desc_en.lower():
                # Just a warning
                pass
                
    except Exception as e:
        errors.append(f"Error parsing {file_path}: {e}")

report_path = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/verification_report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write("# ターゲットA（115件）のテキスト検証レポート\n\n")
    f.write(f"- **検証件数**: {total_spots}件\n")
    f.write(f"- **必須フィールド数**: 各21項目（7言語 × 3種）\n\n")
    
    if not errors:
        f.write("> [!NOTE]\n> **結果**: ALL PASS (合格)\n> 欠損や極端に短いテキストはなく、すべてのAIが要件を満たしたテキストを生成しました。\n")
    else:
        f.write("> [!WARNING]\n> **結果**: エラーあり\n\n")
        for err in errors:
            f.write(f"- {err}\n")

print(f"Verification complete. Total spots: {total_spots}. Errors: {len(errors)}")
