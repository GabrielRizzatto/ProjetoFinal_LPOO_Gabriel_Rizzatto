class Livro:
    def __init__(self, titulo: str, autor: str, qtd: int ,id: int = None, ativo: bool = True):
        self.id = id
        self.titulo = titulo.lower().title()
        self.autor = autor
        self.qtd = qtd
        self.ativo = ativo
