import os
from DML import insert


def nv_cadastro():

    print('*' * 50)
    print(f'*{"CADASTRAR":^48}{"*":>0}')
    print('*' * 50)
    nome = str(input('Nome:')).title()
    endereco = str(input('Endereço:')).title()
    n_casa = int(input('N°'))
    email = str(input('Email:'))

    commit = insert(f"DEFAULT, '{nome}', '{endereco}', {n_casa}, '{email}'", 'alunos')

    if commit:

        print('Cadastro Realizado com Sucesso!.')
        print('*' * 50)
        os.system('cls')
    else:

        print('erro tente novamente!.')

        return nv_cadastro()

    resp_novo_cdt = str(input('Quer fazer um novo cadastro? \n[1]SIM [2]NÃo'))

    while True:
        if resp_novo_cdt in '1':

            return True

        if resp_novo_cdt in '2':

            return False

        else:
            os.system('cls')
            resp_novo_cdt = str(input('Opção invalida! \n[1]SIM||[2]NÃo'))
            os.system('cls')
