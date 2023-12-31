# Faculty of Information
# University of Toronto
# BI program
# Course: INF452
# Instructor: Dr. Maher Elshakankiri
# Name: Rae Zhang, Julie Nguyen, Linrong Li
# Assignment: Final Project
# Date Create: December 1, 2023
# Last Modified: December 13, 2023
# Description: Store contact information 

# Set up and import packages
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk
import Contacts
import Data_manager
from datetime import datetime

class AddContact:
    def __init__(self, root, tv):
        # Initialize the GUI components
        self.root = root
        self.tv = tv
        self.root.title("New contact")

        # Load contacts from CSV
        self.contacts = Data_manager.load_contacts_from_csv()  # Load contacts from CSV

        # Load calendar icon
        self.calendar_icon = PhotoImage(file="GUI graphics/calendar_icons.png")

        # Create the "Add Contact" button
        self.add_button = Button(root, text="Add Contact", command=self.add_contact)

        # Set up the UI
        self.setup_ui()

    def setup_ui(self):
        frame = Frame(self.root)
        frame.pack(fill=X, padx=10, pady=5)

        # Create frame for name input
        name_frame = Frame(frame)
        name_frame.pack(fill=X, padx=5, pady=5)
        Label(name_frame, text="Name:").pack(side=LEFT)
        self.name_entry = Entry(name_frame)
        self.name_entry.pack(side=LEFT, padx=(18, 5), pady=5)

        # Create frame for email input
        email_frame = Frame(frame)
        email_frame.pack(fill=X, padx=5, pady=5)
        Label(email_frame, text="Email:").pack(side=LEFT)
        self.email_entry = Entry(email_frame)
        self.email_entry.pack(side=LEFT, padx=(20, 5), pady=5)

        # Create frame for birthday input
        birthday_frame = Frame(frame)
        birthday_frame.pack(fill=X, padx=5, pady=5)

        Label(birthday_frame, text="Birthday:").pack(side=LEFT)
        self.birthday_entry = Entry(birthday_frame)
        self.birthday_entry.pack(side=LEFT, padx=(3, 5), pady=5)

        self.calendar_button_birthday = Button(birthday_frame, command=self.open_calendar_birthday, image=self.calendar_icon, compound="left")
        self.calendar_button_birthday.pack(side=LEFT, padx=(0, 5), pady=5)

        # Create frame for category input
        category_frame = Frame(frame)
        category_frame.pack(fill=X, padx=5, pady=5)
        Label(category_frame, text="Category:").pack(side=LEFT)
        categories = ["Work", "Personal", "Family", "Friends"]
        self.category_combobox = ttk.Combobox(category_frame, values=categories,width=18)
        self.category_combobox.pack(side=LEFT, padx=(2, 5), pady=5)

        # Create frame for last met date input
        last_met_frame = Frame(frame)
        last_met_frame.pack(fill=X, padx=5, pady=5)
        Label(last_met_frame, text="Last met:").pack(side=LEFT)
        self.last_met_entry = Entry(last_met_frame)
        self.last_met_entry.pack(side=LEFT, padx=(3, 5), pady=5)

        self.calendar_button_last_met = Button(last_met_frame, command=self.open_calendar_last_met, image=self.calendar_icon)
        self.calendar_button_last_met.pack(side=LEFT, padx=(0, 5), pady=5)

        # Create frame for note input
        note_frame = Frame(frame)
        note_frame.pack(fill=X, padx=5, pady=5)
        Label(note_frame, text="Note:").pack(side=LEFT)
        self.note_entry = Text(note_frame, height=5, width=27)
        self.note_entry.pack(side=LEFT, fill='both', padx=(26, 3), pady=5)

        # Add Contact Button
        self.add_button.pack(fill=X, padx=5, pady=10)


    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        birthday = self.birthday_entry.get()
        category = self.category_combobox.get()
        last_met = self.last_met_entry.get()
        note = self.note_entry.get("1.0", "end-1c")

        contact_info = f"Name: {name}\nEmail: {email}\nBirthday: {birthday}\nCategory: {category}\nLast Met: {last_met}\nNote: {note}"

        # Custom contact information popup
        contact_popup = Toplevel()
        contact_popup.title("Confirm your entry")
        contact_popup.geometry("+100+100")  # Position the popup window to the right

        # Create a label to display contact_info
        contact_label = Label(contact_popup, text=contact_info, justify=LEFT)
        contact_label.pack(padx=20, pady=20, anchor='w')

        # Function to handle confirm button click
        def confirm_contact():
            # Add new contact to the contact list
            messagebox.showinfo("Contact Added", "New contact added successfully!")
            contact = Contacts.Contact(name, datetime.strptime(birthday, "%m-%d-%Y"), email, datetime.strptime(last_met, "%m-%d-%Y"), note, category)
            self.contacts.append(contact)
            Data_manager.save_contacts_to_csv(self.contacts)
            self.update_treeview(contact)
            contact_popup.destroy()

        # Function to handle cancel button click
        def cancel_adding_contact():
            contact_popup.destroy()  # Close the popup

        # Add Confirm and Cancel buttons
        confirm_button = Button(contact_popup, text="Confirm", command=confirm_contact)
        confirm_button.pack(side=RIGHT, padx=10, pady=10)

        cancel_button = Button(contact_popup, text="Cancel", command=cancel_adding_contact)
        cancel_button.pack(side=LEFT, padx=10, pady=10)

        self.root.destroy()

    # Function to open calendar for selecting last met date
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

    # Function to open calendar for selecting birthday date
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

    # Function to update the treeview with the new contact
    def update_treeview(self, contact):
        self.tv.insert('','end',values=(contact.name, contact.birthday, contact.email, contact.last_met, contact.note, contact.category))


if __name__ == "__main__":
    root = Tk()
    tv = ttk.Treeview(root)
    app = AddContact(root, tv)
    root.mainloop()
