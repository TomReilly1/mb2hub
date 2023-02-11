import os
from dotenv import load_dotenv
from helper_json import read_json, write_json


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f"{PROJ_DIR}/{VERSION}/json/spcultures.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/cultures.json"


def reduce_cultures():
    json_arr = read_json(R_PATH)['SPCultures']['Culture']
    output_array = []

    for culture in json_arr:
        output_object = {}

        output_object['id'] = culture['@id']
        output_object['name'] = culture['@name'].split('}')[1]
        is_main_culture = culture.get('@is_main_culture')
        if is_main_culture == 'true':
            output_object['is_main_culture'] = True
        else: # 'false' or None
            output_object['is_main_culture'] = False
        output_object['desc_text'] = (culture['@text'].split('}')[1]
                                        if culture.get('@text')
                                        else None)

        output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == "__main__":
    reduce_cultures()
