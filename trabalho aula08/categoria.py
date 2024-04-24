class categoria():
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
    def __str__(self):
        return f"Id {self.id} \n Nome Categoria {self.nome}"