import pathlib
from platformdirs import user_config_path, user_data_path

def reset():
    

mode = input("Input Dev Option")

if mode.lower() == 'reset':
    reset()