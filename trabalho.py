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
passUserAtual=''# Esta variável permite determinar qual é a senha utilizador ativo no momento.
#---#
login = 0
status = 0

if not os.path.exists(pasta): #Verfica a existencia da pasta inicio
    os.mkdir(pasta)

def criarConta(username, password,gender,type,lista):
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
            User.write("")
            User.close()

            Noticias = open(ficheiroUserNoticias, "a", encoding="utf8")
            Noticias.write("")
            Noticias.close()

            print(username)

            lista.insert(END, username)
        else:
            msg = 'Não é possível a utilização de caracteres inválidos\nCatacteres inválidos: ;'
            messagebox.showwarning('Estado', msg)
    else:
        msg = 'Já existe uma conta com "{}" como username.'.format(username)
        messagebox.showwarning('Estado', msg)

def loginConta(username, txtMenuLoginNome, nameLogin,
               password, txtMenuLoginSenha, passwordLogin,
               nameInfo, genderInfo, typeInfo, txtDescricao,
               btnLogin,
               cbModo,btnMenuCriar_Login_Modos,
               cbGenero,cbTipo):
    #print(username)
    #print(password)
    global login, userAtual, passUserAtual, btnOpcao2, btnOpcao3, btnOpcao4, numListaSelecionado
    acessos = open(ficheiroUsurios, "r", encoding="utf8")
    linhas = acessos.readlines()
    acessos.close()
    print(login)
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
                passUserAtual = password

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
                msg = "Bem vindo " + username 
                if login == 0:
                    messagebox.showinfo(title="Estado",message=msg)
                numListaSelecionado = 0
                login = 1

                addNotificacoes(userAtual)
                atualizarLembretes(userAtual)
                btnVerNotficacao.config(state='normal')
                btnVerNaoLido.config(state='normal')
                btnVerLido.config(state='normal')
                btnVerTodos.config(state='normal')
                btnAtualizarLembretes.config(state='normal')


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
        treeNotificacoes.delete(*treeNotificacoes.get_children())
        treeLembretes.delete(*treeLembretes.get_children())
        btnVerNotficacao.config(state='disabled')
        btnVerNaoLido.config(state='disabled')
        btnVerLido.config(state='disabled')
        btnVerTodos.config(state='disabled')
        btnAtualizarLembretes.config(state='disabled')

        btnLogin.config(text = "Login")

        msg = "Volte sempre"
        messagebox.showinfo(title="Estado",message=msg)

        login = 0

def checkModo(cbModo,btnMenuCriar_Login_Modos,lblBase,nameInfo,genderInfo,typeInfo,txtDescricao):
    if cbModo.get() == "Registrar":
        print("Registrar")
        telaAreaPessoalCriar(lblBase,nameInfo, genderInfo, typeInfo, txtDescricao)
    elif cbModo.get() == "Login":
        print("Login")
        telaAreaPessoalLogin(lblBase,nameInfo, genderInfo, typeInfo, txtDescricao,cbModo,btnMenuCriar_Login_Modos)

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
    cbGenero.set("Masculino")
    cbGenero.place(x=20,y=65)
    #----------------------------------------------------------------#
    lblMenuCriarTipo = Label(lblMenuCriar,width=13,height=1,text="Tipos de conta", font = ("arial",12))
    lblMenuCriarTipo.place(x=155,y=44)
    tiposLista = ["","Comum","Profissional"]
    tiposCriar = StringVar()
    cbTipo = ttk.Combobox(lblMenuCriar, width=12, value=tiposLista, textvariable=tiposCriar)
    cbTipo.place(x=170,y=65)
    #----------------------------------------------------------------#
    
    btnRegistrar = Button(lblMenuCriar,width=12,height=1, text="Registrar", font = ("arial",25),command= lambda: criarConta(nameCriar.get(),passwordCriar.get(),generoCriar.get(),tiposCriar.get(),nameCriar.get()))
    btnRegistrar.place(x = 23, y = 110)

