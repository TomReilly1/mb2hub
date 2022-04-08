import os, xmltodict, json
from pathlib import Path


def reduceJSON(prefix, file):
	output_json = []
	file_path = prefix / file

	with open(file_path) as f:
		data = json.load(f)
		list_of_AR_obj = data['Items']['Item']

		for i in list_of_AR_obj:
			curr_obj = {}

			curr_obj['id'] = i['@id']
			curr_obj['name'] = i['@name']
			curr_obj['culture'] = i['@culture'].split('.')[1]
			curr_obj['weight'] = i['@weight']
			curr_obj['type'] = i['@Type']
			curr_obj['armor'] = {}

			try:
				curr_obj['armor']['head'] = i['ItemComponent']['Armor']['@head_armor']
			except:
				curr_obj['armor']['head'] = "0"

			try:
				curr_obj['armor']['body'] = i['ItemComponent']['Armor']['@body_armor']
			except:
				curr_obj['armor']['body'] = "0"
			
			try:
				curr_obj['armor']['arm'] = i['ItemComponent']['Armor']['@arm_armor']
			except:
				curr_obj['armor']['arm'] = "0"
			
			try:
				curr_obj['armor']['leg'] = i['ItemComponent']['Armor']['@leg_armor']
			except:
				curr_obj['armor']['leg'] = "0"


			output_json.append(curr_obj)


	new_json_name = file.split('.')[0] + "_reduced.json"
	with open(new_json_name, "w") as final:
		json.dump(output_json, final)
	# json.dumps(output_json, indent=4)



if __name__ == "__main__":
	# Get current working directory
	cwd = os.getcwd()

	# CHANGE THE BELOW PREFIX TO THE CORRESPONDING VERSION
	prefix = Path(cwd + "/1.7.2beta/json/")

	
	reduceJSON(prefix, "head_armors.json")
	reduceJSON(prefix, "shoulder_armors.json")
	reduceJSON(prefix, "body_armors.json")
	reduceJSON(prefix, "arm_armors.json")
	reduceJSON(prefix, "leg_armors.json")
