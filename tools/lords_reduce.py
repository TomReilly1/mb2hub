import json

"""
 "@id": "lord_1_4",
				"@name": "{=WrAMfIG1}Phenoria",
				"@age": "53",
				"@voice": "curt",
				"@is_hero": "true",
				"@is_female": "true",
				"@culture": "Culture.empire",
				"@occupation": "Lord",
				"@default_group": "Cavalry",
"""

R_PATH = "/home/tom/Github/mb2hub/1.7.2beta/json/lords.json"
W_PATH = "/home/tom/Github/mb2hub/1.7.2beta/json-reduced/lords.json"
output_array = []

with open(R_PATH, 'r') as file:
	json_data = json.load(file)
	json_arr = json_data['NPCCharacters']['NPCCharacter']


	for i in json_arr:
		if i['@id'].split('_')[0] == 'lord':
			output_object = {}
			print(i['@id'])

			output_object['id'] = i['@id']
			output_object['name'] = i['@name'].split('}')[1]
			output_object['culture'] = i['@culture'].split('.')[1]
			output_object['group'] = i['@default_group']
			output_object['age'] = i.get('@age')
			if i.get('@is_female') is not None:	
				output_object['sex'] = 'female'
			else:
				output_object['sex'] = 'male'


			output_array.append(output_object)


with open(W_PATH, "w") as file:
	json.dump(output_array, file)


