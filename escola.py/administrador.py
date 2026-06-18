def listar_todos(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(aluno)


def relatorio(conexao):
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    quantidade = len(alunos)

    print("Quantidade de alunos:", quantidade)

    if quantidade > 0:
        cursor.execute("""
            SELECT AVG((nota1 + nota2) / 2)
            FROM aluno
        """)
        media_geral = cursor.fetchone()[0]

        print("Média geral:", round(media_geral, 2))
    else:
        print("Não há alunos cadastrados.")


def limpar_registros(conexao):
    cursor = conexao.cursor()

    confirmacao = input("Tem certeza que deseja apagar todos os registros? (S/N): ").strip().upper()

    if confirmacao == "S":
        cursor.execute("DELETE FROM aluno")
        conexao.commit()
        print("Registros apagados!")
    else:
        print("Operação cancelada.")


def menu_admin(conexao):

    while True:

        print("\n ADMINISTRADOR ")
        print("1 - Listar todos os alunos")
        print("2 - Relatório")
        print("3 - Limpar registros")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        # Validação de campo vazio
        if not opcao:
            print("Erro: Digite uma opção.")
            continue

        # Validação de opções permitidas
        if opcao not in ["0", "1", "2", "3"]:
            print("Erro: Opção inválida.")
            continue

        if opcao == "1":
            listar_todos(conexao)

        elif opcao == "2":
            relatorio(conexao)

        elif opcao == "3":
            limpar_registros(conexao)

        elif opcao == "0":
            print("Voltando...")
            break