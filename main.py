from App.logica_sistema import cadastrar_aluno, listar_alunos, detalhar_aluno, deletar_aluno, cadastrar_curso



comando = ""

while comando != "sair":
    comando = input(f"Escolha uma opção:\n"
                    f"1: Cadastrar alunos\n"
                    f"2: Listar alunos\n"
                    f"3: Detalhar aluno\n"
                    f"4: Deletar aluno\n"
                    f"5: Cadastrar curso\n"
                    f"Digite 'sair' para sair.")


    match comando:
        case "1":
            nome = input("\nInforme o nome do aluno: ")
            nascimento = input("Informe a data de nascimento do aluno:")
            curso = input("Informe o curso do aluno, se ele tiver, se não, deixe vazio")

            print(cadastrar_aluno(nome, nascimento, curso))

        case "2":
            print(listar_alunos())

        case "3":
            matricula = input("Informe a matricula do aluno: ")
            print (detalhar_aluno(matricula))

        case "4":
            matricula = input("Informa a matricula do aluno: ")
            print(deletar_aluno(matricula))

        case "5":
            nome_curso = input("Informe o nome do curso: ")
            duracao_curso = input("Informe a duração do curso: ")
            professor_curso = input("Informe o nome do professor: ")
            materias_curso = input("Informe as matérias do curso: ")

            print(cadastrar_curso(nome_curso, duracao_curso, professor_curso, materias_curso))


        case "sair":
            print("Saindo do sistema.")
