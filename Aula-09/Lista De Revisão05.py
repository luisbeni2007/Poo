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