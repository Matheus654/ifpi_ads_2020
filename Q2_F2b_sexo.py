def main():
    sexo = input('Digite a letra: ')

    verifica_sexo(sexo)


def verifica_sexo(sexo):
    if sexo == 'F':
        print('F - Feminino')
    elif sexo == 'M':
        print('M - Masculino')
    else:
        print('Sexo invalido')


main()    