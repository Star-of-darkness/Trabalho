from dbConnection import *
from aluno import menu_aluno
from professor import menu_professor
from administrador import menu_admin
 
conexao = create_connection()
 
create_database(conexao)
use_database(conexao)
create_table(conexao)
 
while True:
 
    print("\n SISTEMA ESCOLAR ")
 
    print("1 - Aluno")
    print("2 - Professor")
    print("3 - Administrador")
    print("0 - Sair")
 
    opcao = input("Escolha uma opção: ")
 
    if opcao == "1":
        menu_aluno(conexao)
 
    elif opcao == "2":
        menu_professor(conexao)
 
    elif opcao == "3":
        menu_admin(conexao)
 
    elif opcao == "0":
        print("Sistema encerrado.")
        break
 
    else:
        print("Opção inválida.")