import os, json
from dotenv import load_dotenv
from reduce.helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/<CONCEPT>.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/<CONCEPT>.json"


def reduce_CONCEPT():
    json_arr = read_json(R_PATH)['<ITEMS>']['<ITEM>']
    output_array = []

    for i in json_arr:
        output_object = {}

        # every concept will have an id and name at least
        output_object['id'] = i['@id']
        output_object['name'] = i['@name'].split('}')[1]
        # ...

        output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == '__main__':
    reduce_CONCEPT()
