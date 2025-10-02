from datetime import datetime, timedelta
from treino import Treino

class TreinoUI:
    def __init__(self):
        self.treinos = []
    
    def main(self):
        while True:
            opcao = self.menu()
            if opcao == 1:
                self.Inserir()
            elif opcao == 2:
                self.listar()
            elif opcao == 3:
                self.listar_Id()
            elif opcao == 4:
                self.Atualizar()
            elif opcao == 5:
                self.Excluir
            elif opcao == 6:
                self.MaisRapido()
            elif opcao == 0:
                print("Encerrando o programa")
                break
            else:
                print("Opção invalida. Tente novamente")
    def Menu(self):
        print("\ nMenu")
        print("1-Inserir treino")
        print("2-Listar todos os treinos")
        print("3-Listar treino por id")
        print("4-Atualizar treino")
        print("5-Excluir treino")
        print("6-Mostrar treino mais rápido (maior velocidade)")
        print("0-sair")
        try:
           return int(input("Escolha uma opção"))
        except ValueError:
            return -1
        
def Inserir(self):
    try:
       id = int(input("ID do treino"))
       data = datetime.strptime(input("Data(dd/mm/aaa): "),"%d/%m/%Y")
       distancia = float(input("Distância(em km):"))
       tempo_min = float(input("Tempo(em minutos)"))
       tempo = timedelta(minutes = tempo_min)

        treino = Treino(id, data, distancia, tempo)
        self.treinos.append(treino)
        print("treino inserido com sucesso!")
    except Exception as e:
        print("Erro ao inserir treino:", e)

def listar(self):
        if not self.treinos:
            print("nenhum treino cadastrado")
        else:
            for treino in self.treinos:
                print(treino)
                print("-", * 30)

def listar_id(self):
        try:
          id = int(input("Digte o ID do treino a ser listado"))
          for treino in self.treinos:
              if treino.get_id() == id:
                  print(treino)
                  return
              print("Treino não encontrado")
        except ValueError:
              print("ID inválido")

def atualizar(self):
        try:
            id = int(input("Digite o ID do treino a ser atualizado")) 
            for treino in self.treinos:
                if treino.get_id() == id:
                 data = datetime.strptime(input("Nova Data(dd/mm/aaa): , %d,%m,%Y"))
                 distancia = float(input("Nova distância(em km):"))
                 tempo_min = float(input("Novo tempo(em minutos)"))
                 tempo = timedelta(minutes=tempo_min)

                treino.set_data(data)
                distancia.set_distancia(distancia)
                tempo.set_tempo(tempo)

                print("treino atualizado com sucesso")
                return
            print("treino não encontrado.")
        except Exception as e:
            print("Erro ao atualizar treino:", e)

def excluir(self):
        try:
            id = int(input("Digite o ID do treino a ser excluído: "))
            for i, treino in enumerate(self.treinos):
                if treino.get_id() == id:
                    del self.treinos[i]
                    print("Treino excluído com sucesso!")
                    return
            print("Treino não encontrado.")
        except ValueError:
            print("ID inválido.")

def MaisRapido(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
            return

        mais_rapido = max(self.treinos, key=lambda t: t.get_distancia() / t.get_tempo().total_seconds())
        print("Treino com maior velocidade média:")
        print(mais_rapido)