import os, json, re



# CHANGE TO DIRECTORY WHERE PROJECT IS STORED (e.g. 'C:\\Users\\Bob\\Documents\\Projects\\mb2hub')
PROJ_DIR = os.environ.get('MB2_PROJ_DIR')

# CHANGE BELOW TO THE CORRECT VERSION (e.g. '1.7.2')
VERSION = '1.8.0'


R_PATH = f'{PROJ_DIR}/{VERSION}/json/spnpccharacters.json'
W_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/troops.json'
TEMPL_PATH = f'{PROJ_DIR}/{VERSION}/json/sandboxcore_skill_sets.json'



def getSkillTemplate(skill_template):
    with open(TEMPL_PATH, 'r') as file:
        json_data = json.load(file)
        json_arr =  json_data['SkillSets']['SkillSet']

        for template in json_arr:
            print(template)
            if template['@id'] == skill_template:
                return template['skill']

        print('TEMPLATE NOT FOUND')



def reduceJson(file_path):
    output_array = []

    with open(file_path, 'r') as file:
        json_data = json.load(file)
        json_arr = json_data['NPCCharacters']['NPCCharacter']

        for troop in json_arr:
            try:
                print(troop['@occupation'])
            except KeyError:
                continue

            troop_occupations = ('Soldier', 'CaravanGuard', 'Mercenary')
            is_troop = False

            for occupation in troop_occupations:
                if occupation == troop['@occupation']:
                    is_troop = True
                    break

            if not is_troop:
                continue


            output_object = {}

            output_object['id'] = troop['@id']
            output_object['name'] = troop['@name'].split('}')[1]
            output_object['culture'] = troop['@culture'].split('.')[1]
            output_object['default_group'] = troop['@default_group']
            output_object['occupation'] = troop['@occupation']
            output_object['level'] = troop['@level']
            try:
                output_object['upgrade_target_1'] = troop['upgrade_targets']['upgrade_target'][0]['@id'].split('.')[1]
            except:
                output_object['upgrade_target_1'] = None
            try:
                output_object['upgrade_target_2'] = troop['upgrade_targets']['upgrade_target'][1]['@id'].split('.')[1]
            except:
                output_object['upgrade_target_2'] = None


            skills_list = ('OneHanded', 'TwoHanded', 'Polearm', 'Bow', 'Crossbow', 'Throwing', 'Riding', 'Athletics')

            if troop['skills'] is None:
                skill_template = troop['@skill_template'].split('.')[1]
                template_skills = getSkillTemplate(skill_template)

                for skill_from_list in skills_list:
                    skill = []
                    skill = re.findall('[A-Z][^A-Z]*', skill_from_list)
                    skill = '_'.join(skill).lower()
                    output_object[skill] = '0'

                    for skill_from_temp in template_skills:
                        if skill_from_list == skill_from_temp['@id']:
                            output_object[skill] = skill_from_temp['@value']
                            break
            else:
                json_skills = troop['skills']['skill']
                for skill_from_list in skills_list:
                    skill = []
                    skill = re.findall('[A-Z][^A-Z]*', skill_from_list)
                    skill = '_'.join(skill).lower()
                    output_object[skill] = '0'

                    for skill_from_json in json_skills:
                        if skill_from_list == skill_from_json['@id']:
                            output_object[skill] = skill_from_json['@value']
                            break

            # # want to move Athletics and Riding to the end
            # riding = output_object.pop('Riding')
            # output_object['Riding'] = riding
            # athletics = output_object.pop('Athletics')
            # output_object['Athletics'] = athletics


            output_array.append(output_object)

    return output_array


def writeReducedJson(arr):
    with open(W_PATH, 'w') as file:
        json.dump(arr, file)



if __name__ == "__main__":
    json_array = reduceJson(R_PATH)
    writeReducedJson(json_array)
