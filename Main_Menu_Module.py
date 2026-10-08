
from Load_Module import load
from Setup_module import setup
from Save_Module import save

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