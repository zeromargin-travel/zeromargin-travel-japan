import json
import os

master_file = 'data/master_spots.json'
with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Load written spots into a dictionary keyed by ID
written_spots = {}
for i in range(1, 6):
    file_path = f'data/target_a_written_{i}.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            spot_id = item['spot']['id']
            written_spots[spot_id] = item['spot']

updated_count = 0

for city, spots in master_data.items():
    for i, spot in enumerate(spots):
        spot_id = spot['id']
        if spot_id in written_spots:
            # Overwrite the spot entirely with the newly written one
            master_data[city][i] = written_spots[spot_id]
            updated_count += 1

with open(master_file, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged {updated_count} completely rewritten spots into master_spots.json.")
