class Livro:
    def __init__(self, titulo: str, autor: str, qtd: int ,id: int = None):
        self.id = id
        self.titulo = titulo.lower().title()
        self.autor = autor
        self.qtd = qtd
