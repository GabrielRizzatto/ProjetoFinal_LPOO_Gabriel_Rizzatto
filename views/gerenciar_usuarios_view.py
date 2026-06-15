import tkinter as tk
from tkinter import messagebox, Button, Frame, END, ttk, Label, Entry
from controllers.usuario_controller import UsuarioController

class GerenciarUsuariosView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.controller = UsuarioController()
        self.geometry("800x500")
        self.title("Gerenciamento de Usuários")

        frame_busca = Frame(self)
        frame_busca.pack(pady=10, fill="x", padx=20)
        
        lbl_busca = Label(frame_busca, text="Buscar Usuário (Nome, CPF ou Login):", font=("Arial", 10))
        lbl_busca.pack(side="left")
        
        self.var_busca = tk.StringVar()
        self.var_busca.trace_add("write", self.buscar)
        
        self.entry_busca = Entry(frame_busca, textvariable=self.var_busca, width=40)
        self.entry_busca.pack(side="left", padx=10)

        colunas = ("codigo", "nome", "cpf", "login", "tipo")
        self.tree = ttk.Treeview(self, columns=colunas, show="headings")
        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        self.tree.heading("codigo", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("cpf", text="CPF")
        self.tree.heading("login", text="Login")
        self.tree.heading("tipo", text="Tipo")

        self.tree.column("codigo", width=50, stretch=False, anchor="center")
        self.tree.column("nome", width=200)
        self.tree.column("cpf", width=120)
        self.tree.column("login", width=120)
        self.tree.column("tipo", width=120)

        frame_botoes = Frame(self)
        frame_botoes.pack(pady=10)

        btn_recarregar = Button(frame_botoes, text="Atualizar Lista", command=self.recarregar_usuarios, width=15)
        btn_recarregar.pack(side="left", padx=10)

        btn_excluir = Button(frame_botoes, text="Excluir Usuário", command=self.excluir_usuario, width=15)
        btn_excluir.pack(side="left", padx=10)

        btn_voltar = Button(frame_botoes, text="Voltar", command=self.voltar, width=15)
        btn_voltar.pack(side="left", padx=10)

        self.protocol("WM_DELETE_WINDOW", self.voltar)
        
        self.todos_os_usuarios = []
        self.recarregar_usuarios()

    def voltar(self):
        self.master.recarregar_livros()
        self.master.deiconify()
        self.destroy()

    def recarregar_usuarios(self):
        try:
            self.todos_os_usuarios = self.controller.listar_usuarios_ativos()
            self.var_busca.set("")
            self.atualizar_tabela(self.todos_os_usuarios)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar usuários: {str(e)}")

    def atualizar_tabela(self, lista_usuarios):
        for linha in self.tree.get_children():
            self.tree.delete(linha)
            
        for u in lista_usuarios:
            self.tree.insert("", END, values=(u.id, u.nome, u.cpf, u.login, u.tipo_usuario.value))

    def buscar(self, *args):
        termo = self.var_busca.get().lower()
        
        usuarios_filtrados = []
        
        for u in self.todos_os_usuarios:
            nome = str(u.nome).lower()
            cpf = str(u.cpf).lower()
            login = str(u.login).lower()
            
            if termo in nome or termo in cpf or termo in login:
                usuarios_filtrados.append(u)
                
        self.atualizar_tabela(usuarios_filtrados)

    def excluir_usuario(self):
        selecao = self.tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione um usuário para excluir.")
            return

        valores = self.tree.item(selecao[0], "values")
        id_usuario = valores[0]
        nome_usuario = valores[1]

        if messagebox.askyesno("Confirmar Exclusão", f"Deseja excluir o usuário {nome_usuario}?"):
            try:
                self.controller.deletar_usuario(int(id_usuario))
                messagebox.showinfo("Sucesso", "Usuário excluído com sucesso e livros devolvidos.")
                self.recarregar_usuarios()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir usuário: {str(e)}")