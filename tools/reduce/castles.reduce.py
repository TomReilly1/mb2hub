import os, json
from dotenv import load_dotenv


load_dotenv()


# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = os.environ['MB2_PROJ_DIR']

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = os.environ['VERSION']


R_PATH = f"{PROJ_DIR}/{VERSION}/json/settlements.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/castles.json"
CLAN_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/clans.json"
output_array = []


def getClanName(clan_id):
    with open(CLAN_PATH, 'r') as file:
        json_arr = json.load(file)
        for i in json_arr:
            if i['id'] == clan_id:
                return i['name']
    return 'NONE'


def getBoundVillages(castle_id):
    with open(R_PATH, 'r') as file:
        json_data = json.load(file)
        json_arr = json_data['Settlements']['Settlement']
        bound_village_array = []

        for i in json_arr:
            if 'village' not in i['@id']:
                continue

            bound_castle_id = i['Components']['Village']['@bound'].split('.')[1]
            if  bound_castle_id == castle_id:
                bound_village_array.append(i['@id'])

        

    return bound_village_array
    
            

with open(R_PATH, 'r') as file:
    json_data = json.load(file)
    json_arr = json_data['Settlements']['Settlement']


    for i in json_arr:
        # if i['@id'].split('_')[0] == 'castle' and i['@id'].split('_')[1] != 'village':
        if 'castle' in i['@id'] and 'village' not in i['@id']:
            output_object = {}


            output_object['id'] = i['@id']
            output_object['name'] = i['@name'].split('}')[1]
            output_object['owner_id'] = i['@owner'].split('.')[1]
            output_object['owner_name'] = getClanName(output_object['owner_id'])
            output_object['culture'] = i['@culture'].split('.')[1]
            output_object['x_position'] = i['@posX']
            output_object['y_position'] = i['@posY']
            output_object['prosperity'] = i['@prosperity']
            output_object['wall_level'] = i['Components']['Town']['@level']

            bound_villages = getBoundVillages(i['@id'])
            print(i['@id'], 'number of villages:', len(bound_villages))
            print(bound_villages)
            output_object['bound_village_1'] = bound_villages[0]
            try:
                output_object['bound_village_2'] = bound_villages[1]
            except:
                output_object['bound_village_2'] = None


            output_array.append(output_object)


with open(W_PATH, "w") as file:
    json.dump(output_array, file)

