import os
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/settlements.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/villages.json"


def get_bound_settlement_name(json_arr, settlement_id):
    for i in json_arr:
        if  i['@id'] == settlement_id:
            return i['@name'].split('}')[1]

    raise Exception(f'Bound settlement not found for "{settlement_id}"')
            
def reduce_villages():
    json_arr = read_json(R_PATH)['Settlements']['Settlement']
    output_array = []

    for i in json_arr:
        if 'village' in i['@id']:
            output_object = {}
            vilg_prefix = i['Components']['Village']

            output_object['id'] = i['@id']
            output_object['name'] = i['@name'].split('}')[1]
            output_object['culture'] = i['@culture'].split('.')[1]
            output_object['village_type'] = vilg_prefix['@village_type'].split('.')[1]
            output_object['x_position'] = i['@posX']
            output_object['y_position'] = i['@posY']
            output_object['hearth'] = vilg_prefix['@hearth']
            # output_object['bound_settlement_json'] = vilg_prefix['@bound'].split('.')[1]
            bound_settlement_id = vilg_prefix['@bound'].split('.')[1]
            output_object['bound_settlement'] = {
                'id': bound_settlement_id,
                'name': get_bound_settlement_name(json_arr, bound_settlement_id)
            
            }
            output_object['desc_text'] = i['@text'].split('}')[1] if i.get('@text') else None

            output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == "__main__":
    reduce_villages()
