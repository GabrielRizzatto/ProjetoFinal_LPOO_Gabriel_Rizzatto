import tkinter as tk
import os
import sys
from views.cadastro_usuario_view import CadastroUsuarioView
from views.login_view import LoginView
from dao.map import mapear_tabelas
from tkinter import Button, Frame

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão de Biblioteca")
        self.geometry("500x300")
        frame_btn = Frame(self)
        frame_btn.pack(expand=True)
        
        self.btn_login = Button(frame_btn, text='Entrar', command=self.abrir_login, font=("Arial", 10))
        self.btn_login.pack(pady=10)

        self.btn_cadastrar = Button(frame_btn, text='Cadastrar Usuario', command=self.abrir_cadastro, font=("Arial", 10))
        self.btn_cadastrar.pack(pady=10)

    def abrir_login(self):
        self.withdraw()
        LoginView(master=self)

    def abrir_cadastro(self):
        self.withdraw()
        CadastroUsuarioView(master=self)


if __name__ == "__main__":
    mapear_tabelas()
    app = JanelaPrincipal()
    app.mainloop()
    
