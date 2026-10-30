from VSM.backup import backup
from VSM.util import json_read as jr
from shutil import move
from shutil import copy
from pathlib import Path
from platformdirs import user_config_path
import json
from datetime import datetime
import os
import sqlite3

def load():

    while True:
        save_to_load = input("What save would you like to load?: ")

        print("Backing up current save...")

        backup()

        save_path = jr()['save_path']
        game_data_path = jr()['game_data_path']
        db_path = user_config_path() / 'vsm.db'

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT  FROM time")

        rows = cursor.fetchall()


        save_name_path = os.path.join(save_path, save_to_load)
        save_dir_check = Path(save_name_path)

        if save_dir_check.exists():

            suffix = ".tres"

            work_dir = Path(save_name_path) 

            for file_name in work_dir.rglob(f"*{suffix}"):
                copy(file_name, game_data_path)
            
            break
        print("Please input a valid save file.")
        
    print('Load successful! Returning to main menu...')