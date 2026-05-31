class Emprestimo:
    def __init__(self, id_usuario: int, id_livro: int, data_retirada, data_devolucao_prevista, status: str, id: int = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_livro = id_livro
        self.data_retirada = data_retirada
        self.data_devolucao_prevista = data_devolucao_prevista
        self.status = status

