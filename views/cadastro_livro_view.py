import tkinter as tk
from tkinter import messagebox, Button, Entry, Label, Frame, END, ttk, Text
from controllers.livro_controller import LivroController
import json
import os

class CadastroLivroView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.controller = LivroController()
        self.geometry("600x450")
        self.title("Cadastrar Novo Livro")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.aba_manual = Frame(self.notebook)
        self.notebook.add(self.aba_manual, text="Cadastro Manual")

        self.aba_json = Frame(self.notebook)
        self.notebook.add(self.aba_json, text="Importar JSON")

        self.setup_aba_manual()
        self.setup_aba_json()

        btn_voltar = Button(self, text="Voltar", command=self.voltar, font=("Arial", 10), width=15)
        btn_voltar.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.voltar)

    def setup_aba_manual(self):
        frame_form = Frame(self.aba_manual)
        frame_form.pack(expand=True)

        lbl_titulo = Label(frame_form, text="Título:", font=("Arial", 10))
        self.txt_titulo = Entry(frame_form, width=40)
        lbl_titulo.pack(pady=5)
        self.txt_titulo.pack()

        lbl_autor = Label(frame_form, text="Autor:", font=("Arial", 10))
        self.txt_autor = Entry(frame_form, width=40)
        lbl_autor.pack(pady=5)
        self.txt_autor.pack()

        lbl_qtd = Label(frame_form, text="Quantidade:", font=("Arial", 10))
        self.txt_qtd = Entry(frame_form, width=40)
        lbl_qtd.pack(pady=5)
        self.txt_qtd.pack()

        btn_salvar = Button(frame_form, text="Cadastrar", command=self.cadastrar_manual, font=("Arial", 10))
        btn_salvar.pack(pady=15)

    def setup_aba_json(self):
        frame_json = Frame(self.aba_json)
        frame_json.pack(expand=True, fill="both", padx=10, pady=10)

        lbl_info = Label(frame_json, text="Cole o JSON com a lista de livros no formato correto:", font=("Arial", 10))
        lbl_info.pack(pady=5)

        self.text_json = Text(frame_json, height=15, width=60)
        self.text_json.pack(pady=5)

        btn_importar = Button(frame_json, text="Importar Livros", command=self.importar_json, font=("Arial", 10))
        btn_importar.pack(pady=10)

    def cadastrar_manual(self):
        titulo = self.txt_titulo.get().strip()
        autor = self.txt_autor.get().strip()
        qtd_str = self.txt_qtd.get().strip()

        if not all([titulo, autor, qtd_str]):
            messagebox.showwarning("Campos Vazios", "Preencha todos os campos do formulário.")
            return

        if not qtd_str.isdigit() or int(qtd_str) <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro maior que zero.")
            return

        try:
            self.controller.cadastrar_livro(titulo, autor, int(qtd_str))
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            self.limpar_manual()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar livro: {str(e)}")

    def limpar_manual(self):
        self.txt_titulo.delete(0, END)
        self.txt_autor.delete(0, END)
        self.txt_qtd.delete(0, END)

    def importar_json(self):
        conteudo_json = self.text_json.get("1.0", END).strip()
        
        if not conteudo_json:
            messagebox.showwarning("Aviso", "O campo de texto está vazio.")
            return

        try:
            qtd_inserida = self.controller.importar_livros_string_json(conteudo_json)
            messagebox.showinfo("Sucesso", f"Foram importados {qtd_inserida} livros com sucesso!")
            self.text_json.delete("1.0", END)
        except ValueError as ve:
            messagebox.showerror("Erro de Formato", str(ve))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao importar dados: {str(e)}")

    def voltar(self):
        if self.master:
            self.master.recarregar_livros()
            self.master.deiconify()
        self.destroy()