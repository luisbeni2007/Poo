from datetime import date, datetime


class paciente:
    def __init__(self,nome: str , cpf: str, telefone: str, nascimento:datetime):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf