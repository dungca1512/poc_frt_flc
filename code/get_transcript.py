import json

with open('../json/data/dataM3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
transcripts = []

for call in data:
    fileName = call['fileName']
    content = call['content']
    transcripts.append({
        'fileName': fileName,
        'content': content
    })
    
with open('../json/data/transcriptM3.json', 'w', encoding='utf-8') as df:
    json.dump(transcripts, df, ensure_ascii=False, indent=4)