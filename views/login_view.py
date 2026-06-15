import tkinter as tk
from tkinter import messagebox, Button, Entry, Label, Frame, END
from controllers.usuario_controller import UsuarioController
from views.livros_view import LivrosView

class LoginView(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.controller = UsuarioController()
        self.geometry("500x300")
        self.usuario = None

        frame_login = Frame(self)
        frame_login.pack(expand=True)  

        lbl_login = Label(frame_login, text="Login:", font=("Arial", 10))
        self.txt_login = Entry(frame_login)
        lbl_login.pack()
        self.txt_login.pack()

        lbl_senha = Label(frame_login, text="Senha:", font=("Arial", 10))
        self.txt_senha = Entry(frame_login, show="*")
        lbl_senha.pack()
        self.txt_senha.pack()

        btn_entrar = Button(frame_login, text="Entrar", command=self.login, font=("Arial", 10))
        btn_entrar.pack(pady=10)


        btn_voltar = Button(self, text="Voltar", command=self.voltar, font=("Arial", 10))
        btn_voltar.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

        self.protocol("WM_DELETE_WINDOW", self.voltar)

    def login(self):
        usuario_txt = self.txt_login.get()
        senha_txt = self.txt_senha.get()
        usuario = self.controller.efetuar_login(usuario_txt, senha_txt)

        if not usuario:
            messagebox.showerror(title="Erro", message="Usuario ou Senha incorreto")
            self.txt_login.delete(0, END)
            self.txt_senha.delete(0, END)
            return
        
        self.usuario = usuario

        self.withdraw()
        LivrosView(self.usuario, master=self)



    def voltar(self):
        self.master.deiconify()
        self.destroy()
        
