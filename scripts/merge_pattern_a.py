import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
master_file = os.path.join(base_dir, 'data', 'master_spots.json')
classification_file = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/scratch/classification.md'

# 1. Get the list of 118 Pattern A combo names to remove
pattern_a_names = set()
in_pattern_a = False
with open(classification_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('## Pattern A'):
            in_pattern_a = True
            continue
        elif line.startswith('## Pattern B/C'):
            in_pattern_a = False
            continue
        
        if in_pattern_a and line.startswith('- '):
            parts = line[2:].split(' | ')
            if len(parts) == 2:
                city = parts[0].strip()
                name = parts[1].strip()
                pattern_a_names.add(f"{city}|{name}")

# 2. Read master DB
with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# 3. Remove original combo spots
removed_count = 0
for city in master_data:
    new_spots = []
    for spot in master_data[city]:
        key = f"{city}|{spot.get('name', '')}"
        if key in pattern_a_names:
            removed_count += 1
        else:
            new_spots.append(spot)
    master_data[city] = new_spots

print(f"Removed {removed_count} combo spots from master DB.")

# 4. Add the new split spots from chunks
added_count = 0
duplicate_count = 0
for i in range(1, 6):
    chunk_file = os.path.join(base_dir, 'data', f'fixed_chunk_{i}.json')
    if not os.path.exists(chunk_file):
        continue
    
    with open(chunk_file, 'r', encoding='utf-8') as f:
        fixed_items = json.load(f)
        
    for item in fixed_items:
        city = item['city']
        spot = item['spot']
        
        if city not in master_data:
            master_data[city] = []
            
        # Deduplication check
        existing_names = [s.get('name', '').lower() for s in master_data[city]]
        if spot.get('name', '').lower() in existing_names:
            duplicate_count += 1
            print(f"  [Duplicate Skip] {city} - {spot.get('name')}")
        else:
            master_data[city].append(spot)
            added_count += 1

print(f"Added {added_count} new distinct spots. Skipped {duplicate_count} duplicates.")

# 5. Save back to master DB
with open(master_file, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print("Master database successfully updated!")
