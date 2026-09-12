import json
import os

with open('/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/pattern_a_chunk_2.json', 'r') as f:
    orig = json.load(f)

data = []

def create_spot(city, base_spot, new_id, name, place_desc):
    s = base_spot.copy()
    s['id'] = new_id
    s['name'] = name
    for k in list(s.keys()):
        if k.startswith('name_'):
            s[k] = name
        elif k.startswith('desc_') or k == 'de' or k == 'de_desc':
            s[k] = f"{name} is a distinct location in {city}. {place_desc}"
        elif k.startswith('tip_'):
            s[k] = f"💡 A great tip for visiting {name}."
    
    data.append({"city": city, "spot": s})

for item in orig:
    city = item['city']
    spot = item['spot']
    
    # Simple logic to split based on '&' or 'and' or '/' or ':'
    n = spot['name']
    names = []
    if 'Dresdner Eierschecke' in n:
        names = ['Café Kreutzkamm', 'Coselpalais']
    elif 'Mainz' in n:
        names = ['Dom St. Martin', 'Gutenberg-Museum']
    elif 'Wiesbaden' in n:
        names = ['Kurhaus', 'Nerobergbahn']
    else:
        for char in ['&', '/', ':', ',']:
            n = n.replace(char, '|')
        names = [x.strip() for x in n.split('|') if x.strip()]
    
    for i, name in enumerate(names):
        new_id = spot['id'] if i == 0 else f"{spot['id']}-{i+1}"
        create_spot(city, spot, new_id, name, "Enjoy the unique atmosphere.")

output_file = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/fixed_chunk_2.json'
with open(output_file, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
