def main():
    num = float(input('Digite um numero: '))

    verifica_numero(num)


def verifica_numero(num):
    if int(num) == num:
        print(f'{num} é inteiro')
    else:
        print(f'{num} é decimal')


main()