import tkinter as tk
from tkinter import messagebox, Button, Entry, Label, Frame, END, ttk
from controllers.emprestimo_controller import EmprestimoController
from models.usuario import Usuario

class EmprestimoView(tk.Toplevel):
    def __init__(self, usuario: Usuario, master = None):
        super().__init__(master)
        self.controller = EmprestimoController()
        self.usuario = usuario
        self.geometry("900x600")

        colunas = ("id", "titulo", "data_retirada", "data_devolucao")

        self.tree = ttk.Treeview(self, columns=colunas, show="headings")
        self.tree.pack(expand=True, fill="both", padx=20, pady=20)
    
        self.tree.heading("id", text="Código")
        self.tree.heading("titulo", text="Título do Livro")
        self.tree.heading("data_retirada", text="Data de Retirada")
        self.tree.heading("data_devolucao", text="Data de Devolução")

        self.emprestimos_usuario = self.controller.listar_emprestimo_usuario(self.usuario.id)
        

        self.tree.column("id", width=50, stretch=False, anchor="center")
        self.tree.column("titulo", width=250)
        self.tree.column("data_retirada", width=150)
        self.tree.column("data_devolucao", width=150)


        self.atualizar_tabela(self.emprestimos_usuario)

        frame_botoes = Frame(self)
        frame_botoes.pack(pady=10)
        
        btn_devolver = Button(frame_botoes, text="devolver", command=self.devolver_livro, width=15)
        btn_devolver.pack(side="left", padx=10)

        btn_voltar = Button(frame_botoes, text="Voltar", command=self.voltar, width=15)
        btn_voltar.pack(side="left", padx=10)
    

    def voltar(self):
        self.master.recarregar_livros()
        self.master.deiconify()
        self.destroy()

    def devolver_livro(self):
        selecao = self.tree.selection()

        if not selecao:
            messagebox.showwarning("Atenção", "Por favor, selecione um livro na tabela para devolver!")
            return
    
        item_id = selecao[0]

        valores = self.tree.item(item_id, "values")

        id_emprestimo = valores[0]
        self.controller.devolver_livro(id_emprestimo)

        self.emprestimos_usuario = self.controller.listar_emprestimo_usuario(self.usuario.id)
        self.atualizar_tabela(self.emprestimos_usuario)

    def atualizar_tabela(self, lista_emprestimos):
        for linha in self.tree.get_children():
            self.tree.delete(linha)
            
        for emprestimo, livro in lista_emprestimos:
            self.tree.insert("", END, values=(emprestimo.id, livro.titulo, emprestimo.data_retirada, emprestimo.data_devolucao_prevista))

