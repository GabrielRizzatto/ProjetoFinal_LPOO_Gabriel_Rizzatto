import tkinter as tk
from tkinter import Button, Label, Frame

class SobreView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("450x320")
        self.title("Sobre o Sistema")
        self.resizable(False, False)

        frame_conteudo = Frame(self, padx=20, pady=20)
        frame_conteudo.pack(expand=True, fill="both")

        lbl_titulo = Label(frame_conteudo, text="Sistema de Gestão de Biblioteca", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=(0, 15))

        descricao = (
            "Aplicação desktop desenvolvida para informatizar e modernizar\n"
            "o controlo de acervos e empréstimos literários.\n\n"
            "Garante a integridade dos dados e um controlo de acesso seguro,\n"
            "aplicando os padrões MVC, Strategy e DAO."
        )
        lbl_desc = Label(frame_conteudo, text=descricao, font=("Arial", 10), justify="center")
        lbl_desc.pack(pady=10)

        lbl_autor = Label(frame_conteudo, text="Desenvolvido por: Gabriel Rizzatto", font=("Arial", 11, "italic"))
        lbl_autor.pack(pady=10)

        lbl_disciplinas = Label(frame_conteudo, text="Disciplinas: LPOO e APS", font=("Arial", 10))
        lbl_disciplinas.pack(pady=5)

        btn_fechar = Button(frame_conteudo, text="Fechar", command=self.voltar, width=15)
        btn_fechar.pack(side="bottom", pady=10)

        self.protocol("WM_DELETE_WINDOW", self.voltar)

    def voltar(self):
        if self.master:
            self.master.deiconify()
        self.destroy()