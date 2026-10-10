#This takes a snapshot of the save files and saves them.

import Load_Module
from shutil import copy
from pathlib import Path
import os
import json
import time
import datetime
import math
from Json_Module import check_jsonl

def check_time():

    check_jsonl()

    with open("Data.json", "r") as file:
        json_data = json.load(file)
    scum_time = float(json_data['save_scum_time'])

    with open("Time.jsonl", "r") as file:
        load_time = json.load(file)
        load_time_check = float(load_time) + scum_time

    time_now = time.time()

    if time_now >= load_time_check:
        can_move = 'yes'
        
    else:
        can_move = 'no'
    return can_move
        


def save():
    with open("Data.json", "r") as file:
        json_data = json.load(file)

    base_path = json_data['base_path']
    game_data_dir = json_data['game_data_dir']
    save_scum_time = json_data['save_scum_time']

    if check_time() == 'no':

        with open("Time.jsonl", "r") as time_file:
            time_of_save = json.load(time_file)
        save_time_add = time_of_save + float(save_scum_time)

        time_now = time.time()

        time_round = math.ceil(save_time_add - time_now)
        
        time_to_print = datetime.timedelta(seconds=time_round)

        print('You have', time_to_print, "left. Please wait until saving again" )
        return()
    
    elif check_time() == 'yes':
        pass
    
    else:
        print("ERROR: can_move not defined")
        return()


    save_name = input("Please input a name: ")

    save_dir = os.path.join(base_path, save_name)


    os.makedirs(save_dir, exist_ok=True)

#Defines the ".tres" suffix. I shouldn't need to do this but its the only way this shit will work.
    suffix = ".tres"

#I think this is converting game_data_dir to a path instead of a string. IDK becuase when I removed it, everything fucking broke
    work_dir = Path(game_data_dir) 

    for file_name in work_dir.rglob(f"*{suffix}"):
        copy(file_name, save_dir)
    
    save_time = time.time() 

    with open("Time.jsonl", "w") as file:
        json.dump(save_time, file)