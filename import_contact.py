import csv
from tkinter import filedialog

class importContact:
    def __init__(self):
        self.headers = ['Name', 'Email', 'Birthday', 'Last Met', 'Note', 'Category']  
        self.contacts = []

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