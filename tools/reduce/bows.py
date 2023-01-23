import os
from dotenv import load_dotenv
from helper_json import *

load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/weapons.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/bows.json"


def reduce_bows():
    json_arr = read_json(R_PATH)['Items']['Item']
    output_array = []

    for i in json_arr:
        if i['@Type'] in ('Bow', 'Crossbow'):
            stats = i['ItemComponent']['Weapon']
            fire_on_mount = True
            reload_on_mount = True
            output_object = {}

            if '@culture' not in i:
                culture = 'neutral'
            else:
                culture = i['@culture'].split('.')[1]

            if stats['@item_usage'] == 'long_bow':
                fire_on_mount = False
                reload_on_mount = False
            elif '@CantReloadOnHorseback' in stats['WeaponFlags']:
                reload_on_mount = False

            output_object['id'] = i['@id']
            output_object['name'] = i['@name'].split('}')[1]
            output_object['culture'] = culture
            output_object['weight'] = i['@weight']
            output_object['type'] = i['@Type']
            output_object['subtype'] = stats['@item_usage']
            output_object['difficulty'] = i['@difficulty']
            output_object['speed_rating'] = stats['@speed_rating']
            output_object['missile_speed'] = stats['@missile_speed']
            output_object['accuracy'] = stats['@accuracy']
            output_object['damage'] = stats['@thrust_damage']
            output_object['fire_on_mount'] = fire_on_mount
            output_object['reload_on_mount'] = reload_on_mount

            output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == '__main__':
    reduce_bows()
