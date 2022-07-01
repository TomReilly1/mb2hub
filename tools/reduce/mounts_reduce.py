import os, json
from dotenv import load_dotenv


load_dotenv()


# CHANGE TO DIRECTORY WHERE PROJECT IS STORED
PROJ_DIR = os.environ['MB2_PROJ_DIR']

# CHANGE BELOW TO THE CORRECT VERSION (no spaces)
VERSION = os.environ['VERSION']


R_PATH = f"{PROJ_DIR}/{VERSION}/json/horses_and_others.json"
W_PATH = f"{PROJ_DIR}/{VERSION}/json-reduced/mounts.json"


def reduceGoods(file_path):
    output_array = []

    with open(file_path, 'r') as file:
        json_data = json.load(file)
        json_arr = json_data['Items']['Item']

        for horse in json_arr:
            try:
                print(horse['@id'])
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


    return output_array



def writeReducedJson(arr):
    with open(W_PATH, 'w') as file:
        json.dump(arr, file)



if __name__ == "__main__":
    json_array = reduceGoods(R_PATH)
    writeReducedJson(json_array)
