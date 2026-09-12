import json

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

out_path = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/scratch/suspicious_names.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    for city, spots in data.items():
        for spot in spots:
            name = spot.get('name', '')
            if " & " in name or " and " in name.lower() or " / " in name:
                out.write(f"{city} | {name}\n")
print(f"Wrote names to {out_path}")
