from sqlalchemy.orm import Session
from models.emprestimo import Emprestimo
from models.livro import Livro
from dao.generic_dao import GenericDAO


class EmprestimoDAO(GenericDAO):
    def __init__(self, session: Session):
        self.session = session

    def salvar(self, emprestimo: Emprestimo):
        self.session.add(emprestimo)
        self.session.commit()
        return emprestimo
    
    def atualizar(self, emprestimo: Emprestimo):
        self.session.merge(emprestimo)
        self.session.commit()
        return emprestimo
    
    def deletar(self, id_emprestimo: int):
        emprestimo = self.buscar_por_id(id_emprestimo)
        if emprestimo:
            self.session.delete(emprestimo)
            self.session.commit()
            return True
        return False
    
    def buscar_todos(self):
        return self.session.query(Emprestimo).all()
    
    def buscar_por_id(self, id_emprestimo: int):
        return self.session.query(Emprestimo).filter(Emprestimo.id == id_emprestimo).first()
    

    def buscar_ativos_por_id_usuario(self, id_usuario: int):
        return self.session.query(Emprestimo, Livro).join(Livro, Emprestimo.id_livro == Livro.id).filter(Emprestimo.status == "ATIVO").order_by(Emprestimo.data_retirada).all()
        