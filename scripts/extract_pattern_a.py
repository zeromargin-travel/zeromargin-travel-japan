import json
import re

classification_file = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/scratch/classification.md'
master_file = 'data/master_spots.json'

# Parse Pattern A from classification.md
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
            # Format: - City | Name
            parts = line[2:].split(' | ')
            if len(parts) == 2:
                city = parts[0].strip()
                name = parts[1].strip()
                pattern_a_names.add(f"{city}|{name}")

# Extract full JSON objects
with open(master_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

extracted_spots = []
for city, spots in data.items():
    for spot in spots:
        name = spot.get('name', '')
        key = f"{city}|{name}"
        if key in pattern_a_names:
            extracted_spots.append({
                'city': city,
                'spot': spot
            })

print(f"Extracted {len(extracted_spots)} Pattern A spots.")

# Split into 5 chunks
chunks = 5
chunk_size = len(extracted_spots) // chunks + (len(extracted_spots) % chunks > 0)

for i in range(chunks):
    chunk_data = extracted_spots[i*chunk_size : (i+1)*chunk_size]
    if not chunk_data:
        continue
    out_file = f'data/pattern_a_chunk_{i+1}.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(chunk_data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(chunk_data)} spots to {out_file}")
