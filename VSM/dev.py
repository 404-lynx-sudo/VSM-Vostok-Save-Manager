from pathlib import Path
from VSM.util import json_read as jr, ansi
import shutil
from platformdirs import user_config_path, user_data_path
import sqlite3
author_name = 'Manhattan Cafe'
project_name = 'Vostok Save Manager'
config_path = user_config_path(project_name, author_name)
data_path = user_data_path(project_name, author_name)
db_path = user_config_path(project_name, author_name) / 'vsm.db'

def reset():
    try:
        shutil.rmtree(config_path)
    except FileNotFoundError:
        print(f'{ansi["loading"]}Config path does not exist, skipping...{ansi["end"]}')
    try:
        shutil.rmtree(data_path)
    except FileNotFoundError:
        print(f'{ansi["loading"]}Data path does not exist, skipping...{ansi["end"]}')

    print(f'{ansi["good"]}Reset succesful{ansi["end"]}')

def list_data():
    try:
        for ls in data_path.iterdir():
            print(ls)
    except FileNotFoundError:
        print(f'{ansi["error"]}Directory does not exist{ansi["end"]}')

def list_config():
    try:
        for ls in config_path.iterdir():
            print(ls)
    except FileNotFoundError:
        print(f'{ansi["error"]}Directory does not exist{ansi["end"]}')

def json_print():

    try:
        json_data = jr()
    except FileNotFoundError:
        print(f'{ansi["error"]}Json does not exist{ansi["end"]}')
        return

    while True:
        field = input(f'{ansi["input"]}What field?: {ansi["end"]}')

        if field == "all":
            print(json_data)
        elif field in ("gp", "game_data_path"):
            print(json_data["game_data_path"])
        elif field in ("sp", "save_path"):
            print(json_data["save_path"])
        elif field in ("bp", "backup_path"):
            print(json_data["backup_path"])
        elif field in ("st", "scum_time"):
            print(json_data["scum_time"])
        elif field in ("lt", "load_times"):
            print(json_data["load_times"])
        elif field == "exit":
            break
        else:
            print(f'{ansi["error"]}field does not exist{ansi["end"]}')
def sql_print():
    try:

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM times")
        sql = cursor.fetchall()

        conn.close

        for data in sql:
            sql_print = data
            print(sql_print)
    except sqlite3.OperationalError:
        print(f'{ansi["error"]}Database file does not exist or is unable to be read from{ansi["end"]}')



def dev():
    while True:
        mode = input(f'{ansi["input"]}Input Dev Option: {ansi["end"]}')

        if mode.lower() == 'reset':
            reset()
        elif mode.lower() ==  'lsdata':
            list_data()
        elif mode.lower() == 'lsconf':
            list_config()
        elif mode.lower() == 'lsall':
            list_data()
            list_config()
        elif mode.lower() == 'jr':
            json_print()
        elif mode.lower() == 'sqlr':
            sql_print()
        elif mode.lower() == 'exit':
            print(f'{ansi["loading"]}Exiting...{ansi["end"]}')
            break
        else:
            print(f'{ansi["error"]}Input a valid option{ansi["end"]}')
