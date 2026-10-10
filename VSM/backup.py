from shutil import copy
from pathlib import Path
from util import json_read as jr
import os
from datetime import datetime
import json

def backup():

    line = "1"

    backup_path = jr()['backup_path']
    game_data_path = jr()['game_data_path']
    print(game_data_path)

    backup_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_path = os.path.join(backup_path, backup_time)

    os.makedirs(backup_path, exist_ok=True)

#Defines the ".tres" suffix. I shouldn't need to do this but its the only way this shit will work.
    suffix = ".tres"

#I think this is converting game_data_dir to a path instead of a string. IDK becuase when I removed it, everything fucking broke
    work_dir = Path(game_data_path) 

    for file_name in work_dir.rglob(f"*{suffix}"):
        copy(file_name, backup_path)