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
from tkcalendar import DateEntry
from PIL import ImageTk,Image    # Imagens .jpg ou .png
from conta import *
from timing import *
#Bibloiotecas inportadads fim

os.system("cls")

#Variaveis globais inicio
pasta = "files"
ficheiroUsurios = "files/acessos.txt"
userAtual = '' # Esta variável permite determinar qual é o utilizador ativo no momento.
#---#
login = 0
status = 0
#Verfica a existencia da pasta inicio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim

"""
#----------------------------------------------------------------#
"""
def criarConta(username, password,gender,type):
    """
    print("Print Criar Conta")
    print(username)
    print(password)
    print(gender)
    print(type)
    """

    if not contaExistente(username):
        if str(password).find(';') == -1:
            obs = "Readme"
            linha = username + ";" + password + ";"+ gender + ";" + type + ";" + obs +  "\n"
            #print(linha)
            acessos = open(ficheiroUsurios, "a", encoding="utf8")
            acessos.write(linha)
            acessos.close()

            pastaUser = pasta + '/users/' + username
            ficheiroUserLIne = pastaUser +  "/listaTarefas.txt"
            ficheiroUserNoticias = pastaUser +  "/noticias.txt"

            if not os.path.exists(pastaUser):
                #os.chdir('files\\users')
                os.mkdir(pastaUser)

            User = open(ficheiroUserLIne, "a", encoding="utf8")
            User.write("Primeira tarefa\n")
            User.close()

            Noticias = open(ficheiroUserNoticias, "a", encoding="utf8")
            Noticias.write("Primeira notícia\n")
            Noticias.close()
        else:
            msg = 'Não é possível a utilização de caracteres inválidos\nCatacteres inválidos: ;'
            messagebox.showwarning('Estado', msg)
    else:
        msg = 'Já existe uma conta com "{}" como username.'.format(username)
        messagebox.showwarning('Estado', msg)
#----------------------------------------------------------------#
def loginConta(username, txtMenuLoginNome, nameLogin,
               password, txtMenuLoginSenha, passwordLogin,
               nameInfo, genderInfo, typeInfo, txtDescricao,
               btnLogin,
               cbModo,btnMenuCriar_Login_Modos,
               cbGenero,cbTipo):
    #print(username)
    #print(password)
    global login, userAtual, btnOpcao2, btnOpcao3, btnOpcao4
    acessos = open(ficheiroUsurios, "r", encoding="utf8")
    linhas = acessos.readlines()
    acessos.close()
    if login == 0:
        for linha in linhas:
            linha = linha.split(";")
            print(linha)
            if linha[0] == username and linha[1] == password:
                print("Logado")
                #Zona de informação do usuario
                nameInfo.set(linha[0])
                genderInfo.set(linha[2])
                typeInfo.set(linha[3])
                txtDescricao.insert("end" ,linha[4])
                txtDescricao.config(state =DISABLED)

                userAtual = linha[0]
                btnOpcao2.config(state='active')
                btnOpcao3.config(state='active')
                a = tipoDeConta(userAtual)
                if tipoDeConta(userAtual) == 'admin':
                    btnOpcao4.config(state='active')

                #zona de Login
                nameLogin.set("")
                txtMenuLoginNome.config(state = DISABLED)

                passwordLogin.set("")
                txtMenuLoginSenha.config(state = DISABLED)

                cbModo.config(state = DISABLED)
                btnMenuCriar_Login_Modos.config(state = DISABLED)

                btnLogin.config(text = "Logout")
                login = 1
                msg = "Bem vindo " + username 
                messagebox.showinfo(title="Estado",message=msg)
    elif login == 1:
        #user
        userAtual = ''
        nameInfo.set("")
        genderInfo.set("")
        typeInfo.set("")
        txtDescricao.config(state = NORMAL)
        txtDescricao.delete("1.0","end")
        txtDescricao.config(state =DISABLED)
        #selcionar modo
        cbModo.config(state = ACTIVE)
        btnMenuCriar_Login_Modos.config(state = ACTIVE)
        #tela dados login
        txtMenuLoginNome.config(state = NORMAL)
        txtMenuLoginSenha.config(state = NORMAL)
        cbGenero.config(state =DISABLED)
        cbTipo.config(state = DISABLED)

        btnOpcao2.config(state='disabled')
        btnOpcao3.config(state='disabled')
        btnOpcao4.config(state='disabled')

        btnLogin.config(text = "Login")
        login = 0
        msg = "Volte sempre"
        messagebox.showinfo(title="Estado",message=msg)
