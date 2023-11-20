import json

data = json.load(open('C:\\Users\\admin\\Enhance\\debug_hc\\json\\response\\evaluate_m3.json', 'r', encoding='utf-8'))
fileName = input("Enter filename: ")
call_evaluate = None

for call in data:
    if call['fileName'] == fileName:
        call_evaluate = call

response_evaluate = []

for evaluate in call_evaluate:
    result_evaluate = {"fileName": fileName,
                        "nopaySummary": call_evaluate['nopaySummary'],
                        "paidSummary": call_evaluate['paidSummary'],
                        "willpaySummary": call_evaluate['willpaySummary'],
                        "criterias_order": call_evaluate['criterias_order']}
                    
response_evaluate.append(result_evaluate)
    
with open('C:\\Users\\admin\\Enhance\\debug_hc\\json\\response\\call_evaluate_m3.json', 'w', encoding='utf-8') as json_file:
    json.dump(response_evaluate, json_file, ensure_ascii=False, indent=4)
    