import os
from dotenv import load_dotenv
from helper_json import *


load_dotenv()

PROJ_DIR = os.environ['MB2_PROJ_DIR']
VERSION = os.environ['VERSION']

R_PATH = f'{PROJ_DIR}/{VERSION}/json/spkingdoms.json'
W_PATH = f'{PROJ_DIR}/{VERSION}/json-reduced/kingdoms.json'


def reduce_kingdoms():
    json_arr = read_json(R_PATH)['Kingdoms']['Kingdom']
    output_array = []

    for kingdom in json_arr:
        output_object = {}

        output_object['id'] = kingdom['@id']
        output_object['name'] = kingdom['@name'].split('}')[1]
        output_object['title'] = kingdom['@title'].split('}')[1]
        output_object['ruler_title'] = kingdom['@ruler_title'].split('}')[1]
        output_object['culture'] = kingdom['@culture'].split('.')[1]
        output_object['primary_banner_color'] = kingdom['@primary_banner_color']
        output_object['secondary_banner_color'] = kingdom['@secondary_banner_color']
        output_object['label_color'] = kingdom['@label_color']
        output_object['color_1'] = kingdom['@color']
        output_object['color_2'] = kingdom['@color2']
        output_object['alternative_color_1'] = kingdom['@alternative_color']
        output_object['alternative_color_2'] = kingdom['@alternative_color2']
        output_object['desc_text'] = kingdom['@text'].split('}')[1]

        output_array.append(output_object)

    write_json(W_PATH, output_array)


if __name__ == '__main__':
    reduce_kingdoms()
