import json

R_PATH = "/home/tom/Projects/mb2hub/website/frontend/src/data/armors.json"
W_PATH = "/home/tom/Projects/mb2hub/website/frontend/src/data/new_armors.json"
new_array = []

with open(R_PATH, 'r') as file:
    json_data = json.load(file)
    

    for i in json_data:
        print(i['name'])
        i['name'] = i['name'].split('}')[1]
        print(i['name'])

        new_array.append(i)

with open(W_PATH, "w") as file:
    json.dump(new_array, file)
