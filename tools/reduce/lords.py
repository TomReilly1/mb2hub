import os
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/lords.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/lords.json"


def reduce_lords():
    json_arr = read_json(R_PATH)['NPCCharacters']['NPCCharacter']
    output_array = []

    for i in json_arr:
        if i['@id'].split('_')[0] == 'lord':
            output_object = {}

            output_object['id'] = i['@id']
            output_object['name'] = i['@name'].split('}')[1]
            output_object['culture'] = i['@culture'].split('.')[1]
            output_object['default_group'] = i['@default_group']
            output_object['age'] = i.get('@age')
            if i.get('@is_female') is not None:	
                output_object['sex'] = 'female'
            else:
                output_object['sex'] = 'male'

            output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == '__main__':
    reduce_lords()
