from datetime import datetime, timedelta

class treino:
    def __init__(self,id: int, dt: datetime, ds: float, t: timedelta):
        self.__id = id
        self.__data = dt
        self.__distancia = ds
        self.__tempo = t

    def get_id(self):
        return self.__id
    
    def get_data(self):
        return self.__data
    
    def get_distancia(self):
        return self.__distancia
    
    def get_tempo(self):
        return self.__tempo
    
    def set_id(self, id: int):
        return self._id == id
    
    def set_data(self,data: datetime):
        return self._data == data
    
    def set_distancia(self,distancia:float):
        return self._distancia == distancia
    
    def set_tempo(self,tempo: timedelta):
        return self._tempo == tempo
    
    def __str__(self):
        return(f"Treino:ID: {self.__id}\ n"
               f"Data: {self._data.strftime}\ n"
               f"Distância:{self.__distancia}\ n"
               f"tempo:{self.__tempo}")