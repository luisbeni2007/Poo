class frete:
    def __init__(self,produto,distancia,peso):
        self.produto = produto
        self.distancia = distancia
        self.peso = peso
    
    def get_produto(self):
        return self.__produto()
    
    def get_distancia(self):
        return self.__distancia()
    
    def get_peso(self):
        return self.__peso()
    
    def set_produto(self,produto):
        self.__produto = produto

    def set_distancia(self,distancia):
        if isinstance(distancia, (int, float)) and distancia > 0:
         self.__distancia = distancia
        else:
            raise ValueError("Distância deve ser um número positivo")

    def set_peso(self, peso):
         if isinstance(peso, (int, float)) and peso > 0:
          self.__peso = peso

    def preço(self):
        return (self .__distancia * self .__peso) / 100


class UI:
    def menu(self):
        print("\n--- MENU ---")
        print("1 – Calcular")
        print("2 – Fim")
        opcao = input("Escolha uma opção: ")
        return opcao.strip()

    def calculo(self):
        try:
            produto = input("Digite o nome do produto: ").strip()
            distancia = float(input("Digite a distância em km: "))
            peso = float(input("Digite o peso em kg: "))

            frete = frete(produto, distancia, peso)

            print("\n--- DADOS DO FRETE ---")
            print(f"Produto: {frete.get_produto()}")
            print(f"Distância: {frete.get_distancia()} km")
            print(f"Peso: {frete.get_peso()} kg")
            print(f"Preço do frete: R$ {frete.preco():.2f}")

        except ValueError as e:
            print(f"Erro: {e}")

    def main(self):
        while True:
            opcao = self.menu()
            if opcao == "1":
                self.calculo()
            elif opcao == "2":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")
