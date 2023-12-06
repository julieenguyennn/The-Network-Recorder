import datetime
from tkinter import *
import csv

class Contact:
    def __init__(self, name: str, birthday: datetime, email: str, last_contact: datetime,
                 note: str, category: str):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.last_contact = last_contact
        self.note = note
        self.category = category

    def last_contact_from_now(self):
        current_date = datetime.date.today()
        difference = abs(current_date - self.last_contact)
        # Calculate the difference in months
        months_difference = difference.days // 30
        return months_difference

    def contains_partial(self, keyword):
        # Check if the keyword is present in the name
        return keyword.lower() in self.name.lower()

class addContact:
    def addContact(contact_list):
        name_input = input("Add name: ")
        birthday_input = input("Add birthday: ")
        email_input = input("Add email: ")
        date_input = input("Add date: ")
        contact_list.append(name_input, datetime.strptime(birthday_input), email_input, datetime.strptime(date_input))
        return contact_list

class exportList:
    # Export contact history as CSV
    def exportList(contact_list):
        file_path = 'contact_list.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Birthday", "Email", "Date"])
            for contact in contact_list:
                writer.writerow([contact.name, contact.birthday, contact.email, contact.last_contact])

class displayContact:
    # Display contact
    def displayContact(self, root, contact_list):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, contact_list[i][j])

        total_rows = len(contact_list)
        total_columns = len(contact_list[0])

# create root window
root = Tk()
Contact.addContact(contact_list)
t = displayContact.displayContact(root, contact_list)
root.mainloop()