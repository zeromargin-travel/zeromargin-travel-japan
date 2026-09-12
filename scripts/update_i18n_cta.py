import re

with open('js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

updates = {
    'en': {'hero.cta': '👇 Choose your destination'},
    'nl': {'hero.cta': '👇 Kies je bestemming'},
    'fr': {'hero.cta': '👇 Choisissez votre destination'},
    'de': {'hero.cta': '👇 Wähle dein Reiseziel'},
    'es': {'hero.cta': '👇 Elige tu destino'},
    'ja': {'hero.cta': '👇 目的地を選択'},
    'zh': {'hero.cta': '👇 选择您的目的地'}
}

parts = content.split('translations: {')
if len(parts) == 2:
    prefix = parts[0]
    json_part = parts[1]
    
    new_json_part = json_part
    for lang, trans_dict in updates.items():
        lang_split = new_json_part.split(f'"{lang}": {{')
        if len(lang_split) >= 2:
            inner_content = lang_split[1]
            
            for key, val in trans_dict.items():
                escaped_val = val.replace('"', '\\"')
                pattern = rf'("{key}":\s*")[^"]*(")'
                inner_content = re.sub(pattern, rf'\g<1>{escaped_val}\g<2>', inner_content, count=1)
                
            lang_split[1] = inner_content
            new_json_part = f'"{lang}": {{'.join(lang_split)
            
    with open('js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(prefix + 'translations: {' + new_json_part)
    print("i18n successfully updated!")
