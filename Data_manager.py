import csv
from datetime import datetime
from Contacts import *


def save_contacts_to_csv(contact_list, filename='contacts.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Birthday", "Email", "Last Met", "Note", "Category"])
        for contact in contact_list:
            last_met_formatted = contact.last_met.strftime("%m-%d-%Y") if contact.last_met is not None else ""
            writer.writerow([
                contact.name,
                contact.birthday.strftime("%m-%d-%Y") if contact.birthday is not None else "",
                contact.email,
                last_met_formatted,  # Handling last_met when it's None
                contact.note,
                contact.category
            ])

def load_contacts_from_csv(filename='contacts.csv'):
    contacts = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        try:
            headers = next(reader)  # Skip header row
            # Process the rest of the rows
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
                contacts.append(contact)
        except StopIteration:
            print("CSV file is empty or contains only headers")
    return contacts
