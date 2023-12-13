# Faculty of Information
# University of Toronto
# BI program
# Course: INF452
# Instructor: Dr. Maher Elshakankiri
# Name: Rae Zhang, Julie Nguyen, Linrong Li
# Assignment: Final Project
# Date Create: December 1, 2023
# Last Modified: December 13, 2023
# Description: Store contact information

# Set up and import packages
from tkinter import *
from tkinter import filedialog
import csv
from datetime import *

# Set up class
class Contact:
    # Initiation
    def __init__(self, name, birthday, email, last_met, note, category):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.last_met = last_met
        self.note = note
        self.category = category

    # Create a function to calculate month difference between the current date and last contact date
    def last_contact_from_now(self):
        current_date = datetime.now().date()
        difference = abs(current_date - self.last_met.date())
        # Calculate the difference in months
        months_difference = difference.days // 30
        return months_difference

    def contains_partial(self, keyword):
        # checks if a lowercase version of the provided keyword is a substring of the lowercase version of the
        # object's name for the search function
        return keyword.lower() in self.name.lower()