def telaAreaPessoalLogin(lblBase,nameInfo, genderInfo, typeInfo, txtDescricao,cbModo,btnMenuCriar_Login_Modos):
    global login,userAtual,passUserAtual
    if login == 0:
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
        txtMenuLoginSenha = Entry(lblMenuLogin,width=15,justify=CENTER, textvariable=passwordLogin, show="*")
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
        

    elif login == 1 and userAtual != "":
        #--------------------------------------------------------------------#
        lblMenuLogin = LabelFrame(lblBase,width=295,height=210,text="Logar Conta")
        lblMenuLogin.place(x=5,y=33)
    #---#
        lblMenuLoginNome = Label(lblMenuLogin,width=5,height=1,text="Nome", font = ("arial", 12))
        lblMenuLoginNome.place(x=39,y=5)
        nameLogin = StringVar()
        nameLogin.set(userAtual)
        txtMenuLoginNome = Entry(lblMenuLogin,width=15,justify=CENTER,textvariable=nameLogin)
        txtMenuLoginNome.place(x=20,y=25)
        #----------------------------------------------------------------#
        lblMenuLoginSenha = Label(lblMenuLogin,width=5,height=1,text="Senha", font = ("arial", 12))
        lblMenuLoginSenha.place(x=189,y=5)
        passwordLogin = StringVar()
        passwordLogin.set(passUserAtual)
        txtMenuLoginSenha = Entry(lblMenuLogin,width=15,justify=CENTER, textvariable=passwordLogin, show="*")
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
        btnLogin.invoke()
         
def telaAreaPessoal():
    global generos
    global img, userAtual,passUserAtual,login

    panelNomes = PanedWindow(window, width = 400, height= 450,bg="gray")
    panelNomes.place(x=300, y= 0)
#----------------------------------------------------------------#
    help = Menu(menubar, tearoff=0)
    help.add_command(label="Movimentos")
    help.add_command(label="CLS", command= lambda: os.system("cls"))
    help.add_command(label="Exit", command=window.destroy)
    window.config(menu=help)
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
    if login == 0:
        btnMenuCriar_Login_Modos = Button(lblMenuCriar_login,width=15, height=1, text="Selecionar Modo",command = lambda:checkModo(cbModo,btnMenuCriar_Login_Modos,lblMenuCriar_login,nameInfo, genderInfo, typeInfo, txtDescricao))
        btnMenuCriar_Login_Modos.place(x=155,y=5)
    elif login == 1:
        modos.set("Login")
        btnMenuCriar_Login_Modos = Button(lblMenuCriar_login,width=15, height=1, text="Selecionar Modo",command = lambda:checkModo(cbModo,btnMenuCriar_Login_Modos,lblMenuCriar_login,nameInfo, genderInfo, typeInfo, txtDescricao))
        btnMenuCriar_Login_Modos.place(x=155,y=5)
        btnMenuCriar_Login_Modos.invoke()

def telaGerirTarefas():
    global userAtual, lbLista, nomeTarefa, listaTemporaria, categoriaTarefa, calData, horaLembrete, minutoLembrete, numListaSelecionado, numLinhas

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
    nomeTarefa = StringVar()
    txtTarefa = Entry(lblTarefas, width=20, font = ("arial",12), textvariable=nomeTarefa)
    txtTarefa.place(x = 185, y=70)

    lblTxtData = Label(lblTarefas,width=8,text="Data", font =("arial",12))
    lblTxtData.place(x=240,y=95)

    calData = DateEntry(lblTarefas,selectmode='day')
    calData.place(x = 185, y=115)

    lblDoisPontos =Label(lblTarefas,width=1,text=":")
    lblDoisPontos.place(x=323,y=115)
    horaLembrete = StringVar()
    spnBxHora = Spinbox(lblTarefas, width=3, from_=0, to=23, textvariable=horaLembrete)
    spnBxHora.place(x=290,y=115)
    minutoLembrete = StringVar()
    spnBxMinuto = Spinbox(lblTarefas, width=3, from_=0, to=59, textvariable=minutoLembrete)
    spnBxMinuto.place(x=340,y=115)
    
    #txtData = Entry(lblTarefas, width=20, font = ("arial",12))
    #txtData.place(x = 185, y=115)
    
    lblTxtCategoria = Label(lblTarefas,width=8,text="Categoria", font =("arial",12))
    lblTxtCategoria.place(x=240,y=138)
    categoriaTarefa = StringVar()
    txtCategoria = Entry(lblTarefas, width=16, font = ("arial",12), textvariable=categoriaTarefa)
    txtCategoria.place(x = 185, y=160)
    btnProcurarCategoria = Button(panelTarefas,width=2,height=1, bg='black', command= lambda: procurarCategoria(userAtual, txtCategoria.get()))
    btnProcurarCategoria.place(x=350,y=164)

    lblTxtFavorito = Label(lblTarefas,width=8,text="Favorito", font =("arial",12))
    lblTxtFavorito.place(x=240,y=138+44)
    txtFavorito = Entry(lblTarefas, width=20, font = ("arial",12))
    txtFavorito.place(x = 185, y=205)

    btnAdcionar = Button(lblTarefas,width=19,height=1,text="Adcionar", font =("arial",12),command= lambda: addTarefa(userAtual, txtTarefa.get(), categoria=txtCategoria.get(),dataAAcionar= str(calData.get_date()),horaAAcionar='{}:{}:00'.format(spnBxHora.get(),spnBxMinuto.get())))
    btnAdcionar.place(x=187,y=235)
    
    btnRemover = Button(lblTarefas,width=19,height=1,text="Remover", font =("arial",12), command= lambda: delTarefa(userAtual, lbLista.curselection()))
    btnRemover.place(x=187,y=275)

    btnAtualizar = Button(lblTarefas,width=19,height=1,text="Atualizar", font =("arial",12), command= lambda: atualizarTarefa(userAtual, numLinhas[numListaSelecionado]))
    btnAtualizar.place(x=187,y=315)

    docTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(userAtual), 'r', encoding='UTF-8')
    listaTarefas = docTarefas.readlines()
    docTarefas.close()

    listaTemporaria = []
    lbLista.delete(0,END)
    numLinhas = []
    for i in listaTarefas:
        linha = i.split(';')
        lbLista.insert(END, linha[1])
        listaTemporaria.append([linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6].split(','),linha[7]])
        numLinhas.append(linha[0])
    
    lbLista.bind('<<ListboxSelect>>', selecionarTarefa)

