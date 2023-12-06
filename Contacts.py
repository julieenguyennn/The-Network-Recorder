import datetime


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
