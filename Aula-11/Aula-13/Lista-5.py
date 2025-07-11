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
def get_telefone(self):
        return self.__telefone

def get_nascimento(self):
        return self.__nascimento


def set_nome(self, nome):
        self.__nome = nome

def set_cpf(self, cpf):
        self.__cpf = cpf

def set_telefone(self, telefone):
        self.__telefone = telefone

def set_nascimento(self, nascimento):
        self.__nascimento = nascimento

    # Método idade
def idade(self):
        hoje = date.today()
        nascimento = self.__nascimento.date()

        anos = hoje.year - nascimento.year
        meses = hoje.month - nascimento.month

        if hoje.day < nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"

def __str__(self):
        return (
            f"Nome: {self.__nome}\n"
            f"CPF: {self.__cpf}\n"
            f"Telefone: {self.__telefone}\n"
            f"Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}\n"
            f"Idade: {self.idade()}"
        )

# UI para testar a classe
if __name__ == "__main__":
    print("Cadastro de Paciente")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    nascimento_str = input("Data de nascimento (dd/mm/aaaa): ")

    # Converter string para datetime
    try:
        nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")
    except ValueError:
        print("Data inválida! Use o formato dd/mm/aaaa.")
        exit()

    # Criar objeto Paciente
    paciente = Paciente(nome, cpf, telefone, nascimento)

    print("\n---- DADOS DO PACIENTE ----")
    print(paciente)

    # Atualização do telefone
    atualizar = input("\nDeseja atualizar o telefone? (s/n): ").lower()
    if atualizar == "s":
        novo_telefone = input("Novo telefone: ")
        paciente.set_telefone(novo_telefone)
        print("\n---- DADOS ATUALIZADOS ----")
        print(paciente)