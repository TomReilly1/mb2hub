import os, json
from dotenv import load_dotenv


load_dotenv()


# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = os.environ['MB2_PROJ_DIR']

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/spcultures.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/cultures.json"


def reduceCultures(file_path):
	output_array = []

	with open(file_path, 'r') as file:
		json_data = json.load(file)
		json_arr = json_data['SPCultures']['Culture']

		for culture in json_arr:
			output_object = {}

			output_object['id'] = culture['@id']
			output_object['name'] = culture['@name'].split('}')[1]
			try:
				output_object['is_main_culture'] = culture['@is_main_culture']
			except:
				output_object['is_main_culture'] = False
			try:
				output_object['desc_text'] = culture['@text'].split('}')[1]
			except:
				output_object['desc_text'] = None


			output_array.append(output_object)

	return output_array


def writeReducedJson(arr):
	with open(W_PATH, 'w') as file:
		json.dump(arr, file)



if __name__ == "__main__":
	json_array = reduceCultures(R_PATH)
	writeReducedJson(json_array)
