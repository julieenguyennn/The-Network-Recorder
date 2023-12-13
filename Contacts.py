
from tkinter import *
from tkinter import filedialog
import csv
from datetime import *


class Contact:
    def __init__(self, name: str, birthday=None, email=None, last_met=None,
                 note=None, category=None):
        if name is None:
            raise ValueError("Name is required")
        
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
    
    @classmethod
    def from_dict(cls, data_dict):
        date_formats = ["%m-%d-%Y", "%m/%d/%Y"]  # List of possible date formats
        birthday = None
        last_met = None

        for format in date_formats:
            try:
                birthday_str = data_dict.get('Birthday')
                last_met_str = data_dict.get('Last Met')

                # Check if the date strings are not empty before conversion
                if birthday_str.strip() and last_met_str.strip():
                    birthday = datetime.strptime(birthday_str, format)
                    last_met = datetime.strptime(last_met_str, format)
                    break  # Stop trying formats once a successful parse occurs
            except (ValueError, TypeError):
                continue  # Continue to the next format if the current one fails

        return cls(
            name=data_dict['Name'],
            birthday=birthday,
            email=data_dict.get('Email'),
            last_met=last_met,
            note=data_dict.get('Note'),
            category=data_dict.get('Category')
        )