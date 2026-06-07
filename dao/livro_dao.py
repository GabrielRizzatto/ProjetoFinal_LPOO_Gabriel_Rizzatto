from sqlalchemy.orm import Session
from models.livro import Livro
from dao.generic_dao import GenericDAO

class LivroDAO(GenericDAO):
    def __init__(self, session: Session):
        self.session = session

    def salvar(self, livro: Livro):
        self.session.add(livro)
        self.session.commit()
        return livro

    def buscar_por_id(self, id_livro: int):
        return self.session.query(Livro).filter(Livro.id == id_livro).first()

    def buscar_todos(self):
        return self.session.query(Livro).order_by(Livro.id).all()

    def atualizar(self, livro: Livro):
        self.session.merge(livro)
        self.session.commit()
        return livro

    def deletar(self, id_livro: int):
        livro = self.buscar_por_id(id_livro)
        if livro:
            self.session.delete(livro)
            self.session.commit()
            return True
        return False

    def buscar_por_titulo(self, titulo: str):
        return self.session.query(Livro).filter(Livro.titulo == titulo).first()