from dao.emprestimo_dao import EmprestimoDAO
from dao.livro_dao import LivroDAO
from models.emprestimo import Emprestimo
from dao.db_config import pegar_session
from datetime import datetime, timedelta

class EmprestimoController:
    def __init__(self):
        pass

    def realizar_emprestimo(self, id_usuario, id_livro):
        with pegar_session() as session:
            livro_dao = LivroDAO(session)
            livro = livro_dao.buscar_por_id(id_livro)

            if not livro or livro.qtd <= 0:
                raise ValueError("O livro selecionado não possui exemplares disponíveis.")

            livro.qtd -= 1
            livro_dao.atualizar(livro)

            emprestimo_dao = EmprestimoDAO(session)
            novo_emprestimo = Emprestimo(
                id_usuario = id_usuario,
                id_livro = id_livro,
                data_retirada = datetime.now(),
                data_devolucao_prevista =  datetime.now() + timedelta(days=7),
                status="ATIVO"
            )
            return emprestimo_dao.salvar(novo_emprestimo)


    def devolver_livro(self, id_emprestimo):
        with pegar_session() as session:
            emprestimo_dao = EmprestimoDAO(session)
            emprestimo = emprestimo_dao.buscar_por_id(id_emprestimo)

            if not emprestimo or emprestimo.status == "DEVOLVIDO":
                raise ValueError("Empréstimo não encontrado ou já consta como devolvido.")

            emprestimo.status = "DEVOLVIDO"
            emprestimo_dao.atualizar(emprestimo)

            livro_dao = LivroDAO(session)
            livro = livro_dao.buscar_por_id(emprestimo.id_livro)
            
            if livro:
                livro.qtd += 1
                livro_dao.atualizar(livro)

            return emprestimo
        
    def listar_emprestimo_usuario(self, id_usuario):
        with pegar_session() as session:
            dao = EmprestimoDAO(session)
            return dao.buscar_ativos_por_id_usuario(id_usuario)