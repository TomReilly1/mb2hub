import json


def read_json(r_path):
    try:
        file = open(file=r_path, mode='r', encoding='utf-8')
        json_data = json.load(file)
    except FileNotFoundError as exc:
        raise Exception(f'Error: [read_json] file not found on the path "{r_path}"') from exc
    finally:
        file.close()

    return json_data


def write_json(w_path, output_array):
    try:
        file = open(file=w_path, mode='w', encoding='utf-8')
        json.dump(output_array, file)
        print(f'File successfully written on path {w_path}')
    except Exception as exc:
        raise Exception(f'Error: [write_json] could not write file on path "{w_path}"') from exc
    # finally:
    #     file.close()


def get_clan_name(clan_id, path):
    json_arr = read_json(path)

    for i in json_arr:
        if i['id'] == clan_id:
            return i['name']

    raise Exception('Error: clan not found in via "get_clan_name"')


def get_clan_leader(leader_id, path):
    json_arr = read_json(path)

    for lord in json_arr:
        if lord['id'] == leader_id:
            return lord['name']

    raise Exception('Error: Lord not found via "get_clan_leader"')


def get_town_bound_villages(town_id, json_arr):
    bound_village_array = []

    for i in json_arr:
        settlement_type = i['@id'].split('_')[0]
        if settlement_type != 'village':
            continue

        bound_town_id = i['Components']['Village']['@bound'].split('.')[1]
        if  bound_town_id == town_id:
            bound_village_array.append(i['@id'])

    return bound_village_array


def get_castle_bound_villages(castle_id, json_arr):
    bound_village_array = []

    for i in json_arr:
        if 'village' not in i['@id']:
            continue

        bound_castle_id = i['Components']['Village']['@bound'].split('.')[1]
        if  bound_castle_id == castle_id:
            bound_village_array.append(i['@id'])

    return bound_village_array


def get_skill_template(skill_template, path):
    json_arr = read_json(path)['SkillSets']['SkillSet']

    for template in json_arr:
        if template['@id'] == skill_template:
            return template['skill']

    raise Exception('Error: template not found via "get_skill_template"')
