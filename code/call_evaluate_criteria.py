import json 
import requests

with open("../json/content/dataM3.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

state = input("Nhập môi trường: ")
    
project_info_m3 = json.load(open(f'../json/project_info/m3_project_info_{state}.json', encoding="utf-8"))["project_info"]
criteria_names = [i for i in project_info_m3]

project_info = {}
for criteria in criteria_names:
    project_info.update({criteria: project_info_m3[criteria]})
    
criteria_oh = ["oh2"]
project_info_oh = {}
for oh in criteria_oh:
    project_info_oh.update({oh: project_info_m3[oh]})

if state == "nlp" or state == "test":
    endpoint = "http://103.176.146.250:5005" # môi trường nlp
else:
    endpoint = "https://cqe-dev-nlp.fpt.ai/dme" # môi trường dev

url = f"{endpoint}/predict/dialogue/test"

metadata = {}
response = []
call_result = None

fileName = input("Nhập tên file: ")

for call in data:
    try:
        if call['fileName'] == fileName:
            call_result = call
    except:
        pass
    
headers = {
    'Content-Type': 'application/json'
}
body = {
    "project_info": project_info_oh,
    "transcript": call_result['content'],
    "metadata": metadata,
    "criteria": criteria_oh,
    "fileName": call_result['fileName'],
    "agentChannel": 1
}
payload = json.dumps(body)
result = requests.request("POST", url=url, headers=headers, data=payload).json()
response.append(result)

with open(f'../json/response/evaluate_call_m3_{state}.json', 'w', encoding='utf-8') as json_file:
    json.dump(response, json_file, ensure_ascii=False, indent=4)