import json

VERSION = '1.8.0'

R_PATH = f"/home/tom/Projects/mb2hub/{VERSION}/json/spcultures.json"
W_PATH = f"/home/tom/Projects/mb2hub/{VERSION}/json-reduced/cultures.json"




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

			output_array.append(output_object)

	return output_array


def writeReducedJson(arr):
	with open(W_PATH, 'w') as file:
		json.dump(arr, file)



if __name__ == "__main__":
	json_array = reduceCultures(R_PATH)
	writeReducedJson(json_array)
