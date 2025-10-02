class Profissional:
    def __init__(self, id=None, nome="", especialidade="", telefone=""):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.telefone = telefone

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_especialidade(self):
        return self.especialidade

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone
