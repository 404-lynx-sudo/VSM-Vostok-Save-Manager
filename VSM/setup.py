import json
from VSM.util import check_paths, json_read as jr
from pathlib import Path
from platformdirs import user_config_path

def setup():

    json_path = user_config_path('Vostok Save Manager', 'Manhattan Cafe') / 'Data.json'
    def write():
        print('Writing to config...')

        data_to_write = {"game_data_path": game_data_path,
                "save_path": save_path,
                "backup_path": backup_path,
                "scum_time": scum_time}
        with open(json_path, 'w') as file:
            json.dump(data_to_write, file, indent=2)
        print("Write successful! Returning to main menu...")
    check_paths()

    backup_path_json = jr()['backup_path']
    save_path_json = jr()['save_path']
    game_data_path_json = jr()['game_data_path']
    scum_time_json = jr()['scum_time']

    while True:

        game_data_path = input("Input the directory your save files are in. If you already did this type 'No': ")
        game_data_path_check = Path(game_data_path)

        if game_data_path.lower() == "no":

            game_data_path = game_data_path_json

            break

        if game_data_path_check.exists():

            break

        print("Please input a proper path or option. Ensure your path does not have any qoutes or special characters")

    while True:

        save_path = input("Input the directory you want the files to be saved in: Default (recomended): ")
        save_path_check = Path(save_path)

        if save_path.lower() == "default":

            save_path = save_path_json

            break

        if save_path_check.exists():

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
        scum_time = input("The application uses an anti-save-scum feature prevents abusing the save feature. Please input a the ammount of time you want between saves in secconds: Default: 5400 (1.5 hours): ")

        if scum_time.lower() == "default":

            scum_time = scum_time_json

            break
        else:

            try:
                is_valid = float(scum_time)
                break

            except ValueError:
                print("Input must be an integer, float (number with or without decimal) or 'default'")


    write()