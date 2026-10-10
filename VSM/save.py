#This takes a snapshot of the save files and saves them.
from shutil import copy
from pathlib import Path
from VSM.util import jsonl_read as jlr, check_paths, json_read as jr
import os
import json
import time
import datetime
import math
from platformdirs import user_config_path

jsonl_path = user_config_path('Vostok Save Manager', 'Manhattan Cafe') / 'Time.jsonl'

def check_time():

    scum_time_value = float(jr()['scum_time'])
    last_load_time = jlr()
    till_next_load = float(last_load_time) + scum_time_value

    time_now = time.time()

    if time_now >= till_next_load:
        can_move = 'yes'
        
    else:
        can_move = 'no'
    return can_move
        


def save():

    save_path = jr()['save_path']
    game_data_path = jr()['game_data_path']
    scume_time_value = jr()['scum_time']

    print('Checking last save time...')

    if check_time() == 'no':

        time_of_save = jlr()

        save_time_add = time_of_save + float(scume_time_value)

        time_now = time.time()

        till_next_load = math.ceil(save_time_add - time_now)
        
        readable_time = datetime.timedelta(seconds=till_next_load)

        print('You have', readable_time, "left. Please wait until saving again" )
        return()
    
    elif check_time() == 'yes':

        print('You can save!')
        
        pass
    
    else:
        print("ERROR: can_move not defined")
        return()


    save_name = input("Please input a name: ")

    print('Saving...')

    save_name_path = os.path.join(save_path, save_name)


    os.makedirs(save_name_path, exist_ok=True)

#Defines the ".tres" suffix. I shouldn't need to do this but its the only way this shit will work.
    suffix = ".tres"

#I think this is converting game_data_dir to a path instead of a string. IDK becuase when I removed it, everything fucking broke
    work_dir =  Path(game_data_path) 

    for tres_file in work_dir.rglob(f"*{suffix}"):
        copy(tres_file, save_name_path)
    
    time_of_save = time.time() 

    with open(jsonl_path, "w") as file:
        json.dump(time_of_save, file)

    print('Succesfully saved!')