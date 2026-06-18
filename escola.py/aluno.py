def menu_aluno(conexao):    
    id_aluno = input("Digite o seu ID de aluno: ")
   
    cursor = conexao.cursor()
   
 
    cursor.execute("SELECT nome, idade, turma, media FROM aluno WHERE id = %s", (id_aluno,))
    aluno = cursor.fetchone()
   
    if not aluno:
        print("Aluno não encontrado.")
        return
 
   
    dados_alunos = [{
        'Nome': aluno[0],
        'Idade': aluno[1],
        'Turma': aluno[2],
        'Nota Final': aluno[3] if aluno[3] is not None else "Sem nota"
    }]
 
    while True:
        print("\n ALUNO ")
        print("1 - Visualizar Boletim")
        print("0 - Voltar")
       
        opcao = input("Escolha: ")
       
        if opcao == "1":
            print("\n")
            print(f"{'Nome':<10} | {'Idade':<5} | {'Turma':<5} | {'Nota Final':<10}")
            print("-" * 42)
 
            for item in dados_alunos:
                print(f"{item['Nome']:<10} | {item['Idade']:<5} | {item['Turma']:<5} | {item['Nota Final']:<10}")
       
        elif opcao == "0":
            break
           
        else:
            print("Opção inválida.")
