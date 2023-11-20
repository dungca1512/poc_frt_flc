import json
import pandas as pd

state = input("Nhập môi trường: ")

with open(f"../json/response/response_processed_{state}.json", "r") as f:
    response_test = json.load(f)
    
with open("../json/response/response_processed.json", "r") as f:
    predictions_before = json.load(f)
    
with open("../json/response/oh2_labels.json", "r") as f:
    labels = json.load(f)

def oh2_postprocess(response):  
    entities_needed = ["payment_datetime", "amount", "oh_solution", "motivation_title"]
    re = {}
    for call_name in response:
        count = 0
        response_i = response[call_name]
        slots = response_i["slots"]
        
        for entity in entities_needed:
            if entity in slots: count += 1
            
        if count == 4: result = "Yes"
        else: result = "No"
        
        re[call_name] = result

    return re

predictions_after = oh2_postprocess(response_test)

df_call_improved = pd.DataFrame({'Name': [], 'Label': [], 'Prediction before': [], 'Prediction after': []})
df_call_lost = pd.DataFrame({'Name': [], 'Label': [], 'Prediction before': [], 'Prediction after': []})

before_acc = 0
after_acc = 0
call_lost = []
call_improved = []
n = len(labels)

for call_name in labels:
    label = labels[call_name]
    
    if label == predictions_before[call_name]: 
        before_acc += 1
    if label == predictions_after[call_name]: 
        after_acc += 1
    
    if label != predictions_before[call_name] and label == predictions_after[call_name]:
        new_record = {'Name': call_name, 'Label': label, 'Prediction before': predictions_before[call_name], 'Prediction after': predictions_after[call_name]}
        df_call_improved.loc[len(df_call_improved)] = new_record
        call_improved.append(call_name)
    elif label == predictions_before[call_name] and label != predictions_after[call_name]: 
        new_record = {'Name': call_name, 'Label': label, 'Prediction before': predictions_before[call_name], 'Prediction after': predictions_after[call_name]}
        df_call_lost.loc[len(df_call_lost)] = new_record
        call_lost.append(call_name)

print("Accuracy Before:", before_acc/n)
print("Accuracy After:", after_acc/n)
print("Number of Call Lost:", len(call_lost))
print("Number of Call Improved:", len(call_improved))

with open('../csv/test/call_improved.csv', 'w', encoding='utf-8') as f:
    df_call_improved.to_csv(f, index=False)

with open('../csv/test/call_lost.csv', 'w', encoding='utf-8') as f:
    df_call_lost.to_csv(f, index=False)