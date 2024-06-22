# Gerenciamento das operações de banco de dados
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
from models.book import Book
from models.user import User

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    # Adiciona um livro ao banco de dados
    def add_book(self, book):
        self.cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (book.title, book.author, book.price))
        self.conn.commit()

    # Obtém todos os livros do banco de dados
    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    # Atualiza um livro no banco de dados
    def update_book(self, book_id, title, author, price):
        self.cursor.execute("UPDATE books SET title = ?, author = ?, price = ? WHERE id = ?", (title, author, price, book_id))
        self.conn.commit()

    # Remove um livro do banco de dados
    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()

    # Adiciona um usuário ao banco de dados
    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email))
        self.conn.commit()

    # Obtém todos os usuários do banco de dados
    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    # Atualiza um usuário no banco de dados
    def update_user(self, user_id, name, email):
        self.cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        self.conn.commit()

    # Remove um usuário do banco de dados
    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    # Fecha a conexão com o banco de dados
    def close(self):
        self.conn.close()

# Função para criar as tabelas no banco de dados
def create_tables():
    with sqlite3.connect('database/livraria.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            price REAL NOT NULL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE)''')
        conn.commit()

if __name__ == "__main__":
    create_tables()
