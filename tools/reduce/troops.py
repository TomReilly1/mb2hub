import os
import re
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f'{PROJ_DIR}/{VERSION}/json/spnpccharacters.json'
W_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/troops.json'
SKILL_TEMPLATE_PATH = f'{PROJ_DIR}/{VERSION}/json/sandboxcore_skill_sets.json'


def reduce_troops():
    json_arr = read_json(R_PATH)['NPCCharacters']['NPCCharacter']
    output_array = []

    for troop in json_arr:
        flag = troop.get('@occupation')
        if not flag:
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
        
        # need to check if there is 0, 1, or 2 upgrade targets
        # None/null indicates 0, dict indicates 1, list indicates 2
        output_object['upgrade_targets'] = []
        if troop.get('upgrade_targets'):
            if isinstance(troop['upgrade_targets']['upgrade_target'], dict):
                target = troop['upgrade_targets']['upgrade_target']['@id'].split('.')[1]
                output_object['upgrade_targets'].append(target)
            elif isinstance(troop['upgrade_targets']['upgrade_target'], list):
                target_1 = troop['upgrade_targets']['upgrade_target'][0]['@id'].split('.')[1]
                output_object['upgrade_targets'].append(target_1)
                target_2 = troop['upgrade_targets']['upgrade_target'][1]['@id'].split('.')[1]
                output_object['upgrade_targets'].append(target_2)
            else:
                raise Exception('Unkown upgrade_target data structure')
            


        skills_list = ('OneHanded', 'TwoHanded', 'Polearm', 'Bow', 'Crossbow', 'Throwing', 'Riding', 'Athletics')
        if troop['skills'] is None:
            skill_template = troop['@skill_template'].split('.')[1]
            template_skills = get_skill_template(skill_template, SKILL_TEMPLATE_PATH)

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

    write_json(W_PATH, output_array)


if __name__ == "__main__":
    reduce_troops()
