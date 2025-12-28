# Personal Notebook Manager

### By Nof Jawamis



#### Description

This is a Python console application that allows you to create and manage personal notes.

Each note has a title, content, tags, and a date.

Notes are saved to a JSON file, ensuring they are retained even after the program is closed.


#### Features

* Add a new note
* List all notes - View all saved notes in a readable format
* Search notes by keyword (title or content)
* Filter notes by specific tag
* Edit a note - Update existing notes
* Delete a note
* Notes are saved automatically to the JSON file

#### Requirements

* Python 3 installed
* No external libraries are needed. The code uses only built-in Python modules that come pre-installed with Python. You do not need to use pip install for anything. The following specific built-in libraries are used in the solution: JSON, os, and datetime. The colors and UI effects were achieved using ANSI Escape Codes, which are special character sequences interpreted directly by the terminal rather than requiring a library like colorama.


#### How to Run

1. Download the project folder to your computer.
2. Make sure the file "notebook\_manager.py" is inside the folder.
3. Open Command Prompt or Terminal.
4. Navigate to the folder where you saved the file.
   \* \*Windows:\* Right-click the folder > "Open in Terminal" or type `cmd` in the address bar.
   \* \*Mac/Linux:\* Open Terminal and use `cd` to go to the directory.
5. Run the program - Type the following command and press Enter: python notebook\_manager.py   (or python3 notebook\_manager.py on some systems)
6. Using the app: Follow the on-screen menu instructions (enter `1` to Add, `2` to List, etc.)

#### Notes Storage

The program automatically creates and uses:
My_Notes.json
Do not delete this file if you want to keep your saved notes.

#### Exit Program

Choose option:
0 - Exit
The program will save your notes and close.


#### Extra Notes

* If My\_Notes.json does not exist, it will be created.
* Tags should be written separated by commas. Example: home, school, todo
* You can edit or delete notes after creating them.
