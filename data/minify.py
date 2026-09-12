import json

with open('/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/fixed_chunk_2.json', 'r') as f:
    data = json.load(f)

minified = []
for item in data:
    s = item['spot']
    s_mini = {
        'id': s['id'],
        'name': s['name'],
        'locationZone': s.get('locationZone'),
        'lat': s.get('lat'),
        'lng': s.get('lng'),
        'desc_en': s.get('desc_en'),
        'tip_en': s.get('tip_en')
    }
    minified.append({'city': item['city'], 'spot': s_mini})

with open('/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/fixed_chunk_2_mini.json', 'w') as f:
    json.dump(minified, f, indent=2)
