import json

with open('../json/response/compare_evaluate.json', 'r', encoding='utf-8') as f:
    compare_response = json.load(f)
    
compare_call_fail = []
count = 0
call_name = []
    
for call in compare_response:
    if str(call['old']) != str(call['test']):
        compare_call_fail.append(call)
        count += 1
        call_name.append(call['fileName'])
        
with open('../json/response/compare_call_fail.json', 'w', encoding='utf-8') as json_file:
    json.dump(compare_call_fail, json_file, ensure_ascii=False, indent=4)
    
print(count)
print(call_name)