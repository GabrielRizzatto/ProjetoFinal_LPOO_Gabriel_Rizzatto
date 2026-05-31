from sqlalchemy import Table, Column, Integer, String, Enum, MetaData, ForeignKey, Date, Text
from sqlalchemy.orm import registry
from models.usuario import Usuario
from models.tipo_usuario import TipoUsuario
from models.livro import Livro
from models.emprestimo import Emprestimo

mapper_registry = registry()
metadata = mapper_registry.metadata

tabela_usuarios = Table(
    'usuarios',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nome', String(100), nullable=False),
    Column('cpf', String(14), unique=True, nullable=False),
    Column('login', String(100), unique=True, nullable=False),
    Column('senha', String, nullable=False),
    Column('tipo_usuario', Enum(TipoUsuario), nullable=False)
)

tabela_livros = Table(
    'livros',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('titulo', String(200), nullable=False),
    Column('autor', String(150), nullable=False)
)

tabela_emprestimos = Table(
    'emprestimos',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_usuario', Integer, ForeignKey('usuario.id'), nullable=False),
    Column('id_livro', Integer, ForeignKey('livro.id'), nullable=False),
    Column('data_retirada', Date, nullable=False),
    Column('data_devolucao_prevista', Date, nullable=False),
    Column('status', String(50), nullable=False)
)

def mapear_tabelas():
    mapper_registry.map_imperatively(Usuario, tabela_usuarios)
    mapper_registry.map_imperatively(Livro, tabela_livros)
    mapper_registry.map_imperatively(Emprestimo, tabela_emprestimos)