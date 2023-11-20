import json

with open('../data/transcript_flc_poc.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
count = 0

for call in data:
    count += 1
    
print(count)
