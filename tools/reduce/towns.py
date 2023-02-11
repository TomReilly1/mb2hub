import os
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/settlements.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/towns.json"
CLAN_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/clans.json"


def get_owner_clan_name(clan_id):
    json_arr = read_json(CLAN_PATH)

    for clan in json_arr:
        if clan['id'] == clan_id:
            return clan['name']

    print('CLAN NOT FOUND')

def get_bound_villages(town_id, json_arr):
    bound_village_array = []

    for i in json_arr:
        if 'village' not in i['@id']:
            continue

        bound_castle_id = i['Components']['Village']['@bound'].split('.')[1]
        if  bound_castle_id == town_id:
            village_obj = {
                'id': i['@id'],
                'name': i['@name'].split('}')[1]
            }
            bound_village_array.append(village_obj)

    return bound_village_array


def reduce_towns():
    json_arr = read_json(R_PATH)['Settlements']['Settlement']
    output_array = []

    for i in json_arr:
        if i['@id'].split('_')[0] == 'town':
            output_object = {}

            output_object['id'] = i['@id']
            output_object['name'] = i['@name'].split('}')[1]
            clan_id = i['@owner'].split('.')[1]
            output_object['owner_clan'] = {
                'id': clan_id,
                'name': get_owner_clan_name(clan_id)
            }
            output_object['culture'] = i['@culture'].split('.')[1]
            output_object['x_position'] = i['@posX']
            output_object['y_position'] = i['@posY']
            output_object['prosperity'] = i['@prosperity']
            output_object['wall_level'] = i['Components']['Town']['@level']
            output_object['desc_text'] = i['@text'].split('}')[1] if i.get('@text') else None
            output_object['bound_villages'] = get_bound_villages(i['@id'], json_arr)

            output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == '__main__':
    reduce_towns()
