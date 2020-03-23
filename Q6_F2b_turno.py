def main():
    turno = input('Digite o turno em que voce estuda: M - Matutino, V - Vespertino e N - Noturno: ')

    verifica_turno(turno)


def verifica_turno(turno):
    if turno == 'M':
        print('Bom Dia')
    elif turno == 'V':
        print('Boa Tarde')
    elif turno == 'N':
        print('Boa Noite')
    else:
        print('Turno invalido')


main()