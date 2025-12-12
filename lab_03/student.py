class Stud:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name} Surname: {self.surname}, Phone: {self.phone}, Email: {self.email}"