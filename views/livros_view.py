import tkinter as tk
from tkinter import messagebox, Entry, Label, Frame, END, ttk, Button
from controllers.livro_controller import LivroController
from controllers.emprestimo_controller import EmprestimoController
from models.usuario import Usuario
from views.strategy_factory import StrategyFactory
from views.emprestimo_view import EmprestimoView
from views.sobre_view import SobreView

class LivrosView(tk.Toplevel):
    def __init__(self, usuario: Usuario, master = None):
        super().__init__(master)
        self.controller = LivroController()
        self.emprestimo = EmprestimoController()
        self.usuario = usuario
        self.geometry("900x650")
        self.title("Sistema de Gestão de Biblioteca")

        self.protocol("WM_DELETE_WINDOW", self.fechar_sistema_completo)

        self.menubar = tk.Menu(self)
        menu_ajuda = tk.Menu(self.menubar, tearoff=0)
        menu_ajuda.add_command(label="Sobre o Sistema", command=self.abrir_sobre)
        self.menubar.add_cascade(label="Ajuda", menu=menu_ajuda)
        self.config(menu=self.menubar)

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

        self.tree.column("id", width=50, stretch=False, anchor="center")
        self.tree.column("titulo", width=250)
        self.tree.column("autor", width=150)
        self.tree.column("quantidade", width=50, stretch=False, anchor="center")

        frame_botoes = Frame(self)
        frame_botoes.pack(pady=10)

        estrategia = StrategyFactory.obter_estrategia(self.usuario.tipo_usuario)
        estrategia.renderizar_botoes(frame_botoes, self)

        btn_sair = Button(self, text="Sair", command=self.voltar_login, width=15)
        btn_sair.pack(side="bottom", anchor="sw", padx=20, pady=20)

        self.todos_os_livros = self.controller.listar_livros()
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
        self.withdraw()
        from views.cadastro_livro_view import CadastroLivroView
        CadastroLivroView(master=self)

    def abrir_gerenciar_livros(self):
        self.withdraw()
        from views.gerenciar_livros_view import GerenciarLivrosView
        GerenciarLivrosView(master=self)

    def gerenciar_usuarios(self):
        self.withdraw()
        from views.gerenciar_usuarios_view import GerenciarUsuariosView
        GerenciarUsuariosView(master=self)

    def alugar_livro_selecionado(self):
        selecao = self.tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Por favor, selecione um livro na tabela para alugar!")
            return
        
        item_id = selecao[0]
        valores = self.tree.item(item_id, "values")

        id_livro = valores[0]
        titulo = valores[1]

        mensagem = f"Tem a certeza que deseja alugar o livro '{titulo}'?\nA partir da confirmação deverá entregar o livro em 7 dias."
        
        confirmou = messagebox.askyesno(title="Confirmar Aluguel", message=mensagem)
        
        if confirmou:
            try:
                self.emprestimo.realizar_emprestimo(self.usuario.id, id_livro)
                self.recarregar_livros()
                messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível realizar o empréstimo: {str(e)}")

    def ver_meus_emprestimos(self):
        self.withdraw()
        EmprestimoView(self.usuario, master=self)
        
    def abrir_sobre(self):
        self.withdraw()
        SobreView(master=self)

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