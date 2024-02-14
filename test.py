import json

f = open('response_data')

print(f)
data = json.load(f)

print(data)

for i in data["images"]:
    print(i)
    
    