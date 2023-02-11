import os
from dotenv import load_dotenv
from helper_json import read_json, write_json


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/spclans.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/clans.json"
LORD_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/lords.json'


def get_clan_leader(leader_id):
    json_arr = read_json(LORD_PATH)

    for lord in json_arr:
        if lord['id'] == leader_id:
            return lord['name']

    print('LORD NOT FOUND')

def reduce_clans():
    json_arr = read_json(R_PATH)['Factions']['Faction']
    output_array = []

    for clan in json_arr:
        if clan['@id'][:4] == 'clan':
            output_object = {}

            output_object['id'] = clan['@id']
            output_object['name'] = clan['@name'].split('}')[1]
            output_object['owner_lord'] = {
                'id': clan['@owner'].split('.')[1],
                'name': get_clan_leader(clan['@owner'].split('.')[1])
            }
            output_object['kingdom'] = clan['@super_faction'].split('.')[1]
            output_object['culture'] = clan['@culture'].split('.')[1]
            output_object['tier'] = clan['@tier']

            if clan['@tier'] == '6':
                output_object['is_ruling_clan'] = True
            else:
                output_object['is_ruling_clan'] = False

            output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == "__main__":
    reduce_clans()
