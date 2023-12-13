# The Network Recorder

## Description
The Network Recorder is a program that allows user to note down the information of whom they have recently met. It helps user store information such as name, birthday, email, and even the day that they have met. The program aims at increasing the user's productivity compared to manual and physical note. Users can add new contact whenever they need to, import the list they currently have and view reminder of whom they haven't talked to.

## File structure
There are four files in this folder:

* `home_view.py` is the main file for executing the program
* `contacts.py` stores the contact object and its atrributes
* `add_contact_view.py` stores the code for the "Add Contact" window when it is executed 
* `reminder_view.py` stores the code for the "Reminder" window when it is executed
* `import_contact.py` stores the code for the "Import CSV file" window when it is executed
* `data_manager.py` saves the contact object when user adds a new contact and loads the information from `contacts.csv` when user reopens the program
* `contacts.csv` is the mediate file used to save added information

## Execution instructions
In order to run this program smoothly, please be advised that Python and other packages are installed. You can download Python from the official website if it's not already installed: https://www.python.org/downloads/. Other packages including `tkinter`, `csv` and `datetime` can be installed by entering `pip install [package name]` in the terminal.

In order to run this program:
1. Download all the code files and save them in the same folder
2. Open `home_view.py` and run it
2. The program will open an external window
3. Execute on the window

## Sample run
### First execution
A home window will appear on screen when the program is executed. The window includes a search bar and button, an "Add Contact" button, a "Reminder" button, an "Import CSV file" button, with the list of recent contacts below.

### When "Add Contact" is clicked
An additional window will be opened on top. Users will see placeholders for information such as Name, Email, Birthday, Category, Note, Last Met and be able to input the information. After adding the contact information, user will be prompted with a confirmation box. The box should disappear and newly-added information will be shown on the homepage immediately.

### When "Reminder" is clicked
A **pop up window [fix this if we cannot do it]** will be opened on top. Users can see a list of contacts that they last talked to 1 year, 6 months, or 3 months ago.

### When "Import CSV file" is clicked
A window from the computer system will be opened on top, which allows user to import a CSV file into the program.

### Close and reopen the program



## Sources
The logo used in the program is obtained from [please input link here]
## License
This Network Recorder is released under the MIT License. Feel free to use, modify, and distribute it for personal or educational purposes.