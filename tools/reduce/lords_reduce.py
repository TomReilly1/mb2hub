import os, json


# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = os.environ.get('MB2_PROJ_DIR')

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = '1.8.0'


R_PATH = f"{PROJ_DIR}/{VERSION}/json/lords.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/lords.json"
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
			output_object['default_group'] = i['@default_group']
			output_object['age'] = i.get('@age')
			if i.get('@is_female') is not None:	
				output_object['sex'] = 'female'
			else:
				output_object['sex'] = 'male'


			output_array.append(output_object)


with open(W_PATH, "w") as file:
	json.dump(output_array, file)


