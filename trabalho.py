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
ficheiro = "files/acessos.txt" 
login = 0
#Variaveis globais fim

#Verfica a existencia da pasta inicio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim

#tela Area Pessoal inicio
def telaAreaPessoal():
    global login
    global img
    
    if login==0:
        panelProvas = PanedWindow(window, width = 400, height= 450)
        panelProvas.place(x=300, y= 0)

        ctnImagemPerfil = Canvas(panelProvas,width=60,height=60)
        ctnImagemPerfil.place(x=10,y=10)
        img = PhotoImage(file="imagens/person_50x50.png")
        ctnImagemPerfil.create_image(30, 30, anchor= "center", image = img)

        txtInfoNome = Label(panelProvas, width = 0, height = 1, text = "Nome:", font = ("arial", 12))
        txtInfoNome.place(x = 136,y = 8)
        txtInfoGenero = Label(panelProvas, width = 0, height = 1, text = "Genero:", font = ("arial", 12))
        txtInfoGenero.place(x = 127,y = 27)
        txtInfoConta = Label(panelProvas, width = 0, height = 1, text = "Tipo de Conta:", font = ("arial", 12))
        txtInfoConta.place(x = 80,y = 47)
        
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

        frame0 = LabelFrame(panelProvas,text="Descrição",width=310,height=150, fg="blue")
        frame0.place(x=10,y=70)
        txtDescricao = Text(frame0, width=36, height= 7)
        txtDescricao.place(x=5,y=5)
    
        frame1 = LabelFrame(panelProvas,text="configurações",width=310,height=150, fg="blue")
        frame1.place(x=10,y=220)
        
        txtInfo = Label(frame1, width = 0, height = 3, text = "             Nome:\n           Genero:\n Tipo de conta:", font = ("arial", 12))
        txtInfo.place(x = 10,y = 10)

        name = StringVar()
        txtNome = Entry(frame1, width=20,justify=CENTER, textvariable=name)
        txtNome.place(x=150, y = 10)
        
        gender = StringVar()
        txtGenero = Entry(frame1, width=20,justify=CENTER, textvariable=gender)
        txtGenero.place(x=150, y = 30)

        type = StringVar()
        txtConta= Entry(frame1, width=20,justify=CENTER, textvariable=type)
        txtConta.place(x=150, y = 50)

        btnAtualizar = Button(frame1, width=30,height=2,justify=CENTER,text="Atualizar",  font = ("arial", 11))
        btnAtualizar.place(x=10, y=80)

    elif login==1:
        panelProvas = PanedWindow(window,bg= "green", width = 400, height= 450)
        panelProvas.place(x=300, y= 0)

        ctnImagemPerfil = Canvas(panelProvas,width=60,height=60)
        ctnImagemPerfil.place(x=10,y=10)
        img = PhotoImage(file="imagens/person_50x50.png")
        ctnImagemPerfil.create_image(30, 30, anchor= "center", image = img)
#tela Area Pessoal fim

#tela Gerir Tarefas inicio
def telaGerirTarefas():
    panelProvas = PanedWindow(window,bg= "red", width = 400, height= 450)
    panelProvas.place(x=300, y= 0)


#tela Gerir Tarefas fim

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
                    command=telaGerirTarefas)
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