from pathlib import Path
from VSM.util import json_read as jr
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
        print("Config path does not exist, skipping...")
    try:
        shutil.rmtree(data_path)
    except FileNotFoundError:
        print("Data path does not exist, skipping...")

    print("Reset succesful")

def list_data():
    try:
        for ls in data_path.iterdir():
            print(ls)
    except FileNotFoundError:
        print("Directory does not exist")

def list_config():
    try:
        for ls in config_path.iterdir():
            print(ls)
    except FileNotFoundError:
        print("Directory does not exist")

def json_print():

    try:
        json_data = jr()
    except FileNotFoundError:
        print("Json does not exist")

    while True:
        field = input("What field?: ")

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
            print("field does not exist")
def sql_print():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM times")
    sql = cursor.fetchall()

    for data in sql:
        sql_print = data
        print(sql_print)



def dev():
    while True:
        mode = input("Input Dev Option: ")

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
            print("Exiting...")
            break
        else:
            print("Input a valid option")
