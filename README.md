# VSM: An open source, dead simple save manager for Road to Vostok

## WARNINGS. Read before you use
- I am not responsible for any lost progress and saves, I encourage you to back up your files first
- I encourage you not to abuse this. The game is supposed to be hardcore, so only use this when you genuinely need it.
- DO NOT TRY TO USE THIS WHILE THE GAME IS RUNNING. I have not tested what will happen, but my assumption is nothing good.

## Note on macOS
This application is a python project, is installed from pypi and automatically detects the operating system. There is no reason this should not work on mac, but I do not own a mac so I can not confirm it. 

# Installation

## Dependencies
Requires python 3.10 (havn't verified if it works on older versions) or newer
Requires pipx. For windows users, you can _technically_ use standard pip since windows allows you to install packages directly to global, but pipx is better and is a requirment on linux.

## Linux

1. Use pipx to install the package 
```shell
pipx install vostok-save-manager
```
2. You should automatically get access to the command ```VSM```. This is the command to launch the "main menu" 
3. After you type ```VSM``` you should see in your terminal ```What you like to do?: Load, Save, Setup, Exit: ```. Type ```setup``` to continue the setup
4. You will be asked where the game data is located. This is not the game installation folder as Road to Vostok puts its game data in a different location than its installation
5. You will be asked where you want your saved files to be stored. The recomended is ```default``` since it automatically creates a default directory.
6. You will be asked where you want your backuped up save  files to be stored. The recomended is ```default``` since it automatically creates a default directory.
7. You will be asked how much time you want before you can save again. The default time is 5400 secconds, which is 1 hour and 30 minutes. You can change this to whatever you want, but it must be input as secconds and as an interger (whole number) or float (number with decimal).
8. The setup is now done.

## Windows

1. Use pipx to install the package 
```shell
pipx install vostok-save-manager
```
Or since windows doesn't strictly require packages be in a virtual environment
```shell
pip install vostok-save-manager
```
But pipx is recomended

2. You should automatically get access to the command ```VSM```. This is the command to launch the "main menu". If you get an error along the lines of "VSM is not recognized as command" run
```shell
pipx ensurepath
```
and try again.

3. After you type ```VSM``` you should see in your terminal ```What you like to do?: Load, Save, Setup, Exit: ```. Type ```setup``` to continue the setup
4. You will be asked where the game data is located. This is not the game installation folder as Road to Vostok puts its game data in a different location than its installation
5. You will be asked where you want your saved files to be stored. The recomended is ```default``` since it automatically creates a default directory.
6. You will be asked where you want your backuped up save  files to be stored. The recomended is ```default``` since it automatically creates a default directory.
7. You will be asked how much time you want before you can save again. The default time is 5400 secconds, which is 1 hour and 30 minutes. You can change this to whatever you want, but it must be input as secconds and as an interger (whole number) or float (number with decimal).
8. The setup is now done.

# How to use
 
## How to save
1. On the main menu type "Save."
2. You will be prompted to name the save. This can be anything.
3. After you input your save, the game will automatically copy and store the current save files in your game directory. No backup is needed since it is not moving or replacing anything.
4. If you input the name of an already existing save it WILL overwrite it.
5. You have now saved your game.

## How to load
1. On the main menu type "Load."
2. You will be prompted to give the name of a save. This has to be EXACT and is case sensitive.
3. The application automatically backs up the save files currently in your game data directory.
4. You have now loaded a save.

# Things to add
- A GUI
- a command to list all saves while I learn how to make a GUI

# Credits

Purchase Road to Vostok on [Steam.](https://store.steampowered.com/app/1963610/Road_to_Vostok/)
