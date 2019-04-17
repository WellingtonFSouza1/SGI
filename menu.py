from os import system


def menu():
    print('*' * 50)
    print(f'{"*":<0}{" Sistema Gestão Integrado ":^48}{"*":>0}')
    print('*' * 50)
    print(f'* [1]ATULIZAR{"*":>37}')
    print(f'* [2]BUSCAR{"*":>39}')
    print(f'* [3]CADASTRAR{"*":>36}')
    print(f'* [4]EXCLUIR{"*":>38}')
    print(f'* [5]SAIR{"*":>41}')
    print('*' * 50)
    option = str(input())

    if option.isnumeric() and 0 < int(option) < 6:

        system('cls')
        return option

    else:
        while True:

            print('Opção invalida.\ntente novamente:', end='')
            option = str(input())
            system('cls')

            if option.isnumeric() and 0 < int(option) < 6:
                return option
