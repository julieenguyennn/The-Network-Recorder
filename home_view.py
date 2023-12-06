import tkinter as tk
from tkinter import ttk
from reminder_view import Reminder  # Import the Reminder class from reminder_view module
# from add_contact_view import AddContact  # Import the AddContact class from add_contact_view module
import datetime
import Contacts

def open_add_contact():
    add_contact_window = tk.Toplevel(root)
    # add_contact_app = AddContact(add_contact_window)

def open_reminder():
    reminder_window = tk.Toplevel(root)
    reminder_app = Reminder(reminder_window)

def search():
    # Add code for searching here
    query = search_entry.get()
    print(f"Searching for: {query}")

# Create the main window
root = tk.Tk()
root.title("Home")

# Create and place the search bar
search_label = tk.Label(root, text="Search:")
search_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

search_entry = ttk.Entry(root, width=30)
search_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

search_button = ttk.Button(root, text="Search", command=search)
search_button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

# Create and place the buttons for Add Contact and Reminder
add_contact_button = ttk.Button(root, text="Add Contact", command=open_add_contact)
add_contact_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

reminder_button = ttk.Button(root, text="Reminder", command=open_reminder)
reminder_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

# Start the main event loop
root.mainloop()
