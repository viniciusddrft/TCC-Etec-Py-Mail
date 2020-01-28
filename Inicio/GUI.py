from tkinter import *
import os
import sys
#---------------------------


def fechar_software():
	sys.exit()
#------------------------------------
def abrir_buscador():
    os.system("cd ..")
    os.system("xterm -sb -e python3 /home/viniciusddrft/.TCC/Aplicacoes/busca.py")
#------------------------------------
def abrir_enviador():
	os.system("xterm -sb -e python3 /home/viniciusddrft/.TCC/Aplicacoes/envio.py")
#------------------------------------
def creditos():
	os.system("xterm -sb -e python3 /home/viniciusddrft/.TCC/Documentacao/creditos.py")
#------------------------------------
def separador():
	os.system("xterm -sb -e python3 /home/viniciusddrft/.TCC/Aplicacoes/separador.py")
#------------------------------------
def documentacao():
	os.system("xterm -sb -e python3 /home/viniciusddrft/.TCC/Documentacao/documentacao.py")

#------------------------------------
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

#------------------------------------

#------------------------------------
janela1 = Tk()
janela1.title("Py - Mail")
janela1.geometry("350x280")
janela1.resizable(False,False)
janela1.configure(background="gray")
#------------------------------------
texto1 = Label(janela1, text="Instruções")
texto1.pack()
texto1.place(x= 150, y=20)
#------------------------------------
texto_botao1 = StringVar()
texto_botao1.set('Documentacão')

btn1 = Button(janela1, textvariable=texto_botao1, width=27, height=-4, command=documentacao)
btn1.pack()
btn1.place(x=60, y=50)
#------------------------------------
texto_botao2 = StringVar()
texto_botao2.set('Créditos')

btn2 = Button(janela1, textvariable=texto_botao2, width=11, height=-2, command=creditos)
btn2.pack()
btn2.place(x=60, y=90)

#------------------------------------
texto2 = Label(janela1, text="Funções")
texto2.pack()
texto2.place(x=150, y=140)
#------------------------------------
texto_botao3 = StringVar()
texto_botao3.set("Buscar E-mails")

btn3 = Button(janela1, textvariable=texto_botao3, command=abrir_buscador)
btn3.pack()
btn3.place(x=60, y=170)

#------------------------------------
texto_botao4 = StringVar()
texto_botao4.set('enviar E-mails')

btn4 = Button(janela1, textvariable=texto_botao4, command=abrir_enviador)
btn4.pack()
btn4.place(x=187, y=170)
#------------------------------------
texto_botao5 = StringVar()
texto_botao5.set('Separar E-mails')

btn5 = Button(janela1, textvariable=texto_botao5, width=27, height=-4, command=separador)
btn5.pack()
btn5.place(x=60 , y=207)

#------------------------------------

texto_botao6 = StringVar()
texto_botao6.set('Sair')

btn6 = Button(janela1, textvariable=texto_botao6, width=11, height=-2, command=fechar_software)

btn6.pack()
btn6.place(x=187, y=90)
#------------------------------------
#photo = PhotoImage(file = "imagem.png")
#label = Label(janela1, image = photo)
#label.pack()


status = Label(janela1,text = "Seja bem vindo..." ,bd =1, relief = SUNKEN,anchor =W )
status.pack(side = BOTTOM, fill = X)


menubar = Menu(janela1)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Documentação", command=documentacao)
filemenu.add_command(label="Créditos", command=creditos)

filemenu.add_separator()

filemenu.add_command(label="Sair", command=janela1.quit)
menubar.add_cascade(label="Instruções", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Buscar E-mails", command=abrir_buscador)
editmenu.add_command(label="Enviar E-mails", command=abrir_enviador)
editmenu.add_command(label="Separar E-mails", command=separador)


menubar.add_cascade(label="Funções", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)



janela1.config(menu=menubar)
janela1.mainloop()


#, padx=10, pady=10,side=RIGHT
