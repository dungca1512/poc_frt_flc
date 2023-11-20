import json
import requests
import time

state = input("Nhập môi trường: ")

project = input("Nhập tên project: ")

start = time.time()

with open(f"../data/transcript_{project}.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

project_info_poc = json.load(open(f"../project_info/{project}.json", encoding="utf-8"))["project_info"]
criteria_names = [i for i in project_info_poc]

project_info = {}
for criteria in criteria_names:
    project_info.update({criteria: project_info_poc[criteria]})
    
criteria_frt = [i for i in project_info_poc]
project_info_frt = {}
for cri in criteria_frt:
    project_info_frt.update({cri: project_info_poc[cri]})

endpoint = "http://103.176.146.250:5005" # môi trường nlp

url = f"{endpoint}/predict/dialogue/test"

metadata = {}
response = []
agentChannel = 2

for call in data:
    headers = {
        'Content-Type': 'application/json'
    }
    body = {
        "project_info": project_info_frt,
        "transcript": call['content'],
        "metadata": metadata,
        "criteria": criteria_frt,
        "fileName": call['name'],
        "agentChannel": agentChannel
    }
    payload = json.dumps(body)  
    result = requests.request(method="POST", url=url, headers=headers, data=payload).json()
    response.append(result)
    time.sleep(0.4)
    
with open(f'../response/{project}_evaluate.json', 'w', encoding='utf-8') as json_file:
    json.dump(response, json_file, ensure_ascii=False, indent=4)

end = time.time()

print("Hoàn thành!")
print(f"Thời gian chạy: {end - start} s")