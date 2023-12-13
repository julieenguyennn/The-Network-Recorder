import tkinter as tk
from tkinter import ttk
from reminder_view import Reminder
import datetime
from add_contact_view import *
from Contacts import *

class home:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")

        self.contact_manager = contactManager()  # Instantiate contact manager

        # Load the search icon image
        search_icon = Image.open("search_icon.png")
        search_icon = search_icon.resize((20, 20), Image.ANTIALIAS)  # Resize the image as needed
        self.search_image = ImageTk.PhotoImage(search_icon)

        # Create and place the search icon button
        self.search_button = ttk.Button(self.root, image=self.search_image, command=self.search)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

        # Create and place the buttons for Add Contact, Import Contacts, and Display Contacts
        self.add_contact_button = ttk.Button(self.root, text="Add Contact", command=self.open_add_contact)
        self.add_contact_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.import_contacts_button = ttk.Button(self.root, text="Import Contacts", command=self.import_contacts)
        self.import_contacts_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.display_contacts_button = ttk.Button(self.root, text="Display Contacts", command=self.display_contacts)
        self.display_contacts_button.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)

    def open_add_contact(self):
        add_contact_window = tk.Toplevel(self.root)
        add_contact_app = addContact(add_contact_window)
        add_contact_app.displayWindow()

    def import_contacts(self):
        self.contact_manager.import_contacts()  # Call contactManager's import_contacts method

    def display_contacts(self):
        self.contact_manager.display_contacts_gui()  # Call contactManager's display_contacts_gui method

    def search(self):
        # Add code for searching here
        query = self.search_entry.get()
        print(f"Searching for: {query}")

    def open_reminder():
        reminder_window = tk.Toplevel(root)
        Reminder(reminder_window)

def main():
    root = tk.Tk()
    app = home(root)
    root.mainloop()

if __name__ == "__main__":
    main()
