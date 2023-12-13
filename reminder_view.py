# Faculty of Information
# University of Toronto
# BI program
# Course: INF452
# Instructor: Dr. Maher Elshakankiri
# Name: Rae Zhang, Julie Nguyen, Linrong Li
# Assignment: Final Project
# Date Create: December 1, 2023
# Last Modified: December 13, 2023
# Description: View reminder feature

# Set up
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import datetime
import Contacts
import Data_manager


def categorize_contacts(contact_list):
    # Categorize users based on the date of last contact
    one_year_contacts = []
    six_month_contacts = []
    three_month_contacts = []

    for contact in contact_list:
        months_difference = contact.last_contact_from_now()

        if months_difference >= 12:
            one_year_contacts.append(contact)
        elif months_difference >= 6:
            six_month_contacts.append(contact)
        elif months_difference >= 3:
            three_month_contacts.append(contact)

    return one_year_contacts, six_month_contacts, three_month_contacts


class Reminder(Toplevel):
    def __init__(self, root=None):
        super().__init__(root)  # initialize reminder view
        self.contact_list = Data_manager.load_contacts_from_csv()  # load data from the database
        self.create_ui()  # initialize the UI

    def create_ui(self):
        # create the UI / all the UI components
        self.tree = ttk.Treeview(self, columns=("Name", "Email", "Last Contact"))
        self.tree.heading("#0", text="Time since last contact")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Last Contact", text="Last Contact")

        one_year_contacts, six_month_contacts, three_month_contacts = categorize_contacts(self.contact_list)

        self.populate_tree("1 Year", one_year_contacts)
        self.populate_tree("6 Months", six_month_contacts)
        self.populate_tree("3 Months", three_month_contacts)

        self.tree.pack(expand=True, fill=BOTH)

    def populate_tree(self, category, contacts):
        # add an item to the view based on the category
        category_item = self.tree.insert("", "end", text=category)

        for contact in contacts:
            self.tree.insert(category_item, "end", values=(contact.name, contact.email, contact.last_met))

        self.tree.item(category_item, open=True)


if __name__ == "__main__":
    root = Tk()
    app = Reminder(root)
    root.mainloop()