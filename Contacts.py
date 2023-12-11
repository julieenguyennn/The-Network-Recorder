import datetime
from tkinter import *
from tkinter import filedialog
import csv
from datetime import datetime

class Contact:
    def __init__(self, name: str, birthday: datetime, email: str, last_met: datetime,
                 note: str, category: str):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.last_met = last_met
        self.note = note
        self.category = category
        
    def last_contact_from_now(self):
        current_date = datetime.date.today()
        difference = abs(current_date - self.last_met)
        # Calculate the difference in months
        months_difference = difference.days // 30
        return months_difference

class contactManager:
    def __init__(self):
        self.contacts = []  # List to store contacts
        self.headers = ["Name", "Birthday", "Email", "Note", "Last Contact"]

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_contacts_to_csv(self, filename='contacts.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)
            for contact in self.contacts:
                writer.writerow([
                    contact.name,
                    contact.birthday.strftime("%m-%d-%Y"),
                    contact.email,
                    contact.last_met.strftime("%m-%d-%Y"),
                    contact.note,
                    contact.category
                ])
    
    def load_contacts_from_csv(self, filename='contacts.csv'):
        self.contacts = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            try:
                headers = next(reader)  # Skip header row
                # Process the rest of the rows
                for row in reader:
                    # Process each row data
                    pass  # Your code to process rows goes here
            except StopIteration:
                print("CSV file is empty or contains only headers")
            for row in reader:
                name, birthday, email, last_met, note, category = row
                try:
                    birthday = datetime.strptime(birthday, "%m-%d-%Y")
                    last_met = datetime.strptime(last_met, "%m-%d-%Y")
                except ValueError as e:
                    print(f"Error converting dates in CSV: {e}")
                    # Handle the error as needed, e.g., log the error or skip this row
                    continue  # Skip to the next row if there's an error with dates
                contact = Contact(name, birthday, email, last_met, note, category)
                self.contacts.append(contact)