import json
from pathlib import Path

default_json = {"game_data_dir": "null",
                "base_path": "Saves/",
                "backup_path": "Backup/"}


def get_json_template():
    import Setup_module as sm
    sm.get_input_data()
    json_template = {"game_data_dir": sm.get_input_data(),
                    "base_path": sm.setup("base_path_input"),
                    "backup_path": sm.setup("backup_path_input")}
    return json_template

json_path = "Data.json"

def load(field_name):


    with open(json_path, "r") as file:
        data = json.load(file)
        return data.get(field_name)

def check():

    json_path_check = Path(json_path)

    if not json_path_check.exists:
        mode = 2
    else:
        mode = 1
    return mode

    write()

def write():

    if check("mode") == 2:
        data = default_json
    elif check("mode") == 1:

        data = get_json_template("json_template")

    with open(json_path, 'w') as file:
        json.dump(data, file, indent=2)