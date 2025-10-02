class Servico:
    def __init__(self, id: int, nome: str, preco: float, descricao: str = ""):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def __str__(self):
        return f"[{self.id}] {self.nome} - R${self.preco:.2f} ({self.descricao})"
