from sqlalchemy.orm import Session
from models.usuario import Usuario
from dao.generic_dao import GenericDAO

class UsuarioDAO(GenericDAO):
    def __init__(self, session: Session):
        self.session = session

    def salvar(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def buscar_por_id(self, id_usuario: int):
        return self.session.query(Usuario).filter(Usuario.id == id_usuario).first()

    def buscar_todos(self):
        return self.session.query(Usuario).all()

    def atualizar(self, usuario: Usuario):
        self.session.merge(usuario)
        self.session.commit()
        return usuario

    def deletar(self, id_usuario: int):
        usuario = self.buscar_por_id(id_usuario)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
            return True
        return False

    def buscar_por_login(self, login: str):
        return self.session.query(Usuario).filter(Usuario.login == login).first()