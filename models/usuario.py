from models.tipo_usuario import TipoUsuario

class Usuario:
    def __init__(self, nome: str, cpf: str, login: str, senha: str, tipo_usuario: TipoUsuario, id: int = None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.login = login
        self.senha = senha
        self.tipo_usuario = tipo_usuario