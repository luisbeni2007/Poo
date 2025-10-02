class ProfissionalDAO:
    def __init__(self):
        self.profissionais = []  # Lista simulando banco de dados

    def adicionar(self, profissional):
        profissional.set_id(len(self.profissionais) + 1)
        self.profissionais.append(profissional)

    def listar(self):
        return self.profissionais

    def buscar_por_id(self, id):
        for prof in self.profissionais:
            if prof.get_id() == id:
                return prof
        return None

    def atualizar(self, profissional):
        for i, prof in enumerate(self.profissionais):
            if prof.get_id() == profissional.get_id():
                self.profissionais[i] = profissional
                return True
        return False

    def remover(self, id):
        for prof in self.profissionais:
            if prof.get_id() == id:
                self.profissionais.remove(prof)
                return True
        return False
