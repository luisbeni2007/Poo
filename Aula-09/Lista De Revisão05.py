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
        