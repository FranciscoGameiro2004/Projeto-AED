'''
Cada tarefa é constituída da seguinte forma:
[Numero da Tarefa];[Tarefa];[Descrição];[Data];[Hora];[Favorito];[[Data a ser acionado],[Hora a ser acionado]];[Categoria]
Índice:  0            1          2         3      4        5                           6                            7
Índice para o acionamento de um lembrete:                                  0                     1
'''

def addTarefa(username, tarefa, descrição='', favorito=False, dataAAcionar=None, horaAAcionar=None, categoria=None):
    from datetime import date, datetime
    global lbLista

    print(lbLista.get())

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
    ficheiroTarefas.close()

def delTarefa(username, numTar):
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

def addFavorito(username, numTar):
    while True:
        try:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r+', encoding='UTF-8')
            break
        except:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'x', encoding='UTF-8')
            ficheiroTarefas.close()

    
    listaTarefas = ficheiroTarefas.readlines()
    for i in listaTarefas:
        if int(i.split(';')[0]) == numTar:
            tarefa = i.split(';')[1]
            descricao = i.split(';')[2]
            data = i.split(';')[3]
            hora = i.split(';')[4]
            lembrete = '{},{}'.format(i.split(';')[6].split(',')[0],i.split(';')[6].split(',')[1])
            categoria = i.split(';')[7].replace('\n','')
            break

    if listaTarefas[numTar].split(';')[5].replace('\n','') == 'True':
        isFavorito = False
    else:
        isFavorito = True

    del listaTarefas[numTar]
    listaTarefas.insert(numTar, '{};{};{};{};{};{};{};{}\n'.format(numTar,tarefa,descricao,data,hora,isFavorito,lembrete,categoria))
    
    ficheiroTarefas.close()

    ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'w', encoding='UTF-8')

    for i in listaTarefas:
        ficheiroTarefas.write(i)
    
    ficheiroTarefas.close()

def alterarCategoria(username, numTar, categoria):
    while True:
        try:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r+', encoding='UTF-8')
            break
        except:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'x', encoding='UTF-8')
            ficheiroTarefas.close()

    
    listaTarefas = ficheiroTarefas.readlines()
    for i in listaTarefas:
        if int(i.split(';')[0]) == numTar:
            tarefa = i.split(';')[1]
            descricao = i.split(';')[2]
            data = i.split(';')[3]
            hora = i.split(';')[4]
            isFavorito = i.split(';')[5]
            lembrete = '{},{}'.format(i.split(';')[6].split(',')[0],i.split(';')[6].split(',')[1])
            break

    if listaTarefas[numTar].split(';')[5].replace('\n','') == 'True':
        isFavorito = False
    else:
        isFavorito = True

    del listaTarefas[numTar]
    listaTarefas.insert(numTar, '{};{};{};{};{};{};{};{}\n'.format(numTar,tarefa,descricao,data,hora,isFavorito,lembrete,categoria))
    
    ficheiroTarefas.close()

    ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'w', encoding='UTF-8')

    for i in listaTarefas:
        ficheiroTarefas.write(i)
    
    ficheiroTarefas.close()

#addTarefa('admin','Tomar banho', dataAAcionar='12-01-2023', horaAAcionar='12:00:00', categoria='tarefa de casa')

#delTarefa('admin', 0)

#addFavorito('admin', 0)

#alterarCategoria('admin', 0, 'Higiene pessoal')