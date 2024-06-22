# Definição da classe Book que representa um livro
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, Price: {self.price}"
