from abc import ABC, abstractmethod
from tkinter import Button

class PermissaoStrategy(ABC):
    @abstractmethod
    def renderizar_botoes(self, frame, view):
        pass

class PermissaoAdmin(PermissaoStrategy):
    def renderizar_botoes(self, frame, view):
        btn_cadastrar = Button(frame, text="Cadastrar Novo Livro", width=20, command=view.abrir_cadastro_livro)
        btn_cadastrar.pack(side="left", padx=10)

        btn_gerenciar_livros = Button(frame, text="Gerenciar Livros", width=20, command=view.abrir_gerenciar_livros)
        btn_gerenciar_livros.pack(side="left", padx=5)
        
        btn_gerenciar = Button(frame, text="Gerenciar Usuários", width=20, command=view.gerenciar_usuarios)
        btn_gerenciar.pack(side="left", padx=10)

        btn_alugar = Button(frame, text="Alugar Livro Selecionado", width=25, command=view.alugar_livro_selecionado)
        btn_alugar.pack(side="left", padx=10)
        
        btn_meus_livros = Button(frame, text="Meus Empréstimos", width=20, command=view.ver_meus_emprestimos)
        btn_meus_livros.pack(side="left", padx=10)

class PermissaoComum(PermissaoStrategy):
    def renderizar_botoes(self, frame, view):
        btn_alugar = Button(frame, text="Alugar Livro Selecionado", width=25, command=view.alugar_livro_selecionado)
        btn_alugar.pack(side="left", padx=10)
        
        btn_meus_livros = Button(frame, text="Meus Empréstimos", width=20, command=view.ver_meus_emprestimos)
        btn_meus_livros.pack(side="left", padx=10)