import json 

# Opening JSON file
with open("content.json", "r", encoding='utf-8') as data:
    content_data = json.load(data)

result = []

for call in content_data:
    file_name = call['file_name']
    agentChannel = 1
    transcript = call['transcript']
    tr = []
    for sentences in transcript:
        text = {}
        text["channel"] = sentences['channel']
        text["text"] = sentences['text']
        tr.append(text)
    result.append({"file_name": file_name, "agentChannel": agentChannel, "content": tr})
        
with open('result_content.json', 'w', encoding='utf-8') as fp:
    json.dump(result, fp, ensure_ascii=False, indent=4)
    
print(len(result))