def addTarefa(username, tarefa, descrição='', favorito=False, dataAAcionar=None, horaAAcionar=None, categoria=None):
    from datetime import date, datetime
    global lbLista, listaTemporaria, numLinhas

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
    
    
    ficheiroTarefas.write('{};{};{};{};{};{};{},{};{}\n'.format(numTarefa,tarefa,descrição,data,hora,favorito,dateConvert(dataAAcionar),horaAAcionar,categoria))
    listaTemporaria.append([numTarefa,tarefa,descrição,data,hora,favorito,[dateConvert(dataAAcionar),horaAAcionar],categoria])
    lbLista.insert(END, tarefa)
    ficheiroTarefas.close()

    listaTemporaria = []
    lbLista.delete(0,END)
    numLinhas = []
    for i in listaTarefas:
        linha = i.split(';')
        lbLista.insert(END, linha[1])
        listaTemporaria.append([linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6].split(','),linha[7]])
        numLinhas.append(linha[0])

def delTarefa(username, numTar):
    global lbLista, numLinhas

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

    listaTemporaria = []
    lbLista.delete(0,END)
    numLinhas = []
    for i in listaTarefas:
        linha = i.split(';')
        lbLista.insert(END, linha[1])
        listaTemporaria.append([linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6].split(','),linha[7]])
        numLinhas.append(linha[0])

def selecionarTarefa(event):
    global nomeTarefa, categoriaTarefa, calData, lbLista, listaTemporaria, horaLembrete, minutoLembrete, numListaSelecionado, numLinhas
    print(numLinhas)
    try:
        nomeTarefa.set(listaTemporaria[int(numLinhas[int(str(lbLista.curselection()).replace('(','').replace(',)',''))])][1])
        categoriaTarefa.set(listaTemporaria[int(numLinhas[int(str(lbLista.curselection()).replace('(','').replace(',)',''))])][7])
        calData.set_date(listaTemporaria[int(numLinhas[int(str(lbLista.curselection()).replace('(','').replace(',)',''))])][6][0])
        horas = str(listaTemporaria[int(numLinhas[int(str(lbLista.curselection()).replace('(','').replace(',)',''))])][6][1]).split(':')
        horaLembrete.set(horas[0])
        minutoLembrete.set(horas[1])

        numListaSelecionado = int(str(lbLista.curselection()).replace('(','').replace(',)',''))
        print(numListaSelecionado)
    except:
        print('Selecionado: {}'.format(numListaSelecionado))

