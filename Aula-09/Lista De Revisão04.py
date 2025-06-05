class viagem:
    def __init__(self, destino, distancia, litros):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)

    def get_destino(self):
        return self.__destino
    
    def get_distancia(self):
        return self.__distancia
    
    def get_litros(self):
        return self.__litros
    
    def set_destino(self,destino):
        self.destino =  destino

    def set_distancia(self,distancia):
        self.distancia = distancia

    def set_litros(self,litros):
        self.litros = litros
    
    def consumo(self):
        return self.__distancia / self.__litros