import csv
from tkinter import filedialog, messagebox
import data_manager
from contacts import *

class importContact:
    def __init__(self):
        self.headers = ['Name', 'Birthday', 'Email', 'Last Met', 'Note', 'Category']  
        self.contacts = []

    # Create a function to check the CSV file before import
    def check_csv_headers(self, file_name):
        try:
            with open(file_name, 'r') as file:
                reader = csv.DictReader(file)
                file_headers = reader.fieldnames
                return file_headers == self.headers
        except FileNotFoundError:
            return False

    # Create a function to import CSV file into the program
    def import_contacts(self, update_callback=None):
        file_name = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_name:
            headers_match = self.check_csv_headers(file_name)
            if headers_match:
                try:
                    with open(file_name, 'r') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            contact = contact.from_dict(row)  # Create a Contact object from each row
                            self.contacts.append(contact)
                        messagebox.showinfo(message="Contacts imported successfully.")
                        data_manager.save_contacts_to_csv(self.contacts)
                        if update_callback:
                            update_callback()  # Call the provided callback to update the Treeview
                except FileNotFoundError:
                    messagebox.showerror(message="File not found. Please provide a valid file name.")
            else:
                messagebox.showwarning(message="Headers in the CSV file do not match the expected headers.")