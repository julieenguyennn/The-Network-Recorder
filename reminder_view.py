from tkinter import *
from tkinter.ttk import *
import datetime
import contacts
import data_manager


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


class Reminder(Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.contact_list = data_manager.load_contacts_from_csv()
        self.create_ui()

    def create_ui(self):
        self.tree = Treeview(columns=("Name", "Email", "Last Contact"))
        self.tree.heading("#0", text="Time since last contact")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Last Contact", text="Last Contact")
        print(self.contact_list)

        one_year_contacts, six_month_contacts, three_month_contacts = categorize_contacts(self.contact_list)

        self.populate_tree("1 Year", one_year_contacts)
        self.populate_tree("6 Months", six_month_contacts)
        self.populate_tree("3 Months", three_month_contacts)

        self.tree.pack(expand=True, fill=BOTH)

    def populate_tree(self, category, contacts):
        category_item = self.tree.insert("", "end", text=category)

        for contact in contacts:
            self.tree.insert(category_item, "end", values=(contact.name, contact.email, contact.last_met))

        self.tree.item(category_item, open=True)

if __name__ == "__main__":
    root = Tk()
    app = Reminder(root)
    root.mainloop()