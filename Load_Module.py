from Backup_Module import backup
from shutil import move
from shutil import copy
from pathlib import Path
import json
from datetime import datetime
import os

def load():

    while True:
        save_to_load = input("What save would you like to load?: ")

        backup()

        with open("Data.json", "r") as file:
            json_data = json.load(file)

        base_path = json_data['base_path']
        game_data_dir = json_data['game_data_dir']


        save_dir = os.path.join(base_path, save_to_load)
        save_dir_check = Path(save_dir)

        if save_dir_check.exists():

            suffix = ".tres"

            work_dir = Path(save_dir) 

            for file_name in work_dir.rglob(f"*{suffix}"):
                copy(file_name, game_data_dir)
            
            break
        print("Please input a valid save file.")