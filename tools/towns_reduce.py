import json


R_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json/settlements.json"
W_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json-reduced/towns.json"
CLAN_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json-reduced/clans.json"
output_array = []

def getClanName(clan_id):
	with open(CLAN_PATH, 'r') as file:
		json_arr = json.load(file)
		for i in json_arr:
			if i['id'] == clan_id:
				return i['name']
	return 'NONE'


with open(R_PATH, 'r') as file:
	json_data = json.load(file)
	json_arr = json_data['Settlements']['Settlement']


	for i in json_arr:
		if i['@id'].split('_')[0] == 'town':
			output_object = {}

			output_object['id'] = i['@id']
			output_object['name'] = i['@name'].split('}')[1]
			output_object['owner-id'] = i['@owner'].split('.')[1]
			output_object['owner-name'] = getClanName(output_object['owner-id'])
			output_object['culture'] = i['@culture'].split('.')[1]
			output_object['x-position'] = i['@posX']
			output_object['y-position'] = i['@posY']
			output_object['prosperity'] = i['@prosperity']
			output_object['wall-level'] = i['Components']['Town']['@level']

			output_array.append(output_object)


with open(W_PATH, "w") as file:
	json.dump(output_array, file)

