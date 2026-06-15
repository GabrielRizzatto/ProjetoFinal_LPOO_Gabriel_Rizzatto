import tkinter as tk
from tkinter import messagebox, Button, Entry, Label, Frame, END, ttk
from controllers.usuario_controller import UsuarioController
from models.tipo_usuario import TipoUsuario

class CadastroUsuarioView(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.controller = UsuarioController()
        self.geometry("500x300")

        frame_cadastro = Frame(self)
        frame_cadastro.pack(expand=True)  

        lbl_nome = Label(frame_cadastro, text="Nome:", font=("Arial", 10))
        self.txt_nome = Entry(frame_cadastro)
        lbl_nome.pack(pady=5)
        self.txt_nome.pack()

        lbl_cpf = Label(frame_cadastro, text="CPF:", font=("Arial", 10))
        self.txt_cpf = Entry(frame_cadastro)
        lbl_cpf.pack(pady=5)
        self.txt_cpf.pack()

        lbl_login = Label(frame_cadastro, text="Login:", font=("Arial", 10))
        self.txt_login = Entry(frame_cadastro)
        lbl_login.pack(pady=5)
        self.txt_login.pack()

        lbl_senha = Label(frame_cadastro, text="Senha:", font=("Arial", 10))
        self.txt_senha = Entry(frame_cadastro)
        lbl_senha.pack(pady=5)
        self.txt_senha.pack()

        lb_tipo = Label(frame_cadastro, text="Tipo de Permissão:", font=("Arial", 10))
        lb_tipo.pack(pady=5)
        self.combo_tipo = ttk.Combobox(
            frame_cadastro, 
            values=[tipo.value for tipo in TipoUsuario], 
            font=("Arial", 10), 
            width=32, 
            state="readonly"
        )
        self.combo_tipo.set(TipoUsuario.COMUM.value)
        self.combo_tipo.pack(pady=2)
        

        btn_cadastrar = Button(frame_cadastro, text="Cadastrar", command=self.cadastrar, font=("Arial", 10))
        btn_cadastrar.pack(pady=10)


        btn_voltar = Button(self, text="Voltar", command=self.voltar, font=("Arial", 10))
        btn_voltar.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

        self.protocol("WM_DELETE_WINDOW", self.voltar)


    def voltar(self):
        self.master.deiconify()
        self.destroy()

    def cadastrar(self):
        nome = self.txt_nome.get().strip()
        cpf = self.txt_cpf.get().strip()
        login = self.txt_login.get().strip()
        senha = self.txt_senha.get().strip()
        tipo_str = self.combo_tipo.get()
        
        if not all([nome, cpf, login, senha, tipo_str]):
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos do formulário.")
            return
            
        tipo_usuario = TipoUsuario(tipo_str)
        
        try:
            usuario = self.controller.cadastrar_usuario(nome, cpf, login, senha, tipo_usuario)
            if usuario:
                messagebox.showinfo("Sucesso", f"Usuário {usuario.nome} cadastrado com sucesso!")
                if self.master:
                    self.master.deiconify()
                self.destroy()
            else:
                messagebox.showerror("Erro", "Não foi possível realizar o cadastro.")
                self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {str(e)}")
            self.limpar_campos()
        
    def limpar_campos(self):
        self.txt_nome.delete(0, END)
        self.txt_cpf.delete(0, END)
        self.txt_login.delete(0, END)
        self.txt_senha.delete(0, END)
        self.combo_tipo.set(TipoUsuario.COMUM.value)
