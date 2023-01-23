import os
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/shields.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/shields.json"


def reduce_shields():
    json_arr = read_json(R_PATH)['Items']['Item']
    output_array = []

    for i in json_arr:
        output_object = {}

        output_object['id'] = i['@id']
        output_object['name'] = i['@name'].split('}')[1]
        try:
            output_object['culture'] = i['@culture'].split('.')[1]
        except KeyError:
            output_object['culture'] = 'neutral'
        output_object['weight'] = i['@weight']

        w_prefix = i['ItemComponent']['Weapon']
        output_object['thrust_speed'] = w_prefix['@thrust_speed']
        output_object['speed_rating'] = w_prefix['@speed_rating']
        output_object['weapon_length'] = w_prefix['@weapon_length']
        output_object['hit_points'] = w_prefix['@hit_points']

        output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == '__main__':
    reduce_shields()
