import json
from requests import request
import time
import pandas as pd
import timeit

start = timeit.default_timer()
def postprocess_response(response):
    re = {}
    for call in response:
        call_dict = {"name": None,
                    "decision": None,
                    "slots": []}
        for call_result in response[call]:
            call_dict["name"] = call_result["criteria_name"]
            call_dict["decision"] = call_result["decision"]
            slots = call_result["slots"]
            for slot in slots:
                call_dict["slots"].append(slot)        
        re[call] = call_dict
    return re

state = input("Nhập môi trường: ")

with open(f"../json/project_info/m3_project_info_{state}.json", "r") as f:
    project_info_full = json.load(f)
    
with open("../json/content/dataM3.json", "r", encoding = "utf-8") as f:
    calls = json.load(f)
    
# with open("../json/response/call_to_exclude.json", "r") as f:
#     calls_to_exclude = json.load(f)

call_names_to_call = list(pd.read_csv("../csv/20230919_091610.csv")["File Name"].unique())

criteria_names = ["oh2"]

project_info = {}
for criteria in criteria_names:
    project_info[criteria] = project_info_full["project_info"][criteria]

if state == "nlp" or state == "test":
    endpoint = "http://103.176.146.250:5005" # môi trường nlp
else:
    endpoint = "https://cqe-dev-nlp.fpt.ai/dme" # môi trường dev

url = f"{endpoint}/predict/dialogue/test"

metadata = {}

headers = {
  'Content-Type': 'application/json'
}

re = {}
success = 0
fail = 0
for call in calls:
    if call["fileName"] in call_names_to_call:
        payload = json.dumps({"project_info": project_info,
                            "transcript": call["content"],
                            "metadata": metadata,
                            "criteria": criteria_names,
                            "fileName": call["fileName"],
                            "agentChannel": 1})
        try:
            response = request("POST", url, headers=headers, data=payload).json()
        except:
            fail += 1
            continue
        
        try:
            call_name = response["fileName"]
            success += 1
        except:
            fail += 1
            continue
        
        # for criteria in criteria_names:
            
        #     criteria_result[criteria] = {"decision": response[criteria]["decision"],
        #                                        "position": response[criteria]["position"]}
        
        # For many criteria
        re[call_name] = response["criterias_order"]
        
        # For one criteria
        # eval = response[criteria_names[0]]["evaluate"]
        # decision = response[criteria_names[0]]["decision"]
        # re[call_name] = {"evaluate": eval,
        #                  "decision": decision}
        time.sleep(0.4)
        
with open(f"../json/response/response_processed_{state}.json", "w", encoding = "utf-8") as f:
    json.dump(postprocess_response(re), f, ensure_ascii=False, indent=4)

end = timeit.default_timer()

print("Number of success calls:", success)
print("Number of fail calls:", fail)
print("Time:", end - start)
