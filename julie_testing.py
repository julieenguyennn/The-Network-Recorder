from tkinter import *
from tkinter import ttk
import Contacts
from add_contact_view import *
from reminder_view import Reminder
from import_contact import importContact
import os
import Data_manager
from Contacts import Contact

# Create a function to load contacts whenever the program is reopened
def load_contacts():
    if not os.path.exists('contacts.csv'):
        open('contacts.csv', 'a').close()
    Data_manager.load_contacts_from_csv()

# Create a function to import contact from a CSV file
def import_contacts_from_file():
    import_manager = importContact()
    import_manager.import_contacts(update_treeview) 

# Create a function to update the contact table display
def update_treeview():
    tv.delete(*tv.get_children())
    for contact in contact_list:
        tv.insert('', 'end', values=(contact.name, contact.birthday, contact.email, contact.last_met, contact.note, contact.category))

# Create a function to search by name
def search_by_name():
    contact_list = Data_manager.load_contacts_from_csv()
    keyword = item.get()
    results = []
    for contact in contact_list:
        if contact.contains_partial(keyword):
            results.append(contact)

    tv.delete(*tv.get_children())

    # Insert search results into the Treeview
    for result in results:
        tv.insert('', 'end',
                  values=(result.name, result.birthday, result.email, result.last_met, result.note, result.category))

# Main program
root = Tk()
item = StringVar()

load_contacts() # Load saved contacts (if any)

contact_list = Data_manager.load_contacts_from_csv() # What is this for idk???

# Menu bar
menu = LabelFrame(root, text="Menu Bar") # Create a menu bar container
menu.pack(padx=20, pady=20)

# Create a search box and search button inside the menu container
search_box = Entry(menu, textvariable=item)
search_box.pack(side=LEFT, padx=20)

search_button = Button(menu, text="Search", command=search_by_name)
search_button.pack(side=LEFT, padx=20)

# Create a button to add new contact inside the menu container
add_contact_button = Button(menu, text="Add Contact")
add_contact_button.pack(side=LEFT, padx=20)
add_contact_button.bind("<Button>", lambda e: addContact(root, tv))

# Create a button to view reminder inside the menu container
reminder_button = Button(menu, text="Reminder")
reminder_button.pack(side=LEFT, padx=20)
reminder_button.bind("<Button>", lambda e: Reminder(root))

# Create a button to import a CSV file inside the menu container
import_csv_button = Button(menu, text="Import CSV file", command=import_contacts_from_file)
import_csv_button.pack(side=LEFT, padx=20)

# Table space
table_space = LabelFrame(root, text="Contact list")
table_space.pack(padx=20, pady=20)

# Create table inside the table space container
tv = ttk.Treeview(table_space, columns=(1,2,3,4,5,6), show="headings", height=10)
tv.pack(padx=20, pady=20)

# Set up heading for the table
tv.heading(1, text="Name")
tv.heading(2, text="Birthday")
tv.heading(3, text="Email")
tv.heading(4, text="Last Met")
tv.heading(5, text="Note")
tv.heading(6, text="Category")

# Set up column width for the table
tv.column(1, width=100)
tv.column(2, width=100)
tv.column(3, width=100)
tv.column(4, width=100)
tv.column(5, width=100)
tv.column(6, width=100)

update_treeview() # Update the table when 

# Set up the root container
root.title("Network Recorder")
root.geometry("1000x800")
root.resizable(False, False)
root.mainloop()