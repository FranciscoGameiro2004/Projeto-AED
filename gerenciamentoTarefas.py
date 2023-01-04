'''
Cada tarefa é constituída da seguinte forma:
[Tarefa];[Descrição]
'''

def addTarefa(username, tarefa, descrição=''):
    while True:
        try:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'a', encoding='UTF-8')
            break
        except:
            ficheiroTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'c')
            ficheiroTarefas.close()
    
    ficheiroTarefas.write('{};{}\n'.format(tarefa,descrição))
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

#addTarefa('admin','Dar mimo à Ufinha')

#delTarefa('admin', 1)