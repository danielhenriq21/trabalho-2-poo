# Definição da classe User que herda de Person
from models.person import Person

class User(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_details(self):
        return f"User: {self.name}, Email: {self.email}"
