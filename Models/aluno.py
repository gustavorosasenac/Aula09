import datetime
from uuid import uuid4

from Models.curso import Curso


class Aluno:

    #ATRIBUTOS
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.matricula = str(uuid4()) #uuid4 vai gerar um id
        self.ingresso = datetime.timezone #puxar a data atual do sistema
        self.curso = None
        self.notas = []

    #COMPORTAMENTOS
    def marcar_prova(self, data_prova, nome_prova):
        provas = {}
        prova = provas.get(nome_prova)

        if not prova: #se não tiver uma prova
            raise Exception # lança uma exceção

        prova ["data"] = data_prova
        prova ["aluno"] = self.matricula

        return f"Sua prova foi marcada para o dia {data_prova} com sucesso!"


    def fazer_media(self):
        if not self.notas:
            return "Nenhuma nota foi encontrada"

        media = sum(self.notas)/len(self.notas) #SUM vai somar todas as notas, LEN para pegar quantas notas tem, / vai dividir

        return f"sua média é de {media}"


    def repor_aula(self, nome_aula, data_reposicao):
        aulas_perdidas = {}
        aula =  aulas_perdidas.get(nome_aula)

        if not aula:
            return "Você ja fez esta aula"

        aula["data_reposicao"] = data_reposicao
        aula["aluno"] = self.matricula

        return f"Sua aula foi marcada para o dia {data_reposicao}"





