import json
import re

classification_file = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/curation_report.md'
master_file = 'data/master_spots.json'

# 1. Parse REJECTs
rejects = set()
with open(classification_file, 'r', encoding='utf-8') as f:
    for line in f:
        # e.g., * **[REJECT]** - Amsterdam, Netherlands: Marken
        match = re.search(r'\*\s*\*\*\[REJECT\]\*\*\s*-\s*(.+?):\s*(.+)', line)
        if match:
            city = match.group(1).strip()
            name = match.group(2).strip()
            rejects.add(f"{city}|{name}")

# 2. Simulate master DB after applying rejects
with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

simulated_db = {}
for city, spots in master_data.items():
    simulated_db[city] = []
    for spot in spots:
        key = f"{city}|{spot.get('name', '')}"
        if key not in rejects:
            simulated_db[city].append(spot)

# 3. Analyze Balance
print(f"{'City':<30} | {'Total':<5} | {'Category Breakdown'}")
print("-" * 100)

for city, spots in simulated_db.items():
    total = len(spots)
    
    # Categorize
    # Spots have a 'category' string or 'categories' array. Let's use 'categories' if available, else 'category'
    cat_counts = {}
    for spot in spots:
        # Just use the primary 'category' string for simplicity
        primary_cat = spot.get('category', 'Unknown').split('&')[0].strip()
        cat_counts[primary_cat] = cat_counts.get(primary_cat, 0) + 1
        
    # Sort categories by count
    sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
    cat_str = ", ".join([f"{k}({v})" for k, v in sorted_cats[:4]]) # top 4 categories
    
    print(f"{city:<30} | {total:<5} | {cat_str}")

total_spots = sum(len(spots) for spots in simulated_db.values())
print("-" * 100)
print(f"Total simulated spots: {total_spots} (Original was 1194 before splits)")
