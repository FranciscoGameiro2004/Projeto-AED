from timing import *

def rececaoLembretes(username):
    docTarefas = open('files\\users\\{}\\listaTarefas.txt'.format(username), 'r', encoding='utf-8')

    listaTarefas = docTarefas.readlines()

    docTarefas.close()

    for i in listaTarefas:
        dataEHoraAAcionar = i.split(';')[6].replace('\n','').split(',')

        if targetTime(dataEHoraAAcionar[0], dataEHoraAAcionar[1]):
            print('Recebe notificação')
        else:
            print('nada')

def rececaoNoticias(username):
    '''
    Constituição de uma notícia:
    [Estado];;;[Autor];;;[Título da notícia];;;[Lead da notícia];;;[Texto da notícia];;;[[Data],[Hora]]
        0         1               2                     3                  4                   5
                                                                                            0     1
    '''
    docNoticias = open('files\\users\\{}\\noticias.txt'.format(username), 'r', encoding='utf-8')

    listaNoticias = docNoticias.readlines()

    docNoticias.close()

    for i in listaNoticias:
        noticia = i.split(';;;')
        if noticia[0] == 'Não lido':
            print(noticia[2], ' de ', noticia[1], '\n')
            print(noticia[3], '\n')
            print(noticia[4])
            print('\n')

#rececaoLembretes('admin')
#rececaoNoticias('admin')