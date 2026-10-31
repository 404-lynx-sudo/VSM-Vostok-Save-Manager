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

        author_name = 'Manhattan Cafe'
        project_name = 'Vostok Save Manager'

        db_path = user_config_path(project_name, author_name) / 'vsm.db'

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT loads_left FROM times")

        loads_left = cursor.fetchone()
        conn.close
        

        if sum(loads_left) <= 0:
            print("You have used all your loads, please try again later")
            break
        else:

            save_to_load = input("What save would you like to load?: ")
            save_path = jr()['save_path']
            game_data_path = jr()['game_data_path']

            save_name_path = os.path.join(save_path, save_to_load)
            save_dir_check = Path(save_name_path)



            if save_dir_check.exists():
            
                print("Backing up current save...")

                backup()

                suffix = ".tres"

                work_dir = Path(save_name_path) 

                for file_name in work_dir.rglob(f"*{suffix}"):
                    copy(file_name, game_data_path)

                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()

                    loads_left_now = sum(loads_left) - 1

                    cursor.execute(
                        "UPDATE times SET loads_left = ?",
                        (loads_left_now,)
                        )
                    conn.commit()
                    conn.close()
            else:
                print("Please input a valid save file.")
        conn.close()
        print(f'Load successful! You have {loads_left_now} loads left. Returning to main menu...')
        break