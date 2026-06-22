import tkinter as tk
from tkinter import messagebox, Button, Entry, Label, Frame, END, ttk
from controllers.livro_controller import LivroController

class GerenciarLivrosView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.controller = LivroController()
        self.geometry("800x600")
        self.title("Gerenciar Livros (Editar / Excluir)")

        colunas = ("id", "titulo", "autor", "quantidade")
        self.tree = ttk.Treeview(self, columns=colunas, show="headings", height=10)
        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        self.tree.heading("id", text="Código")
        self.tree.heading("titulo", text="Título do Livro")
        self.tree.heading("autor", text="Autor")
        self.tree.heading("quantidade", text="Quantidade")

        self.tree.column("id", width=50, stretch=False, anchor="center")
        self.tree.column("titulo", width=300)
        self.tree.column("autor", width=200)
        self.tree.column("quantidade", width=80, stretch=False, anchor="center")

        self.tree.bind("<<TreeviewSelect>>", self.preencher_formulario)

        frame_form = Frame(self)
        frame_form.pack(pady=10, fill="x", padx=20)

        Label(frame_form, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.txt_id = Entry(frame_form, width=10, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        Label(frame_form, text="Título:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.txt_titulo = Entry(frame_form, width=40)
        self.txt_titulo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        Label(frame_form, text="Autor:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.txt_autor = Entry(frame_form, width=40)
        self.txt_autor.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        Label(frame_form, text="Quantidade:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.txt_qtd = Entry(frame_form, width=10)
        self.txt_qtd.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        frame_botoes = Frame(self)
        frame_botoes.pack(pady=15)

        btn_salvar = Button(frame_botoes, text="Salvar Edição", command=self.salvar_edicao, width=15)
        btn_salvar.pack(side="left", padx=10)

        btn_excluir = Button(frame_botoes, text="Excluir Livro", command=self.excluir_livro, width=15)
        btn_excluir.pack(side="left", padx=10)

        btn_voltar = Button(frame_botoes, text="Voltar", command=self.voltar, width=15)
        btn_voltar.pack(side="left", padx=10)

        self.protocol("WM_DELETE_WINDOW", self.voltar)
        self.recarregar_livros()

    def recarregar_livros(self):
        for linha in self.tree.get_children():
            self.tree.delete(linha)
        
        livros = self.controller.listar_livros()
        for livro in livros:
            self.tree.insert("", END, values=(livro.id, livro.titulo, livro.autor, livro.qtd))
            
        self.limpar_campos()

    def preencher_formulario(self, event):
        selecao = self.tree.selection()
        if not selecao:
            return
            
        valores = self.tree.item(selecao[0], "values")
        
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, END)
        self.txt_id.insert(0, valores[0])
        self.txt_id.config(state="readonly")
        
        self.txt_titulo.delete(0, END)
        self.txt_titulo.insert(0, valores[1])
        
        self.txt_autor.delete(0, END)
        self.txt_autor.insert(0, valores[2])
        
        self.txt_qtd.delete(0, END)
        self.txt_qtd.insert(0, valores[3])

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, END)
        self.txt_id.config(state="readonly")
        self.txt_titulo.delete(0, END)
        self.txt_autor.delete(0, END)
        self.txt_qtd.delete(0, END)

    def salvar_edicao(self):
        id_livro = self.txt_id.get()
        titulo = self.txt_titulo.get().strip()
        autor = self.txt_autor.get().strip()
        qtd_str = self.txt_qtd.get().strip()

        if not id_livro:
            messagebox.showwarning("Atenção", "Selecione um livro na tabela para editar.")
            return

        if not all([titulo, autor, qtd_str]):
            messagebox.showwarning("Campos Vazios", "Preencha todos os campos do livro.")
            return

        if not qtd_str.isdigit() or int(qtd_str) < 0:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro válido.")
            return

        try:
            self.controller.atualizar_livro(int(id_livro), titulo, autor, int(qtd_str))
            messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
            self.recarregar_livros()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar livro: {str(e)}")

    def excluir_livro(self):
        id_livro = self.txt_id.get()
        titulo = self.txt_titulo.get()

        if not id_livro:
            messagebox.showwarning("Atenção", "Selecione um livro na tabela para excluir.")
            return

        if messagebox.askyesno("Confirmar Exclusão", f"Tem a certeza que deseja excluir o livro '{titulo}'?"):
            try:
                self.controller.deletar_livro(int(id_livro))
                messagebox.showinfo("Sucesso", "Livro excluído com sucesso.")
                self.recarregar_livros()
            except ValueError as ve:
                messagebox.showerror("Erro de Regra de Negócio", str(ve))
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível excluir. Detalhes: {str(e)}")

    def voltar(self):
        if self.master:
            if hasattr(self.master, "recarregar_livros"):
                self.master.recarregar_livros()
            self.master.deiconify()
        self.destroy()