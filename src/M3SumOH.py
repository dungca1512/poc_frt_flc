import json

with open("../json/response/nlp_response_m3.json", "r", encoding='utf-8') as f:
    file = json.load(f)
call_name = input("Nhập tên file: ")
call_result = None

for call in file:
    try:
        if call['fileName'] == call_name:
            call_result = call
    except:
        pass

call_data = call_result['data']
re = {}
for data in call_data:
    sum = data['m3SumOH__latest']
    text = sum['text']
    intents = sum['intents']
    entities = sum['entities']
    if text != "":
        re[text] ={'intent': intents, 
                    'entities': entities}

json_obj = json.dumps(re, indent=4, ensure_ascii=False)

with open("../json/response/sumoh.json", "w", encoding='utf-8') as outfile:
    outfile.write(json_obj)