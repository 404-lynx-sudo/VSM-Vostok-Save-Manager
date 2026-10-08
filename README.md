# VSM: An open source, dead simple save manager for Road To Vostok

## WARNINGS. Read before you use
- I am not responsible for any lost progress and saves, I encourage you to back up your files first
- I encourage you not to abuse this. The game is supposed to be hardcore, so only use this when you genuinely need it.
- DO NOT TRY TO USE THIS WHILE THE GAME IS RUNNING. I have not tested what will happen, but my assumption is nothing good.
- This is currently only designed to work on windows. Linux support is planned, however MacOS may or may not happen.

## Note on Linux/MacOS setup
Technically there is no reason that this should not work on Linux. I only stated that it is not supported since there is no precompiled and ready to use file for Linux. If you want to use Linux before I add official support, then clone the git repo and execute "Setup_module.py". That is just what the .exe on Windows does anyway. 

## How to set up
**Note:** Python needs to be installed
1. Go to the releases page, download the zip file, and unzip it.
2. Inside is a shortcut for "RSM.EXE" open it.
3. A terminal window should pop up with the text "What you like to do?: Load, Save, Setup, Exit:" This is the "main menu."
4. Type "Setup" and hit enter
5. Input the directory your game stores its data, NOT the directory you installed the game. Default for windows is "C:\Users\[Input Your User]\AppData\Roaming\Road to Vostok.
6. You will be prompted to provide a save directory and a backup directory. This are already set by default so just type "Default"
7. You are done with the setup.


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

## Things to add
- A GUI
- An anti-save-scum feature
- Linux support

## Credits

Purchase Road To Vostok on [Steam.](https://store.steampowered.com/app/1963610/Road_to_Vostok/)
