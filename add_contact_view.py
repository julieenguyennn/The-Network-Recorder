# Final Project - GUI
# Course Name: INF 452:Information Design V: Coding
# Institution: University of Toronto
# Instructor: Dr. Maher Elshakankiri
# Creator: Rae Zhang
# Created: 11/29/2023
# Last Modified:

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import *
import Contacts
import Data_manager

class addContact(Toplevel):
    def __init__(self, root=None, tv=None):
        super().__init__(root)
        self.root = root
        self.tv = tv
        self.title("Add Contact")
        self.geometry("400x500")

        Label(self, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        Label(self, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        Label(self, text="Birthday:").grid(row=2, column=0, padx=5, pady=5)
        Label(self, text="Category:").grid(row=3, column=0, padx=5, pady=5)
        Label(self, text="Note:").grid(row=4, column=0, padx=5, pady=5)
        Label(self, text="Last met:").grid(row=5, column=0, padx=5, pady=5)

        self.name_entry = Entry(self)
        self.email_entry = Entry(self)
        self.birthday_entry = Entry(self)
        self.note_entry = Entry(self)
        self.last_met_entry = Entry(self)
        self.category_combobox = ttk.Combobox(self, values=["Work", "Personal", "Family", "Friends"])

        self.category_combobox.grid(row=3, column=1, padx=5, pady=5)

        calendar_icon = PhotoImage(file="./GUI graphics/calendar_icons.png")

        calendar_button_birthday = Button(self, command=self.open_calendar_birthday, image=calendar_icon, compound="left")
        calendar_button_birthday.grid(row=2, column=2, padx=(0, 2), pady=5, sticky="w")

        calendar_button_last_met = Button(self, command=self.open_calendar_last_met, image=calendar_icon, compound="left")
        calendar_button_last_met.grid(row=5, column=2, padx=(0, 2), pady=5, sticky="w")

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)
        self.birthday_entry.grid(row=2, column=1, padx=5, pady=5)
        self.note_entry.grid(row=4, column=1, padx=5, pady=5)
        self.last_met_entry.grid(row=5, column=1, padx=5, pady=5)

        self.contacts = Data_manager.load_contacts_from_csv()

        add_button = Button(self, text="Add Contact", command=self.add_contact)
        add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        last_met = self.last_met_entry.get()
        birthday = self.birthday_entry.get()
        category = self.category_combobox.get()
        note = self.note_entry.get()

        contact_info = f"Name: {name}\nEmail: {email}\nLast Met: {last_met}\nBirthday: {birthday}\nCategory: {category}\nNote: {note}"
        messagebox.showinfo("Confirm your entry", contact_info)

        # Assuming the Contact class is defined in "Contacts.py"
        contact = Contacts.Contact(name, datetime.strptime(birthday, "%m-%d-%Y"), email, datetime.strptime(last_met, "%m-%d-%Y"), note, category)
        self.contacts.append(contact)
        Data_manager.save_contacts_to_csv(self.contacts)
        self.update_treeview(contact)



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
        top = Toplevel(self)
        cal = Calendar(top, selectmode='day', date_pattern='mm-dd-yyyy', foreground='black')
        cal.pack(padx=10, pady=10)

        def get_selected_date():
            selected_date = cal.get_date()
            self.last_met_entry.delete(0, END)
            self.last_met_entry.insert(0, selected_date)
            top.destroy()

        Button(top, text="Select Date", command=get_selected_date).pack(pady=5)

    def update_treeview(self, contact):
        self.tv.insert('', 'end', values=(contact.name, contact.birthday.strftime("%m-%d-%Y"), contact.email, contact.last_met.strftime("%m-%d-%Y"), contact.note, contact.category))


if __name__ == "__main__":
    root = Tk()
    app = addContact(root)
    root.mainloop()