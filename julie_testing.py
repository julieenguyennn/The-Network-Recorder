from tkinter import *
from tkinter import ttk
import os
import Data_manager
from add_contact_view import AddContact
from reminder_view import Reminder
from import_contact import importContact
from Contacts import Contact

class Home:
    def __init__(self, root):
        self.root = root
        self.item = StringVar()
        self.load_contacts()
        self.contact_list = Data_manager.load_contacts_from_csv()

        self.menu = LabelFrame(self.root, text="Menu Bar")
        self.menu.pack(padx=20, pady=20)

        # Left side of the menu bar
        left_menu = Frame(self.menu)
        left_menu.pack(side=LEFT)

        # Load the search icon image and resize it
        search_icon = PhotoImage(file="GUI graphics/search_icon.png")
        resized_search_icon = search_icon.subsample(30, 30)  # Adjust the subsample values as needed

        # Create a button with the search icon
        search_button = Button(left_menu, text="Search", image=resized_search_icon, compound="left", command=self.search_by_name)
        search_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_box = Entry(left_menu, textvariable=self.item)
        self.search_box.grid(row=0, column=0, padx=5, pady=5)

        # Right side of the menu bar
        right_menu = Frame(self.menu)
        right_menu.pack(side=RIGHT)

        # Add contact icon
        addcontact_icon = PhotoImage(file="GUI graphics/addcontact_icon.png")
        resized_addcontact_icon = addcontact_icon.subsample(10, 10)
        self.add_contact_button = Button(right_menu, text=" New Contact", image=resized_addcontact_icon, compound="left") #command=self.search_by_name)
        self.add_contact_button.grid(row=0, column=1, padx=5, pady=5)
        self.add_contact_button.bind("<Button>", lambda e: AddContact(self.root, self.tv))

        # Add reminder icon
        reminder_no_icon = PhotoImage(file="GUI graphics/reminder_no_icon.png")
        resized_reminder_no_icon = reminder_no_icon.subsample(1, 1)  # Adjust the subsample values as needed
        self.reminder_button = Button(right_menu, image=resized_reminder_no_icon, compound="left")
        self.reminder_button.grid(row=0, column=3, padx=5, pady=5)
        self.reminder_button.bind("<Button>", lambda e: Reminder(self.root))

        def update_reminder_icon(new_reminder):
            if new_reminder:
                reminder_yes_icon_path = "GUI graphics/reminder_yes_icon.png"
                reminder_yes_icon = PhotoImage(file=reminder_yes_icon_path)
                resized_reminder_yes_icon = reminder_yes_icon.subsample(1, 1)  # Adjust subsample values as needed
                self.reminder_button.config(image=resized_reminder_yes_icon)
                self.reminder_button.image = resized_reminder_yes_icon  # Keep reference to avoid garbage collection
        
        # Upload csv icon
        csv_icon = PhotoImage(file="GUI graphics/csv_icon.png")
        resized_csv_icon = csv_icon.subsample(28, 28)
        self.import_csv_button = Button(right_menu, text=" Upload CSV List", image=resized_csv_icon,  compound="left", command=self.import_contacts_from_file)
        self.import_csv_button.grid(row=0, column=2, padx=5, pady=5)

        # Table space
        table_space = LabelFrame(root, text="Contact list")
        table_space.pack(padx=20, pady=20)

        tv = ttk.Treeview(table_space, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=10)
        tv.pack(padx=20, pady=20)

        tv.heading(1, text="Name")
        tv.heading(2, text="Birthday")
        tv.heading(3, text="Email")
        tv.heading(4, text="Last Met")
        tv.heading(5, text="Note")
        tv.heading(6, text="Category")
        tv.heading(7, text="   ")


        tv.column(1, width=100)
        tv.column(2, width=100)
        tv.column(3, width=100)
        tv.column(4, width=100)
        tv.column(5, width=100)
        tv.column(6, width=100)
        tv.column(7, width=20)

        # Load data into the table
        update_treeview()

        root.title("Network Recorder")
        root.geometry("1000x800")
        root.resizable(False, False)

        # Positioning elements within the root window
        menu.pack(side=TOP)
        table_space.pack(side=TOP)

    def load_contacts(self):
        if not os.path.exists('contacts.csv'):
            open('contacts.csv', 'a').close()
        Data_manager.load_contacts_from_csv()

    def import_contacts_from_file(self):
        import_manager = importContact()
        import_manager.import_contacts()

    def update_treeview(self):
        contact_list = Data_manager.load_contacts_from_csv()  # Retrieve contacts from the file
        self.tv.delete(*self.tv.get_children())
        for contact in contact_list:
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

root = Tk()
app = Home(root)
root.mainloop()