def atualizarTarefa(username, numTar):
    global numLinhas
    numTar = int(numLinhas[int(numTar)])
    print(numTar)
    ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r', encoding='UTF-8')
    listaTarefas = ficheiroTarefas.readlines()
    ficheiroTarefas.close()
    linhaTarefa = listaTarefas[numTar]
    tarefa = linhaTarefa.split(';')
    tarefa[1] = nomeTarefa.get()
    tarefa[7] = categoriaTarefa.get() + '\n'
    print(tarefa)

    linhaTarefa=''
    for i in range(len(tarefa)-1):
        linhaTarefa += tarefa[i] + ';'
    linhaTarefa += tarefa[len(tarefa)-1]

    print(linhaTarefa)

    listaTarefas[numTar] = linhaTarefa

    ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'w', encoding='UTF-8')

    for i in listaTarefas:
        ficheiroTarefas.write(i)
    ficheiroTarefas.close()

    listaTemporaria = []
    lbLista.delete(0,END)
    numLinhas = []
    for i in listaTarefas:
        linha = i.split(';')
        lbLista.insert(END, linha[1])
        listaTemporaria.append([linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6].split(','),linha[7]])
        numLinhas.append(linha[0])
    ()

def procurarCategoria(username, categoriaAlvo=''):
    global numLinhas
    ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r', encoding='UTF-8')
    listaTarefas = ficheiroTarefas.readlines()
    print(listaTarefas)
    ficheiroTarefas.close()

    listaTemporaria = []
    lbLista.delete(0,END)
    numLinhas = []
    for i in listaTarefas:
        linha = i.split(';')
        if categoriaAlvo == '':
            lbLista.insert(END, linha[1])
            listaTemporaria.append([linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6].split(','),linha[7]])
            numLinhas.append(linha[0])
        elif linha[7].replace('\n','')==categoriaAlvo:
            lbLista.insert(END, linha[1])
            listaTemporaria.append([linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6].split(','),linha[7]])
            numLinhas.append(linha[0])
    ()

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

def delUser(listaBase):
    pastaUser =""
    pos = listaBase.curselection()
    print(pos)
    print(listaBase)
    user = listaBase.get(pos)
    print(user)
    acessos = open(ficheiroUsurios, "r", encoding="utf8")
    linhas = acessos.readlines()
    acessos.close()
    
    
    os.system("cls")
    for linha in linhas:
        linha = linha.split(";")
        print(linha)
        if linha[0] == user:
            print("confirma")
            
            pastaUser ='files/users/' + user
            print(pastaUser)
            ficheiroUserLIne = pastaUser +  "/listaTarefas.txt"
            os.remove(ficheiroUserLIne)
            ficheiroUserNoticias = pastaUser +  "/noticias.txt"
            os.remove(ficheiroUserNoticias)
            os.rmdir(pastaUser)
            listaBase.delete(listaBase.curselection())
            
        ptr = 0
        acessos = open(ficheiroUsurios, "w", encoding="utf8")
        for i in listaBase.curselection():
            index = i
            print(index)
        for linha in linhas:
            print(linha)
            print(index)
            if ptr != index:
                print("funciona")
                acessos.write(linha)
            ptr += 1
        acessos.close()

def atualizarUser(username, password,gender,typeL,listaBase):
    os.system("cls")

    acessosInicial = open(ficheiroUsurios, "r", encoding="utf8")
    linhas = acessosInicial.readlines()
    acessosInicial.close()

    pos = listaBase.curselection()
    print(pos)
    print(listaBase)
    user = listaBase.get(pos)
    print(user)

    pastaUserAntes = pasta + '/users/' + user
    print(pastaUserAntes)
    pastaUserDepois = pasta + '/users/' + username
    print(pastaUserDepois)

    acessos = open(ficheiroUsurios, "w", encoding="utf8")
    acessos.close()
    linhaFinal = ""
    ptr = 0
    for i in listaBase.curselection():
        index = i
        print(index)
    os.system("cls")
    for linha in linhas:
        print(linha)
        linha = linha.split(";")
        print(linha)   
        print("\n") 
        acessos = open(ficheiroUsurios, "a", encoding="utf8")
        if ptr == index:
            linhaFinal = ""
            print("ptr == index")
            linha[0] = username
            linha[1] = password
            linha[2] = gender
            linha[3] = typeL
            linhaFinal = linha[0] + ";" + linha[1] + ";" + linha[2] + ";" + linha[3] + ";" + linha[4]
            print(linhaFinal)
            acessos.write(linhaFinal)
            acessos.close()
        else:
            linhaFinal = ""
            linhaFinal =  linha[0] + ";" + linha[1] + ";" + linha[2] + ";" + linha[3] + ";" + linha[4]
            acessos.write(linhaFinal)
            acessos.close()
        ptr += 1
    acessos.close()
    os.rename(pastaUserAntes,pastaUserDepois)