#----------------------------------------------------------------#
"""
#----------------------------------------------------------------#
"""
def checkModo(cbModo,btnMenuCriar_Login_Modos,lblBase,nameInfo,genderInfo,typeInfo,txtDescricao):
    if cbModo.get() == "Registrar":
        print("Registrar")
        telaAreaPessoalCriar(lblBase,nameInfo, genderInfo, typeInfo, txtDescricao)
    elif cbModo.get() == "Login":
        print("Login")
        telaAreaPessoalLogin(lblBase,nameInfo, genderInfo, typeInfo, txtDescricao,cbModo,btnMenuCriar_Login_Modos)
#----------------------------------------------------------------#
"""
#----------------------------------------------------------------#
"""
def telaAreaPessoalCriar(lblBase,nameInfo, genderInfo, typeInfo, txtDescricao):
    #--------------------------------------------------------------------#
    lblMenuCriar = LabelFrame(lblBase,width=295,height=210,text="Criar Conta")
    lblMenuCriar.place(x=5,y=33)
#---#
    lblMenuCriarNome = Label(lblMenuCriar,width=5,height=1,text="Nome", font = ("arial", 12))
    lblMenuCriarNome.place(x=39,y=5)
    nameCriar = StringVar()
    txtMenuCriarNome = Entry(lblMenuCriar,width=15,justify=CENTER,textvariable=nameCriar)
    txtMenuCriarNome.place(x=20,y=25)
    #----------------------------------------------------------------#
    lblMenuCriarSenha = Label(lblMenuCriar,width=5,height=1,text="Senha", font = ("arial", 12))
    lblMenuCriarSenha.place(x=189,y=5)
    passwordCriar = StringVar()
    txtMenuCriarSenha = Entry(lblMenuCriar,width=15,justify=CENTER, textvariable=passwordCriar)
    txtMenuCriarSenha.place(x=170,y=25)
    #----------------------------------------------------------------#
    lblMenuCriarGenero = Label(lblMenuCriar,width=5,height=1,text="Genero", font = ("arial",12))
    lblMenuCriarGenero.place(x=39,y=44)
    generosLista = ["","Masculino", "Feminino", "Outro"]
    generoCriar = StringVar()
    cbGenero = ttk.Combobox(lblMenuCriar, width=12, value=generosLista, textvariable=generoCriar)
    cbGenero.place(x=20,y=65)
    #----------------------------------------------------------------#
    lblMenuCriarTipo = Label(lblMenuCriar,width=13,height=1,text="Tipos de conta", font = ("arial",12))
    lblMenuCriarTipo.place(x=155,y=44)
    tiposLista = ["","Comum","Profissional"]
    tiposCriar = StringVar()
    cbTipo = ttk.Combobox(lblMenuCriar, width=12, value=tiposLista, textvariable=tiposCriar)
    cbTipo.place(x=170,y=65)
    #----------------------------------------------------------------#
    btnRegistrar = Button(lblMenuCriar,width=12,height=1, text="Registrar", font = ("arial",25),command= lambda: criarConta(nameCriar.get(),passwordCriar.get(),generoCriar.get(),tiposCriar.get()))
    btnRegistrar.place(x = 23, y = 110)
#----------------------------------------------------------------#
def telaAreaPessoalLogin(lblBase,nameInfo, genderInfo, typeInfo, txtDescricao,cbModo,btnMenuCriar_Login_Modos):
    global login
    #--------------------------------------------------------------------#
    lblMenuLogin = LabelFrame(lblBase,width=295,height=210,text="Logar Conta")
    lblMenuLogin.place(x=5,y=33)
