import os
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/settlements.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/castles.json"
CLAN_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/clans.json"


def reduce_castles():
    json_arr = read_json(R_PATH)['Settlements']['Settlement']
    output_array = []

    for i in json_arr:
        if 'castle' in i['@id'] and 'village' not in i['@id']:
            output_object = {}

            output_object['id'] = i['@id']
            output_object['name'] = i['@name'].split('}')[1]
            output_object['owner_id'] = i['@owner'].split('.')[1]
            output_object['owner_name'] = get_clan_name(output_object['owner_id'], CLAN_PATH)
            output_object['culture'] = i['@culture'].split('.')[1]
            output_object['x_position'] = i['@posX']
            output_object['y_position'] = i['@posY']
            output_object['prosperity'] = i['@prosperity']
            output_object['wall_level'] = i['Components']['Town']['@level']

            bound_villages = get_castle_bound_villages(i['@id'], json_arr)
            output_object['bound_villages'] = []
            for village in bound_villages:
                output_object['bound_villages'].append(village)

            output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == '__main__':
    reduce_castles()