def reiniciarNoticia():
    print('aaa')
    tituloNoticia.set('[Título da notícia]')

    txtLead.delete('0.0','end')
    txtLead.insert('insert','[Lead da notícia]')

    textNoticia.delete('0.0','end')
    textNoticia.insert('insert','[Notícia]')

def submeterNoticia():
    from datetime import date, datetime
    data = date.today()
    hora = datetime.now().strftime('%H:%M:%S')

    linhaNoticia = 'Não Lido;;;{};;;{};;;{};;;{},{}\n'.format(tituloNoticia.get(),txtLead.get('0.0','end').replace('\n',''),textNoticia.get('0.0','end').replace('\n',''),data,hora)
    users = []
    listaAcessos = open('files\\acessos.txt', "r", encoding="utf8")
    linhas = listaAcessos.readlines()
    listaAcessos.close()

    for i in linhas:
        users.append(i.split(';')[0])
    ()

    for user in users:
        ficheiroNoticias = open('files\\users\\{}\\noticias.txt'.format(user), 'a', encoding='utf-8')
        ficheiroNoticias.write(linhaNoticia)
        ficheiroNoticias.close()

def telaAdmin():
    global userAtual, lbLista, nomeTarefa, listaTemporaria, categoriaTarefa, calData, horaLembrete, minutoLembrete, tituloNoticia, txtLead, textNoticia

    panelTarefas = PanedWindow(window, width = 400, height= 450,bg="gray")
    panelTarefas.place(x=300, y= 0)

    lblTarefas = LabelFrame(panelTarefas, width=385,height=440)
    lblTarefas.place(x=5,y=5)

    lblAdmin = LabelFrame(lblTarefas, width=370,height=40)
    lblAdmin.place(x=5,y=5)

    lblTxtTarefas = Label(lblAdmin,width=8,text="ADMIN", font =("arial",15))
    lblTxtTarefas.place(x=140,y=5)

    lbListaUser = Listbox(lblTarefas,width =28, height = 10, justify=CENTER)
    lbListaUser.place(x=5 , y=50)

    lblFrmCriarNoticia = LabelFrame(lblTarefas,width =180, height = 210, text='Criar notícia')
    lblFrmCriarNoticia.place(x=5 , y=220)

    tituloNoticia = StringVar()
    txtTitulo = Entry(lblFrmCriarNoticia, width=28, textvariable=tituloNoticia)
    tituloNoticia.set('[Título da notícia]')
    txtTitulo.place(x=0,y=0)

    txtLead = Text(lblFrmCriarNoticia, height=2, width=28, font=('Helvetica', 8))
    txtLead.delete('0.0','end')
    txtLead.insert('insert','[Lead da notícia]')
    txtLead.place(x=0,y=20)

    textNoticia = Text(lblFrmCriarNoticia, height=8, width=28, font=('Helvetica', 8))
    textNoticia.delete('0.0','end')
    textNoticia.insert('insert','[Notícia]')
    textNoticia.place(x=0,y=40)

    btnSubmeterNoticia = Button(lblFrmCriarNoticia, width=10, text='Submeter', command=submeterNoticia)
    btnSubmeterNoticia.place(x=5,y=160)
    btnReiniciarNoticia = Button(lblFrmCriarNoticia, width=10, text='Reiniciar', command=reiniciarNoticia)
    btnReiniciarNoticia.place(x=90,y=160)

    lblTxtUser = Label(lblTarefas,width=8,text="Nome", font =("arial",12))
    lblTxtUser.place(x=240,y=50)
    User = StringVar()
    txtUser = Entry(lblTarefas, width=20, font = ("arial",12), textvariable=User)
    txtUser.place(x = 185, y=70)

    lblTxtPass = Label(lblTarefas,width=8,text="Password", font =("arial",12))
    lblTxtPass.place(x=240,y=95)
    Pass = StringVar()
    txtPass = Entry(lblTarefas, width=20, font = ("arial",12), textvariable=Pass)
    txtPass.place(x = 185, y=115)

    lblTxtGender = Label(lblTarefas,width=8,text="Genero", font =("arial",12))
    lblTxtGender.place(x = 240, y = 138)
    GenderLista = ["","Masculino", "Feminino", "Outro"]
    Gender = StringVar()
    cbGender = ttk.Combobox(lblTarefas, width=18, values=GenderLista, textvariable=Gender, font =("arial",12), state="readonly")
    cbGender.place(x = 185,y = 160)

    lblTxtType = Label(lblTarefas,width=8,text="Tipo", font =("arial",12))
    lblTxtType.place(x = 240, y = 187)
    TypeLista = ["","Comum","Profissional","admin"]
    TypeAc = StringVar()
    cbType = ttk.Combobox(lblTarefas, width=18, values=TypeLista, textvariable=TypeAc, font =("arial",12), state="readonly")
    cbType.place(x = 185,y = 209)


    btnAdcionar = Button(lblTarefas,width=18,height=1,text="Adcionar", font =("arial",12),command= lambda: criarConta(User.get(),Pass.get(),Gender.get(),TypeAc.get(),lbListaUser))
    btnAdcionar.place(x=187,y=235)
    
    btnRemover = Button(lblTarefas,width=19,height=1,text="Remover", font =("arial",12), command= lambda: delUser(lbListaUser))
    btnRemover.place(x=187,y=275)

    btnAtualizar = Button(lblTarefas,width=19,height=1,text="Atualizar", font =("arial",12),command= lambda: atualizarUser(User.get(),Pass.get(),Gender.get(),TypeAc.get(),lbListaUser))
    btnAtualizar.place(x=187,y=315)
    
    acessos = open(ficheiroUsurios, "r", encoding="utf8")
    linhas = acessos.readlines()
    acessos.close()
    os.system("cls")
    for linha in linhas:
        linha = linha.split(";")
        print(linha[0])
        lbListaUser.insert("end",linha[0])