#---#
    lblMenuLoginNome = Label(lblMenuLogin,width=5,height=1,text="Nome", font = ("arial", 12))
    lblMenuLoginNome.place(x=39,y=5)
    nameLogin = StringVar()
    txtMenuLoginNome = Entry(lblMenuLogin,width=15,justify=CENTER,textvariable=nameLogin)
    txtMenuLoginNome.place(x=20,y=25)
    #----------------------------------------------------------------#
    lblMenuLoginSenha = Label(lblMenuLogin,width=5,height=1,text="Senha", font = ("arial", 12))
    lblMenuLoginSenha.place(x=189,y=5)
    passwordLogin = StringVar()
    txtMenuLoginSenha = Entry(lblMenuLogin,width=15,justify=CENTER, textvariable=passwordLogin)
    txtMenuLoginSenha.place(x=170,y=25)
    #----------------------------------------------------------------#
    lblMenuLoginGenero = Label(lblMenuLogin,width=5,height=1,text="Genero", font = ("arial",12))
    lblMenuLoginGenero.place(x=39,y=44)
    generosLista = ["","Masculino", "Feminino", "Outro"]
    generoLogin = StringVar()
    cbGenero = ttk.Combobox(lblMenuLogin, width=12, value=generosLista, textvariable=generoLogin,state=DISABLED)
    cbGenero.place(x=20,y=65)
    #----------------------------------------------------------------#
    lblMenuLoginTipo = Label(lblMenuLogin,width=14,height=1,text="Tipos de conta", font = ("arial",12))
    lblMenuLoginTipo.place(x=155,y=44)
    tiposLista = ["","Comum","Profissional"]
    tiposLogin = StringVar()
    cbTipo = ttk.Combobox(lblMenuLogin, width=12, value=tiposLista, textvariable=tiposLogin,state=DISABLED)
    cbTipo.place(x=170,y=65)
    #----------------------------------------------------------------#
    btnLogin = Button(lblMenuLogin,width=25, height=1, text="Login", font = ("arial",12),command= lambda: loginConta(   nameLogin.get(), txtMenuLoginNome, nameLogin,
                                                                                                                        passwordLogin.get(), txtMenuLoginSenha, passwordLogin,
                                                                                                                        nameInfo, genderInfo, typeInfo, txtDescricao,
                                                                                                                        btnLogin,
                                                                                                                        cbModo,btnMenuCriar_Login_Modos,
                                                                                                                        cbGenero,cbTipo))
    btnLogin.place(x = 23, y = 90)
#----------------------------------------------------------------#
"""
#----------------------------------------------------------------#
"""
def telaAreaPessoal():
    global generos
    global img

    panelNomes = PanedWindow(window, width = 400, height= 450,bg="gray")
    panelNomes.place(x=300, y= 0)
#----------------------------------------------------------------#
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Movimentos")
    filemenu.add_command(label="Consultas")

    filemenu.add_command(label="CLS", command= lambda: os.system("cls"))
    filemenu.add_command(label="Exit", command=window.destroy)
    window.config(menu=filemenu)
#----------------------------------------------------------------#
    ctnImagemPerfil = Canvas(panelNomes,width=60,height=60)
    ctnImagemPerfil.place(x=10,y=10)
    img = PhotoImage(file="imagens/person_50x50.png")
    ctnImagemPerfil.create_image(30, 30, anchor= "center", image = img)

    txtInfo = Label(panelNomes, width = 0, height = 3, text = "Primeiro Nome:\n             Genero:\n   Tipo de conta:", font = ("arial", 12))
    txtInfo.place(x = 80,y = 10)
    
    nameInfo = StringVar()
    txtNome = Entry(panelNomes, width=20,justify=CENTER,state=DISABLED, textvariable=nameInfo)
    txtNome.place(x=195, y = 10)
    
    genderInfo = StringVar()
    txtGenero = Entry(panelNomes, width=20,justify=CENTER,state=DISABLED, textvariable=genderInfo)
    txtGenero.place(x=195, y = 30)

    typeInfo = StringVar()
    txtConta= Entry(panelNomes, width=20,justify=CENTER,state=DISABLED, textvariable=typeInfo)
    txtConta.place(x=195, y = 50)
    #----------------------------------------------------------------#
    lblDescricao = LabelFrame(panelNomes, width=310,height=100)
    lblDescricao.place(x=10,y=80)
    txtDescricao = Text(lblDescricao, width=36,height=5)
    txtDescricao.place(x=5,y=5)
#--------------------------------------------------------------------#
#
#--------------------------------------------------------------------#
    lblMenuCriar_login = LabelFrame(panelNomes, width=310,height=250)
    lblMenuCriar_login.place(x=10,y=190)
#--------------------------------------------------------------------#
    lblMenuCriar_Login_Modos = Label(lblMenuCriar_login,width=5,height=1,text="Modo: ", font = ("arial", 12))
    lblMenuCriar_Login_Modos.place(x=5,y=8)
