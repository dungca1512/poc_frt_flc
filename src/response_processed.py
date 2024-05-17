import json

state = input("Enter enviroment: ")

with open(f'../json/response/evaluate_m3_{state}.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

response = {}

for call in data:
    name = "oh2",
    decision = call['oh2']['decision']
    if len(call['criterias_order']) != 0:
        slots = call['criterias_order']['slots']
    else:
        slots = []
    response[name] = {'decision': decision, 'slots': slots}

with open(f'../json/response/evaluate_m3_{state}_processed.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)