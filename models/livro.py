class Livro:
    def __init__(self, titulo: str, autor: str, id: int = None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
