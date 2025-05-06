import math
class círculo:
    def __init__(self,raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def calcular_circuferencia(self):
        return 2 * math.pi * self.raio

def main():
    círculo = círculo(5)
    
    area = círculo.calcular_area()
    print(f"Area do círculo: {area:.2f}")

    circuferencia = circuferencia.calcular_circuferencia()
    print(f"circuferencia do círculo: {circuferencia:.2f}")
    if __name__ == "__main__": main()