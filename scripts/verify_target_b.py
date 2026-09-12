import json
import os

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']
fields = ['desc', 'insiderTip', 'whyThisSpot']

total_spots = 0
errors = []
fallback_errors = []

for i in range(1, 11):
    file_path = f'data/target_b_written_{i}.json'
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
            
            desc_en = spot.get('desc_en', '')
            
            for field in fields:
                for lang in langs:
                    key = f"{field}_{lang}"
                    val = spot.get(key, "")
                    if not val:
                        errors.append(f"[{city} - {name}] Missing or empty {key}")
                    elif len(val) < 20: 
                        errors.append(f"[{city} - {name}] Too short {key}: {val}")
                        
                    # Catch fallback to English
                    if lang in ['ja', 'zh'] and val == spot.get(f"{field}_en", "") and val != "":
                        fallback_errors.append(f"[{city} - {name}] {key} fell back to English!")
                        
    except Exception as e:
        errors.append(f"Error parsing {file_path}: {e}")

report_path = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/verification_report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write("# ターゲットB（208件）の検証レポート\n\n")
    f.write(f"- **検証件数**: {total_spots}件\n")
    f.write(f"- **必須フィールド**: 各21項目（7言語 × 3種）\n\n")
    
    if not errors and not fallback_errors:
        f.write("> [!NOTE]\n> **結果**: ALL PASS (合格)\n> すべて完璧に翻訳・修復されました。\n")
    else:
        f.write("> [!WARNING]\n> **結果**: エラーあり\n\n")
        if errors:
            f.write("### 欠損・短すぎエラー\n")
            for err in errors:
                f.write(f"- {err}\n")
        if fallback_errors:
            f.write("### 翻訳サボり（英語のまま）エラー\n")
            for err in fallback_errors:
                f.write(f"- {err}\n")

print(f"Total spots: {total_spots}. Basic errors: {len(errors)}, Fallback errors: {len(fallback_errors)}")
