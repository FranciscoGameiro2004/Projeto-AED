"""
doc string
"""

#Bibloiotecas inportadasa inicio
import os  # biblioteca os
import datetime
from tkinter import *  # biblioteca tkinter
from tkinter import ttk # biblioteca tkinter treeview
from tkinter import messagebox # biblioteca tkinter messagebox
from tkinter import filedialog
from PIL import ImageTk,Image    # Imagens .jpg ou .png
#Bibloiotecas inportadads fim

#Arquivos Funções externas inicio
from login import *

#Arquivos Funções externas fim

#Variaveis globais inicio
pasta = "files"
ficheiro = "files/acessos.txt" #Numero;data_sistema;hora_sistema;tipo_acesso
#Variaveis globais fim

#Verfica a existencia da pasta inicio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim


def criarConta(name,senha,conta):
    linha = name + ";" + senha + ";" + conta +"\n"
    acessos = open(ficheiro, "a", encoding="utf8")
    acessos.write(linha)
    acessos.close()





def telaAreaPessoal():
    global login
    global img

    panelProvas = PanedWindow(window, width = 400, height= 450)
    panelProvas.place(x=300, y= 0)

    ctnImagemPerfil = Canvas(panelProvas,width=60,height=60)
    ctnImagemPerfil.place(x=10,y=10)
    img = PhotoImage(file="imagens/person_50x50.png")
    ctnImagemPerfil.create_image(30, 30, anchor= "center", image = img)

    txtInfo = Label(panelProvas, width = 0, height = 3, text = "Primeiro Nome:\n             Genero:\n   Tipo de conta:", font = ("arial", 12))
    txtInfo.place(x = 80,y = 10)
    
    name = StringVar()
    name.set("desconhecido")
    txtNome = Entry(panelProvas, width=20,justify=CENTER,state=DISABLED, textvariable=name)
    txtNome.place(x=195, y = 10)
    
    gender = StringVar()
    gender.set("outro")
    txtGenero = Entry(panelProvas, width=20,justify=CENTER,state=DISABLED, textvariable=gender)
    txtGenero.place(x=195, y = 30)

    type = StringVar()
    type.set("desconhecido")
    txtConta= Entry(panelProvas, width=20,justify=CENTER,state=DISABLED, textvariable=type)
    txtConta.place(x=195, y = 50)



#codigo principal inicio
window = Tk()

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1100                             # tamanho (pixeis) da window a criar
appHeight = 450
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title("Programa")
#-----------------------------------------------------------------------------------------------------------------------------#
menubar = Menu(window)
#-----------------------------------------------------------------------------------------------------------------------------#
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Movimentos")
filemenu.add_command(label="Consultas")
filemenu.add_command(label="teste",command=criarConta)
filemenu.add_command(label="CLS", command= lambda: os.system("cls"))
filemenu.add_command(label="Exit", command=window.destroy)
window.config(menu=filemenu)

#-----------------------------------------------------------------------------------------------------------------------------#
panel1 = PanedWindow(window, bg = "black",width = 300, height = 450)
panel1.place(x=0 , y=0)
#Area pessoal-----------------------------------------------------------------------------------------------------------------#
imageIco1 = PhotoImage(file = "imagens/person_50x50.png" )
btnOpcao1 = Button(panel1, text = "Area\nPessoal", image = imageIco1, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=telaAreaPessoal)
btnOpcao1.place (x=40, y=5)
#-----------------------------------------------------------------------------------------------------------------------------#
imageIco2 = PhotoImage(file = "imagens/person_50x50.png" )
btnOpcao2 = Button(panel1, text = "Gerir\ntarefas", image = imageIco2, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    )
btnOpcao2.place (x=40, y=95)
"""
#-----------------------------------------------------------------------------------------------------------------------------#
imageIco3 = PhotoImage(file = "imagens/person_50x50.png" )
btnOpcao3 = Button(panel1, text = "Consultar\ntarefas", image = imageIco3, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=lambda: print("btnOpcao3"))
btnOpcao3.place (x=40, y=185)
#-----------------------------------------------------------------------------------------------------------------------------#
imageIco4 = PhotoImage(file = "imagens/person_50x50.png" )
btnOpcao4 = Button(panel1, text = "Admin", image = imageIco4, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=lambda: print("btnOpcao4"))
btnOpcao4.place (x=40, y=275)
"""
#-----------------------------------------------------------------------------------------------------------------------------#
imageIco5 = PhotoImage(file = "imagens/person_50x50.png" )
btnOpcao5 = Button(panel1, text = "Sair", image = imageIco2, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=window.destroy)
btnOpcao5.place (x=40, y=365)

window.mainloop()