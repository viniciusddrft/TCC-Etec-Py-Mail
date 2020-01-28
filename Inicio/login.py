from tkinter import *
from tkinter.messagebox import *
import os
import sys


janela = Tk()
janela.title("Py - Login")
janela.geometry("200x100+100+100")
janela.resizable(False,False)


#============================================================

def entrar():
	log = str(ed1.get())
	se = str(ed2.get())

	if log == "admin" and se =="admin":
		showinfo(title="Login",message="Acesso Liberado")
		os.system("python3 /home/viniciusddrft/.TCC/Inicio/GUI.py")

	else:
		showinfo(title="Login",message="Acesso Negado")

#============================================================

lb1 = Label(janela, text="Login: ")
lb2 = Label(janela, text="Senha: ")

ed1 = Entry(janela,)
ed2 = Entry(janela, show='*')

bt1 = Button(janela, text="Confirmar", command= entrar)

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt1.grid(row=2, column=1)


janela.mainloop()
