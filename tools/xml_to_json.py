import os, xmltodict, json
from pathlib import Path


def convertToJSON(prefix, file):
	file_path = prefix / file

	with open(file_path) as xml_file:
		
		data_dict = xmltodict.parse(xml_file.read())
		xml_file.close()
		

		json_data = json.dumps(data_dict)
		
		name = file.split(".")[0]
		with open(name + ".json", "w") as json_file:
			json_file.write(json_data)
			json_file.close()


if __name__ == "__main__":
	# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
	VERSION = '1.7.2beta'
	
	
	prefix = Path(f"../{VERSION}/xml/")

	# convertToJSON(prefix, "head_armors.xml")
	# convertToJSON(prefix, "shoulder_armors.xml")
	# convertToJSON(prefix, "body_armors.xml")
	# convertToJSON(prefix, "arm_armors.xml")
	# convertToJSON(prefix, "leg_armors.xml")

	# convertToJSON(prefix, "spnpccharacters.xml")

	convertToJSON(prefix, "sandboxcore_skill_sets.xml")


