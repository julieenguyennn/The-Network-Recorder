from tkinter import *
from tkinter import ttk
from Contacts import *
from add_contact_view import *
from reminder_view import Reminder
from import_contact import importContact
import os

def save_contacts():
    contact_manager.save_contacts_to_csv()

def load_contacts():
    if not os.path.exists('contacts.csv'):
        open('contacts.csv', 'a').close()
    contact_manager.load_contacts_from_csv()

def import_contacts_from_file():
    import_manager = importContact()
    import_manager.import_contacts()

def searchName():
    search_input = Contact(item.get())
    name = search_input.name()
    birthday = search_input.birthday()
    email = search_input.email()
    last_met = search_input.last_met()
    note = search_input.note()
    category = search_input.category()
    tv.insert('','end', values=(name, birthday, email, last_met, note, category))

root = Tk()
contact_manager = contactManager()
item = StringVar()

load_contacts()

# Menu bar
menu = LabelFrame(root, text="Menu Bar")
menu.pack(padx=20, pady=20)

search_box = Entry(menu, textvariable=item)
search_box.pack(side=LEFT, padx=20)

search_button = Button(menu, text="Search", command=searchName)
search_button.pack(side=LEFT, padx=20)

add_contact_button = Button(menu, text="Add Contact")
add_contact_button.pack(side=LEFT, padx=20)
add_contact_button.bind("<Button>", lambda e: addContact(root, tv))

reminder_button = Button(menu, text="Reminder")
reminder_button.pack(side=LEFT, padx=20)
reminder_button.bind("<Button>", lambda e: Reminder(root))

import_csv_button = Button(menu, text="Import CSV", command=import_contacts_from_file)
import_csv_button.pack(side=LEFT, padx=20)

# Table space
table_space = LabelFrame(root, text="Contact list")
table_space.pack(padx=20, pady=20)

tv = ttk.Treeview(table_space, columns=(1,2,3,4,5,6), show="headings", height=10)
tv.pack(padx=20, pady=20)

tv.heading(1, text="Name")
tv.heading(2, text="Birthday")
tv.heading(3, text="Email")
tv.heading(4, text="Last Met")
tv.heading(5, text="Note")
tv.heading(6, text="Category")

tv.column(1, width=100)
tv.column(2, width=100)
tv.column(3, width=100)
tv.column(4, width=100)
tv.column(5, width=100)
tv.column(6, width=100)

root.title("Network Recorder")
root.geometry("1000x800")
root.resizable(False, False)
root.mainloop()