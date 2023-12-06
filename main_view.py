import datetime
import csv
from datetime import *
import Contacts


current_date = datetime.date.today()

# Create contact list
contact_list = []


# Add new contact
def addContact():
    name_input = input("Add name: ")
    birthday_input = input("Add birthday: ")
    email_input = input("Add email: ")
    date_input = input("Add date: ")
    contact_list.append(
        Contacts.Contact(name_input, datetime.strptime(birthday_input), email_input, datetime.strptime(date_input)))


# Export contact history as CSV
def exportList():
    file_path = 'contact_list.csv'
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Birthday", "Email", "Date"])
        for contact in contact_list:
            writer.writerow([contact.name, contact.birthday, contact.email, contact.last_contact])

addContact()
exportList() 