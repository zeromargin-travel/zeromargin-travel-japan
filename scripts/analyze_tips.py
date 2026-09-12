import json
import subprocess

# 1. Load current master_spots.json
with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# 2. Load original master_spots.json from commit d6c8bc5 (before Target A & B)
result = subprocess.run(['git', 'show', 'd6c8bc5:data/master_spots.json'], capture_output=True, text=True, cwd='/Users/jnabi1/Desktop/zeromargin-travel.github.io')
orig_data = json.loads(result.stdout)

curr_tip_count = {'en': 0, 'fr': 0, 'de': 0, 'es': 0, 'nl': 0}
orig_tip_count = {'en': 0, 'fr': 0, 'de': 0, 'es': 0, 'nl': 0}

missing_tips = []

# Analyze original data
for city, spots in orig_data.items():
    for spot in spots:
        for lang in orig_tip_count.keys():
            if spot.get(f'tip_{lang}'):
                orig_tip_count[lang] += 1

# Analyze current data
for city, spots in master_data.items():
    for spot in spots:
        has_en = False
        for lang in curr_tip_count.keys():
            val = spot.get(f'insiderTip_{lang}')
            if val and str(val).strip():
                curr_tip_count[lang] += 1
                if lang == 'en': has_en = True
        
        # Check if a spot had a tip originally but lost it
        # Note: Original was 'tip_en', current is 'insiderTip_en'
        orig_spot = next((s for c, sp in orig_data.items() for s in sp if s['id'] == spot['id']), None)
        if orig_spot and orig_spot.get('tip_en'):
            if not spot.get('insiderTip_en'):
                missing_tips.append(spot['id'])

print("--- Tip Count Comparison ---")
print("Language | Original (tip_*) | Current (insiderTip_*) | Difference")
for lang in curr_tip_count.keys():
    orig = orig_tip_count[lang]
    curr = curr_tip_count[lang]
    print(f"{lang:8} | {orig:16} | {curr:22} | {curr - orig}")

print(f"\nSpots that HAD 'tip_en' in original but NO 'insiderTip_en' now: {len(missing_tips)}")

if len(missing_tips) > 0:
    print(f"Sample missing spot IDs: {missing_tips[:5]}")
    
# Let's also check the JSON structure of a spot that should have it
sample_spot = next((s for c, sp in master_data.items() for s in sp if s['id'] == 'par_p_1'), None)
if sample_spot:
    print("\nSample Spot keys (par_p_1):", list(sample_spot.keys()))
