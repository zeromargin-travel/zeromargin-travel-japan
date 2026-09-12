import json
import statistics

# Load current data
with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

current_spots = {}
for city, spots in master_data.items():
    for spot in spots:
        current_spots[spot.get('id')] = spot

# 2. Which language is richest on average?
langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']
lang_lengths = {lang: [] for lang in langs}

for spot in current_spots.values():
    for lang in langs:
        text = spot.get(f'desc_{lang}', '')
        lang_lengths[lang].append(len(text))

avg_lengths = {lang: statistics.mean(lengths) for lang, lengths in lang_lengths.items()}

# 3. Discrepancy analysis
# Let's say "rich" is > 80 chars, "poor" is < 40 chars
translation_solvable = 0
terrible_everywhere = 0

for spot in current_spots.values():
    lengths = {lang: len(spot.get(f'desc_{lang}', '')) for lang in langs}
    max_len = max(lengths.values())
    min_len = min(lengths.values())
    
    if max_len < 40:
        terrible_everywhere += 1
    elif max_len > 80 and min_len < 40:
        translation_solvable += 1

print(f"Total current spots: {len(current_spots)}")
print("\nAverage Description Length by Language (Characters):")
# Note: Asian languages (JA, ZH) convey more meaning per character than European languages.
# A 100-char JA text is often equivalent in information to a 200-char EN text.
for lang, avg in sorted(avg_lengths.items(), key=lambda x: x[1], reverse=True):
    print(f"  {lang.upper()}: {avg:.1f} chars")
    
print(f"\nSpots terrible everywhere (Max length across all languages < 40 chars): {terrible_everywhere}")
print(f"Spots solvable by translation (At least one language > 80 chars, but some < 40 chars): {translation_solvable}")

print("\nSpot check on Curry 36 text lengths across languages:")
for spot in current_spots.values():
    if 'Curry 36' in spot.get('name', ''):
        print(f"Lengths for {spot.get('name')}:")
        for lang in langs:
            print(f"  {lang}: {len(spot.get(f'desc_{lang}', ''))} chars -> {spot.get(f'desc_{lang}', '')}")
        break

print("\nSpot check on Brandenburg Gate (Short everywhere):")
for spot in current_spots.values():
    if 'Brandenburger Tor' in spot.get('name', ''):
        for lang in langs:
            print(f"  {lang}: {len(spot.get(f'desc_{lang}', ''))} chars")
        break