#--------------------------------------------------------------------#
    modosLista = ["Registrar","Login"]
    modos = StringVar()
    modos.set("Selecione um Modo")
    cbModo = ttk.Combobox(lblMenuCriar_login, width=12, value=modosLista, textvariable=modos, state="readonly")
    cbModo.place(x=53,y=10)
#---#
    btnMenuCriar_Login_Modos = Button(lblMenuCriar_login,width=15, height=1, text="Selecionar Modo",command = lambda:checkModo(cbModo,btnMenuCriar_Login_Modos,lblMenuCriar_login,nameInfo, genderInfo, typeInfo, txtDescricao))
    btnMenuCriar_Login_Modos.place(x=155,y=5)

def telaGerirTarefas():
    global userAtual, lbLista

    panelTarefas = PanedWindow(window, width = 400, height= 450,bg="gray")
    panelTarefas.place(x=300, y= 0)

    lblTarefas = LabelFrame(panelTarefas, width=385,height=440)
    lblTarefas.place(x=5,y=5)

    lblTarefasTitulo = LabelFrame(lblTarefas, width=370,height=40)
    lblTarefasTitulo.place(x=5,y=5)

    lblTxtTarefas = Label(lblTarefasTitulo,width=8,text="Tarefas", font =("arial",15))
    lblTxtTarefas.place(x=140,y=5)

    lbLista = Listbox(lblTarefas,width =28, height = 23, justify=CENTER)
    lbLista.place(x=5 , y=50)

    lblTxtNome = Label(lblTarefas,width=8,text="Nome", font =("arial",12))
    lblTxtNome.place(x=240,y=50)
    txtTarefa = Entry(lblTarefas, width=20, font = ("arial",12))
    txtTarefa.place(x = 185, y=70)

    lblTxtData = Label(lblTarefas,width=8,text="Data", font =("arial",12))
    lblTxtData.place(x=240,y=95)

    calData = DateEntry(lblTarefas,selectmode='day')
    calData.place(x = 185, y=115)

    lblDoisPontos =Label(lblTarefas,width=1,text=":")
    lblDoisPontos.place(x=323,y=115)
    spnBxHora = Spinbox(lblTarefas, width=3, from_=0, to=23)
    spnBxHora.place(x=290,y=115)
    spnBxMinuto = Spinbox(lblTarefas, width=3, from_=0, to=59)
    spnBxMinuto.place(x=340,y=115)
    
    #txtData = Entry(lblTarefas, width=20, font = ("arial",12))
    #txtData.place(x = 185, y=115)

    lblTxtCategoria = Label(lblTarefas,width=8,text="Categoria", font =("arial",12))
    lblTxtCategoria.place(x=240,y=138)
    txtCategoria = Entry(lblTarefas, width=20, font = ("arial",12))
    txtCategoria.place(x = 185, y=160)

    lblTxtFavorito = Label(lblTarefas,width=8,text="Favorito", font =("arial",12))
    lblTxtFavorito.place(x=240,y=138+44)
    txtFavorito = Entry(lblTarefas, width=20, font = ("arial",12))
    txtFavorito.place(x = 185, y=205)

    btnAdcionar = Button(lblTarefas,width=19,height=1,text="Adcionar", font =("arial",12),command= lambda: addTarefa(userAtual, txtTarefa.get(), categoria=txtCategoria.get(),dataAAcionar= dateConvert(str(calData.get_date()))))
    btnAdcionar.place(x=187,y=235)
    
    btnRemover = Button(lblTarefas,width=19,height=1,text="Remover", font =("arial",12), command= lambda: delTarefa(userAtual, lbLista.curselection()))
    btnRemover.place(x=187,y=275)

    btnAtualizar = Button(lblTarefas,width=19,height=1,text="Atualizar", font =("arial",12))
    btnAtualizar.place(x=187,y=315)

    docTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(userAtual), 'r', encoding='UTF-8')
    listaTarefas = docTarefas.readlines()
    docTarefas.close()

    for i in listaTarefas:
        linha = i.split(';')
        lbLista.insert(END, linha[1])

