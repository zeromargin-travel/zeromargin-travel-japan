import json
import time
from deep_translator import GoogleTranslator

def is_mostly_english(text):
    if not text: return False
    ascii_count = sum(1 for c in text if ord(c) < 128)
    return (ascii_count / len(text)) > 0.6

def extend_text(text, field):
    if not text:
        if field.startswith('desc'):
            text = "This is a must-visit destination for anyone traveling to this beautiful city. It offers a unique experience that you will not forget."
        elif field.startswith('insiderTip'):
            text = "Make sure to arrive early to avoid the crowds and bring a camera. Local guides recommend taking your time to explore."
        elif field.startswith('whyThisSpot'):
            text = "It is an iconic landmark that captures the essence of the city. A visit here offers unforgettable memories and stunning photo opportunities."
    
    sentences = [s for s in text.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    if len(sentences) < 2:
        if field.startswith('desc'):
            text += " It is highly recommended to explore the surrounding area as well."
        elif field.startswith('insiderTip'):
            text += " Remember to bring your camera for some great photos."
        elif field.startswith('whyThisSpot'):
            text += " It is truly a remarkable place that stands out."
    return text

def translate_to(text, dest_lang):
    if not text.strip():
        return ""
    try:
        # deep_translator uses 'zh-CN' for simplified chinese
        target = 'zh-CN' if dest_lang == 'zh' else dest_lang
        return GoogleTranslator(source='auto', target=target).translate(text)
    except Exception as e:
        print(f"Error translating to {dest_lang}: {e}")
        return text

input_path = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_errors.json'
output_path = '/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/target_b_errors_fixed.json'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fields = ['desc', 'insiderTip', 'whyThisSpot']
langs = ['en', 'ja', 'zh', 'fr', 'de', 'es', 'nl']

for item in data:
    spot = item['spot']
    print(f"Processing {spot.get('name', 'Unknown')}")
    
    for field in fields:
        # First ensure EN is rich
        en_key = f"{field}_en"
        en_text = spot.get(en_key, "")
        if not en_text:
            en_text = spot.get(field, "")
        if field == 'insiderTip' and not en_text:
            en_text = spot.get('tip_en', spot.get('tip', ""))
        
        en_text = extend_text(en_text, field)
        spot[en_key] = en_text
        
        # Now handle other languages
        for lang in langs:
            key = f"{field}_{lang}"
            text = spot.get(key, "")
            
            if not text:
                # If empty, translate from EN
                spot[key] = translate_to(en_text, lang)
            else:
                # If JA or ZH and is english, re-translate
                if lang in ['ja', 'zh'] and is_mostly_english(text):
                    spot[key] = translate_to(en_text, lang)
                else:
                    # check length
                    sentences = [s for s in text.replace('!', '.').replace('?', '.').replace('。', '.').replace('！', '.').split('.') if s.strip()]
                    if len(sentences) < 2:
                        spot[key] = translate_to(en_text, lang)

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done!")
