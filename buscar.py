from DML import select
from os import system


def buscar(msg=f'*{"*":>49}'):

    print('*' * 50)
    print(f'*{"PESQUISAR DADOS":^48}{"*":50}')
    print(f'*' * 50)
    print(f'* {"[1]Pesquisar por nome"}{"*":>27} '
          f'\n{"* [2]Pesquisar por endereço"}{"*":>23} '
          f'\n{"* [3]Pesquisar por email"}{"*":>26} \n{"* [4]Relatorio Completo"}{"*":>27}')
    print(f'*' * 50)
    print(msg)
    print(f'*' * 50)

    while True:

        option_busc = str(input())

        if option_busc == '1':

            pesquisa1()

        if option_busc == '2':

            pesquisa2()

        if option_busc == '3':

            pesquisa3()

        if option_busc == '4':

            pesquisa4()

        print('OPÇÃO INVALIDA')


def decisao_pesquisa():
    print('*' * 50)
    print(f'*\033[34m{"NOVA PESQUISA":^48}\033[m{"*":>0}')
    print(f'*\033[34m{"[1]SIM||[2]NÃO":^48}\033[m{"*":>0}')
    print('*' * 50)

    decisao = int(input())

    while True:

        if decisao == 1:

            system('cls')
            return True

        if decisao == 2:

            system('cls')
            return False

        system('cls')
        print('*' * 50)
        print(f'\033[31m{"OPÇÃO INVALIDA":^50}\033[m')
        decisao = str(input())
        print('*' * 50)
        system('cls')


def pesquisa1():

    system('cls')
    print(f'*' * 50)

    nome = str(input('Nome:')).title()
    resultado = select('id,nome, endereco, num_endereco,'
                       ' email', 'Alunos', f"nome like '%{nome}%'")
    print('*' * 50)

    if resultado:
        print(f'*\033[34m{"RESULTADO ENCONTRADO":^48}\033[m{"*":>0}')
        print('*' * 50)
        for v in resultado:
            print(f'Cod:{v["id"]} \nNome:{v["nome"]} \nEndereço:{v["endereco"]}'
                  f' N°{v["num_endereco"]} \nEmail:{v["email"]}')
            if len(resultado) > 1:
                print('*' * 50)
    else:
        print(f'*\033[31m{"NENHUM RESULTADO ENCONTRADO.":^48}\033[m{"*":>0}')

    respo = decisao_pesquisa()
    if respo:
        return True
    else:
        return False


def pesquisa2():

    system('cls')
    print(f'*' * 50)

    endereco = str(input('Endereço:')).title()
    resultado = select('id,nome, endereco, num_endereco,'
                       ' email', 'Alunos', f"endereco like '%{endereco}%'")
    print('*' * 50)

    if resultado:
        print(f'*\033[34m{"RESULTADO ENCONTRADO":^48}\033[m{"*":>0}')
        print('*' * 50)
        for v in resultado:
            print(f'Cod:{v["id"]} \nNome:{v["nome"]} \nEndereço:{v["endereco"]}'
                  f' N°{v["num_endereco"]} \nEmail:{v["email"]}')
            if len(resultado) > 1:
                print('*' * 50)
    else:
        print(f'*\033[31m{"NENHUM RESULTADO ENCONTRADO.":^48}\033[m{"*":>0}')

    respo = decisao_pesquisa()
    if respo:
        return True
    else:
        return False


def pesquisa3():

    system('cls')
    print(f'*' * 50)

    email = str(input('Email:')).title()
    resultado = select('id,nome, endereco, num_endereco,'
                       ' email', 'Alunos', f"email like '%{email}%'")
    print('*' * 50)

    if resultado:
        print(f'*\033[34m{"RESULTADO ENCONTRADO":^48}\033[m{"*":>0}')
        print('*' * 50)
        for v in resultado:
            print(f'Cod:{v["id"]} \nNome:{v["nome"]} \nEndereço:{v["endereco"]}'
                  f' N°{v["num_endereco"]} \nEmail:{v["email"]}')
            if len(resultado) > 1:
                print('*' * 50)
    else:
        print(f'*\033[31m{"NENHUM RESULTADO ENCONTRADO.":^48}\033[m{"*":>0}')

    respo = decisao_pesquisa()
    if respo:
        return True
    else:
        return False


def pesquisa4():
    system('cls')
    print(f'*' * 50)

    resultado = select('*', 'Alunos')
    print('*' * 50)

    if resultado:
        print(f'*\033[34m{"RESULTADO ENCONTRADO":^48}\033[m{"*":>0}')
        print('*' * 50)
        for v in resultado:
            print(f'Cod:{v["id"]} \nNome:{v["nome"]} \nEndereço:{v["endereco"]}'
                  f' N°{v["num_endereco"]} \nEmail:{v["email"]}')
            if len(resultado) > 1:
                print('*' * 50)

    respo = decisao_pesquisa()
    if respo:
        return True
    else:
        return False
