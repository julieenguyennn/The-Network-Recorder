import tkinter as tk
from tkinter import ttk
import datetime
import Contacts


def categorize_contacts(contact_list):
    one_year_contacts = []
    six_month_contacts = []
    three_month_contacts = []

    for contact in contact_list:
        months_difference = contact.last_contact_from_now()

        if months_difference > 12:
            one_year_contacts.append(contact)
        elif months_difference > 6:
            six_month_contacts.append(contact)
        elif months_difference > 3:
            three_month_contacts.append(contact)

    return one_year_contacts, six_month_contacts, three_month_contacts


class Reminder:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder")

        self.contact_list = [
            Contacts.Contact("John Doe", datetime.date(1990, 1, 1), "john@example.com",
                             datetime.date(2022, 1, 1), "", ""),
            Contacts.Contact("Jane Smith", datetime.date(1985, 5, 15), "jane@example.com",
                             datetime.date(2022, 5, 1), "", ""),
            Contacts.Contact("Bob Johnson", datetime.date(1995, 8, 10), "bob@example.com",
                             datetime.date(2023, 2, 1), "", ""),
            # Add more contacts as needed
        ] # TODO: Hard-coded example for now. Should get it from read the csv file

        self.create_ui()

    def create_ui(self):
        self.tree = ttk.Treeview(self.root, columns=("Name", "Email", "Last Contact"))
        self.tree.heading("#0", text="Time Since Last Contact")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Last Contact", text="Last Contact")

        one_year_contacts, six_month_contacts, three_month_contacts = categorize_contacts(self.contact_list)

        self.populate_tree("1 Year", one_year_contacts)
        self.populate_tree("6 Months", six_month_contacts)
        self.populate_tree("3 Months", three_month_contacts)

        self.tree.pack(expand=True, fill=tk.BOTH)

    def populate_tree(self, category, contacts):
        category_item = self.tree.insert("", "end", text=category)

        for contact in contacts:
            self.tree.insert(category_item, "end", values=(contact.name, contact.email, contact.last_contact))

        self.tree.item(category_item, open=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = Reminder(root)
    root.mainloop()
