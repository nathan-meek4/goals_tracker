Configure to Run on Startup

Windows

Create a Batch File:

Open Notepad and paste the following:

pythonw "path\to\GoalsManager\goals_viewer.py"

Replace path\to\GoalsManager with the actual path to the folder containing your goals_viewer.py script.

Save the file as GoalsManager.bat.

Add to Startup Folder:

Press Win + R, type shell:startup, and press Enter.

Copy the GoalsManager.bat file into the Startup folder.

macOS/Linux

Add to Crontab:

Open a terminal and type:

crontab -e

Add the following line:

@reboot python3 /path/to/GoalsManager/goals_viewer.py

Replace /path/to/GoalsManager with the full path to your project directory.

Save and exit.
