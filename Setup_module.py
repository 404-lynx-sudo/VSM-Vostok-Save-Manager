import json
import Json_Module as jm
from pathlib import Path

write_mode = 0


def setup():

    jm.check()

    while True:

        game_dir_input = input("Input the directory your save files are in. If you already did this type 'No': ")
        game_data_dir_check = Path(game_dir_input)

        if game_dir_input.lower() == "no":

            game_dir_input = jm.load("game_dir_json")

            break

        if game_data_dir_check.exists():

            break

        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    while True:

        base_path_input = input("Input the directory you want the files to be saved in: Default (recomended): ")
        base_path_check = Path(base_path_input)

        if base_path_input.lower() == "default":

            base_path_input = jm.load("base_path_json")

            break

        if base_path_check.exists:

            break
        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    while True:

        backup_path_input = input ("Input the backup directory. This is used to backup your current save files before loading: Default (recomended): ")
        backup_path_check = Path(backup_path_input)

        if backup_path_input.lower() == "default":

            backup_path_input = jm.load("backup_path_json")

            break

        if backup_path_check.exists:

             break
        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    

    input_data = {"back_path_input": backup_path_input,
                  "base_path_input": base_path_input,
                  "game_dir_input": game_dir_input}
    
    def get_input_data(field_name):

        input_data_2 = input_data

        return input_data_2.get(field_name)

    jm.write()