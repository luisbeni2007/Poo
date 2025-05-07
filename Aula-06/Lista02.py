class Viagem:
    def __init__(self,distancia,horas,minutos):
     self.distancia = distancia
     self.horas = horas
     self.minutos = minutos

    def calcular_velocidade_media(self):
       
       tempo_total = self.horas + (self.minutos / 60)

       return self.distancia / tempo_total
    

def main():
       
     viagem = Viagem(200,2,30)

       
     velocidade = viagem.calcular_velocidade_media()
     print(f"Distância percorrida = {viagem.distancia}km")
     print(f"Tempo Gasto: {viagem.horas}h{viagem.minutos}min")
     print(f"Velocidade media = {velocidade:.2f} km/h")

if __name__ == "__main__":
    main()