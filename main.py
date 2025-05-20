from App.logica_sistema import adicionar_aluno_curso, cadastrar_aluno, deletar_curso, detalhar_curso, listar_alunos, detalhar_aluno, deletar_aluno, cadastrar_curso, listar_curso



comando = ""

while comando != "sair":
    comando = input(f"-------------------MENU-------------------\n"
                    f"1: Cadastrar alunos\n"
                    f"2: Listar alunos\n"
                    f"3: Detalhar aluno\n"
                    f"4: Deletar aluno\n"
                    f"5: Cadastrar curso\n"
                    f"6: Listar cursos\n"
                    f"7: Detalhar curso\n"
                    f"8: Deletar curso\n"
                    f"9: Adicionar aluno ao curso\n"
                    f"Digite 'sair' para sair.\n"
                    f"Escolha uma opção: ")
    if comando not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "sair"]:
        print("Opção inválida. Tente novamente.")
        continue


    match comando:
        case "1":
            nome = input("\nInforme o nome do aluno: ")
            nascimento = input("Informe a data de nascimento do aluno:")

            print(cadastrar_aluno(nome, nascimento))

        case "2":
            print(listar_alunos())
            if not listar_alunos():
                print("Nenhum aluno cadastrado.")

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

            cadastrar_curso(nome_curso, duracao_curso, professor_curso, materias_curso)
            print(f"Curso {nome_curso} cadastrado com sucesso!")6
        
        case "6":
            print(listar_curso())
            if not listar_curso():
                print("Nenhum curso cadastrado.")
        
        case "7":
            nome_curso = input("Informe o nome do curso: ")
            print(detalhar_curso(nome_curso))
        
        case "8":
            nome_curso = input("Informe o nome do curso: ")
            print(deletar_curso(nome_curso))

        case "9":
            nome_curso = input("Informe o nome do curso: ")
            matricula = input("Informe a matricula do aluno: ")
            print(adicionar_aluno_curso(nome_curso, matricula))


        case "sair":
            print("Saindo do sistema.")
