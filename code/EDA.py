from sklearn.metrics import classification_report
import pandas as pd
import requests
import json
from tqdm import tqdm
import numpy as np
import time
import math
tqdm.pandas()

def json_read(path: str):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return data

labels = pd.read_csv("C:\\Users\\admin\\Enhance\\debug_hc\\csv\\20230830_031310.csv")
filenames = labels["File Name"].unique().tolist()

call_data = pd.read_json("C:\\Users\\admin\\Enhance\\debug_hc\\json\\data\\m3_call_clean.json")
call_data = call_data[call_data["name"].isin(filenames)]
call_data.sample()

m3_project_info = json_read("C:\\Users\\admin\\Enhance\\debug_hc\\json\\project_info\\m3_project_info.json")["project_info"]
criteria_name = ["willpaySummary", "nopaySummary", "paidSummary"]

def test_criteria(project_info, criteria_name, transcript, metadata, agent_channel, file_name="test"):
    url = "https://cqe-dev-nlp.fpt.ai/dme/predict/dialogue/test"
    payload = json.dumps({
        "project_info": project_info,
        "transcript": transcript,
        "metadata": metadata,
        "criteria": criteria_name,
        "fileName": file_name,
        "agentChannel": agent_channel
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def calculate_criteira(rec, wc_project_info, criteria_name):
    while True:
        try:
            result = test_criteria(wc_project_info, criteria_name,
                           rec["content"], rec["metadata"],
                           rec["agentChannel"], file_name=rec["name"])
            for criteria in criteria_name:
                rec[criteria] = result[criteria]["decision"]
            break
        except:
            print(result.keys())
            print(rec["name"])
            time.sleep(10)
    return rec

sample = call_data.sample().to_dict("records")[0]
result = test_criteria(m3_project_info, criteria_name, sample["content"], sample["metadata"], sample["agentChannel"], file_name=sample["name"])
call_data = call_data.progress_apply(lambda rec: calculate_criteira(rec, m3_project_info, criteria_name), axis=1)

compare = labels.loc[labels["Criterion Name"] == "Contain all information"].merge(call_data, left_on='File Name', right_on='name')
compare = compare[["name", "Criterion Name", "Expected Result"] + criteria_name]
compare['Expected Result'] = compare['Expected Result'].replace(np.nan, "no")
compare["Expected Result"] = compare["Expected Result"].apply(str.lower)
compare['Expected Result'] = compare['Expected Result'].replace("partially", "no")
compare['Expected Result'].value_counts()

acc_willpay = 1-len(compare["Expected Result"].compare(compare["willpaySummary"]))/len(compare)
acc_nopay = 1-len(compare["Expected Result"].compare(compare["nopaySummary"]))/len(compare)
acc_paid = 1-len(compare["Expected Result"].compare(compare["paidSummary"]))/len(compare)

# print(acc_willpay)
# print(acc_nopay)
# print(acc_paid)

accuracy = np.mean([acc_willpay, acc_nopay, acc_paid])
print(f"Accuracy: {accuracy}")
