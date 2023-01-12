from timing import *

def rececaoLembretes(username):
    docTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r')

    listaTarefas = docTarefas.readlines()

    docTarefas.close()

    for i in listaTarefas:
        dataEHoraAAcionar = i.split(';')[6].replace('\n','').split(',')

        if targetTime(dataEHoraAAcionar[0], dataEHoraAAcionar[1]):
            print('Recebe notificação')
        else:
            print('nada')

#rececaoLembretes('admin')