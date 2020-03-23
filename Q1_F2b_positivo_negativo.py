def main():
    num = int(input('Digite um numero:'))

    verifica_numero(num)


def verifica_numero(num):
    if num < 0:
        print('O numero é negativo')
    else:
        print('O numero é positivo')


main()