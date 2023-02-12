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


def handle_armor_rating_values(armor_type: str, prefix: dict) -> dict:
    armor_val_dict = {
        'head_armor': None,
        'body_armor': None,
        'arm_armor': None,
        'leg_armor': None
    }

    match armor_type:
        case 'HeadArmor':
            armor_val_dict['head_armor'] = (prefix.get('@head_armor')
                                            if prefix.get('@head_armor') else 0)
        case 'ShoulderArmor':
            armor_val_dict['body_armor'] = (prefix.get('@body_armor')
                                            if prefix.get('@body_armor') else 0)
            armor_val_dict['arm_armor'] = (prefix.get('@arm_armor')
                                            if prefix.get('@arm_armor') else 0)
        case 'BodyArmor':
            armor_val_dict['body_armor'] = (prefix.get('@body_armor')
                                            if prefix.get('@body_armor') else 0)
            armor_val_dict['arm_armor'] = (prefix.get('@arm_armor')
                                            if prefix.get('@arm_armor') else 0)
            armor_val_dict['leg_armor'] = (prefix.get('@leg_armor')
                                            if prefix.get('@leg_armor') else 0)
        case 'ArmArmor':
            armor_val_dict['arm_armor'] = (prefix.get('@arm_armor')
                                            if prefix.get('@arm_armor') else 0)
        case 'LegArmor':
            armor_val_dict['leg_armor'] = (prefix.get('@leg_armor')
                                            if prefix.get('@leg_armor') else 0)
        case _:
            raise Exception('unkown armor type')

    for key, val in armor_val_dict.items():
        if val:
            armor_val_dict[key] = int(val)

    return armor_val_dict


def add_armor_type(read_path: str) -> list:
    json_arr = read_json(read_path)['Items']['Item']
    output_array = []

    for i in json_arr:
        curr_obj = {}

        if 'dummy' in i['@id']:
            continue
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

        armor_prefix = i['ItemComponent']['Armor']
        armor_vals_dict = handle_armor_rating_values(curr_obj['type'], armor_prefix)
        for key, val in armor_vals_dict.items():
            curr_obj[key] = val

        output_array.append(curr_obj)

    return output_array


def reduce_armors() -> None:
    final_array = add_armor_type(R_PATH_HEAD)
    final_array += add_armor_type(R_PATH_SHOULDER)
    final_array += add_armor_type(R_PATH_BODY)
    final_array += add_armor_type(R_PATH_ARM)
    final_array += add_armor_type(R_PATH_LEG)

    write_json(W_PATH, final_array)


if __name__ == "__main__":
    reduce_armors()
