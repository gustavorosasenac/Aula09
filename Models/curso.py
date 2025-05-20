class Curso:
    def __init__(self, nome_curso, duracao_curso, professor_curso, materias_curso):
        self.nome_curso = nome_curso
        self.alunos = {}
        self.duracao_curso = duracao_curso
        self.professor_curso = professor_curso
        self.materias_curso = materias_curso
        self.aulas_curso = []



    def conbilizar_presença(self):
        pass


    def listar_alunos_aprovados(self):
        for aluno in self.alunos:
            notas = aluno.notas  # Supondo que 'notas' seja uma lista de 4 notas
            if len(notas) != 4:
                print(f"Aluno {aluno.nome} não possui 4 notas cadastradas.")
                continue
            media = sum(notas) / 4
            if media >= 9:
                situacao = "Aprovado com excelência"
            elif 6 <= media < 9:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"
            print(f"Aluno: {aluno.nome} | Média: {media:.2f} | Situação: {situacao}")

