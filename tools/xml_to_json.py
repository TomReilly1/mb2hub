import os, xmltodict, json
from pathlib import Path



# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = '/home/tom/Projects/mb2hub'

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = '1.8.0'


XML_DIR = f'{PROJ_DIR}/{VERSION}/xml'
JSON_DIR = f'{PROJ_DIR}/{VERSION}/json'


def convertToJSON(file):
	file_path = Path(f'{XML_DIR}/{file}')

	with open(file_path) as xml_file:
		
		data_dict = xmltodict.parse(xml_file.read())
		xml_file.close()
		

		json_data = json.dumps(data_dict)
		
		name = file.split('.')[0]
		with open(f'{JSON_DIR}/{name}.json', 'w') as json_file:
			json_file.write(json_data)
			json_file.close()


if __name__ == '__main__':
	# convertToJSON(prefix, "spcultures.xml")

	# convertToJSON('spkingdoms.xml')

	convertToJSON('head_armors.xml')
	convertToJSON('shoulder_armors.xml')
	convertToJSON('body_armors.xml')
	convertToJSON('arm_armors.xml')
	convertToJSON('leg_armors.xml')

	convertToJSON('spnpccharacters.xml')

	convertToJSON('sandboxcore_skill_sets.xml')

	convertToJSON('weapons.xml')

	convertToJSON('settlements.xml')

	convertToJSON('spclans.xml')

	convertToJSON('lords.xml')

