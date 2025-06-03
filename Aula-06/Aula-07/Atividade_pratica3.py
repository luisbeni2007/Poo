class ContaBancaria:
    def __init__(self, titular,número):
        self._titular = titular
        self._número  = número
        self._saldo   = 0
    
    def get_titular(self):
        return self._titular
    
    def get_número(self):
        return self._número

    def get_saldo(self):
        return self._saldo
    
    def depositar(self,valor):  #saque
        self._saldo = self._saldo + valor
    
    def sacar(self, valor):    #saque
        if valor > self._saldo: raise ValueError("Saldo insuficiente")
        self._saldo = self._saldo - valor

    def set_titular(self, novo_titular):
        self._titular = novo_titular
    
    def set_número(self, novo_número):
        self._número = novo_número

        
x = ContaBancaria("Luis", "1234")
print(x.get_saldo())
x.depositar(100)
print(x.get_saldo())
x.depositar(50)
print(x.get_saldo())
x.sacar(40)
print(x.get_saldo())
x.sacar(40)
print(x.get_saldo())
x.sacar(40)
print(x.get_saldo())
#x.sacar(200)   #Erro
print(x.get_saldo())