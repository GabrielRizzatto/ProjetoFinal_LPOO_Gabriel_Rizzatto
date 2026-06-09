from passlib.context import CryptContext
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario
from dao.db_config import pegar_session
from sqlalchemy.exc import IntegrityError

class UsuarioController:
    def __init__(self):
        self.bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def cadastrar_usuario(self, nome, cpf, login, senha, tipo_usuario):
        senha_criptografada = self.bycrypt_context.hash(senha)
        
        try:
            with pegar_session() as session:
                dao = UsuarioDAO(session)
                novo_usuario = Usuario(
                    nome=nome, 
                    cpf=cpf, 
                    login=login, 
                    senha=senha_criptografada, 
                    tipo_usuario=tipo_usuario
                )
                return dao.salvar(novo_usuario)
        except IntegrityError:
            raise ValueError("O CPF ou Login informado já existe no sistema.")

    def efetuar_login(self, login, senha):
        with pegar_session() as session:
            dao = UsuarioDAO(session)
            usuario = dao.buscar_por_login(login)
            
            if usuario and self.bycrypt_context.verify(senha, usuario.senha):
                return usuario
            
            return None
        
    