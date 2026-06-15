from models.tipo_usuario import TipoUsuario

class Usuario:
    def __init__(self, nome: str, cpf: str, login: str, senha: str, tipo_usuario: TipoUsuario, id: int = None, ativo : bool = True):
        if not self.validar_cpf(cpf):
            raise ValueError("O CPF informado é inválido.")
            
        self.id = id
        self.nome = nome
        self.cpf = cpf.strip().replace('.', '').replace('-', '')
        self.login = login
        self.senha = senha
        self.tipo_usuario = tipo_usuario
        self.ativo = ativo

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        cpf_limpo = cpf.strip().replace('.', '').replace('-', '')
        
        if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
            return False

        if cpf_limpo == cpf_limpo[0] * 11:
            return False

        soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        
        if resto == 10:
            resto = 0
            
        if resto != int(cpf_limpo[9]):
            return False

        soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        
        if resto == 10:
            resto = 0
            
        if resto != int(cpf_limpo[10]):
            return False

        return True