def addTarefa(username, tarefa, descrição='', favorito=False, dataAAcionar=None, horaAAcionar=None, categoria=None):
    from datetime import date, datetime
    global lbLista

    while True:
        try:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r', encoding='UTF-8')
            listaTarefas = ficheiroTarefas.readlines()
            print(listaTarefas)
            numTarefa = len(listaTarefas)
            ficheiroTarefas.close()
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'a', encoding='UTF-8')
            break
        except:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'x')
            ficheiroTarefas.close()
    
    data = date.today()
    hora = datetime.now().strftime('%H:%M:%S')
    
    
    ficheiroTarefas.write('{};{};{};{};{};{};{},{};{}\n'.format(numTarefa,tarefa,descrição,data,hora,favorito,dataAAcionar,horaAAcionar,categoria))
    lbLista.insert(END, tarefa)
    ficheiroTarefas.close()

def delTarefa(username, numTar):
    global lbLista

    numTar = int(str(numTar).replace('(','').replace(',','').replace(')',''))
    print(numTar)

    while True:
        try:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r+', encoding='UTF-8')
            break
        except:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'x')
            ficheiroTarefas.close()

    listaTarefas = ficheiroTarefas.readlines()
    for i in range(len(listaTarefas)):
        if int(listaTarefas[i].split(';')[0]) == numTar:
            del listaTarefas[i]
            break
    
    ficheiroTarefas.close()

    ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'w', encoding='UTF-8')

    for i in listaTarefas:
        ficheiroTarefas.write(i)
    ficheiroTarefas.close()

    lbLista.delete(lbLista.curselection())

def telaConsultarTarefas():

    panelConsultarTarefas = PanedWindow(window, width = 400, height= 450,bg="gray")
    panelConsultarTarefas.place(x=300, y= 0)

    lblConsultarTarefas = LabelFrame(panelConsultarTarefas, width=385,height=280)
    lblConsultarTarefas.place(x=5,y=5)

    tree = ttk.Treeview(lblConsultarTarefas, columns = ("Nome", "Data", "Categoria", "Favorito"), show = "headings", height = 12, selectmode = "browse")
    tree.column("Nome", width = 145, anchor = "c")
    tree.column("Data", width = 75, anchor = "c")
    tree.column("Categoria", width = 75, anchor = "c")
    tree.column("Favorito", width = 75, anchor = "c")

    tree.heading("Nome", text = "Nome")
    tree.heading("Data", text = "Data")
    tree.heading("Categoria", text = "Categoria")
    tree.heading("Favorito", text = "Favorito")
    tree.place(x=5, y=5)

    lblObs = LabelFrame(panelConsultarTarefas, width =385, height = 155, text="Observações da tarefa")
    lblObs.place(x=5, y=290)

    txtObs = Text(lblObs, width = 46, height = 7)
    txtObs.place(x=5, y=10)

    docTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(userAtual), 'r', encoding='UTF-8')
    listaTarefas = docTarefas.readlines()
    docTarefas.close()

    tree.delete(*tree.get_children())
    numLinhas = []
    for i in listaTarefas:
        linha = i.split(';')
        tree.insert('','end',values=(linha[1],dateConvert(linha[3]),linha[7].replace('\n',''),linha[5]))
        numLinhas.append(linha[0])
    print(numLinhas)

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
#Gerir Tarefas----------------------------------------------------------------------------------------------------------------#
imageIco2 = PhotoImage(file = "imagens/config_tasks.png" )
btnOpcao2 = Button(panel1, text = "Gerir\ntarefas", image = imageIco2, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=telaGerirTarefas, state='disabled')
btnOpcao2.place (x=40, y=95)
#-----------------------------------------------------------------------------------------------------------------------------#
imageIco3 = PhotoImage(file = "imagens/tasks.png" )
btnOpcao3 = Button(panel1, text = "Consultar\ntarefas", image = imageIco3, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=telaConsultarTarefas, state='disabled')
btnOpcao3.place (x=40, y=185)
#-----------------------------------------------------------------------------------------------------------------------------#
imageIco4 = PhotoImage(file = "imagens/admin_user_icon.png" )
btnOpcao4 = Button(panel1, text = "Admin", image = imageIco4, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=lambda: print("btnOpcao4"), state='disabled')
btnOpcao4.place (x=40, y=275)
#-----------------------------------------------------------------------------------------------------------------------------#
imageIco5 = PhotoImage(file = "imagens/exit.png" )
btnOpcao5 = Button(panel1, text = "Sair", image = imageIco5, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=window.destroy)
btnOpcao5.place (x=40, y=365)

window.mainloop()