class viagem:
    def __init__(self):
        self.distancia = 0.0
        self.tempo = 0.0

    def set_distancia(self,d):
        self.distancia = d

    def set_tempo(self,t):
        self.tempo = t
    
    def get_distancia(self):
        return self.distancia
    
    def get_tempo(self):
        return self.tempo
    
    def velocidade_media(self):
        if self.tempo > 0:
            return self.distancia / self.tempo
        else:
            return 0.0