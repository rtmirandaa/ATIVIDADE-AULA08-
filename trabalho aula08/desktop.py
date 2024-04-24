from categoria import categoria
from produto import produto

class desktop(produto):
    adm = True
    def __init__(self, modelo, cor, preco,categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte
    def __setNovaPotencia__(self, novaPotencia):
        self._potenciaDaFonte =  novaPotencia
    