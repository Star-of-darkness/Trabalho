import mysql.connector
 
def create_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026"
    )
 
    return connection
def create_database(connection):
 
    cursor = connection.cursor()
 
    cursor.execute("""
        CREATE DATABASE IF NOT EXISTS sistema_escolar
    """)
 
    print("Banco criado!")
def use_database(connection):
 
    cursor = connection.cursor()
 
    cursor.execute("""
        USE sistema_escolar
    """)
def create_table(connection):
 
    cursor = connection.cursor()
 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno (
 
            id INT AUTO_INCREMENT PRIMARY KEY,
 
            nome VARCHAR(100) NOT NULL,
 
            idade INT NOT NULL,
 
            turma VARCHAR(50) NOT NULL,
 
            media FLOAT,
 
            situacao VARCHAR(20)
 
        )
    """)
 
    print("Tabela criada!")