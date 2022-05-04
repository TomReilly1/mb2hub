import json



R_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json/spnpccharacters.json"
W_PATH = "/home/tom/Projects/mb2hub/1.7.2beta/json-reduced/skills.json"
VERSION = '1.7.2beta'
TEMPL_PATH = f'../1.7.2beta/json/sandboxcore_skill_sets.json'




def getSkillTemplate(skill_template):
	with open(TEMPL_PATH, 'r') as file:
		json_data = json.load(file)
		json_arr =  json_data['SkillSets']['SkillSet']

		for template in json_arr:
			print(template)
			if template['@id'] == skill_template:
				return template['skill']

		print('TEMPLATE NOT FOUND')


def getReducedSkills(file_path):
	output_array = []

	with open(file_path, 'r') as file:
		json_data = json.load(file)
		json_arr = json_data['NPCCharacters']['NPCCharacter']


		for npc in json_arr:
			# initialize object; helps handle the nulls
			output_object = {
				'id': npc['@id'],
				'name': npc['@name'].split('}')[1],
				'OneHanded': '0',
				'TwoHanded': '0',
				'Polearm': '0',
				'Bow': '0',
				'Crossbow': '0',
				'Throwing': '0',
				'Riding': '0',
				'Athletics': '0'

			}

			if npc['skills'] is None:
				skill_template_name = npc['@skill_template'].split('.')[1]
				npc_object_skills = getSkillTemplate(skill_template_name)

				for skill in npc_object_skills:
					output_object[skill['@id']] = skill['@value']
			else:
				npc_object_skills = npc['skills']['skill']
				

				for skill in npc_object_skills:
					output_object[skill['@id']] = skill['@value']

			output_array.append(output_object)

	return output_array


def writeReducedJson(arr):
	with open(W_PATH, 'w') as file:
		json.dump(arr, file)



if __name__ == "__main__":
	json_array = getReducedSkills(R_PATH)
	writeReducedJson(json_array)
