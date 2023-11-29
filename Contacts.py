import datetime


class Contact:
    def __init__(self, name: str, birthday: datetime, email: str, last_contact: datetime):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.last_contact = last_contact
