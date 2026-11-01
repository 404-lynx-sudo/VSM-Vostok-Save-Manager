from shutil import copy
from pathlib import Path
from VSM.util import check_paths, json_read as jr, db_reset as dbr, ansi
import os
import json
import time
import datetime
import math
from platformdirs import user_config_path
import sqlite3


author_name = 'Manhattan Cafe'
project_name = 'Vostok Save Manager'
db_path = user_config_path(project_name, author_name) / 'vsm.db'

def check_time():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT last_save FROM times")

    last_save = cursor.fetchone()

    scum_time_value = float(jr()['scum_time'])
    last_save_float = float
    till_next_load = float(last_save[0]) + scum_time_value

    time_now = time.time()

    conn.close()

    if time_now >= till_next_load:
        can_move = 'yes'
        
    else:
        can_move = 'no'
    return can_move
    
        


def save():

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT last_save FROM times")

    last_save = cursor.fetchone()

    save_path = jr()['save_path']
    game_data_path = jr()['game_data_path']
    scume_time_value = jr()['scum_time']

    conn.close

    print(f'{ansi["loading"]}Checking last save time...{ansi["end"]}')

    if check_time() == 'no':

        save_time_add = float(last_save[0]) + float(scume_time_value)

        time_now = time.time()

        till_next_load = math.ceil(save_time_add - time_now)
        
        readable_time = datetime.timedelta(seconds=till_next_load)

        print(f'{ansi["info"]}You have {readable_time} left. Please wait until saving again{ansi["end"]}')
        return()
    
    elif check_time() == 'yes':

        print(f'{ansi["info"]}You can save!{ansi["end"]}')
        
        pass
    
    else:
        print(f'{ansi["error"]}ERROR: can_move not defined{ansi["end"]}')
        return()


    save_name = input(f'{ansi["input"]}Please input a name: {ansi["end"]}')

    print(f'{ansi["loading"]}Saving...{ansi["end"]}')

    save_name_path = os.path.join(save_path, save_name)


    os.makedirs(save_name_path, exist_ok=True)

#Defines the ".tres" suffix. I shouldn't need to do this but its the only way this shit will work.
    suffix = ".tres"

#I think this is converting game_data_dir to a path instead of a string. IDK becuase when I removed it, everything fucking broke
    work_dir =  Path(game_data_path) 

    for tres_file in work_dir.rglob(f"*{suffix}"):
        copy(tres_file, save_name_path)
    
    time_of_save = time.time()

    cursor.execute(
        "UPDATE times SET last_save = ?",
        (time_of_save,)
    )
    conn.commit()
    conn.close()

    dbr()

    print(f'{ansi["good"]}Succesfully saved!{ansi["end"]}')