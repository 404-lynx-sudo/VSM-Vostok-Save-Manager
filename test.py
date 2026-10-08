import json

data = {"game_data_dir": "null",
        "base_path": "Saves/",
        "backup_path": "Backup/"}

jsonp = "/home/lynx/Documents/Code Projects/VSM-Vostok-Save-Manager/VSM-Main/Data.json"

with open(jsonp, 'w') as file:
    json.dump(data, file, indent=2)