# Final Project - GUI
#
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
import Contacts
from datetime import datetime


def add_contact():
    name = name_entry.get()
    email = email_entry.get()
    last_met = last_met_entry.get()
    birthday = birthday_entry.get()  # Get the selected birthday
    category = category_combobox.get()
    note = note_entry.get()

    contact_info = f"Name: {name}\nEmail: {email}\nLast Met: {last_met}\nBirthday: {birthday}\nCategory: {category}\nNote: {note}"
    messagebox.showinfo("Confirm your entry", contact_info)

    return Contacts.Contact(name, datetime.strptime(birthday, "%m-%d-%Y"),
                            email, datetime.strptime(last_met, "%m-%d-%Y"),
                            note, category)


def open_calendar(entry_widget):
    top = Toplevel(root)
    cal = Calendar(top, selectmode='day', date_pattern='mm-dd-yyyy', foreground='black')
    cal.pack(padx=10, pady=10)

    def get_selected_date():
        selected_date = cal.get_date()
        entry_widget.delete(0, END)
        entry_widget.insert(0, selected_date)
        top.destroy()

    Button(top, text="Select Date", command=get_selected_date).pack(pady=5)


root = Tk()
root.title("New contact")

Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5)
Label(root, text="Birthday:").grid(row=2, column=0, padx=5, pady=5)
Label(root, text="Category:").grid(row=3, column=0, padx=5, pady=5)
Label(root, text="Note:").grid(row=4, column=0, padx=5, pady=5)
Label(root, text="Last met:").grid(row=5, column=0, padx=5, pady=5)  # Add label for Birthday
birthday_entry = Entry(root)
birthday_entry.grid(row=5, column=1, padx=5, pady=5)

name_entry = Entry(root)
email_entry = Entry(root)
last_met_entry = Entry(root)
note_entry = Entry(root)

# Dropdown list for Category
categories = ["Work", "Personal", "Family", "Friends"]  # Define categories
category_combobox = ttk.Combobox(root, values=categories)
category_combobox.grid(row=3, column=1, padx=5, pady=5)

# Load the calendar icon
calendar_icon = PhotoImage(file="./GUI graphics/calendar_icons.png")  # Replace "calendar_icon.png" with your image file

# Button to open calendar for date selection with calendar icon
calendar_button = Button(root, command=open_calendar, image=calendar_icon, compound="left")
add_button = Button(root, text="Add Contact", command=add_contact)
calendar_button_last_met = Button(root, command=lambda: open_calendar(last_met_entry), image=calendar_icon,
                                  compound="left")
calendar_button_last_met.grid(row=2, column=2, columnspan=5, padx=(0, 2), pady=5, sticky="w")

calendar_button_birthday = Button(root, command=lambda: open_calendar(birthday_entry), image=calendar_icon,
                                  compound="left")
calendar_button_birthday.grid(row=5, column=2, columnspan=5, padx=(0, 2), pady=5, sticky="w")

# Arrange the position of grid
name_entry.grid(row=0, column=1, padx=5, pady=5)
email_entry.grid(row=1, column=1, padx=5, pady=5)
birthday_entry.grid(row=2, column=1, padx=5, pady=5)
calendar_button.grid(row=2, column=2, columnspan=5, padx=(0, 2), pady=5, sticky="w")
note_entry.grid(row=4, column=1, padx=5, pady=5)
add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)
last_met_entry.grid(row=5, column=1, padx=5, pady=5)
root.mainloop()
