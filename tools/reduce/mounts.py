import os
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/horses_and_others.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/mounts.json"


def reduce_mounts():
    json_arr = read_json(R_PATH)['Items']['Item']
    output_array = []

    for horse in json_arr:
        try:
            horse_type = horse['@Type']
            horse_catg = horse['@item_category']
            
            if (
                horse_type != 'Horse' or
                horse_catg == 'sumpter_horse' or
                'tournament' in horse['@id']
            ):
                continue
        except:
            continue

        output_object = {}

        output_object['id'] = horse['@id']
        output_object['name'] = horse['@name'].split('}')[1]
        try:
            output_object['culture'] = horse['@culture'].split('.')[1]
        except:
            output_object['culture'] = 'neutral_culture'
        output_object['subtype'] = horse['@item_category']
        output_object['difficulty'] = int(horse['@difficulty'])
        try:
            is_merch = horse['@is_merchandise']
            if is_merch == 'false':
                output_object['is_merchandise'] = False
        except:
            output_object['is_merchandise'] = True

        horse_stats = horse['ItemComponent']['Horse']
        output_object['maneuver'] = int(horse_stats['@maneuver'])
        output_object['speed'] = int(horse_stats['@speed'])
        output_object['charge_damage'] = int(horse_stats['@charge_damage'])
        
        base_health = 200
        try:
            output_object['health'] = base_health + int(horse_stats['@extra_health'])
        except:
            output_object['health'] = base_health

        output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == "__main__":
    reduce_mounts()
