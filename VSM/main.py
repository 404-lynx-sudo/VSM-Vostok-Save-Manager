from VSM.load import load
from VSM.save import save
from VSM.setup import setup
from VSM.dev import dev
from VSM.util import ansi

def launch():
    while True:

        mode = input(f"{ansi['input']}What would you like to do?: Load, Save, Setup, Exit: {ansi['end']}")

        if mode.lower() == "setup":
            print(f'{ansi["loading"]}Loading setup module...{ansi["end"]}')
            setup()

        elif mode.lower() == "save":
            print(f'{ansi["loading"]}loading save module...{ansi["end"]}')
            save()

        elif mode.lower() == "load":
            print(f'{ansi["loading"]}loading load module...{ansi["end"]}')
            load()

        elif mode.lower() == "dev":
            print(f'{ansi["loading"]}Entering dev terminal{ansi["end"]}')
            dev()

        elif mode.lower() == "exit":
            print(f'{ansi["loading"]}exiting...{ansi["end"]}')
            exit()

        else:
            print(f'{ansi["error"]}Please input a proper option{ansi["end"]}')
