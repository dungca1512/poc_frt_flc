import requests
import json

state = input("Nhập môi trường: ")

if state == "nlp" or state == "test":
  endpoint = "http://103.176.146.250:5005" # môi trường nlp
else:
  endpoint = "https://cqe-dev-nlp.fpt.ai/dme" # môi trường dev

url = f"{endpoint}/projects/hc_clx_m3/latest"

payload = {}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url=url, headers=headers, data=payload).json()

with open(f'../json/project_info/m3_project_info_{state}.json', 'w', encoding='utf-8') as json_file:
    json.dump(response, json_file, ensure_ascii=False, indent=4)
