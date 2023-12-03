import datetime
import csv

current_date = datetime.date.today()

# Create contact list
contact_list = [
    {
        'name': '',
        'birthday': '',
        'email': '',
        'date': ''
    }
]

# Add new contact
def addContact():
    name_input = input("Add name: ")
    birthday_input = input("Add birthday: ")
    email_input = input("Add email: ")
    date_input = input("Add date: ")
    new_contact = {'name': name_input, 'birthday': birthday_input, 'email': email_input, 'date': date_input}
    contact_list.append(new_contact)

# Export contact history as CSV
def exportList():
    file_path = 'contact_list.csv'
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'birthday', 'email', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contact_list)

addContact()
exportList()