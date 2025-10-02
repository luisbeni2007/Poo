from Servico import Servico
from ServicoDAO import ServicoDAO

class ManterServicoUI:
    @staticmethod
    def inserir():
        descricao = input("Descrição do serviço: ")
        valor = float(input("Valor do serviço: "))
        s = Servico(0, descricao, valor)
        ServicoDAO.inserir(s)

    @staticmethod
    def listar():
        for s in ServicoDAO.listar():
            print(s)

    @staticmethod
    def atualizar():
        ManterServicoUI.listar()
        id = int(input("Informe o id do serviço que deseja atualizar: "))
        descricao = input("Nova descrição: ")
        valor = float(input("Novo valor: "))
        s = Servico(id, descricao, valor)
        ServicoDAO.atualizar(s)

    @staticmethod
    def excluir():
        ManterServicoUI.listar()
        id = int(input("Informe o id do serviço que deseja excluir: "))
        for s in ServicoDAO.listar():
            if s.get_id() == id:
                ServicoDAO.excluir(s)
                break
