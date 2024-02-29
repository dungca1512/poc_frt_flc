import json

with open("C:\\Users\\admin\\Enhance\\debug_hc\\json\\response\\new_response_m3.json", "r", encoding='utf-8') as f:
    file = json.load(f)
        
call_name = input()
call_result = None

for call in file:
    try:
        if call['fileName'] == call_name:
            call_response = call['response']
    except:
        pass
    
response = []

for contents in call_response:
    content = contents["content"]
    data = contents["data"]
    response.append({"content": content, "data": data})
    
with open('C:\\Users\\admin\\Enhance\\debug_hc\\json\\response\\new_call_response_m3.json', 'w', encoding='utf-8') as fp:
    json.dump(response, fp, ensure_ascii=False, indent=4)