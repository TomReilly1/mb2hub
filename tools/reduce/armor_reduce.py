import os, json
from dotenv import load_dotenv


load_dotenv()


# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = os.environ['MB2_PROJ_DIR']

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = os.environ['VERSION']



def reduceJSON(read_path):
	output_arr = []

	with open(read_path) as f:
		data = json.load(f)
		list_of_AR_obj = data['Items']['Item']

		for i in list_of_AR_obj:
			curr_obj = {}

			curr_obj['id'] = i['@id']
			curr_obj['name'] = i['@name'].split('}')[1]
			curr_obj['culture'] = i['@culture'].split('.')[1]
			curr_obj['weight'] = i['@weight']
			curr_obj['type'] = i['@Type']

			try:
				curr_obj['head_armor'] = i['ItemComponent']['Armor']['@head_armor']
			except:
				curr_obj['head_armor'] = "0"
			try:
				curr_obj['body_armor'] = i['ItemComponent']['Armor']['@body_armor']
			except:
				curr_obj['body_armor'] = "0"
			try:
				curr_obj['arm_armor'] = i['ItemComponent']['Armor']['@arm_armor']
			except:
				curr_obj['arm_armor'] = "0"
			try:
				curr_obj['leg_armor'] = i['ItemComponent']['Armor']['@leg_armor']
			except:
				curr_obj['leg_armor'] = "0"

			output_arr.append(curr_obj)

	return output_arr


def writeReducedJSON(write_path, json_dict):
	with open(write_path, 'w') as file:
		json.dump(json_dict, file)



if __name__ == "__main__":
	W_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/armors.json'

	R_PATH_HEAD = f'{PROJ_DIR}/{VERSION}/json/head_armors.json'
	R_PATH_SHOULDER = f'{PROJ_DIR}/{VERSION}/json/shoulder_armors.json'
	R_PATH_BODY = f'{PROJ_DIR}/{VERSION}/json/body_armors.json'
	R_PATH_ARM = f'{PROJ_DIR}/{VERSION}/json/arm_armors.json'
	R_PATH_LEG = f'{PROJ_DIR}/{VERSION}/json/leg_armors.json'


	final_arr = reduceJSON(R_PATH_HEAD)
	final_arr += reduceJSON(R_PATH_SHOULDER)
	final_arr += reduceJSON(R_PATH_BODY)
	final_arr += reduceJSON(R_PATH_ARM)
	final_arr += reduceJSON(R_PATH_LEG)


	writeReducedJSON(W_PATH, final_arr)