#codigo principal inicio
window = Tk()

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1100                             # tamanho (pixeis) da window a criar
appHeight = 450
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.resizable(0,0)
window.title("Programa")
#-----------------------------------------------------------------------------------------------------------------------------#
menubar = Menu(window)
#-----------------------------------------------------------------------------------------------------------------------------#
help = Menu(menubar, tearoff=0)
help.add_command(label="Atualizar")
help.add_command(label="CLS", command= lambda: os.system("cls"))
help.add_command(label="Exit", command=window.destroy)
window.config(menu=help)

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
                    command=telaAdmin, state='disabled')
btnOpcao4.place (x=40, y=275)
#-----------------------------------------------------------------------------------------------------------------------------#
imageIco5 = PhotoImage(file = "imagens/exit.png" )
btnOpcao5 = Button(panel1, text = "Sair", image = imageIco5, compound=LEFT, relief = "sunken", 
                    width = 200, height = 70, font="calibri, 11",
                    command=window.destroy)
btnOpcao5.place (x=40, y=365)

panel2 = PanedWindow(window, bg = "black",width = 500, height = 450)
panel2.place(x=700 , y=0)

treeNotificacoes = ttk.Treeview(panel2, columns=('Estado','Título', 'Num'),show='headings')
treeNotificacoes.heading('Estado', text='Estado')
treeNotificacoes.column('Estado', width=60, anchor='c')

treeNotificacoes.heading('Título', text='Título')
treeNotificacoes.column('Título', width=320, anchor='w')

treeNotificacoes.column('Num', width=0, anchor='w')

treeLembretes = ttk.Treeview(panel2, columns=('Lembrete','Tarefa'),show='headings', height=5)

treeLembretes.heading('Tarefa', text='Tarefa')
treeLembretes.column('Tarefa', width=320, anchor='w')

treeLembretes.column('Lembrete', width=100, anchor='w')

scrollBarNotificacoes = ttk.Scrollbar(panel2, orient='vertical', command=treeNotificacoes.yview())
treeNotificacoes.configure(yscrollcommand=scrollBarNotificacoes.set)
scrollBarNotificacoes.place(x=380,y=0, height=230)

scrollBarLembrete = ttk.Scrollbar(panel2, orient='vertical', command=treeLembretes.yview())
treeLembretes.configure(yscrollcommand=scrollBarLembrete.set)
scrollBarLembrete.place(x=380,y=280, height=125)

treeNotificacoes.place(x=0,y=0)
treeLembretes.place(x=0,y=280)

