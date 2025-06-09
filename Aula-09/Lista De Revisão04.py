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
        self.__destino =  destino

    def set_distancia(self,distancia):
        self.__distancia = distancia

    def set_litros(self,litros):
        self.__litros = litros
    
    def consumo(self):
        return self.__distancia / self.__litros
    
class ViagemUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1:
                ViagemUI.calculo()
    @staticmethod
    def menu():
        return int(input("1-calcular, 2-fim:"))
    @staticmethod
    def calculo():
        destino = input("Informe o destino:")
        distancia = float(input("distancia:"))
        litros = float(input("litros:"))
        X = viagem(destino,distancia,litros)
        print(f"o consumo foi de {X.consumo():.1f}km/l")
ViagemUI.main()