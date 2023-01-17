def tipoDeConta(username):
    docContas = open('files\\acessos.txt', 'r', encoding='utf-8')
    listaContas = docContas.readlines()
    docContas.close()

    for i in listaContas:
        if i.split(';')[0] == username:
            return i.split(';')[3].replace('\n', '')

#print(tipoDeConta('admin'))