import os
from dotenv import load_dotenv
from helper_json import read_json, write_json


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

W_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/armors.json'
R_PATH_HEAD = f'{PROJ_DIR}/{VERSION}/json/head_armors.json'
R_PATH_SHOULDER = f'{PROJ_DIR}/{VERSION}/json/shoulder_armors.json'
R_PATH_BODY = f'{PROJ_DIR}/{VERSION}/json/body_armors.json'
R_PATH_ARM = f'{PROJ_DIR}/{VERSION}/json/arm_armors.json'
R_PATH_LEG = f'{PROJ_DIR}/{VERSION}/json/leg_armors.json'


def add_armor_type(read_path):
    json_arr = read_json(read_path)['Items']['Item']
    output_array = []

    for i in json_arr:
        curr_obj = {}

        curr_obj['id'] = i['@id']
        curr_obj['name'] = i['@name'].split('}')[1]
        curr_obj['culture'] = i['@culture'].split('.')[1]
        curr_obj['weight'] = i['@weight']
        if i['@Type'] == 'Cape':
            curr_obj['type'] = 'ShoulderArmor'
        elif i['@Type'] == 'HandArmor':
            curr_obj['type'] = 'ArmArmor'
        else:
            curr_obj['type'] = i['@Type']

        try:
            curr_obj['head_armor'] = i['ItemComponent']['Armor']['@head_armor']
        except KeyError:
            curr_obj['head_armor'] = "0"
        try:
            curr_obj['body_armor'] = i['ItemComponent']['Armor']['@body_armor']
        except KeyError:
            curr_obj['body_armor'] = "0"
        try:
            curr_obj['arm_armor'] = i['ItemComponent']['Armor']['@arm_armor']
        except KeyError:
            curr_obj['arm_armor'] = "0"
        try:
            curr_obj['leg_armor'] = i['ItemComponent']['Armor']['@leg_armor']
        except KeyError:
            curr_obj['leg_armor'] = "0"

        output_array.append(curr_obj)

    return output_array


def reduce_armors():
    final_array = add_armor_type(R_PATH_HEAD)
    final_array += add_armor_type(R_PATH_SHOULDER)
    final_array += add_armor_type(R_PATH_BODY)
    final_array += add_armor_type(R_PATH_ARM)
    final_array += add_armor_type(R_PATH_LEG)

    write_json(W_PATH, final_array)


if __name__ == "__main__":
    reduce_armors()
