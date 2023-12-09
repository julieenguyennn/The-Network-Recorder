# Final Project - GUI
# Course Name: INF 452:Information Design V: Coding
# Institution: University of Toronto
# Instructor: Dr. Maher Elshakankiri
# Creator: Rae Zhang
# Created: 11/29/2023
# Last Modified:

from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk  # Import ttk module for Combobox
from Contacts import Contact
from datetime import datetime

class addContact:
    def __init__(self, root, name_entry, email_entry, last_met_entry, birthday_entry, category_combobox, note_entry):
        self.root = root
        self.root.title("New contact")

        Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        Label(root, text="Birthday:").grid(row=2, column=0, padx=5, pady=5)
        Label(root, text="Category:").grid(row=3, column=0, padx=5, pady=5)
        Label(root, text="Note:").grid(row=4, column=0, padx=5, pady=5)
        Label(root, text="Last met:").grid(row=5, column=0, padx=5, pady=5)  # Add label for Birthday

        self.name_entry = Entry(root)
        self.email_entry = Entry(root)
        self.last_met_entry = Entry(root)
        self.birthday_entry = Entry(root)
        self.category_combobox = Entry(root)
        self.note_entry = Entry(root)

        self.category_combobox = ttk.Combobox(root, values=["Work", "Personal", "Family", "Friends"])
        self.category_combobox.grid(row=3, column=1, padx=5, pady=5)

        calendar_icon = PhotoImage(file="./GUI graphics/calendar_icons.png")

        calendar_button_birthday = Button(root, command=self.open_calendar_birthday, image=calendar_icon, compound="left")
        calendar_button_birthday.grid(row=2, column=2, columnspan=5, padx=(0, 2), pady=5, sticky="w")

        calendar_button_last_met = Button(root, command=self.open_calendar_last_met, image=calendar_icon, compound="left")
        calendar_button_last_met.grid(row=5, column=2, columnspan=5, padx=(0, 2), pady=5, sticky="w")

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)
        self.birthday_entry.grid(row=2, column=1, padx=5, pady=5)
        self.note_entry.grid(row=4, column=1, padx=5, pady=5)
        self.last_met_entry.grid(row=5, column=1, padx=5, pady=5)

        self.contacts = []

        add_button = Button(root, text="Add Contact", command=self.add_contact)
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

        contact = Contact(name, datetime.strptime(birthday, "%m-%d-%Y"), email, datetime.strptime(last_met, "%m-%d-%Y"), note, category)

        self.contacts.append(contact)

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

if __name__ == "__main__":
    root = Tk()
    app = addContact(root)
    root.mainloop()
