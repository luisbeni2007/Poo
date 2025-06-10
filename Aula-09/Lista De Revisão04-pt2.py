class Pais:
    def __init__(self, nome: str, populacao: int, area: float):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def get_nome(self):
        return self._nome

    def get_populacao(self):
        return self._populacao

    def get_area(self):
        return self._area

    def set_nome(self, nome):
        if not nome:
            raise ValueError()
        self._nome = nome

    def set_populacao(self, populacao):
        if populacao <= 0:
            raise ValueError()
        self._populacao = populacao

    def set_area(self, area):
        if area <= 0:
            raise ValueError()
        self._area = area

    def densidade(self):
        return self._populacao / self._area

    def __str__(self):
        return f"{self._nome}, {self._populacao}, {self._area:.2f} km²"


class PaisUI:
    @staticmethod
    def menu():
        print("1 – Calcular")
        print("2 – Fim")
        try:
            return int(input())
        except:
            return 0

    @staticmethod
    def calculo():
        try:
            nome = input()
            populacao = int(input())
            area = float(input())
            pais = Pais(nome, populacao, area)
            print(pais)
            print(f"{pais.densidade():.2f}")
        except:
            print("Erro")

    @staticmethod
    def main():
        while True:
            opcao = PaisUI.menu()
            if opcao == 1:
                PaisUI.calculo()
            elif opcao == 2:
                break


if __name__ == "__main__":
    PaisUI.main()
