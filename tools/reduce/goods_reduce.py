import os, json


# Get current working directory
PROJ_DIR = os.environ.get('MB2_PROJ_DIR')

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = '1.8.0'


R_PATH = f"{PROJ_DIR}/{VERSION}/json/horses_and_others.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/goods.json"



def reduceGoods(file_path):
	output_array = []

	with open(file_path, 'r') as file:
		json_data = json.load(file)
		json_arr = json_data['Items']['Item']

		for good in json_arr:
			try:
				print(good['@Type'])
				if good['@Type'] != 'Goods' or good['@id'] == 'stolen_goods':
					continue
			except:
				continue


			output_object = {}


			output_object['id'] = good['@id']
			
			name_arr = good['@name'].split('{')
			output_object['name'] = name_arr[1].split('}')[1]
			output_object['plural'] = name_arr[2].split('}')[1]

			output_object['value'] = int(good['@value'])
			output_object['weight'] = int(good['@weight'])
			
			try:
				print(good['ItemComponent']['Trade']['@morale_bonus'])
				if '@IsFood' in good:
					output_object['is_food'] = True
					output_object['morale_bonus'] = int(good['ItemComponent']['Trade']['@morale_bonus'])
			except:
				output_object['is_food'] = False
				output_object['morale_bonus'] = None
			

			output_array.append(output_object)

	return output_array


def writeReducedJson(arr):
	with open(W_PATH, 'w') as file:
		json.dump(arr, file)



if __name__ == "__main__":
	json_array = reduceGoods(R_PATH)
	writeReducedJson(json_array)
