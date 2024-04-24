from abc import ABC, abstractmethod
from categoria import categoria

@abstractmethod
class produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def __getInformacoes__(self):
        info_str = ""
        for attr, value in vars(self).items():
            info_str += f"{attr}: {value}\n"
        return info_str
        
    def cadastrar(self):
        escolha = input("Deseja cadastrar este item? S ou N")
        while True:
            if escolha.upper() == "S":
                print("Produto cadastrado")
                exit()
            elif escolha.upper() == "N":
                print("Produto não cadastrado")
                exit()
            else:
                print("Escolha não encontrada")
             
