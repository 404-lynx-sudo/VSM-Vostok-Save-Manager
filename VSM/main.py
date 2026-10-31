from VSM.load import load
from VSM.save import save
from VSM.setup import setup
from VSM.dev import dev

def launch():
    while True:

        mode = input("What would you like to do?: Load, Save, Setup, Exit: ")

        if mode.lower() == "setup":
            print("Loading setup module...")
            setup()

        elif mode.lower() == "save":
            print ("loading save module...")
            save()

        elif mode.lower() == "load":
            print("loading load module...")
            load()

        elif mode.lower() == "dev":
            print("Entering dev terminal")
            dev()

        elif mode.lower() == "exit":
            print("exiting...")
            exit()

        else:
            print("Please input a proper option")
