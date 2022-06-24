import os, json
from dotenv import load_dotenv


load_dotenv()


# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = os.environ['MB2_PROJ_DIR']

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = os.environ['VERSION']


R_PATH = f"{PROJ_DIR}/{VERSION}/json/weapons.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/bows.json"


def reduceBows():
	output_array = []

	with open(R_PATH, 'r') as file:
		json_data = json.load(file)
		json_arr = json_data['Items']['Item']

		for i in json_arr:
			if i['@Type'] in ('Bow', 'Crossbow'):
				stats = i['ItemComponent']['Weapon']
				fire_on_mount = True
				reload_on_mount = True
				output_object = {}

				# checks for null culture
				if '@culture' not in i:
					culture = 'neutral'
				else:
					culture = i['@culture'].split('.')[1]

				# checks for usability on mounts
				if stats['@item_usage'] == 'long_bow':
					fire_on_mount = False
					reload_on_mount = False
				elif '@CantReloadOnHorseback' in stats['WeaponFlags']:
					reload_on_mount = False


				output_object['id'] = i['@id']
				output_object['name'] = i['@name'].split('}')[1]
				output_object['culture'] = culture
				output_object['weight'] = i['@weight']
				output_object['type'] = i['@Type']
				output_object['subtype'] = stats['@item_usage']
				output_object['difficulty'] = i['@difficulty']
				output_object['speed_rating'] = stats['@speed_rating']
				output_object['missile_speed'] = stats['@missile_speed']
				output_object['accuracy'] = stats['@accuracy']
				output_object['damage'] = stats['@thrust_damage']
				output_object['fire_on_mount'] = fire_on_mount
				output_object['reload_on_mount'] = reload_on_mount

				output_array.append(output_object)

	return output_array


def writeReducedJson(arr):
	with open(W_PATH, "w") as file:
		json.dump(arr, file)


if __name__ == '__main__':
	json_array = reduceBows()
	writeReducedJson(json_array)

