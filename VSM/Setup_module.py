import json
from Json_Module import check_json
from pathlib import Path


def setup():
    def write():

        data = {"game_data_dir": game_data_dir,
                "base_path": base_path,
                "backup_path": backup_path,
                "save_scum_time": save_timer}
        with open('Data.json', 'w') as file:
            json.dump(data, file, indent=2)
    check_json()

    with open("Data.json", "r") as file:
        json_data = json.load(file)
        backup_path_json = json_data['backup_path']
        base_path_json = json_data['base_path']
        game_data_dir_json = json_data['game_data_dir']
        save_timer_json = json_data['save_scum_time']

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

        if base_path_check.exists():

            break
        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    while True:

        backup_path = input("Input the backup directory. This is used to backup your current save files before loading: Default (recomended): ")
        backup_path_check = Path(backup_path)

        if backup_path.lower() == "default":

            backup_path = backup_path_json

            break

        if backup_path_check.exists():

             break
        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    while True:
        save_timer = input("The application uses an anti-save-scum feature prevents abusing the save feature. Please input a the ammount of time you want between saves in secconds: Default: 5400 (1.5 hours): ")

        if save_timer.lower() == "default":

            save_timer = save_timer_json

            break
        else:

            try:
                is_valid = float(save_timer)
                break

            except ValueError:
                print("Input must be an integer, float (number with or without decimal) or 'default'")


    write()