# Faculty of Information
# University of Toronto
# BI program
# Course: INF452
# Instructor: Dr. Maher Elshakankiri
# Name: Rae Zhang, Julie Nguyen, Linrong Li
# Assignment: Final Project
# Date Create: December 1, 2023
# Last Modified: December 13, 2023
# Description: Handle save input to a database (CSV file) and load back to the program

# Set up and import packages and files
import csv
from datetime import datetime
from Contacts import *

# Create a function to save input contact information into contacts.csv file
def save_contacts_to_csv(contact_list, filename='contacts.csv'):
    existing_contacts = load_contacts_from_csv(filename)  # Load existing contacts from the file
    all_contacts = existing_contacts + contact_list  # Merge existing contacts with the new ones

    # Open contacts.csv
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Birthday", "Email", "Last Met", "Note", "Category"])
        for contact in all_contacts:
            if isinstance(contact.birthday, str):
                try:
                    # Convert string to datetime object using the appropriate format
                    contact.birthday = datetime.strptime(contact.birthday, "%m/%d/%Y")
                except ValueError as e:
                    continue

            if isinstance(contact.last_met, str):
                try:
                    # Convert string to datetime object using the appropriate format
                    contact.last_met = datetime.strptime(contact.last_met, "%m/%d/%Y")
                except ValueError as e:
                    continue
            
            # Write everything to the contact object
            writer.writerow([
                contact.name,
                contact.birthday.strftime("%m-%d-%Y") if contact.birthday is not None else "",
                contact.email,
                contact.last_met.strftime("%m-%d-%Y") if contact.last_met is not None else "",
                contact.note,
                contact.category
            ])

# Create a function to load previously-added contact whenever the file reopens
def load_contacts_from_csv(filename='contacts.csv'):
    contacts = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        try:
            headers = next(reader)  # Skip header row
            # Read the rows and add it to the contacts list
            for row in reader:
                name, birthday, email, last_met, note, category = row
                # Check for dates format
                try:
                    birthday = datetime.strptime(birthday, "%m-%d-%Y")
                    last_met = datetime.strptime(last_met, "%m-%d-%Y")
                except ValueError as e:
                    continue
                contact = Contact(name, birthday, email, last_met, note, category)
                contacts.append(contact)
        except StopIteration:
            print("CSV file is empty or contains only headers")
    return contacts
