import json
import os
from pathlib import Path
from platformdirs import user_data_path

def check_paths():

    data_path = user_data_path('Vostok Save Manger', 'Manhattan Cafe')
    saves_path = data_path / Path('Saves')
    backup_path = data_path / Path('Backups')
    json_path = data_path / Path('Data.json')
    jsonl_path =  data_path / Path('Time.jsonl')


    if not saves_path.exists() and not backup_path.exists():

        saves_path.mkdir(parents=True, exist_ok=True)
        backup_path.mkdir(parents=True, exist_ok=True)
        print("yes")
    else:
        pass

    if json_path.exists():
        pass
    else:

        default_json = {"game_data_path": "null",
                        "save_path": str(saves_path),
                        "backup_path": str(backup_path),
                        "scum_time": "5400"}
        with open(json_path, "w") as file:
            json.dump(default_json, file, indent=2)

    if jsonl_path.exists():
        exit
    else:
    
        default_jsonl = "0"
        with open(jsonl_path, "w") as file:
            json.dump(default_jsonl, file)
    

def json_read():

    data_path = user_data_path('Vostok Save Manger', 'Manhattan Cafe')
    json_path = data_path / Path('Data.json')

    with open(json_path, "r") as file:
        json_data = json.load(file)
    return json_data

def jsonl_read():

    data_path = user_data_path('Vostok Save Manger', 'Manhattan Cafe')
    jsonl_path = data_path / Path('Time.jsonl')

    with open(jsonl_path, "r") as file:
        jsonl_data = json.load(file)
    return jsonl_data