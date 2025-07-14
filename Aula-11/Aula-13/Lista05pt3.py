from datetime import datetime

class Contato:
    def __init__(self, i: int, n: str, e: str, f: str, d: datetime):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__nascimento = d

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
       return self.__email
    
    def get_fone(self):
        return self.__fone
    
    def get_nascimento(self):
        return self.__nascimento
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self,email):
        self.__email = email

    def set_fone(self,fone):
        self.__fone = fone
    
    