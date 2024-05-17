import json

with open("C:/Users/admin/Enhance/debug_hc/json/response/nlp_response_m3.json", "r", encoding='utf-8') as f:
    file = json.load(f)

call_name = input()
call_result = None

for call in file:
    try:
        if call['fileName'] == call_name:
            call_result = call
    except:
        pass

call_data = call_result['data']
result = {}
for data in call_data:
    sum = data['askPaymentInfo']
    text = sum['text']
    intents = sum['intents']
    entities = sum['entities']
    if text != "":
        result[text] = {'intent': intents, 'entities': entities}

with open("C:/Users/admin/Enhance/debug_hc/json/response/response_criteria/nlp_response_askPaymentInfo.json", "w",
          encoding='utf-8') as outfile:
    json.dump(result, outfile, ensure_ascii=False, indent=4)
