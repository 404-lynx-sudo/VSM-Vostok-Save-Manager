import json
from pathlib import Path
from platformdirs import user_data_path, user_config_path
import sqlite3


author_name = 'Manhattan Cafe'
project_name = 'Vostok Save Manager'
json_name = 'Data.json'
db_name= 'vsm.db'
save_path_name = 'Saves'
backup_path_name = 'Backups'
db_path = user_config_path(project_name, author_name) / db_name
ansi = {"error": '\033[91m',
        "input": '\033[96m',
        "loading": '\033[35m',
        "info": '\033[93m',
        "end": '\033[0m',
        "good": '\033[92m'}

def check_paths():
    data_path = user_data_path(project_name, author_name)
    config_path = user_config_path(project_name, author_name)
    saves_path = data_path / Path(save_path_name)
    backup_path = data_path / Path(backup_path_name)
    json_path = config_path / Path(json_name)
    db_path =  config_path / Path(db_name)

    print(f'{ansi["loading"]}Checking default path directories...{ansi["end"]}')

    if not saves_path.exists() and not backup_path.exists():
        print(f'{ansi["loading"]}Directoris do not exist. Creating...{ansi["end"]}')

        saves_path.mkdir(parents=True, exist_ok=True)
        backup_path.mkdir(parents=True, exist_ok=True)
        print(f"{ansi["good"]}Directories created successfully!{ansi["end"]}")
    else:
        print(f'{ansi["good"]}Directories already exist, nothing to do{ansi["end"]}')
        pass

    print(f'{ansi["loading"]}Checking if config exists...{ansi["end"]}')
    if json_path.exists():
        print(f'{ansi["good"]}Config already exists, nothing to do{ansi["end"]}')
        pass
    else:
        print(f'{ansi["loading"]}Config does not exist. Creating with defaults...{ansi["end"]}')
        
        config_path.mkdir(parents=True, exist_ok=True)
        
        default_json = {"game_data_path": "null",
                        "save_path": str(saves_path),
                        "backup_path": str(backup_path),
                        "scum_time": "5400",
                        "load_times": "2"}
        with open(json_path, "w") as file:
            json.dump(default_json, file, indent=2)
        print(f'{ansi["good"]}Config created succesfully!{ansi["end"]}')

    print(f'{ansi["loading"]}Checking if time database exists...{ansi["end"]}')
    if db_path.exists():
        print(f'{ansi["good"]}Database exists nothing to do{ansi["end"]}')
        exit
    else:
        print(f'{ansi["loading"]}Database does not exist, Creating with defaults...{ansi["end"]}')
        config_path.mkdir(parents=True, exist_ok=True)

        db_path = config_path / 'vsm.db'
        default_lastsave = "0"
        default_maxload = 2

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS times (
                last_save FLOAT,
                loads_left INTERGER
            )
        """)

        cursor.execute(
                "INSERT INTO times (last_save, loads_left) VALUES (?, ?)",
                (default_lastsave, default_maxload, )
            )

        conn.commit()
        conn.close()

        print(f'{ansi["good"]}Database created succesfully{ansi["end"]}')

    

def json_read():

    json_path = user_config_path(project_name, author_name) / json_name

    with open(json_path, "r") as file:
        json_data = json.load(file)
    return json_data

def db_reset():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    max_load_json = json_read()['load_times']

    cursor.execute(
        "UPDATE times SET loads_left = ?",
        (max_load_json,)
    )
    conn.commit()
    conn.close()