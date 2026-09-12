import json

with open('data/master_spots.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

combined_spots = []
for city, spots in data.items():
    for spot in spots:
        name = spot.get('name', '')
        # Check for suspicious patterns like " & ", " and ", " / "
        if " & " in name or " and " in name.lower() or " / " in name:
            combined_spots.append({
                'city': city,
                'name': name,
                'id': spot.get('id')
            })

for s in combined_spots:
    print(f"- {s['city']}: {s['name']}")
print(f"\nTotal found: {len(combined_spots)}")
