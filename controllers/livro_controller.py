from dao.livro_dao import LivroDAO
from models.livro import Livro
from dao.db_config import pegar_session
from models.emprestimo import Emprestimo
import json

class LivroController:

    def __init__(self):
        pass

    def cadastrar_livro(self, titulo, autor, quantidade):
        with pegar_session() as session:
            dao = LivroDAO(session)
            novo_livro = Livro(
                titulo=titulo,
                autor=autor,
                qtd=quantidade,
                ativo=True
            )
            return dao.salvar(novo_livro)
        
    def listar_livros(self):
        with pegar_session() as session:
            dao = LivroDAO(session)
            return dao.buscar_todos()
        

    def atualizar_livro(self, id_livro, titulo, autor, quantidade):
        with pegar_session() as session:
            dao = LivroDAO(session)
            livro = dao.buscar_por_id(id_livro)
            
            if livro:
                livro.titulo = titulo
                livro.autor = autor
                livro.qtd = quantidade
                return dao.atualizar(livro)
            
            return None

    def deletar_livro(self, id_livro):
        with pegar_session() as session:
            emprestimo_pendente = session.query(Emprestimo).filter(
                Emprestimo.id_livro == id_livro,
                Emprestimo.status == "ATIVO"
            ).first()
            
            if emprestimo_pendente:
                raise ValueError("Este livro possui empréstimos ativos e não pode ser excluído até que seja devolvido.")
                
            dao = LivroDAO(session)
            return dao.deletar(id_livro)
        
    def importar_livros_string_json(self, conteudo_json):
        try:
            livros = json.loads(conteudo_json)
        except json.JSONDecodeError:
            raise ValueError("O formato do texto fornecido não é um JSON válido.")
            
        quantidade_adicionada = 0
        for livro_data in livros:
            titulo = livro_data.get("titulo")
            autor = livro_data.get("autor")
            qtd = livro_data.get("qtd")
            
            if titulo and autor and qtd is not None:
                self.cadastrar_livro(titulo, autor, qtd)
                quantidade_adicionada += 1
                
        return quantidade_adicionada