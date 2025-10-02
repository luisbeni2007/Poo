import json
from models.cliente import Cliente

class ClienteDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj: Cliente):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: 
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def atualizar(cls, obj: Cliente):
        cls.abrir()
        for i, aux in enumerate(cls.__objetos):
            if aux.get_id() == obj.get_id():
                cls.__objetos[i] = obj
                break
        cls.salvar()

    @classmethod
    def excluir(cls, obj: Cliente):
        cls.abrir()
        cls.__objetos = [aux for aux in cls.__objetos if aux.get_id() != obj.get_id()]
        cls.salvar()

    @classmethod
    def salvar(cls):
        with open("clientes.json", "w") as f:
            json.dump([obj.to_json() for obj in cls.__objetos], f)

    @classmethod
    def abrir(cls):
        try:
            with open("clientes.json", "r") as f:
                cls.__objetos = [Cliente.from_json(dic) for dic in json.load(f)]
        except FileNotFoundError:
            cls.__objetos = []
