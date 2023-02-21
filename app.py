import customtkinter as ctk
from tkinter import *
from customtkinter import (CTkLabel,CTkEntry,CTkButton,CTkTabview)
from PySimpleGUI import  popup_error



ctk.set_appearance_mode(mode_string="light")
# ctk.set_default_color_theme("green")


WIDTH = 640
HEIGHT = 520

class JanelaPrincipal():
    def __init__(self) -> None:
        self.__root = ctk.CTk()
        self.__root.resizable(False,False)
        self.__root.geometry("{}x{}".format(WIDTH,HEIGHT)) #TAMANHO DA JANELA
        
        self.menubar = Menu(self.__root)
        
        self.menu_cadastro = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Cadastrar',menu=self.menu_cadastro)
        self.menu_cadastro.add_command(label='produto',command=self.cadastro_produtos)
        self.menu_cadastro.add_command(label='cliente',command=None)
        
        
        

        # LOOP PRINCIPAL DA JANELA
        self.__root.config(menu=self.menubar)
        self.__root.mainloop()
        
    def cadastro_produtos(self):
        self.__top = ctk.CTkToplevel()
        self.lbl_nome = CTkLabel(self.__top,text='Nome Produto:')
        self.inp_nome = CTkEntry(self.__top)
        self.lbl_validade = CTkLabel(self.__top,text='Validade:')
        self.inp_validade = CTkEntry(self.__top)
        self.lbl_quantidade = CTkLabel(self.__top,text='Quantidade:')
        self.inp_quantidade = CTkEntry(self.__top)
        self.lbl_valor = CTkLabel(self.__top,text='valor(R$):')
        self.inp_valor = CTkEntry(self.__top)
        self.btn_cadastrar = CTkButton(self.__top,text="Salvar",command=self.salvar_dados)
        self.btn_limpar = CTkButton(self.__top,text="Limpar",command=self.limpar_dados)
        self.lbl_nome.grid(row=0,column=0,pady=8,padx=8)
        self.inp_nome.grid(row=0,column=1,pady=8,padx=8)
        self.lbl_validade.grid(row=1,column=0,pady=8,padx=8)
        self.inp_validade.grid(row=1,column=1,pady=8,padx=8)
        self.lbl_quantidade.grid(row=2,column=0,pady=8,padx=8)
        self.inp_quantidade.grid(row=2,column=1,pady=8,padx=8)
        self.lbl_valor.grid(row=3,column=0,pady=8,padx=8)
        self.inp_valor.grid(row=3,column=1,pady=8,padx=8)
        self.btn_cadastrar.grid(row=4,column=0,padx=8,pady=8)
        self.btn_limpar.grid(row=4,column=1,padx=8,pady=8)
        
        self.__top.mainloop()
    def salvar_dados(self):
        nome = self.inp_nome.get()
        validade = self.inp_validade.get()
        quantidade = self.inp_quantidade.get()
        valor = self.inp_valor.get()
        dado = dict((('nome',nome),('data_validade',validade),('quantidade',quantidade),("valor",valor)))
        
        for k,v in dado.items():
            if len(v) != 0:
                continue
            else:
                popup_error("Msg")
                break 
        
    # SEM IMPLEMENTAÇÃO
    def limpar_dados(self):
        ...
        
        
        print("Limpo")
app = JanelaPrincipal()