def atualizarLembretes(user):
    global treeLembretes

    ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(user), 'r')
    listaTarefas = ficheiroTarefas.readlines()
    ficheiroTarefas.close()

    for i in listaTarefas:
        tarefa = i.split(';')
        if targetTime(dateConvert(tarefa[6].split(',')[0]),tarefa[6].split(',')[1]):
            treeLembretes.insert('','end',values=('', tarefa[1]))

def verNoticia():
    global treeNotificacoes, lblTituloNoticia, lblLeadNoticia, txtNoticia, panelNoticia

    row_id = treeNotificacoes.focus()
    noticia = int(treeNotificacoes.item(row_id)["values"][2])
    ficheiroNoticias = open('files\\users\\{}\\noticias.txt'.format(userAtual), 'r', encoding='utf-8')
    listaNoticias = ficheiroNoticias.readlines()
    ficheiroNoticias.close()

    linhaNoticia = listaNoticias[noticia]
    lblTituloNoticia.config(text=linhaNoticia.split(';;;')[2])
    lblLeadNoticia.config(text=linhaNoticia.split(';;;')[3])
    txtNoticia.config(state='normal')
    txtNoticia.delete('0.0','end')
    txtNoticia.insert('insert', linhaNoticia.split(';;;')[4])
    txtNoticia.config(state='disabled')

    linhaNoticia = linhaNoticia.replace('Não Lido;;;','Lido;;;')
    listaNoticias[noticia] = linhaNoticia

    ficheiroNoticias = open('files\\users\\{}\\noticias.txt'.format(userAtual), 'w', encoding='utf-8')
    for i in listaNoticias:
        ficheiroNoticias.write(i)
    ficheiroNoticias.close()
    addNotificacoes(userAtual)

    panelNoticia.place(x=700, y=0)

    print(linhaNoticia)

btnVerNotficacao = Button(panel2, text='Ver notificação', command=verNoticia, state='disabled')
btnVerNotficacao.place(x=10,y=240)

btnVerNaoLido = Button(panel2, text='Ver não lidos', command=lambda:addNotificacoes(userAtual, filtro='Não Lido'), state='disabled')
btnVerNaoLido.place(x=120,y=240)

btnVerLido = Button(panel2, text='Ver lidos', command=lambda:addNotificacoes(userAtual, filtro='Lido'), state='disabled')
btnVerLido.place(x=210,y=240)

btnVerTodos = Button(panel2, text='Ver todos', command=lambda:addNotificacoes(userAtual), state='disabled')
btnVerTodos.place(x=290,y=240)

btnAtualizarLembretes = Button(panel2, text='Atualizar lembretes', command=lambda: atualizarLembretes(userAtual), state='disabled')
btnAtualizarLembretes.place(x=140,y=410)

def addNotificacoes(user, filtro=None):
    global treeNotificacoes
    
    ficheiroNoticias = open('files\\users\\{}\\noticias.txt'.format(user), 'r', encoding='utf-8')
    listaNoticias = ficheiroNoticias.readlines()
    ficheiroNoticias.close()
    numNoticia = 0
    treeNotificacoes.delete(*treeNotificacoes.get_children())
    for i in listaNoticias:
        noticia = i.split(';;;')
        if filtro==None:
            treeNotificacoes.insert('','end',values=(noticia[0], noticia[2], numNoticia))
        elif filtro=='Não Lido':
            if noticia[0] == 'Não Lido':
                treeNotificacoes.insert('','end',values=(noticia[0], noticia[2], numNoticia))
        elif filtro=='Lido':
            if noticia[0] == 'Lido':
                treeNotificacoes.insert('','end',values=(noticia[0], noticia[2], numNoticia))
        numNoticia += 1
    
    listaNoticias.clear()

panelNoticia = PanedWindow(window, bg = "gray",width = 500, height = 450)

lblTituloNoticia = Label(panelNoticia, text='Título notícia', fg='black', bg='gray', font=('Helvetica', 24))
lblTituloNoticia.place(x=0,y=30)
lblLeadNoticia = Label(panelNoticia, text='Título notícia', fg='black', bg='gray', font=('Helvetica', 16))
lblLeadNoticia.place(x=0,y=70)

txtNoticia = Text(panelNoticia, width=50, height=20)
txtNoticia.place(x=0,y=100)
txtNoticia.insert('insert', 'Notícia')
txtNoticia.config(state='disabled')

btnFechar = Button(panelNoticia, text='Fechar', command= lambda: panelNoticia.place_forget())
btnFechar.place(x=0,y=0)

window.mainloop()
os.system("cls")