class Contato:
    def __init__(self, i , n , e , f):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_fone(self):
        return self.__fone
    
    def set_nome(self, nome):
       self.__nome = nome
    
    def set_email(self, email):
        self.__email = email
    
    def set_id (self, id):
        self.__id = id

    def set_fone(self,fone):
        self._fone = fone


def __str__(self):

    return f"ID:{self._id } Nome:{self.__nome} Email: {self.__email} Fone: {self.__fone}"

class ContatoUI:
    contatos = []

    @staticmethod
    def menu():
        print("/n == MENU ==")
        print("1 - Inserir contato")
        print("2 - listar contatos")
        print("3 - Atualizar contatos")
        print("4 - Excluir contatos")
        print("5 - Pesquisar contato")
        print("0 - sair")
        return int (input("Escolha uma opção"))
    
    @staticmethod
    def inserir():
         try:
            i = int(input("ID: "))
            nome = int(input("nome: "))
            email = input("email")
            fone = input("fone")
            novo = Contato()