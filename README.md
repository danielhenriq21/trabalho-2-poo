# Sistema de Livraria em Python - CRUD com SQLite

Este é um sistema de livraria desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos (POO) como Abstração, Encapsulamento, Herança e Polimorfismo. O sistema permite realizar operações CRUD (Create, Read, Update, Delete) para livros e usuários, utilizando um banco de dados SQLite.

## Requisitos

- Python 3.x
- Visual Studio Code

## Instalação

### Passo 1: Instalar Python

Baixe e instale a última versão do Python a partir do [site oficial](https://www.python.org/downloads/). Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

### Passo 2: Instalar Extensões Necessárias no VS Code

- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- SQLite (alexcvzz.vscode-sqlite)

## Execução (No terminal)

### Passo 1: Ativar ambiente virtual

- Windows
```
.\venv\Scripts\activate
```
- macOS/Linux:
```
source venv/bin/activate
```
### Passo 2: Navegar para diretório do projeto
```
.../livraria-poo-py
```
### Passo 3: Criar o banco de dados
```
python models/database.py
```
### Passo 4: Executar o sistema
```
python main.py
```
