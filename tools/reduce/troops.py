import os
import re
from dotenv import load_dotenv
from helper_json import read_json, write_json


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f'{PROJ_DIR}/{VERSION}/json/spnpccharacters.json'
W_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/troops.json'
SKILL_TEMPLATE_PATH = f'{PROJ_DIR}/{VERSION}/json/sandboxcore_skill_sets.json'
NOBLE_TROOP_PATH = f'{PROJ_DIR}/{VERSION}/nobleTroops.json'


def get_skill_template(skill_template):
    json_data = read_json(SKILL_TEMPLATE_PATH)
    json_arr =  json_data['SkillSets']['SkillSet']

    for template in json_arr:
        if template['@id'] == skill_template:
            return template['skill']

    raise Exception('TEMPLATE NOT FOUND')

def get_troop_name(json_arr, troop_id):
    for troop in json_arr:
        if troop['@id'] == troop_id:
            return troop['@name'].split('}')[1]

    print('TROOP NOT FOUND')


def get_upgrade_targets(json_arr, troop):
    output_upgrade_target_array = []

    # need to check if there is 0, 1, or 2 upgrade targets
    # None/null indicates 0, dict indicates 1, list indicates 2
    if troop.get('upgrade_targets'):
        target = troop['upgrade_targets']['upgrade_target']
        if isinstance(target, dict):
            target_id = target['@id'].split('.')[1]
            output_upgrade_target_array.append({'id': target_id})
        elif isinstance(target, list):
            target_id_1 = target[0]['@id'].split('.')[1]
            target_id_2 = target[1]['@id'].split('.')[1]
            output_upgrade_target_array.append({'id': target_id_1})
            output_upgrade_target_array.append({'id': target_id_2})
        else:
            raise Exception('Unkown upgrade_target data structure')

    for troop in output_upgrade_target_array:
        l_id = troop['id']
        troop['name'] = get_troop_name(json_arr, l_id)

    return output_upgrade_target_array

def check_nobility(troop_id: str, occupation: str) -> bool:
    if occupation != 'Soldier':
        print('NOT noble')
        return False

    noble_troop_list = read_json(NOBLE_TROOP_PATH)

    if troop_id in noble_troop_list:
        print('IS noble')
        return True
    else:
        print('NOT noble')
        return False


def reduce_troops():
    json_arr = read_json(R_PATH)['NPCCharacters']['NPCCharacter']
    output_array = []

    for troop in json_arr:
        if not troop.get('@occupation'):
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
        output_object['is_noble'] = check_nobility(troop['@id'], troop['@occupation'])
        output_object['upgrade_targets'] = get_upgrade_targets(json_arr, troop)

        skills_list = ('OneHanded', 'TwoHanded', 'Polearm', 'Bow',
                        'Crossbow', 'Throwing', 'Riding', 'Athletics')
        skill_values = None

        if troop['skills'] is None:
            skill_template = troop['@skill_template'].split('.')[1]
            skill_values = get_skill_template(skill_template)
        else:
            skill_values = troop['skills']['skill']

        for i in skills_list:
            temp = re.findall('[A-Z][^A-Z]*', i)
            skill = '_'.join(temp).lower()
            output_object[skill] = '0'

            for j in skill_values:
                if i == j['@id']:
                    output_object[skill] = j['@value']
                    break

        output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == "__main__":
    reduce_troops()
