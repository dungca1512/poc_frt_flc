import json
import requests
import numpy as np
import pandas as pd

with open("C:\\Users\\admin\\Enhance\\debug_hc\\json\\data\\transcriptM3_new.json", "r", encoding="utf-8") as f:
    transcripts = json.load(f)
    
url = "https://api-v35.fpt.ai/api/v3/predict"

method = "POST"
bot_token = "d510dab9b63c3def888ebe10af0b845c"

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer " + bot_token
}

out = []

for i, transcript in enumerate(transcripts):
    fileName = transcript["fileName"]
    temp = []
    for content in transcript["content"]:
        sentence = content["text"]
        
        payload = json.dumps({"content": sentence,
                            "language": "vi"})
        
        response = requests.request(method=method, 
                                    url=url, 
                                    headers=headers, 
                                    data=payload).json()
        
        temp_result = {"content": sentence,
                        "data": response["data"]}

        temp.append(temp_result)
    result = {"fileName": fileName, "response": temp}
    out.append(result)
    if i == 286: break
    
with open("C:\\Users\\admin\\Enhance\\debug_hc\\json\\response\\new_response_m3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=4)
    