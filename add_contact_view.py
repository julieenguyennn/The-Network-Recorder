from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk
import Contacts
import Data_manager
from datetime import datetime


class AddContact:
    def __init__(self, root, tv):
        self.root = root
        self.tv = tv
        self.root.title("New contact")

        self.contacts = data_manager.load_contacts_from_csv()  # Load contacts from CSV

        self.calendar_icon = PhotoImage(file="GUI graphics/calendar_icons.png")

        self.add_button = Button(root, text="Add Contact", command=self.add_contact)

        self.setup_ui()

    # Create GUI
    def setup_ui(self):
        frame = Frame(self.root)
        frame.pack(fill=X, padx=10, pady=5)

        # Create frame for name input
        name_frame = Frame(frame)
        name_frame.pack(fill=X, padx=5, pady=5)
        Label(name_frame, text="Name:").pack(side=LEFT)
        self.name_entry = Entry(name_frame)
        self.name_entry.pack(side=RIGHT, padx=5, pady=5)

        # Create frame for email input
        email_frame = Frame(frame)
        email_frame.pack(fill=X, padx=5, pady=5)
        Label(email_frame, text="Email:").pack(side=LEFT)
        self.email_entry = Entry(email_frame)
        self.email_entry.pack(side=RIGHT, padx=5, pady=5)

        # Create frame for birthday input
        birthday_frame = Frame(frame)
        birthday_frame.pack(fill=X, padx=5, pady=5)
        Label(birthday_frame, text="Birthday:").pack(side=LEFT)
        self.birthday_entry = Entry(birthday_frame)
        self.birthday_entry.pack(side=RIGHT, padx=5, pady=5)
        self.calendar_button_birthday = Button(birthday_frame, command=self.open_calendar_birthday, image=self.calendar_icon, compound="left")
        self.calendar_button_birthday.pack(side=RIGHT, padx=5, pady=5)

        # Create frame for category input
        category_frame = Frame(frame)
        category_frame.pack(fill=X, padx=5, pady=5)
        Label(category_frame, text="Category:").pack(side=LEFT)
        categories = ["Work", "Personal", "Family", "Friends"]
        self.category_combobox = ttk.Combobox(category_frame, values=categories)
        self.category_combobox.pack(side=RIGHT, padx=5, pady=5)

        # Create frame for last met date input
        last_met_frame = Frame(frame)
        last_met_frame.pack(fill=X, padx=5, pady=5)
        Label(last_met_frame, text="Last met:").pack(side=LEFT)
        self.last_met_entry = Entry(last_met_frame)
        self.last_met_entry.pack(side=RIGHT, padx=5, pady=5)
        self.calendar_button_last_met = Button(last_met_frame, command=self.open_calendar_last_met, image=self.calendar_icon)
        self.calendar_button_last_met.pack(side=RIGHT, padx=5, pady=5)

        # Create frame for note input
        note_frame = Frame(frame)
        note_frame.pack(fill=X, padx=5, pady=5)
        Label(note_frame, text="Note:").pack(side=LEFT)
        self.note_entry = Text(note_frame, height=5, width=30)
        self.note_entry.pack(side=RIGHT, fill='both', padx=5, pady=5, expand=True)

        # Add Contact Button
        self.add_button.pack(fill=X, padx=5, pady=10) 

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        birthday = self.birthday_entry.get()
        category = self.category_combobox.get()
        last_met = self.last_met_entry.get()
        note = self.note_entry.get("1.0", "end-1c")

        contact_info = f"Name: {name}\nEmail: {email}\nLast Met: {last_met}\nBirthday: {birthday}\nCategory: {category}\nNote: {note}"
        messagebox.showinfo("Confirm your entry", contact_info)

        contact = contacts.Contact(name, datetime.strptime(birthday, "%m-%d-%Y"), email, datetime.strptime(last_met, "%m-%d-%Y"), note, category)
        self.contacts.append(contact)
        data_manager.save_contacts_to_csv(self.contacts)
        self.update_treeview(contact)
        self.root.destroy()

    def open_calendar_birthday(self):
        top = Toplevel(self)
        cal = Calendar(top, selectmode='day', date_pattern='mm-dd-yyyy', foreground='black')
        cal.pack(padx=10, pady=10)

        def get_selected_date():
            selected_date = cal.get_date()
            self.birthday_entry.delete(0, END)
            self.birthday_entry.insert(0, selected_date)
            top.destroy()

        Button(top, text="Select Date", command=get_selected_date).pack(pady=5)

    def open_calendar_last_met(self):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day', date_pattern='mm-dd-yyyy', foreground='black')
        cal.pack(padx=10, pady=10)

        def get_selected_date():
            selected_date = cal.get_date()
            self.last_met_entry.delete(0, END)
            self.last_met_entry.insert(0, selected_date)
            top.destroy()

        Button(top, text="Select Date", command=get_selected_date).pack(pady=5)

    def open_calendar_birthday(self):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day', date_pattern='mm-dd-yyyy', foreground='black')
        cal.pack(padx=10, pady=10)

        def get_selected_date():
            selected_date = cal.get_date()
            self.birthday_entry.delete(0, END)
            self.birthday_entry.insert(0, selected_date)
            top.destroy()

        Button(top, text="Select Date", command=get_selected_date).pack(pady=5)
    
    def update_treeview(self, contact):
        self.tv.insert('','end',values=(contact.name, contact.birthday, contact.email, contact.last_met, contact.note, contact.category))


if __name__ == "__main__":
    root = Tk()
    tv = ttk.Treeview(root)
    app = AddContact(root, tv)
    root.mainloop()