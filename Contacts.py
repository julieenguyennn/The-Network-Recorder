
from tkinter import *
from tkinter import filedialog
import csv
from datetime import *


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
        current_date = datetime.now().date()
        difference = abs(current_date - self.last_met.date())
        # Calculate the difference in months
        months_difference = difference.days // 30
        return months_difference

    def contains_partial(self, keyword):
        return keyword.lower() in self.name.lower()
