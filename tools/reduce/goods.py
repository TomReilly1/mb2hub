import os
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/horses_and_others.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/goods.json"


def reduce_goods():
    json_arr = read_json(R_PATH)['Items']['Item']
    output_array = []

    for good in json_arr:
        try:
            if good['@Type'] != 'Goods' or good['@id'] == 'stolen_goods':
                continue
        except:
            continue

        output_object = {}

        output_object['id'] = good['@id']
        
        name_arr = good['@name'].split('{')
        output_object['name'] = name_arr[1].split('}')[1]
        output_object['plural'] = name_arr[2].split('}')[1]

        output_object['value'] = int(good['@value'])
        output_object['weight'] = int(good['@weight'])

        if '@IsFood' in good:
            output_object['is_food'] = good['@IsFood']
        else:
            output_object['is_food'] = False
        if 'ItemComponent' in good:
            output_object['morale_bonus'] = int(good['ItemComponent']['Trade']['@morale_bonus'])
        else:
            output_object['morale_bonus'] = 0

        output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == "__main__":
    reduce_goods()
