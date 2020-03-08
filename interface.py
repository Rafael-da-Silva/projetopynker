#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#    Mar 08, 2020 03:59:16 PM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as tkmsg
from tkinter import filedialog
import base64
from base64 import b64encode

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = LoginRetornoPynker (root)
    init(root, top)
    root.resizable(0,0)      #will disable max/min tab of window
    root.mainloop()

w = None
def create_LoginRetornoPynker(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_LoginRetornoPynker(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = LoginRetornoPynker (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_LoginRetornoPynker():
    global w
    w.destroy()
    w = None

class LoginRetornoPynker:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 12 -weight bold"

        top.geometry("403x204+334+191")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Login Retorno Pynker")
        top.configure(background="#d9d9d9")

        self.FrameLogin = tk.Frame(top)
        self.FrameLogin.place(relx=0.025, rely=0.049, relheight=0.907, relwidth=0.955)
        self.FrameLogin.configure(relief='groove')
        self.FrameLogin.configure(borderwidth="2")
        self.FrameLogin.configure(relief="groove")
        self.FrameLogin.configure(background="#d9d9d9")

        self.lblusuariologar = tk.Label(self.FrameLogin)
        self.lblusuariologar.place(relx=0.026, rely=0.162, height=27, width=85)
        self.lblusuariologar.configure(background="#d9d9d9")
        self.lblusuariologar.configure(disabledforeground="#a3a3a3")
        self.lblusuariologar.configure(font=font9)
        self.lblusuariologar.configure(foreground="#000000")
        self.lblusuariologar.configure(text='''USUÁRIO :''')

        self.lblsenhalogar = tk.Label(self.FrameLogin)
        self.lblsenhalogar.place(relx=0.026, rely=0.432, height=27, width=68)
        self.lblsenhalogar.configure(background="#d9d9d9")
        self.lblsenhalogar.configure(disabledforeground="#a3a3a3")
        self.lblsenhalogar.configure(font=font9)
        self.lblsenhalogar.configure(foreground="#000000")
        self.lblsenhalogar.configure(text='''SENHA :''')

        self.txtusuariologar = tk.Entry(self.FrameLogin)
        self.txtusuariologar.place(relx=0.312, rely=0.162, height=30, relwidth=0.66)
        self.txtusuariologar.configure(background="white")
        self.txtusuariologar.configure(disabledforeground="#a3a3a3")
        self.txtusuariologar.configure(font="TkFixedFont")
        self.txtusuariologar.configure(foreground="#000000")
        self.txtusuariologar.configure(insertbackground="black")

        self.txtsenhalogar = tk.Entry(self.FrameLogin, show="*")
        self.txtsenhalogar.place(relx=0.312, rely=0.432, height=30, relwidth=0.66)
        self.txtsenhalogar.configure(background="white")
        self.txtsenhalogar.configure(disabledforeground="#a3a3a3")
        self.txtsenhalogar.configure(font="TkFixedFont")
        self.txtsenhalogar.configure(foreground="#000000")
        self.txtsenhalogar.configure(insertbackground="black")

        self.btnentrarlogin = tk.Button(self.FrameLogin)
        self.btnentrarlogin.place(relx=0.649, rely=0.649, height=44, width=117)
        self.btnentrarlogin.configure(activebackground="#ececec")
        self.btnentrarlogin.configure(activeforeground="#000000")
        self.btnentrarlogin.configure(background="#d9d9d9")
        self.btnentrarlogin.configure(disabledforeground="#a3a3a3")
        self.btnentrarlogin.configure(font=font9)
        self.btnentrarlogin.configure(foreground="#000000")
        self.btnentrarlogin.configure(highlightbackground="#d9d9d9")
        self.btnentrarlogin.configure(highlightcolor="black")
        self.btnentrarlogin.configure(pady="0")
        self.btnentrarlogin.configure(text='''ENTRAR''')
        self.btnentrarlogin.configure(command = self.EntraLogin)


    
    def EntraLogin(self):
        if(self.txtusuariologar.get() == "" and self.txtsenhalogar.get() == ""):
            tkmsg.showwarning('Erro', 'Não é possível logar sem usuário e senha')
        elif(self.txtsenhalogar.get() == ""):
            tkmsg.showwarning('Erro', 'Não é possível logar sem senha')
        elif(self.txtusuariologar.get() == ""):
            tkmsg.showwarning('Erro', 'Não é possível logar sem usuário')
        elif(self.txtusuariologar.get() == "pynker" and self.txtsenhalogar.get() == "efetivaeu"):
            print("Próxima tela")
            destroy_window()
            vp_start_gui_tela()
        else:
            tkmsg.showerror('Erro', 'Usuário ou senha incorretos')


###############################################################################################################################3

global localizacao_arquivo

def init_tela(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window_tela():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def vp_start_gui_tela():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TelaPrincipal (root)
    init_tela(root, top)
    root.resizable(0,0)      #will disable max/min tab of window
    root.mainloop()

w = None
def create_TelaPrincipal(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_TelaPrincipal(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = TelaPrincipal (w)
    init_tela(w, top, *args, **kwargs)
    return (w, top)

def destroy_TelaPrincipal():
    global w
    w.destroy()
    w = None

class TelaPrincipal:

    def encode_base64(self, texto):
        encodedBytes = base64.b64encode(texto.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        return encodedStr

    def verificaparametrosvazios(self):
        if(self.txtnomeusuariosistema.get() == "" and self.txtsiglasistema.get() == "" and self.txttecnologia.get() == "" and self.txtversao.get() == "" and self.txtsiglasistema2.get() == ""):
            tkmsg.showwarning('Erro', 'Não é possível realizar a validação do script sem os parâmetros necessários. Todos são obrigatórios')
            return False

    def verificaalgumparametrovazio(self):
        if(self.txtnomeusuariosistema.get() == "" or self.txtsiglasistema.get() == "" or self.txttecnologia.get() == "" or self.txtversao.get() == "" or self.txtsiglasistema2.get() == ""):
            tkmsg.showwarning('Erro', 'Todos os parâmetros são obrigatórios. Não se esqueça de nenhum')
            return False

    def verificacaminhoarquivovazio(self):
        localizacao = self.txtnomearquivo.get()
        if (localizacao == ""):
            tkmsg.showwarning('Erro', 'Não é possível realizar a validação sem o script. Insira um script válido')
            return False
        else:
            return localizacao
            

    def submeter(self):

        a = True
        b = True
        c = True

        if(True):
            b = self.verificaparametrosvazios()
        if(b != False):
            a = self.verificaalgumparametrovazio()
        
        c = self.verificacaminhoarquivovazio()

        if(a == False or b == False or c == False):
            print('Não vai continuar até todas as informações serem preenchidas')
        else:  

            self.areatexto.config(state="normal")
            self.areatexto.delete(1.0 , END)
            self.areatexto.config(state="disabled")

            try:
                arquivo = open(c, 'r')
                texto = arquivo.read()
                texto_codificado = self.encode_base64(texto)
            except:
                tkmsg.showerror('Erro', "Não foi possível ler e codificar o arquivo. Insira um script válido")
        

            self.printa_conteudo_digitado()
            print(texto_codificado)
            mt = texto_codificado + texto_codificado + texto_codificado + texto_codificado + texto_codificado

            self.areatexto.config(state="normal")
            self.areatexto.insert(tk.INSERT, mt)
            self.areatexto.config(state="disabled")


    def encontra_arquivo(self):
        
        self.areatexto.config(state="normal")
        self.areatexto.delete(1.0 , END)
        self.areatexto.config(state="disabled")


        self.txtnomearquivo.delete(0, 'end')
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("all files","*.*")))
        print (root.filename)
        localizacao_arquivo = root.filename
        self.txtnomearquivo.insert(0,str(localizacao_arquivo))        
        

    def printa_conteudo_digitado(self):
        nome_usuario = self.txtnomeusuariosistema.get()
        sigla = self.txtsiglasistema.get()
        tecnologia = self.txttecnologia.get()
        versao = self.txtversao.get()
        sigla2 = self.txtsiglasistema2.get()
        return (print(nome_usuario + "  " + sigla + "   " + tecnologia + "  " + versao + "  " + sigla2))

        
    def fechar_janela(self):
        if(tkmsg.askyesno("Confirmação", "Tem certeza que deseja fechar?")):
        #exit()
            sys.exit()

  
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("615x567+487+71")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Retorno API Pynker")
        top.configure(background="#d9d9d9")

        self.Tela1 = tk.Frame(top)
        self.Tela1.place(relx=0.013, rely=0.018, relheight=0.961
                , relwidth=0.976)
        self.Tela1.configure(relief='groove')
        self.Tela1.configure(borderwidth="2")
        self.Tela1.configure(relief="groove")
        self.Tela1.configure(background="#d9d9d9")

        self.lblnomeusuariosistema = tk.Label(self.Tela1)
        self.lblnomeusuariosistema.place(relx=0.01, rely=0.033, height=31, width=84)
        self.lblnomeusuariosistema.configure(activebackground="#f0f0f0f0f0f0")
        self.lblnomeusuariosistema.configure(background="#d9d9d9")
        self.lblnomeusuariosistema.configure(disabledforeground="#a3a3a3")
        self.lblnomeusuariosistema.configure(foreground="#000000")
        self.lblnomeusuariosistema.configure(text='''Nome usuario''')

        self.txtnomeusuariosistema = tk.Entry(self.Tela1)
        self.txtnomeusuariosistema.place(relx=0.383, rely=0.037,height=20, relwidth=0.597)
        self.txtnomeusuariosistema.configure(background="white")
        self.txtnomeusuariosistema.configure(disabledforeground="#a3a3a3")
        self.txtnomeusuariosistema.configure(font="TkFixedFont")
        self.txtnomeusuariosistema.configure(foreground="#000000")
        self.txtnomeusuariosistema.configure(insertbackground="black")

        self.lblsiglasistema = tk.Label(self.Tela1)
        self.lblsiglasistema.place(relx=0.01, rely=0.117, height=21, width=181)
        self.lblsiglasistema.configure(background="#d9d9d9")
        self.lblsiglasistema.configure(disabledforeground="#a3a3a3")
        self.lblsiglasistema.configure(foreground="#000000")
        self.lblsiglasistema.configure(text='''Sigla XXXXXXXXXXXXXXXXXXXXX''')

        self.txtsiglasistema = tk.Entry(self.Tela1)
        self.txtsiglasistema.place(relx=0.383, rely=0.109,height=20, relwidth=0.597)
        self.txtsiglasistema.configure(background="white")
        self.txtsiglasistema.configure(disabledforeground="#a3a3a3")
        self.txtsiglasistema.configure(font="TkFixedFont")
        self.txtsiglasistema.configure(foreground="#000000")
        self.txtsiglasistema.configure(insertbackground="black")

        self.lbltecnologia = tk.Label(self.Tela1)
        self.lbltecnologia.place(relx=0.01, rely=0.189, height=21, width=172)
        self.lbltecnologia.configure(background="#d9d9d9")
        self.lbltecnologia.configure(disabledforeground="#a3a3a3")
        self.lbltecnologia.configure(foreground="#000000")
        self.lbltecnologia.configure(text='''Tecnologia XXXXXXXXXXXXXXX''')

        self.txttecnologia = tk.Entry(self.Tela1)
        self.txttecnologia.place(relx=0.383, rely=0.183, height=20, relwidth=0.597)
        self.txttecnologia.configure(background="white")
        self.txttecnologia.configure(disabledforeground="#a3a3a3")
        self.txttecnologia.configure(font="TkFixedFont")
        self.txttecnologia.configure(foreground="#000000")
        self.txttecnologia.configure(insertbackground="black")

        self.lblversao = tk.Label(self.Tela1)
        self.lblversao.place(relx=0.01, rely=0.262, height=21, width=167)
        self.lblversao.configure(background="#d9d9d9")
        self.lblversao.configure(disabledforeground="#a3a3a3")
        self.lblversao.configure(foreground="#000000")
        self.lblversao.configure(text='''Versao xxxxxxxxxxxxxxxxxxxx''')

        self.txtversao = tk.Entry(self.Tela1)
        self.txtversao.place(relx=0.383, rely=0.257,height=20, relwidth=0.597)
        self.txtversao.configure(background="white")
        self.txtversao.configure(disabledforeground="#a3a3a3")
        self.txtversao.configure(font="TkFixedFont")
        self.txtversao.configure(foreground="#000000")
        self.txtversao.configure(insertbackground="black")

        self.lblsigladois = tk.Label(self.Tela1)
        self.lblsigladois.place(relx=0.01, rely=0.336, height=21, width=184)
        self.lblsigladois.configure(background="#d9d9d9")
        self.lblsigladois.configure(disabledforeground="#a3a3a3")
        self.lblsigladois.configure(foreground="#000000")
        self.lblsigladois.configure(text='''Sigla XXXXXXXXXXXXXXXXXXXXX''')

        self.txtsiglasistema2 = tk.Entry(self.Tela1)
        self.txtsiglasistema2.place(relx=0.383, rely=0.329,height=20, relwidth=0.597)
        self.txtsiglasistema2.configure(background="white")
        self.txtsiglasistema2.configure(disabledforeground="#a3a3a3")
        self.txtsiglasistema2.configure(font="TkFixedFont")
        self.txtsiglasistema2.configure(foreground="#000000")
        self.txtsiglasistema2.configure(insertbackground="black")

        self.btnarquivo = tk.Button(self.Tela1)
        self.btnarquivo.place(relx=0.843, rely=0.403, height=24, width=83)
        self.btnarquivo.configure(activebackground="#ececec")
        self.btnarquivo.configure(activeforeground="#000000")
        self.btnarquivo.configure(background="#d9d9d9")
        self.btnarquivo.configure(disabledforeground="#a3a3a3")
        self.btnarquivo.configure(foreground="#000000")
        self.btnarquivo.configure(highlightbackground="#d9d9d9")
        self.btnarquivo.configure(highlightcolor="black")
        self.btnarquivo.configure(pady="0")
        self.btnarquivo.configure(text='''Arquivo''')
        self.btnarquivo.configure(command = self.encontra_arquivo)

        self.txtnomearquivo = tk.Entry(self.Tela1)
        self.txtnomearquivo.place(relx=0.017, rely=0.404, height=20, relwidth=0.79)
        self.txtnomearquivo.configure(background="white")
        self.txtnomearquivo.configure(disabledforeground="#a3a3a3")
        self.txtnomearquivo.configure(font="TkFixedFont")
        self.txtnomearquivo.configure(foreground="#000000")
        self.txtnomearquivo.configure(insertbackground="black")
        
        self.btnsubmeter = tk.Button(self.Tela1)
        self.btnsubmeter.place(relx=0.822, rely=0.470, height=30, width=95)
        self.btnsubmeter.configure(activebackground="#ececec")
        self.btnsubmeter.configure(activeforeground="#000000")
        self.btnsubmeter.configure(background="#d9d9d9")
        self.btnsubmeter.configure(disabledforeground="#a3a3a3")
        self.btnsubmeter.configure(foreground="#000000")
        self.btnsubmeter.configure(highlightbackground="#d9d9d9")
        self.btnsubmeter.configure(highlightcolor="black")
        self.btnsubmeter.configure(pady="0")
        self.btnsubmeter.configure(text='''Submeter''')
        self.btnsubmeter.configure(command = self.submeter)

        self.bntfechar = tk.Button(self.Tela1)
        self.bntfechar.place(relx=0.843, rely=0.946, height=24, width=86)
        self.bntfechar.configure(activebackground="#ececec")
        self.bntfechar.configure(activeforeground="#000000")
        self.bntfechar.configure(background="#d9d9d9")
        self.bntfechar.configure(disabledforeground="#a3a3a3")
        self.bntfechar.configure(foreground="#000000")
        self.bntfechar.configure(highlightbackground="#d9d9d9")
        self.bntfechar.configure(highlightcolor="black")
        self.bntfechar.configure(pady="0")
        self.bntfechar.configure(text='''Fechar''')
        self.bntfechar.configure(command = self.fechar_janela)

        self.areatexto = tk.Text(top,wrap=NONE)
        self.areatexto.place(relx=0.033, rely=0.533, relheight=0.375, relwidth=0.938)
        self.areatexto.configure(background="white")
        self.areatexto.configure(font="TkTextFont")
        self.areatexto.configure(foreground="black")
        self.areatexto.configure(highlightbackground="#d9d9d9")
        self.areatexto.configure(highlightcolor="black")
        self.areatexto.configure(insertbackground="black")
        self.areatexto.configure(selectbackground="#c4c4c4")
        self.areatexto.configure(selectforeground="black")
        self.areatexto.configure(wrap="word")
        self.areatexto.config(state="disabled")

        #self.vscroll = Scrollbar( self.areatexto, orient=VERTICAL, command=self.areatexto.yview)
        #self.areatexto['yscroll'] = self.vscroll.set
        #self.vscroll.pack(side="right", fill="y")

if __name__ == '__main__':
    vp_start_gui()






#if __name__ == '__main__':
#    vp_start_gui()





