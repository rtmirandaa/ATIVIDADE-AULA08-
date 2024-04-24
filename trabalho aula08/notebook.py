from categoria import categoria
from produto import produto

class notebook(produto):
    def __init__(self, modelo, cor, preco, categoria, tempodeBateria):
        super().__init__(modelo, cor, preco,categoria)
        self.__tempodeBateria = tempodeBateria
    def __setNovoTempo__(self, novo_tempo):
        self.__tempodeBateria = novo_tempo
    