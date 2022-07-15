import os
import json
from dotenv import load_dotenv


load_dotenv()


# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = os.environ['MB2_PROJ_DIR']
# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = os.environ['VERSION']



REDUCED_DIR = f'{PROJ_DIR}/{VERSION}/json-reduced/'
output_array = []



def bundleMainMeiliData():
    master_json = []

    for root, dirs, files in os.walk(REDUCED_DIR):
        for file in files:
            json_path = os.path.join(root, file)

            with open(json_path, 'r') as json_file:
                json_arr = json.load(json_file)
                master_json += json_arr

    writeToJson(master_json, 'mb2_main.json')


def bundleReducedMeiliData():
    master_json = []

    for root, dirs, files in os.walk(REDUCED_DIR):
        for file in files:
            json_path = os.path.join(root, file)
            file_name = file.split('.')[0]
            

            with open(json_path, 'r') as json_file:
                json_arr = json.load(json_file)
                new_arr = []
                
                for obj in json_arr:
                    new_obj = {}

                    new_obj['id'] = obj['id']
                    new_obj['name'] = obj['name']
                    new_obj['concept'] = file_name

                    new_arr.append(new_obj)

                print(new_arr)
                master_json += new_arr

    writeToJson(master_json, 'mb2_reduced.json')


def writeToJson(arr, file_name):
    path = REDUCED_DIR + file_name
    with open(path, 'w') as file:
        json.dump(arr, file)


if __name__ == '__main__':
    # bundleMeiliData()
    bundleReducedMeiliData()
