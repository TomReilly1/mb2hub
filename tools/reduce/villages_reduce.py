import os, json
from dotenv import load_dotenv


load_dotenv()


# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = os.environ['MB2_PROJ_DIR']

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = os.environ['VERSION']


R_PATH = f"{PROJ_DIR}/{VERSION}/json/settlements.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/villages.json"



			
def reduceVillages():
	output_array = []

	with open(R_PATH, 'r') as file:
		json_data = json.load(file)
		json_arr = json_data['Settlements']['Settlement']

		for i in json_arr:
			if 'village' in i['@id']:
				output_object = {}


				vil_comp = i['Components']['Village']

				output_object['id'] = i['@id']
				output_object['name'] = i['@name'].split('}')[1]
				output_object['culture'] = i['@culture'].split('.')[1]
				output_object['village_type'] = vil_comp['@village_type'].split('.')[1]
				output_object['x_position'] = i['@posX']
				output_object['y_position'] = i['@posY']
				output_object['hearth'] = vil_comp['@hearth']
				output_object['bound_settlement'] = vil_comp['@bound'].split('.')[1]
				try:
					output_object['desc_text'] = i['@text'].split('}')[1]
				except:
					output_object['desc_text'] = None


				output_array.append(output_object)

	return output_array

def writeReducedJson(arr):
	with open(W_PATH, 'w') as file:
		json.dump(arr, file)



if __name__ == "__main__":
	json_array = reduceVillages()
	writeReducedJson(json_array)
