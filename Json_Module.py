import json
import os
from pathlib import Path

def check_json():
    json_location = "Data.json/"
    json_location_path = Path(json_location)

    os.makedirs('Saves', exist_ok=True)
    os.makedirs('Backup', exist_ok=True)

    if json_location_path.exists():
        print("yes")
        exit
    else:

        default_json = {"game_data_dir": "null",
                        "base_path": "Saves/",
                        "backup_path": "Backup/",
                        "save_scum_time": "5400"}
        with open("Data.json", "w") as file:
            json.dump(default_json, file, indent=2)