def listar_todos(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    for aluno in alunos:
        print(aluno)

def relatorio(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    print("Quantidade de alunos:", len(alunos))


def limpar_registros(conexao):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM aluno")
    conexao.commit()

    print("Registros apagados!")


def menu_admin(conexao):
 
    while True:
 
        print("\n ADMINISTRADOR ")
 
        print("1 - Listar todos os alunos")
        print("2 - Relatório")
        print("3 - Limpar registros")
        print("0 - Voltar")
 
        opcao = input("Escolha: ")
 
        if opcao == "1":
            listar_todos(conexao)
 
        elif opcao == "2":
            relatorio(conexao)
 
        elif opcao == "3":
            limpar_registros(conexao)
 
        elif opcao == "0":
            break
 
        else:
            print("Opção inválida.")