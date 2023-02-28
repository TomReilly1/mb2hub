import os
from dotenv import load_dotenv
from helper_json import read_json, write_json


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/horses_and_others.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/draught_animals.json"


def reduce_draught_animals():
    json_arr = read_json(R_PATH)['Items']['Item']
    output_array = []

    for i in json_arr:
        item_category = i.get('@item_category')

        if item_category == 'sumpter_horse' and 'unmountable' not in i['@id']:
            output_object = {}
            print(i['@name'])

            # every concept will have an id and name at least
            output_object['id'] = i['@id']
            output_object['name'] = i['@name'].split('}')[1]
            output_object['culture'] = i['@culture'].split('.')[1] if i.get('@culture') else 'neutral'

            output_object['value'] = int(i['@value'])
            prefix = i['ItemComponent']['Horse']
            output_object['maneuver'] = int(prefix['@maneuver'])
            output_object['speed'] = int(prefix['@speed'])
            output_object['charge_damage'] = int(prefix['@charge_damage'])
            output_object['health'] = int(prefix['@extra_health']) + 200

            output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == '__main__':
    reduce_draught_animals()
