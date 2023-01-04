def criarConta(username, senha, tipo='Normal'):
    carsInvalidos = ';'
    existeConta = False # A princípio, a conta não existe.
    caracterInvalido = False # A princípio, não existe quaisquer caracter inválido.
    ficheiroContas = open('files\\acessos.txt', 'r') # #Nota 1: Abertura do ficheiro 'acessos.txt' no modo read
    for i in carsInvalidos:
        for j in ficheiroContas.readlines():
            if username.find(i) == -1 and senha.find(i) == -1:
                if j.split(';')[0] == username:
                    existeConta = True
                    break
            else:
                caracterInvalido = True
                break
    ficheiroContas.close()
    
    if existeConta == False and caracterInvalido == False:
        ficheiroContas = open('files\\acessos.txt', 'a')
        ficheiroContas.write('{};{};{}\n'.format(username,senha,tipo))
        ficheiroContas.close()
    elif caracterInvalido == True:
        print('Não é possível usar caracteres especiais.')
    else:
        print('Conta já existe')

def login(username, senha):
    sucesso = False
    ficheiroContas = open('files\\acessos.txt', 'r')
    for i in ficheiroContas.readlines():
        if i.split(';')[0] == username and i.split(';')[1] == senha:
            sucesso = True
            break
    ficheiroContas.close()

    if sucesso == True:
        print('Bem-vindo, {}!'.format(username))
    else:
        print('Não conseguiu entrar. Deve ter errado os parâmetros')



login('a54', '346323')