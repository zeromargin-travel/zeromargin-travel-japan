import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
artifact_path = '/Users/jnabi1/.gemini/antigravity/brain/1d2a3424-9949-4a2a-b152-b7899aed3bf3/curation_report.md'

with open(artifact_path, 'w', encoding='utf-8') as outfile:
    outfile.write("# キュレーション審査レポート（全239件）\n\n")
    outfile.write("AI審査員が、今回新しく分割された239件のスポットを厳格に審査しました。\n\n")
    
    keep_count = 0
    reject_count = 0
    
    # We will read them first to count
    content = ""
    for i in range(1, 6):
        chunk_file = os.path.join(base_dir, 'data', f'curation_chunk_{i}.md')
        if os.path.exists(chunk_file):
            with open(chunk_file, 'r', encoding='utf-8') as infile:
                text = infile.read()
                keep_count += text.count('[KEEP]')
                reject_count += text.count('[REJECT]')
                content += f"## Chunk {i}\n"
                content += text + "\n\n"
                
    outfile.write(f"> [!IMPORTANT]\n> **審査サマリー**\n> - 🟢 厳選リストに残すべき（KEEP）: {keep_count}件\n> - 🔴 除外すべき・重複（REJECT）: {reject_count}件\n\n")
    outfile.write("---\n\n")
    outfile.write(content)

print(f"Merged report created at {artifact_path} with {keep_count} KEEP and {reject_count} REJECT.")
