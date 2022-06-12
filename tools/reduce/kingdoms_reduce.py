import json



# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = '/home/tom/Projects/mb2hub'

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = '1.8.0'



R_PATH = f'{PROJ_DIR}/{VERSION}/json/spkingdoms.json'
W_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/kingdoms.json'



def reduceJson(file_path):
	output_array = []

	with open(file_path, 'r') as file:
		json_data = json.load(file)
		json_arr = json_data['Kingdoms']['Kingdom']

		for kingdom in json_arr:
			output_object = {}

			output_object['id'] = kingdom['@id']
			output_object['name'] = kingdom['@name'].split('}')[1]
			output_object['title'] = kingdom['@title'].split('}')[1]
			output_object['ruler_title'] = kingdom['@ruler_title'].split('}')[1]
			output_object['culture'] = kingdom['@culture'].split('.')[1]
			output_object['primary_banner_color'] = kingdom['@primary_banner_color']
			output_object['secondary_banner_color'] = kingdom['@secondary_banner_color']
			output_object['label_color'] = kingdom['@label_color']
			output_object['color_1'] = kingdom['@color']
			output_object['color_2'] = kingdom['@color2']
			output_object['alternative_color_1'] = kingdom['@alternative_color']
			output_object['alternative_color_2'] = kingdom['@alternative_color2']
			output_object['desc_text'] = kingdom['@text'].split('}')[1]

			output_array.append(output_object)

	return output_array


def writeReducedJson(arr):
	with open(W_PATH, 'w') as file:
		json.dump(arr, file)



if __name__ == '__main__':
	json_array = reduceJson(R_PATH)
	writeReducedJson(json_array)
