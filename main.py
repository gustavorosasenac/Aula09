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
        print("\nOpção inválida. Tente novamente.")
        continue

    match comando:
        case "1":
            nome = input("\nInforme o nome do aluno: ")
            nascimento = input("Informe a data de nascimento do aluno:")
            if not nome or not nascimento:
                print("\nNome e data de nascimento são obrigatórios.")
                continue

            print(cadastrar_aluno(nome, nascimento))

        case "2":
            print(listar_alunos())
            if not listar_alunos():
                print("Nenhum aluno cadastrado.")

        case "3":
            matricula = input("Informe a matricula do aluno: ")
            if not matricula:
                print("\nMatricula invalida.")
                continue
            print (detalhar_aluno(matricula))
            
        case "4":
            matricula = input("Informa a matricula do aluno: ")
            if not matricula:
                print("\nMatricula invalida.")
                continue
            print(deletar_aluno(matricula))
            
        case "5":
            nome_curso = input("Informe o nome do curso: ")
            duracao_curso = input("Informe a duração do curso: ")
            professor_curso = input("Informe o nome do professor: ")
            materias_curso = input("Informe as matérias do curso: ")
            if not nome_curso or not duracao_curso or not professor_curso or not materias_curso:
                print("\nNome, duração, professor e matéria são obrigatórios.")
                continue

            cadastrar_curso(nome_curso, duracao_curso, professor_curso, materias_curso)
            print(f"Curso {nome_curso} cadastrado com sucesso!")
        
        case "6":
            print(listar_curso())
            if not listar_curso():
                print("Nenhum curso cadastrado.")
        
        case "7":
            nome_curso = input("Informe o nome do curso: ")
            if not nome_curso:
                print("\nNome do curso inválido.")
                continue
            print(detalhar_curso(nome_curso))
            if not detalhar_curso(nome_curso):
                print("Nenhum curso cadastrado.")

        case "8":
            nome_curso = input("Informe o nome do curso: ")
            if not nome_curso:
                print("\nNome do curso obrigatorio.")
                continue
            print(deletar_curso(nome_curso))
            if not nome_curso:
                print("\nNome do curso inválido.")
                continue

        case "9":
            nome_curso = input("Informe o nome do curso: ")
            matricula = input("Informe a matricula do aluno: ")
            if not nome_curso or not matricula:
                print("\nNome do curso e matricula obrigatorios.")
                continue
            print(adicionar_aluno_curso(nome_curso, matricula))

        case "sair":
            print("\nSaindo do sistema...")
