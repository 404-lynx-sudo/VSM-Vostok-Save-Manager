import Setup_module as sm
import json
from pathlib import Path

json_path = Path('Data.json')
default_json = data = {"game_data_dir": "null",
                "base_path": "Saves/",
                "backup_path": "Backup/"}

def check():
    
    if json_path.exists():
        pass
    else: 

        write_mode = 2
    write()

def write():

    if sm.write_mode == 2:

        data = {"game_data_dir": "null",
                "base_path": "Saves/",
                "backup_path": "Backup/"}

    if sm.write_mode == 1:

    
        data = {"game_data_dir": sm.game_dir_input,
                "base_path": sm.base_path_input,
                "backup_path": sm.backup_path_input}

    with open('Data.json', 'w') as file:
        json.dump(data, file, indent=2)

def get():
    with open("Data.json", "r") as file:
        json_data = json.load(file)
        backup_path_json = json_data['backup_path']
        base_path_json = json_data['base_path']
        game_dir_json = json_data['game_data_dir'] 