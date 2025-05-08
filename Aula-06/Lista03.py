class contabancaria:
    def __init__(self,nome_titular, numero_conta, saldo ):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.valor += valor
            print(f"deposito de R$ {valor: .2f} realizado com sucesso!")

    def sacar(self, valor):
        if 0 < valor <= self. saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor: .2f}realizado com sucesso!")
        else:
         print("Saldo insuficiente ou valor invalido")

    def mostrar_saldo(self):
        print(f"saldo atual da conta R$ {self.saldo: .2f}")

    def main():
        conta = contabancaria
        conta.depositar(500)
        conta.mostrar_saldo
        conta.sacar(200)
        conta.mostrar_saldo
        conta. sacar(2000)
if __name__ == "__main__": 
        main()