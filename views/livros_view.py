import tkinter as tk
from tkinter import messagebox, Button, Entry, Label, Frame, END, ttk
from controllers.livro_controller import LivroController
from controllers.emprestimo_controller import EmprestimoController
from models.usuario import Usuario
from views.strategy_factory import StrategyFactory
from views.emprestimo_view import EmprestimoView

class LivrosView(tk.Toplevel):
    def __init__(self, usuario: Usuario, master = None):
        super().__init__(master)
        self.controller = LivroController()
        self.emprestimo = EmprestimoController()
        self.usuario = usuario
        self.geometry("900x600")

        self.protocol("WM_DELETE_WINDOW", self.fechar_sistema_completo)


        frame_busca = Frame(self)
        frame_busca.pack(pady=10, fill="x", padx=20)
        
        lbl_busca = Label(frame_busca, text="Buscar Livro (Título ou Autor):", font=("Arial", 10))
        lbl_busca.pack(side="left")
        
        self.var_busca = tk.StringVar()
        self.var_busca.trace_add("write", self.buscar)
        
        self.entry_busca = Entry(frame_busca, textvariable=self.var_busca, width=40)
        self.entry_busca.pack(side="left", padx=10)

        colunas = ("id", "titulo", "autor", "quantidade")

        self.tree = ttk.Treeview(self, columns=colunas, show="headings")
        self.tree.pack(expand=True, fill="both", padx=20, pady=20)
    
        self.tree.heading("id", text="Código")
        self.tree.heading("titulo", text="Título do Livro")
        self.tree.heading("autor", text="Autor")
        self.tree.heading("quantidade", text="Quantidade")

        self.todos_os_livros = self.controller.listar_livros()

        self.tree.column("id", width=50, stretch=False, anchor="center")

        self.tree.column("titulo", width=250)
        self.tree.column("autor", width=150)
        self.tree.column("quantidade", width=50,stretch=False, anchor="center")

        frame_botoes = Frame(self)
        frame_botoes.pack(pady=10)

        estrategia = StrategyFactory.obter_estrategia(self.usuario.tipo_usuario)
        estrategia.renderizar_botoes(frame_botoes, self)

        btn_sair = Button(frame_botoes, text="Sair", command=self.voltar_login, width=15)
        btn_sair.pack(side="bottom", anchor="sw", padx=20, pady=20)

        self.atualizar_tabela(self.todos_os_livros)


    def atualizar_tabela(self, lista_livros):
        for linha in self.tree.get_children():
            self.tree.delete(linha)
            
        for livro in lista_livros:
            self.tree.insert("", END, values=(livro.id, livro.titulo, livro.autor, livro.qtd))

    def buscar(self, *args):
        termo = self.var_busca.get().lower()
        
        livros_filtrados = []
        
        for livro in self.todos_os_livros:
            titulo = str(livro.titulo).lower()
            autor = str(livro.autor).lower()
            
            if termo in titulo or termo in autor:
                livros_filtrados.append(livro)
                
        self.atualizar_tabela(livros_filtrados)

    def abrir_cadastro_livro(self):
       pass


    def gerenciar_usuarios(self):
        pass

    def alugar_livro_selecionado(self):
        selecao = self.tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Por favor, selecione um livro na tabela para alugar!")
            return
        
        item_id = selecao[0]

        valores = self.tree.item(item_id, "values")

        id_livro = valores[0]
        titulo = valores[1]


        mensagem = f"Você tem certeza que deseja alugar o livro '{titulo}'?\n A partir da confirmação devera entragar o Livro em 7 dias"
        
        confirmou = messagebox.askyesno(title="Confirmar Aluguel", message=mensagem)
        
        if confirmou:
            try:
                self.emprestimo.realizar_emprestimo(self.usuario.id, id_livro)
                self.recarregar_livros()

            except Exception as e:
                messagebox.showerror("Erro", f"Não Foi possível realizar o empréstimo: {str(e)}")
        else:
            return

    def ver_meus_emprestimos(self):
        self.withdraw()
        EmprestimoView(self.usuario, master= self)

    def fechar_sistema_completo(self):
        janela_raiz = self.master
        
        while janela_raiz and janela_raiz.master:
            janela_raiz = janela_raiz.master
            

        if janela_raiz:
            janela_raiz.destroy()
        else:
            self.destroy()    

    def voltar_login(self):
        janela_raiz = self.master
        
        while janela_raiz and janela_raiz.master:
            janela_raiz = janela_raiz.master
            
        if janela_raiz:
            janela_raiz.deiconify()
            
        self.destroy()


    def recarregar_livros(self):
        self.todos_os_livros = self.controller.listar_livros()
        self.atualizar_tabela(self.todos_os_livros)