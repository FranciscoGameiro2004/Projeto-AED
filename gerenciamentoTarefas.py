'''
Cada tarefa é constituída da seguinte forma:
[Tarefa];[Descrição];[Data];[Hora];[Favorito]
'''

def addTarefa(username, tarefa, descrição='', favorito=False):
    from datetime import date, datetime

    while True:
        try:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'a', encoding='UTF-8')
            break
        except:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'c')
            ficheiroTarefas.close()
    
    data = date.today()
    hora = datetime.now().strftime('%H:%M:%S')
    
    ficheiroTarefas.write('{};{};{};{};{}\n'.format(tarefa,descrição,data,hora,favorito))
    ficheiroTarefas.close()

def delTarefa(username, numTar):
    while True:
        try:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r+', encoding='UTF-8')
            break
        except:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'c')
            ficheiroTarefas.close()

    listaTarefas = ficheiroTarefas.readlines()
    del listaTarefas[numTar]
    
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
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'c')
            ficheiroTarefas.close()

    listaTarefas = ficheiroTarefas.readlines()
    tarefa = listaTarefas[numTar].split(';')[0]
    descricao = listaTarefas[numTar].split(';')[1]
    data = listaTarefas[numTar].split(';')[2]
    hora = listaTarefas[numTar].split(';')[3]

    if listaTarefas[numTar].split(';')[4].replace('\n','') == 'True':
        isFavorito = False
    else:
        isFavorito = True

    del listaTarefas[numTar]
    listaTarefas.insert(numTar, '{};{};{};{};{}\n'.format(tarefa,descricao,data,hora,isFavorito))
    
    ficheiroTarefas.close()

    ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'w', encoding='UTF-8')

    for i in listaTarefas:
        ficheiroTarefas.write(i)
    
    ficheiroTarefas.close()

#addTarefa('admin','Tomar banho')

#delTarefa('admin', 0)

#addFavorito('admin', 0)