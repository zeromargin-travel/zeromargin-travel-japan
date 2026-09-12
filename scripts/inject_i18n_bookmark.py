import re

with open('js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

translations = {
    'en': {
        'topBanner': '⭐ Tip: Bookmark this page (Ctrl+D) to easily plan your next European trip!',
        'modalTitle': 'Before you go!',
        'modalText': 'Save this tool to your bookmarks (or add to home screen) so you can quickly create tomorrow\'s route.'
    },
    'nl': {
        'topBanner': '⭐ Tip: Bladwijzer deze pagina (Ctrl+D) om eenvoudig je volgende Europese reis te plannen!',
        'modalTitle': 'Voordat je gaat!',
        'modalText': 'Sla deze tool op in je bladwijzers (of voeg toe aan startscherm) zodat je snel de route van morgen kunt maken.'
    },
    'fr': {
        'topBanner': '⭐ Astuce : Mettez cette page en favori (Ctrl+D) pour planifier facilement votre prochain voyage européen !',
        'modalTitle': 'Avant de partir !',
        'modalText': 'Enregistrez cet outil dans vos favoris (ou ajoutez à l\'écran d\'accueil) pour créer rapidement l\'itinéraire de demain.'
    },
    'de': {
        'topBanner': '⭐ Tipp: Lesezeichen für diese Seite setzen (Strg+D), um deine nächste Europareise einfach zu planen!',
        'modalTitle': 'Bevor du gehst!',
        'modalText': 'Speichere dieses Tool in deinen Lesezeichen (oder auf dem Startbildschirm), damit du die morgige Route schnell erstellen kannst.'
    },
    'es': {
        'topBanner': '⭐ Consejo: ¡Guarda esta página en favoritos (Ctrl+D) para planificar fácilmente tu próximo viaje europeo!',
        'modalTitle': '¡Antes de que te vayas!',
        'modalText': 'Guarda esta herramienta en tus favoritos (o añade a la pantalla de inicio) para poder crear rápidamente la ruta de mañana.'
    },
    'ja': {
        'topBanner': '⭐ Tip: 次回のヨーロッパ旅行もすぐ計画できるよう、このページをブックマーク（Ctrl+D）してください！',
        'modalTitle': 'マップを開く前に！',
        'modalText': '明日のルートもすぐ作れるように、このツールをブックマーク（またはホーム画面に追加）しておきましょう。'
    },
    'zh': {
        'topBanner': '⭐ 提示：将此页面加入书签 (Ctrl+D)，轻松规划您的下一次欧洲之旅！',
        'modalTitle': '出发前请注意！',
        'modalText': '将此工具保存到书签（或添加到主屏幕），以便快速创建明天的路线。'
    }
}

for lang, trans in translations.items():
    # Find the insertion point for this language. We'll insert it after "share.toastCopied": "...",
    pattern = r'("share\.toastCopied":\s*"[^"]*",)'
    
    # We need to find the specific block for the language.
    # The JSON structure in i18n is like "en": { ... }, so we can search for "lang": { and then the next share.toastCopied
    
    def repl(m):
        inject_str = f'\n      "bookmark.topBanner": "{trans["topBanner"]}",\n      "bookmark.modalTitle": "{trans["modalTitle"]}",\n      "bookmark.modalText": "{trans["modalText"]}",'
        return m.group(1) + inject_str
        
    # This is a bit tricky with regex. Let's do it by splitting blocks.
    
parts = content.split('share.toastCopied":')
# parts[0] is everything before the first one (which is EN)
# parts[1] is the rest of EN up to the next one
# We can just iterate through the keys in order of appearance in i18n.js
# The order in i18n.js is EN, JA, NL, FR, DE, ES, ZH based on grep.

order = ['en', 'ja', 'nl', 'fr', 'de', 'es', 'zh']
if len(parts) == 8:
    new_content = parts[0]
    for i in range(1, 8):
        lang = order[i-1]
        trans = translations[lang]
        inject_str = f'share.toastCopied":' + parts[i].split(',', 1)[0] + f',\n      "bookmark.topBanner": "{trans["topBanner"]}",\n      "bookmark.modalTitle": "{trans["modalTitle"]}",\n      "bookmark.modalText": "{trans["modalText"]}",' + parts[i].split(',', 1)[1]
        new_content += inject_str
        
    with open('js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Translations injected successfully.")
else:
    print(f"Error: expected 8 parts, found {len(parts)}")
