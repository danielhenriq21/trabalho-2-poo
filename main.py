# Interface do usuário para interagir com o sistema de livraria
from models.book import Book
from models.user import User
from models.database import Database

def menu():
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livros")
    print("3 - Atualizar Livro")
    print("4 - Excluir Livro")
    print("5 - Cadastrar Usuário")
    print("6 - Consultar Usuários")
    print("7 - Atualizar Usuário")
    print("8 - Excluir Usuário")
    print("9 - Sair")

def main():
    db = Database('database/livraria.db')
    while True:
        menu()
        choice = input("Escolha uma opção: ")
        try:
            if choice == '1':
                title = input("Título do Livro: ")
                author = input("Autor do Livro: ")
                price = float(input("Preço do Livro: "))
                book = Book(title, author, price)
                db.add_book(book)
                print("Livro cadastrado com sucesso!")
            elif choice == '2':
                books = db.get_books()
                for book in books:
                    print(book)
            elif choice == '3':
                book_id = int(input("ID do Livro a ser atualizado: "))
                title = input("Novo Título: ")
                author = input("Novo Autor: ")
                price = float(input("Novo Preço: "))
                db.update_book(book_id, title, author, price)
                print("Livro atualizado com sucesso!")
            elif choice == '4':
                book_id = int(input("ID do Livro a ser excluído: "))
                db.delete_book(book_id)
                print("Livro excluído com sucesso!")
            elif choice == '5':
                name = input("Nome do Usuário: ")
                email = input("Email do Usuário: ")
                user = User(name, email)
                db.add_user(user)
                print("Usuário cadastrado com sucesso!")
            elif choice == '6':
                users = db.get_users()
                for user in users:
                    print(user)
            elif choice == '7':
                user_id = int(input("ID do Usuário a ser atualizado: "))
                name = input("Novo Nome: ")
                email = input("Novo Email: ")
                db.update_user(user_id, name, email)
                print("Usuário atualizado com sucesso!")
            elif choice == '8':
                user_id = int(input("ID do Usuário a ser excluído: "))
                db.delete_user(user_id)
                print("Usuário excluído com sucesso!")
            elif choice == '9':
                db.close()
                break
            else:
                print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
