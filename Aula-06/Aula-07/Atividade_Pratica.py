class triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0

    def definir_medidas(self, base, altura):
        if base > 0 and altura > 0:
         self.b = base
         self.h = altura

    def calcular_area(self):
        return(self.b * self.h/2)
    
    def str__(self):
        return f"Triângulo de base {self.b} e altura {self.h} tem área {self.calcular_area()}"