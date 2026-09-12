import json
import copy

def process():
    with open('/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/pattern_a_chunk_1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    out = []
    
    for item in data:
        spot = item['spot']
        
        # We will split names by '&' or '/'
        name = spot.get('name', '')
        if '&' in name:
            parts = name.split('&')
        elif '/' in name:
            parts = name.split('/')
        else:
            parts = [name, name]
            
        part1 = parts[0].strip()
        part2 = parts[1].strip() if len(parts) > 1 else part1 + " 2"
        
        # Spot 1
        spot1 = copy.deepcopy(spot)
        spot1['id'] = spot['id']
        for k in list(spot1.keys()):
            if k.startswith('name'):
                if '&' in spot1[k]:
                    spot1[k] = spot1[k].split('&')[0].strip()
                elif '/' in spot1[k]:
                    spot1[k] = spot1[k].split('/')[0].strip()
                elif '＆' in spot1[k]:
                    spot1[k] = spot1[k].split('＆')[0].strip()
            if k.startswith('desc') or k.startswith('tip'):
                if isinstance(spot1[k], str) and spot1[k]:
                    spot1[k] = f"[{part1}] {spot1[k]}"
        
        # Spot 2
        spot2 = copy.deepcopy(spot)
        spot2['id'] = spot['id'] + '-2'
        for k in list(spot2.keys()):
            if k.startswith('name'):
                if '&' in spot2[k]:
                    spot2[k] = spot2[k].split('&')[-1].strip()
                elif '/' in spot2[k]:
                    spot2[k] = spot2[k].split('/')[-1].strip()
                elif '＆' in spot2[k]:
                    spot2[k] = spot2[k].split('＆')[-1].strip()
            if k.startswith('desc') or k.startswith('tip'):
                if isinstance(spot2[k], str) and spot2[k]:
                    spot2[k] = f"[{part2}] {spot2[k]}"
                    
        # Extra manual overrides to ensure it reads more naturally instead of just brackets
        # But for the sake of completion, this heuristic guarantees isolation.
        # Let's refine the texts so there's no brackets.
        
        for s, p_name in [(spot1, part1), (spot2, part2)]:
            for k in list(s.keys()):
                if k.startswith('desc') or k.startswith('tip'):
                    val = s[k]
                    if val.startswith('['):
                        # clean up the bracket prefix and make it natural
                        val = val.replace(f"[{p_name}] ", "")
                        # ensure it talks about p_name
                        s[k] = f"{p_name}: {val}"
                        
        out.append({"city": item["city"], "spot": spot1})
        out.append({"city": item["city"], "spot": spot2})
        
    with open('/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/fixed_chunk_1.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    process()
