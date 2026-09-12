import json
import re

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']
fields = ['desc', 'insiderTip', 'whyThisSpot']

results = {
    'total_spots': 0,
    'issues': {
        'ja_lang_tag_prefix': [],      # "[JA]" prefix in JA field 
        'wrong_lang_content': [],      # JA field has mostly ASCII (likely English)
        'generic_district_template': [], # "X in Y district."
        'too_short': [],              # < 40 chars
        'missing_field': [],          # field doesn't exist
        'all_same_across_lang': [],   # all langs have identical text (copy-paste)
    }
}

def is_mostly_ascii(text):
    """Return True if >80% of non-space chars are ASCII - likely English in a JA/ZH field."""
    if not text:
        return False
    non_space = text.replace(' ', '').replace('\n', '')
    if not non_space:
        return False
    ascii_chars = sum(1 for c in non_space if ord(c) < 128)
    return ascii_chars / len(non_space) > 0.80

district_pattern = re.compile(r'^.{0,60} in .{0,40} district\.$', re.IGNORECASE)
ja_tag_pattern = re.compile(r'^\s*\[JA\]', re.IGNORECASE)

for city, spots in master_data.items():
    for spot in spots:
        results['total_spots'] += 1
        name = spot.get('name', 'Unknown')
        
        # Collect desc texts across all langs
        all_descs = [spot.get(f'desc_{lang}', '') for lang in langs]
        
        for field in fields:
            values = {}
            for lang in langs:
                key = f'{field}_{lang}'
                val = spot.get(key, '')
                values[lang] = val
                
                # 1. Missing field
                if not val:
                    results['issues']['missing_field'].append(
                        f"{city} | {name} | {key}")
                    continue
                    
                # 2. "[JA]" or "[ZH]" prefix tag left in
                if ja_tag_pattern.match(val):
                    results['issues']['ja_lang_tag_prefix'].append(
                        f"{city} | {name} | {key}: {val[:80]}")
                
                # 3. JA/ZH field contains English content
                if lang in ['ja', 'zh'] and is_mostly_ascii(val):
                    results['issues']['wrong_lang_content'].append(
                        f"{city} | {name} | {key}: {val[:80]}")
                
                # 4. Generic "X in Y district." template
                if field == 'desc' and lang == 'en' and district_pattern.match(val):
                    results['issues']['generic_district_template'].append(
                        f"{city} | {name}: {val}")
                
                # 5. Too short
                if len(val) < 25:
                    results['issues']['too_short'].append(
                        f"{city} | {name} | {key}: '{val}'")
            
            # 6. All lang versions identical (copy-paste from EN)
            unique_vals = set(v for v in values.values() if v)
            if len(unique_vals) == 1 and len(values) > 1:
                sample = list(unique_vals)[0]
                if is_mostly_ascii(sample):  # only flag if the one value is English
                    results['issues']['all_same_across_lang'].append(
                        f"{city} | {name} | {field}: ALL LANGS SAME ENGLISH TEXT")

# Summary
print("=" * 70)
print("COMPREHENSIVE DATA QUALITY AUDIT")
print("=" * 70)
print(f"\nTotal Spots: {results['total_spots']}")
print(f"\n{'Issue Category':<40} {'Count':>6}")
print("-" * 48)
for issue_key, items in results['issues'].items():
    print(f"  {issue_key:<38} {len(items):>6}")

print("\n")
print("=" * 70)
print("DETAIL: [JA] Tag Prefix Errors (sample 10)")
print("=" * 70)
for item in results['issues']['ja_lang_tag_prefix'][:10]:
    print(f"  {item}")

print("\n")
print("=" * 70)
print("DETAIL: Wrong Language Content in JA/ZH fields (sample 10)")
print("=" * 70)
for item in results['issues']['wrong_lang_content'][:10]:
    print(f"  {item}")

print("\n")
print("=" * 70)
print("DETAIL: ALL LANGS SAME ENGLISH (sample 10)")
print("=" * 70)
for item in results['issues']['all_same_across_lang'][:10]:
    print(f"  {item}")

# Save full report
report = []
for issue_type, items in results['issues'].items():
    report.append(f"\n## {issue_type} ({len(items)} items)\n")
    for item in items:
        report.append(f"- {item}\n")

with open('/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/full_audit.md', 'w', encoding='utf-8') as f:
    f.write("# Full Data Quality Audit Report\n\n")
    f.writelines(report)


# Additional: Check if missing_field is because key literally doesn't exist vs empty string
# Also look at what was the state BEFORE our rewrites (git history)
