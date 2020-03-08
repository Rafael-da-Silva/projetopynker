#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#    Mar 08, 2020 03:59:16 PM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as tkmsg

import tela

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
            tela.vp_start_gui()
        else:
            tkmsg.showerror('Erro', 'Usuário ou senha incorretos')

if __name__ == '__main__':
    vp_start_gui()





