import datetime
from tkinter import *
from tkinter import filedialog
import csv

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
        difference = abs(current_date - self.last_contact)
        # Calculate the difference in months
        months_difference = difference.days // 30
        return months_difference

class contactManager:
    def __init__(self):
        self.contacts = []  # List to store contacts
        self.headers = ["Name", "Birthday", "Email", "Note", "Last Contact"]

    def check_csv_headers(self, file_name):
        try:
            with open(file_name, 'r') as file:
                reader = csv.DictReader(file)
                file_headers = reader.fieldnames
                return file_headers == self.headers
        except FileNotFoundError:
            return False

    def import_contacts(self):
        file_name = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_name:
            headers_match = self.check_csv_headers(file_name)
            if headers_match:
                try:
                    with open(file_name, 'r') as file:
                        reader = csv.DictReader(file)
                        imported_contacts = list(reader)
                        self.contacts.extend(imported_contacts)
                        print("Contacts imported successfully.")
                except FileNotFoundError:
                    print("File not found. Please provide a valid file name.")
            else:
                print("Headers in the CSV file do not match the expected headers.")

    def save_list(self):
        file_path = 'contact_list.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.headers)
            for contact in self.contacts:
                writer.writerow([contact.get(field, "") for field in self.headers])

    def display_contacts_gui(self):
        root = Tk()
        root.title("Contact List")

        total_rows = len(self.contacts) + 1  # Add one row for header
        total_columns = len(self.headers)

        # Display header labels
        for i, header in enumerate(self.headers):
            label = Label(root, text=header, font=('Arial', 12, 'bold'))
            label.grid(row=0, column=i, padx=5, pady=5)

        # Display contact information
        for i, contact in enumerate(self.contacts, start=1):
            for j, field in enumerate(self.headers):
                label = Label(root, text=contact.get(field, ""), font=('Arial', 12))
                label.grid(row=i, column=j, padx=5, pady=5)

        root.mainloop()