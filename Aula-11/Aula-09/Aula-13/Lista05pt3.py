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
    
    def set_nascimeto(self,nascimento):
        self.__nascimento = nascimento
    
    def __str__(self):
        return(
            f"ID: {self.__id}/n"
            f"Nome: {self.__nome}/n"
            f"E-mail:{self.__email}/n"
            f"Telefone:{self.__telefone}/n"
            f"Nascimento:{self.__nascimento}/n"
        )
        
    class contatoUI:
        contato = []

    @staticmethod

    def menu():
        print("\n--MENU DA AGENDS--n")
        print("1-Inserir Contato")
        print("2-Listar Contato")
        print("3-Atualizar Contato")
        print("4-Excluir Contato")
        print("5-Pesquisar contato(por inicial)")
        print("6-Aniversariante do mês")
        print("0-sair")
        return input("Escolha Uma Opção")
    
    @staticmethod
    def inserir():
        try:
            id = int(input("ID: "))
            nome = input("Nome: ")
            email = input("E-mail: ")
            fone = input("Telefone: ")
            nasc_str = input("Nascimento (dd/mm/aaaa): ")
            nascimento = datetime.strptime(nasc_str, "%d/%m/%Y")
            contato = Contato(id, nome, email, fone, nascimento)
            ContatoUI.contatos.append(contato)
            print("Contato inserido com sucesso!")
        except ValueError:
            print("Dados inválidos!")

    @staticmethod
    def listar():
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
        else:
            print("\n--- LISTA DE CONTATOS ---")
            for c in ContatoUI.contatos:
                print(c)
                print("-" * 30)

    @staticmethod
    def atualizar():
        try:
            id = int(input("Informe o ID do contato a atualizar: "))
            for c in ContatoUI.contatos:
                if c.get_id() == id:
                    c.set_nome(input("Novo nome: "))
                    c.set_email(input("Novo e-mail: "))
                    c.set_fone(input("Novo telefone: "))
                    nasc_str = input("Nova data de nascimento (dd/mm/aaaa): ")
                    c.set_nascimento(datetime.strptime(nasc_str, "%d/%m/%Y"))
                    print("Contato atualizado com sucesso!")
                    return
            print("Contato não encontrado.")
        except ValueError:
            print("Dados inválidos!")

    @staticmethod
    def excluir():
        try:
            id = int(input("Informe o ID do contato a excluir: "))
            for i, c in enumerate(ContatoUI.contatos):
                if c.get_id() == id:
                    del ContatoUI.contatos[i]
                    print("Contato excluído com sucesso!")
                    return
            print("Contato não encontrado.")
        except ValueError:
            print("ID inválido.")

    @staticmethod
    def pesquisar():
        inicial = input("Digite a letra inicial do nome: ").lower()
        encontrados = [c for c in ContatoUI.contatos if c.get_nome().lower().startswith(inicial)]
        if encontrados:
            print("\n--- CONTATOS ENCONTRADOS ---")
            for c in encontrados:
                print(c)
                print("-" * 30)
        else:
            print("Nenhum contato encontrado.")

    @staticmethod
    def aniversariantes():
        try:
            mes = int(input("Digite o número do mês (1-12): "))
            if mes < 1 or mes > 12:
                print("Mês inválido.")
                return
            aniversariantes = [c for c in ContatoUI.contatos if c.get_nascimento().month == mes]
            if aniversariantes:
                print("\n--- ANIVERSARIANTES DO MÊS ---")
                for c in aniversariantes:
                    print(c)
                    print("-" * 30)
            else:
                print("Nenhum aniversariante neste mês.")
        except ValueError:
            print("Entrada inválida.")

    @staticmethod
    def main():
        while True:
            opcao = ContatoUI.menu()
            if opcao == "1":
                ContatoUI.inserir()
            elif opcao == "2":
                ContatoUI.listar()
            elif opcao == "3":
                ContatoUI.atualizar()
            elif opcao == "4":
                ContatoUI.excluir()
            elif opcao == "5":
                ContatoUI.pesquisar()
            elif opcao == "6":
                ContatoUI.aniversariantes()
            elif opcao == "0":
                print("Saindo da Agenda. Até logo!")
                break
            else:
                print("Opção inválida.")

# Executar
if __name__ == "__main__":
    ContatoUI.main()