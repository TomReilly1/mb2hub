import json


R_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json/spnpccharacters.json"
W_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json-reduced/npcs.json"
output_array = []

with open(R_PATH, 'r') as file:
	json_data = json.load(file)
	json_arr = json_data['NPCCharacters']['NPCCharacter']


	for i in json_arr:
		output_object = {}

		output_object['id'] = i['@id']
		output_object['name'] = i['@name'].split('}')[1]
		output_object['culture'] = i['@culture'].split('.')[1]
		output_object['group'] = i['@default_group']
		output_object['occupation'] = i['@occupation']
		output_object['level'] = i['@level']

		output_array.append(output_object)


with open(W_PATH, "w") as file:
	json.dump(output_array, file)


