import json

project = input("Enter project: ")

criteria = input("Enter criteria: ")

with open(f"../response/{project}_evaluate.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
names = []

for call in data:
    if call[criteria]["evaluate"] == "yes":
        count += 1
        names.append(call["fileName"])

with open(f"../response/{project}_call_name.txt", 'w', encoding='utf-8') as f:
    for name in names:
        f.write(name + "\n")

print(f"Number of calls that have {criteria}: {count}")
print(f"Number of calls: {len(data)}")