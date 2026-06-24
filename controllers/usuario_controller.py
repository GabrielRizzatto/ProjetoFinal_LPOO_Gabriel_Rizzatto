from passlib.context import CryptContext
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario
from dao.db_config import pegar_session
from sqlalchemy.exc import IntegrityError
from controllers.emprestimo_controller import EmprestimoController

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
            
            if usuario and self.bycrypt_context.verify(senha, usuario.senha) and usuario.ativo == True:
                return usuario
            
            return None
        
    def listar_usuarios_ativos(self):
        with pegar_session() as session:
            dao = UsuarioDAO(session)
            return dao.buscar_ativos()

    def deletar_usuario(self, id_usuario):
        emprestimo_ctrl = EmprestimoController()
        emprestimos_ativos = emprestimo_ctrl.listar_emprestimo_usuario(id_usuario)
        
        for emprestimo in emprestimos_ativos:
            emprestimo_ctrl.devolver_livro(emprestimo.id)
            
        with pegar_session() as session:
            dao = UsuarioDAO(session)
            return dao.deletar(id_usuario)
    