import json
from Save_Module import save
from Load_Module import load
from pathlib import Path


def setup():
    def write():

        data = {"game_data_dir": game_data_dir,
                "base_path": base_path,
                "backup_path": backup_path}
        with open('Data.json', 'w') as file:
            json.dump(data, file, indent=2)

    with open("Data.json", "r") as file:
        json_data = json.load(file)
        backup_path = json_data['backup_path']
        base_path_json = json_data['base_path']
        game_data_dir_json = json_data['game_data_dir']

    while True:

        game_data_dir = input("Input the directory your save files are in. If you already did this type 'No': ")
        game_data_dir_check = Path(game_data_dir)

        if game_data_dir.lower() == "no":

            game_data_dir = game_data_dir_json

            break

        if game_data_dir_check.exists():

            break

        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    while True:

        base_path = input("Input the directory you want the files to be saved in: Default (recomended): ")
        base_path_check = Path(base_path)

        if base_path.lower() == "default":

            base_path = base_path_json

            break

        if base_path_check.exists:

            break
        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    while True:

        backup_path = input ("Input the backup directory. This is used to backup your current save files before loading: Default (recomended): ")
        backup_path_check = Path(backup_path)

        if backup_path.lower() == "default":

            backup_path = base_path_json

            break

        if backup_path_check.exists:

             break
        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    write()

while True:

    mode = input("What you like to do?: Load, Save, Setup, Exit: ")

    if mode.lower() == "setup":
        print("Loading setup module...")
        setup()

    elif mode.lower() == "save":
        print ("loading save module")
        save()

    elif mode.lower() == "load":
        print("loading load module")
        load()

    elif mode.lower() == "exit":
        print("exiting...")
        exit()
    else:
        print("Please input a proper option")
