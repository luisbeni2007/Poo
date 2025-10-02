class ManterProfissionalUI:
    def __init__(self, dao):
        self.dao = dao

    def cadastrar_profissional(self):
        nome = input("Nome do profissional: ")
        especialidade = input("Especialidade: ")
        telefone = input("Telefone: ")
        prof = Profissional(nome=nome, especialidade=especialidade, telefone=telefone)
        self.dao.adicionar(prof)
        print("Profissional cadastrado com sucesso!")

    def listar_profissionais(self):
        profissionais = self.dao.listar()
        for p in profissionais:
            print(f"ID: {p.get_id()}, Nome: {p.get_nome()}, Especialidade: {p.get_especialidade()}, Telefone: {p.get_telefone()}")
