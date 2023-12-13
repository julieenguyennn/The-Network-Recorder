# Faculty of Information
# University of Toronto
# BI program
# Course: INF452
# Instructor: Dr. Maher Elshakankiri
# Name: Rae Zhang, Julie Nguyen, Linrong Li
# Assignment: Final Project
# Date Create: December 1, 2023
# Last Modified: December 13, 2023
# Description: Import contact feature

# Set up and import packages
import csv
from tkinter import filedialog, messagebox
import Data_manager
from Contacts import *


# Create class
class importContact:
    # Initiation
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
            headers_match = self.check_csv_headers(file_name) # Check CSV headers
            if headers_match:
                try:
                    with open(file_name, 'r') as file:
                        reader = csv.DictReader(file)
                        # Read each row in the CSV file and creates a Contact object with data from each row
                        for row in reader:
                            contact = Contact(row['Name'], row['Birthday'], row['Email'], row['Last Met'], row['Note'], row['Category'])
                            # Appends each newly created Contact object to self.contacts
                            self.contacts.append(contact)
                        messagebox.showinfo(message="Contacts imported successfully.")
                        # Save the imported contacts to a CSV file
                        Data_manager.save_contacts_to_csv(self.contacts)
                        if update_callback:
                            update_callback()  # Call the provided callback to update the Treeview
                except FileNotFoundError as e:
                    messagebox.showerror(message="File not found. Please provide a valid file name.")
            else:
                messagebox.showwarning(message="Headers in the CSV file do not match the expected headers.")