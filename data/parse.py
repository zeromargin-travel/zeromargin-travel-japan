import json

with open("/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_chunk_8.json", "r") as f:
    data = json.load(f)

for item in data:
    spot = item["spot"]
    print(f"ID: {spot.get('id')}")
    print(f"Name: {spot.get('name')}")
    print(f"Desc: {spot.get('desc_en', spot.get('desc'))}")
    print(f"Tip: {spot.get('tip_en', spot.get('tip'))}")
    print("---")
