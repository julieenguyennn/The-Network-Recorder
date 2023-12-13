from tkinter import *
from tkinter import ttk
import os
import Data_manager
from add_contact_view import AddContact
from reminder_view import Reminder
from import_contact import importContact
from Contacts import Contact
from PIL import Image

class Home:
    def __init__(self, root):
        self.root = root

        self.item = StringVar()
        self.contact_list = []

        self.load_contacts()

        # Load the search icon image and resize it to match the entry box height
        icon_image = Image.open("GUI graphics/search_icon.png")

        # Menu bar
        self.menu = LabelFrame(root)
        self.menu.pack(padx=20, pady=20)

        # Entry for search with icon
        self.search_box = Entry(self.menu, textvariable=self.item, justify=LEFT)
        self.search_box.pack(side=RIGHT, padx=5)

        # Set the search icon as the Entry widget's image
        self.search_box.config(image=self.search_icon, compound=LEFT)
        

        self.search_box = Entry(self.menu, textvariable=self.item)
        self.search_box.pack(side=LEFT, padx=20)

        self.search_button = Button(self.menu, text="Search", command=self.search_by_name)
        self.search_button.pack(side=LEFT, padx=20)

        self.add_contact_button = Button(self.menu, text="Add Contact", command=self.open_add_contact)
        self.add_contact_button.pack(side=LEFT, padx=20)

        self.reminder_button = Button(self.menu, text="Reminder", command=self.open_reminder)
        self.reminder_button.pack(side=LEFT, padx=20)

        self.import_csv_button = Button(self.menu, text="Import CSV", command=self.import_contacts_from_file)
        self.import_csv_button.pack(side=LEFT, padx=20)

        # Table space
        self.table_space = LabelFrame(root, text="Contact list")
        self.table_space.pack(padx=20, pady=20)

        self.tv = ttk.Treeview(self.table_space, columns=(1, 2, 3, 4, 5, 6), show="headings", height=10)
        self.tv.pack(padx=20, pady=20)

        self.tv.heading(1, text="Name")
        self.tv.heading(2, text="Birthday")
        self.tv.heading(3, text="Email")
        self.tv.heading(4, text="Last Met")
        self.tv.heading(5, text="Note")
        self.tv.heading(6, text="Category")

        self.tv.column(1, width=100)
        self.tv.column(2, width=100)
        self.tv.column(3, width=100)
        self.tv.column(4, width=100)
        self.tv.column(5, width=100)
        self.tv.column(6, width=100)

        self.update_treeview()

        self.root.title("Network Recorder")
        self.root.geometry("1000x800")
        self.root.resizable(False, False)
        self.root.mainloop()

    def load_contacts(self):
        if not os.path.exists('contacts.csv'):
            open('contacts.csv', 'a').close()
        Data_manager.load_contacts_from_csv()

    def import_contacts_from_file(self):
        import_manager = importContact()
        import_manager.import_contacts()

    def update_treeview(self):
        self.tv.delete(*self.tv.get_children())
        for contact in self.contact_list:
            self.tv.insert('', 'end', values=(contact.name, contact.birthday, contact.email, contact.last_met, contact.note, contact.category))

    def search_by_name(self):
        contact_list = Data_manager.load_contacts_from_csv()
        keyword = self.item.get()
        results = []
        for contact in contact_list:
            if contact.contains_partial(keyword):
                results.append(contact)

        self.tv.delete(*self.tv.get_children())

        # Insert search results into the Treeview
        for result in results:
            self.tv.insert('', 'end', values=(result.name, result.birthday, result.email, result.last_met, result.note, result.category))

    def open_add_contact(self):
        add_contact_view = AddContact(self.root, self.update_treeview)
        add_contact_view.show_view()

    def open_reminder(self):
        reminder_view = Reminder(self.root)
        reminder_view.show_reminder()

if __name__ == "__main__":
    root = Tk()
    app = Home(root)
