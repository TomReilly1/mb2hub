import json


R_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json/weapons.json"
W_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json-reduced/bows_and_crossbows.json"
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



with open(W_PATH, "w") as file:
	json.dump(output_array, file)


