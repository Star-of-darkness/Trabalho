def listar_alunos(conexao):
    cursor = conexao.cursor()
 
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
 
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
 
    for aluno in alunos:
        print(aluno)
 
def registrar_aluno(conexao):
    nome = input("Nome do aluno: ").strip()

    if not nome:
        print("O nome não pode ficar vazio.")
        return

    try:
        idade = int(input("Idade: "))

        if idade <= 0:
            print("A idade deve ser maior que zero.")
            return

    except ValueError:
        print("Digite uma idade válida.")
        return

    turma = input("Turma: ").strip()

    if not turma:
        print("A turma não pode ficar vazia.")
        return

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO aluno (nome, idade, turma)
        VALUES (%s, %s, %s)
    """, (nome, idade, turma))

    conexao.commit()

    print("Aluno cadastrado com sucesso!")
 
def registrar_nota(conexao):
    id_aluno = input("ID do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
 
    media = (nota1 + nota2) / 2
 
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
 
    cursor = conexao.cursor()
 
    cursor.execute("""
        UPDATE aluno
        SET media = %s, situacao = %s
        WHERE id = %s
    """, (media, situacao, id_aluno))
 
    conexao.commit()
 
    print("Notas registradas com sucesso!")
 
 
def editar_aluno(conexao):
    id_aluno = input("ID do aluno: ")
 
    novo_nome = input("Novo nome: ")
    nova_idade = input("Nova idade: ")
    nova_turma = input("Nova turma: ")
 
    cursor = conexao.cursor()
 
    cursor.execute("""
        UPDATE aluno
        SET nome = %s,
            idade = %s,
            turma = %s
        WHERE id = %s
    """, (novo_nome, nova_idade, nova_turma, id_aluno))
 
    conexao.commit()
 
    print("Aluno atualizado!")
 
 
def remover_aluno(conexao):
    id_aluno = input("ID do aluno: ")
 
    cursor = conexao.cursor()
 
    cursor.execute(
        "DELETE FROM aluno WHERE id = %s",
        (id_aluno,)
    )
 
    conexao.commit()
 
    print("Aluno removido!")
 
 
def buscar_aluno(conexao):
    nome = input("Nome do aluno: ")
 
    cursor = conexao.cursor()
 
    cursor.execute(
        "SELECT * FROM aluno WHERE nome LIKE %s",
        (f"%{nome}%",)
    )
 
    alunos = cursor.fetchall()
 
    if not alunos:
        print("Aluno não encontrado.")
        return
 
    for aluno in alunos:
        print(aluno)


def menu_professor(conexao):
 
    while True:
 
        print("\n PROFESSOR ")
 
        print("1 - Listar alunos")
        print("2 - Registrar notas")
        print("3 - Editar aluno")
        print("4 - Remover aluno")
        print("5 - Buscar aluno")
        print("6 - Registrar aluno")
        print("0 - Voltar")
 
        opcao = input("Escolha: ")
 
        if opcao == "1":
            listar_alunos(conexao)
 
        elif opcao == "2":
            registrar_nota(conexao)

        elif opcao == "3":
            editar_aluno(conexao)
 
        elif opcao == "4":
            remover_aluno(conexao)
 
        elif opcao == "5":
            buscar_aluno(conexao)
    

        elif opcao == "6":
           registrar_aluno(conexao)

        elif opcao == "0":
            break
 
        else:
            print("Opção inválida.")
