class EntradaCinema:
    def __init__(self,dia,horario):
        self._dia = dia.lower()
        self.horario = horario
    def set_dia(self,dia):
        self._dia = dia.lower

    def get_dia(self):
        return self._dia
    
    def set_horario(self,horario):
        self.horario = horario

    def get_horario(self):
        return self.horario
    
    def _valor_base(self):
        if self.__dia == "quarta":
            return 8.00
        elif self.__dia in ["Segunda", "Terça", "Quinta"]:
            return 16.00
        elif self.__dia in ["Sexta", "Sábado", "Domingo"]:
            return 20.00
        else:
          return 0
        
    def _tem_acrescimo(self):
        return 17 <= self.horario <= 23
    
    def calcular_valor_inteiro(self):
        base = self._valor_base()
        if self.__dia == "quarta":
            return base
        elif self._tem_acrescimo():
            return base * 1.5
        else:
            return base
    def calcular_valor_meia(self):
        return self.calcular_valor_inteiro () / 2
    
    def main():