from tkinter import *
from tkinter import ttk
import os
import Data_manager
from add_contact_view import AddContact
from reminder_view import Reminder
from import_contact import importContact
from Contacts import *
import speech_recognition as sr


def open_reminder():
    if not hasattr(root, 'reminder_window') or not root.Reminder:
        root.Reminder = Reminder(root)
    else:
        root.Reminder.focus()


def open_add_contact_window():
    add_contact_window = Toplevel(root)
    add_contact_window.title("Add Contact")
    AddContact(add_contact_window, tv)


def import_contacts_from_file():
    import_manager.import_contacts(update_treeview)


def update_treeview():
    contact_list = Data_manager.load_contacts_from_csv()
    tv.delete(*tv.get_children())
    for contact in contact_list:
        tv.insert('', 'end', values=(
        contact.name, contact.birthday, contact.email, contact.last_met, contact.note, contact.category))


def search_by_name():
    contact_list = Data_manager.load_contacts_from_csv()
    keyword = item.get()
    results = []
    for contact in contact_list:
        if contact.contains_partial(keyword):
            results.append(contact)

    tv.delete(*tv.get_children())

    for result in results:
        tv.insert('', 'end',
                  values=(result.name, result.birthday, result.email, result.last_met, result.note, result.category))


def start_speech_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio_data = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio_data)
        item.set(recognized_text)  # Set recognized text to the search box
        search_by_name()  # Trigger the search
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


root = Tk()

# Variables
item = StringVar()
import_manager = importContact()  # Assuming ImportContact is a valid class

# Load contacts
if not os.path.exists('contacts.csv'):
    open('contacts.csv', 'a').close()
Data_manager.load_contacts_from_csv()

# Menu Bar
menu = LabelFrame(root, text="Menu Bar")
menu.pack(padx=20, pady=20)

# Left side of the menu bar
left_menu = Frame(menu)
left_menu.pack(side=LEFT)

# Speech Recognition Button
speech_icon = PhotoImage(file="GUI graphics/speech_icon.png")
resized_speech_icon = speech_icon.subsample(26, 26)
speech_button = Button(left_menu, image=resized_speech_icon, command=start_speech_recognition)
speech_button.grid(row=0, column=0, padx=5, pady=5)

# Search Button
search_icon = PhotoImage(file="GUI graphics/search_icon.png")
resized_search_icon = search_icon.subsample(30, 30)
search_button = Button(left_menu, text="Search", image=resized_search_icon, compound="left", command=search_by_name)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Search Box
search_box = Entry(left_menu, textvariable=item)
search_box.grid(row=0, column=1, padx=5, pady=5)

# Right side of the menu bar
right_menu = Frame(menu)
right_menu.pack(side=RIGHT)

# Add Contact Button
addcontact_icon = PhotoImage(file="./GUI graphics/addcontact_icon.png")
resized_addcontact_icon = addcontact_icon.subsample(10, 10)
add_contact_button = Button(right_menu, text=" New Contact", image=resized_addcontact_icon, compound="left")
add_contact_button.grid(row=0, column=1, padx=5, pady=5)
add_contact_button.bind("<Button>", lambda e: open_add_contact_window())

# Reminder Button
reminder_no_icon = PhotoImage(file="./GUI graphics/reminder_no_icon.png")
resized_reminder_no_icon = reminder_no_icon.subsample(1, 1)
reminder_button = Button(right_menu, image=resized_reminder_no_icon, compound="left", command=open_reminder)
reminder_button.grid(row=0, column=3, padx=5, pady=5)

# Import CSV Button
csv_icon = PhotoImage(file="./GUI graphics/csv_icon.png")
resized_csv_icon = csv_icon.subsample(28, 28)
import_csv_button = Button(right_menu, text=" Upload CSV File", image=resized_csv_icon, compound="left",
                           command=import_contacts_from_file)
import_csv_button.grid(row=0, column=2, padx=5, pady=5)

# Contact List
table_space = LabelFrame(root, text="Contact list")
table_space.pack(padx=20, pady=20)

tv = ttk.Treeview(table_space, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=10)
tv.pack(padx=20, pady=20)

# Table Headers
tv.heading(1, text="Name")
tv.heading(2, text="Birthday")
tv.heading(3, text="Email")
tv.heading(4, text="Last Met")
tv.heading(5, text="Note")
tv.heading(6, text="Category")
tv.heading(7, text="   ")

# Columns Width
tv.column(1, width=100)
tv.column(2, width=100)
tv.column(3, width=100)
tv.column(4, width=100)
tv.column(5, width=100)
tv.column(6, width=100)
tv.column(7, width=20)

# Load Data into the Table
contact_list = Data_manager.load_contacts_from_csv()
tv.delete(*tv.get_children())
for contact in contact_list:
    tv.insert('', 'end',
              values=(contact.name, contact.birthday, contact.email, contact.last_met, contact.note, contact.category))

# Window Properties
root.title("Network Recorder")
root.geometry("1000x800")
root.resizable(False, False)

# Positioning Elements within the Root Window
menu.pack(side=TOP)
table_space.pack(side=TOP)



root.mainloop()
