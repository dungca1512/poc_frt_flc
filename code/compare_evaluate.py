import json 

old_test = input("Nhập môi trường test cũ: ")
new_test = input("Nhập môi trường test mới: ")

with open(f'../json/response/evaluate_m3_{old_test}.json', 'r', encoding='utf-8') as f:
    old_response = json.load(f)
    
with open(f'../json/response/evaluate_m3_{new_test}.json', 'r', encoding='utf-8') as f:
    test_response = json.load(f)
    
old_re = []
test_re = []
compare = []
    
for old_call in old_response:
    for test_call in test_response:
        if old_call['fileName'] == test_call['fileName']:
            compare.append({
                "fileName": old_call['fileName'],
                "old": {
                    "objectHandling": old_call['objectHandling'],
                    "criterias_order": old_call['criterias_order'],
                },
                "test": {
                    "objectHandling": test_call['object Handling'],
                    "criterias_order": test_call['criterias_order'],
                }
            })
    
with open('../json/response/compare_evaluate.json', 'w', encoding='utf-8') as json_file:
    json.dump(compare, json_file, ensure_ascii=False, indent=4)
    
    