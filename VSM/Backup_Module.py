from shutil import copy
from pathlib import Path
import os
from datetime import datetime
import json

def backup():

    line = "1"
     
    with open("Data.json", "r") as file:
        json_data = json.load(file)

    backup_dir = json_data['backup_path']
    game_data_dir = json_data['game_data_dir']

    save_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    save_dir = os.path.join(backup_dir, save_name)

    os.makedirs(save_dir, exist_ok=True)

#Defines the ".tres" suffix. I shouldn't need to do this but its the only way this shit will work.
    suffix = ".tres"

#I think this is converting game_data_dir to a path instead of a string. IDK becuase when I removed it, everything fucking broke
    work_dir = Path(game_data_dir) 

    for file_name in work_dir.rglob(f"*{suffix}"):
        copy(file_name, save_dir)