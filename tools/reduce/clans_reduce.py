import os, json


# Get current working directory
PROJ_DIR = os.environ.get('MB2_PROJ_DIR')

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = '1.8.0'


R_PATH = f"{PROJ_DIR}/{VERSION}/json/spclans.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/clans.json"
TEMPL_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/lords.json'


def getLeaderOfClan(leader_id):
	with open(TEMPL_PATH, 'r') as file:
		# json_data = json.load(file)
		# json_arr =  json_data['SkillSets']['SkillSet']
		json_arr = json.load(file)

		for lord in json_arr:
			if lord['id'] == leader_id:
				return lord['name']

		print('LORD NOT FOUND')


def reduceClans(file_path):
	output_array = []

	with open(file_path, 'r') as file:
		json_data = json.load(file)
		json_arr = json_data['Factions']['Faction']

		for clan in json_arr:
			if clan['@id'][:4] == 'clan':
				output_object = {}

				output_object['id'] = clan['@id']
				output_object['name'] = clan['@name'].split('}')[1]
				output_object['owner'] = getLeaderOfClan(clan['@owner'].split('.')[1])
				
				temp = clan['@super_faction'].split('.')[1]
				if temp == 'empire':
					output_object['kingdom'] = 'Northern Empire'
				elif temp == 'empire_w':
					output_object['kingdom'] = 'Western Empire'
				elif temp == 'empire_s':
					output_object['kingdom'] = 'Southern Empire'
				else:
					output_object['kingdom'] = temp.capitalize()

				output_object['culture'] = clan['@culture'].split('.')[1]
				output_object['tier'] = clan['@tier']

				if clan['@tier'] == '6':
					output_object['is_ruling_clan'] = True
				else:
					output_object['is_ruling_clan'] = False

				output_array.append(output_object)

	return output_array


def writeReducedJson(arr):
	with open(W_PATH, 'w') as file:
		json.dump(arr, file)



if __name__ == "__main__":
	json_array = reduceClans(R_PATH)
	writeReducedJson(json_array)
