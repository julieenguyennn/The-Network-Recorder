from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk
import contacts
import data_manager
from datetime import datetime


class AddContact:
    def __init__(self, root, tv):
        self.root = root
        self.tv = tv
        self.root.title("New contact")

        self.contacts = data_manager.load_contacts_from_csv()  # Load contacts from CSV

        self.name_entry = Entry(root)
        self.email_entry = Entry(root)
        self.birthday_entry = Entry(root)
        self.last_met_entry = Entry(root)
        self.note_entry = Text(root, height=5, width=30)

        categories = ["Work", "Personal", "Family", "Friends"]
        self.category_combobox = ttk.Combobox(root, values=categories)

        self.calendar_icon = PhotoImage(file="GUI graphics/calendar_icons.png")

        self.calendar_button_birthday = Button(root, command=self.open_calendar_birthday, image=self.calendar_icon, compound="left")
        self.calendar_button_last_met = Button(root, command=self.open_calendar_last_met, image=self.calendar_icon, compound="left")
        self.add_button = Button(root, text="Add Contact", command=self.add_contact)

        self.setup_ui()

    def setup_ui(self):
        Label(self.root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        Label(self.root, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        Label(self.root, text="Birthday:").grid(row=2, column=0, padx=5, pady=5)
        Label(self.root, text="Category:").grid(row=3, column=0, padx=5, pady=5)
        Label(self.root, text="Last met:").grid(row=4, column=0, padx=5, pady=5)
        Label(self.root, text="Note:").grid(row=5, column=0, padx=5, pady=5)

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)
        self.birthday_entry.grid(row=2, column=1, padx=5, pady=5)
        self.category_combobox.grid(row=3, column=1, padx=5, pady=5)
        self.last_met_entry.grid(row=4, column=1, padx=5, pady=5)
        self.note_entry.grid(row=5, column=1, padx=5, pady=5)

        self.calendar_button_birthday.grid(row=2, column=2, columnspan=5, padx=(0, 2), pady=5, sticky="w")
        self.calendar_button_last_met.grid(row=4, column=2, columnspan=5, padx=(0, 2), pady=5, sticky="w")
        self.add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        birthday = self.birthday_entry.get()
        category = self.category_combobox.get()
        last_met = self.last_met_entry.get()
        note = self.note_entry.get("1.0", "end-1c")

        contact_info = f"Name: {name}\nEmail: {email}\nLast Met: {last_met}\nBirthday: {birthday}\nCategory: {category}\nNote: {note}"
        messagebox.showinfo("Confirm your entry", contact_info)

        # Assuming the Contact class is defined in "Contacts.py"
        contact = contacts.Contact(name, datetime.strptime(birthday, "%m-%d-%Y"), email, datetime.strptime(last_met, "%m-%d-%Y"), note, category)
        self.contacts.append(contact)
        data_manager.save_contacts_to_csv(self.contacts)
        self.update_treeview(contact)

    def open_calendar_birthday(self):
        top = Toplevel(self)
        cal = Calendar(top, selectmode='day', date_pattern='mm-dd-yyyy', foreground='black')
        cal.pack(padx=10, pady=10)

        def get_selected_date():
            selected_date = cal.get_date()
            self.birthday_entry.delete(0, END)
            self.birthday_entry.insert(0, selected_date)
            top.destroy()

        Button(top, text="Select Date", command=get_selected_date).pack(pady=5)

    def open_calendar_last_met(self):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day', date_pattern='mm-dd-yyyy', foreground='black')
        cal.pack(padx=10, pady=10)

        def get_selected_date():
            selected_date = cal.get_date()
            self.last_met_entry.delete(0, END)
            self.last_met_entry.insert(0, selected_date)
            top.destroy()

        Button(top, text="Select Date", command=get_selected_date).pack(pady=5)

    def open_calendar_birthday(self):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day', date_pattern='mm-dd-yyyy', foreground='black')
        cal.pack(padx=10, pady=10)

        def get_selected_date():
            selected_date = cal.get_date()
            self.birthday_entry.delete(0, END)
            self.birthday_entry.insert(0, selected_date)
            top.destroy()

        Button(top, text="Select Date", command=get_selected_date).pack(pady=5)

if __name__ == "__main__":
    root = Tk()
    app = AddContact(root, tv)
    root.mainloop()
