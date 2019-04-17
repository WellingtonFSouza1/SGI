from Cadastro import *
from buscar import *
from menu import menu
from os import system

while True:

    resposta = menu()

    if resposta == '1':

        print('Essa função está sendo incrementada.')

    if resposta == '2':

        resp_cadastro2 = buscar()

        if resp_cadastro2:

            buscar()

        else:

            resposta = menu()

    if resposta == '3':

        resp_casdastro = nv_cadastro()

        if resp_casdastro:

            menu()

        else:

            nv_cadastro()

    if resposta == '4':
        print('Essa função está sendo incrementada.')
    if resposta == '5':
        system('exit(n)')
    print(resposta)
