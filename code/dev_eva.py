import json
from requests import request

with open("C:\\Users\\admin\\Enhance\\debug_hc\\json\\project_info\\m3_project_info.json", "r") as f:
    project_info_full = json.load(f)
    
with open("C:\\Users\\admin\\Enhance\\debug_hc\\json\\data\\dataM3_new.json", "r", encoding = "utf-8") as f:
    calls = json.load(f)
    
criteria_names = ["willpaySummary", "nopaySummary", "paidSummary", "callResultAI"]

project_info = {}
for criteria in criteria_names:
    project_info[criteria] = project_info_full["project_info"][criteria]
    
# url = "http://103.176.146.250:5005/predict/dialogue/test" # call API từ môi trường A30
url = "https://cqe-dev-nlp.fpt.ai/dme/predict/dialogue/test" # call API từ môi trường dev

metadata = {}

headers = {
  'Content-Type': 'application/json'
}

re = []
for call in calls:
    payload = json.dumps({"project_info": project_info,
                          "transcript": call["content"],
                          "metadata": metadata,
                          "criteria": criteria_names,
                          "fileName": call["fileName"],
                          "agentChannel": 1})
    
    response = request("POST", url, headers=headers, data=payload).json()
    try:
        call_name = response["fileName"]
    except:
        continue
    criteria_result = {}
    for criteria in criteria_names:
        criteria_result[criteria] = {"decision": response[criteria]["decision"],
                                    "position": response[criteria]["position"]}
    temp_re = {"fileName": call_name}    
    temp_re.update(criteria_result)
    re.append(temp_re)
        
with open("./json/project_info_response.json", "w", encoding = "utf-8") as f:
    json.dump(re, f, ensure_ascii=False, indent=4)
    
