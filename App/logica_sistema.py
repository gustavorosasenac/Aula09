from Models.aluno import Aluno
from Models.curso import Curso


CURSOS = {}
ALUNOS = {}


def cadastrar_aluno(nome, nascimento):
    if not nome or not nascimento:
        return "Parametros inválidos"

    aluno_objeto = Aluno(nome, nascimento)

    ALUNOS[aluno_objeto.matricula] = aluno_objeto


    return {
        "aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula

    }

def listar_alunos():
    resposta = ""
    for aluno in ALUNOS.values(): # para cada aluno na lista ALUNOS
        resposta += (f"\nNome: {aluno.nome} \n"
                 f"Matricula: {aluno.matricula}\n"
                 f"Curso: {aluno.curso if aluno.curso else 'Sem curso no momento'}\n"
                 f"---------------------------------------\n ")

    return resposta


def detalhar_aluno(matricula):
    if not matricula:
        return "\nParametros Invalidos"

    aluno = ALUNOS.get(matricula)

    return (f"\nNome: {aluno.nome}\n"
            f"Matricula: {aluno.matricula} \n"
            f"Data de nascimento: {aluno.nascimento} \n"
            f"Data de ingresso: {aluno.ingresso}\n"
            f"Curso: {aluno.curso or 'Sem curso cadastrado'} \n"
            f"Notas: {aluno.notas}\n "
            )


def deletar_aluno(matricula):
    if not matricula:
        return "\nParametro invalidos"

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "\nEste aluno não está cadastrado"

    if aluno.curso:
        curso = CURSOS.get(aluno.curso.nome)
        curso.alunos.pop(matricula)
    ALUNOS.pop(matricula)

    return "\nAluno excluido com sucesso"


def cadastrar_curso(nome_curso, duracao_curso, professor_curso, materias_curso):
    if not nome_curso or not duracao_curso or not professor_curso or not materias_curso:
        return "Parametros inválidos"
    
    curso_objeto = Curso(nome_curso, duracao_curso, professor_curso, materias_curso)
    CURSOS[nome_curso] = curso_objeto

    return {
        "curso": curso_objeto.nome_curso,
        "duracao": curso_objeto.duracao_curso,
        "professor": curso_objeto.professor_curso,
        "materias": curso_objeto.materias_curso
    }
    


def listar_curso():
    resposta = ""
    for curso in CURSOS.values():
        resposta += (f"\nNome: {curso.nome_curso} \n"
                 f"Duração: {curso.duracao_curso} meses \n"
                 f"Professor: {curso.professor_curso}\n"
                 f"Materias: {curso.materias_curso}\n"
                 f"---------------------------------------\n ")

    return resposta



def detalhar_curso(nome_curso):
    if not nome_curso:
        return "\nParametros Invalidos"

    curso = CURSOS.get(nome_curso)

    return (f"\nNome: {curso.nome_curso}\n"
            f"Professor: {curso.professor_curso} \n"
            f"Materias: {curso.materias_curso} \n"
            f"Aulas: {curso.aulas_curso}\n "
            )

def deletar_curso(nome_curso):
    if not nome_curso:
        return "\nParametros Invalidos"

    curso = CURSOS.get(nome_curso)

    if not curso:
        return "\nEste curso não está cadastrado"

    CURSOS.pop(nome_curso)

    return "\nCurso excluido com sucesso"


def adicionar_aluno_curso(nome_curso, matricula):
    if not nome_curso or not matricula:
        return "\nParametros invalidos"
    
    curso = CURSOS.get(nome_curso)
    aluno = ALUNOS.get(matricula)

    if not curso:
        return "\nCurso não encontrado"

    if not aluno:
        return "\nAluno não encontrado"

    curso.alunos[aluno.matricula] = aluno
    aluno.curso = curso

    return f"\nAluno {aluno.nome} cadastrado no curso {curso.nome_curso}"













