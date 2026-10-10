import json
from pathlib import Path
from platformdirs import user_data_path, user_config_path


author_name = 'Manhattan Cafe'
project_name = 'Vostok Save Manager'
json_name = 'Data.json'
jsonl_name = 'Time.jsonl'
save_path_name = 'Saves'
backup_path_name = 'Backups'

def check_paths():
    data_path = user_data_path(project_name, author_name)
    config_path = user_config_path(project_name, author_name)
    saves_path = data_path / Path(save_path_name)
    backup_path = data_path / Path(backup_path_name)
    json_path = config_path / Path(json_name)
    jsonl_path =  config_path / Path(jsonl_name)

    print("Checking default path directories...")
    if not saves_path.exists() and not backup_path.exists():
        print('Directoris do not exist. Creating...')

        saves_path.mkdir(parents=True, exist_ok=True)
        backup_path.mkdir(parents=True, exist_ok=True)
        print("Directories created successfully!")
    else:
        print('Directories already exist, nothing to do')
        pass

    print('Checking if config exists...')
    if json_path.exists():
        print('Config already exists, nothing to do')
        pass
    else:
        print('Config does not exist. Creating with defaults...')
        
        config_path.mkdir(parents=True, exist_ok=True)
        
        default_json = {"game_data_path": "null",
                        "save_path": str(saves_path),
                        "backup_path": str(backup_path),
                        "scum_time": "5400"}
        with open(json_path, "w") as file:
            json.dump(default_json, file, indent=2)
        print('Config created succesfully!')

    print('Checking if time file exists...')
    if jsonl_path.exists():
        print('File exists, nothing to do')
        exit
    else:
        print('File does not exist, Creating with defaults...')
        config_path.mkdir(parents=True, exist_ok=True)
        
        default_jsonl = "0"
        with open(jsonl_path, "w") as file:
            json.dump(default_jsonl, file)
        print('File created succesfully!')
    print("Check finished succesfully")
    

def json_read():

    json_path = user_config_path(project_name, author_name) / json_name

    with open(json_path, "r") as file:
        json_data = json.load(file)
    return json_data

def jsonl_read():

    jsonl_path = user_config_path(project_name, author_name) / jsonl_name

    with open(jsonl_path, "r") as file:
        jsonl_data = json.load(file)
    return jsonl_data