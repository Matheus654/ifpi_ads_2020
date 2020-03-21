def main():
    n1 = int(input('Digite o 1º angulo: '))
    n2 = int(input('Digite o 2º angulo:'))
    n3 = int(input('Digite o 3º angulo: '))

    angulos(n1, n2, n3)


def angulos(n1, n2, n3):
    if n1 + n2 + n3 == 180:
        if n1 == 90 or n2 == 90 or n3 == 90:
            print('Esses angulos formam um triangulo reto')
        elif n1 == 180 or n2 == 180 or n3 == 180:
            print('Esses angulos formam um triangulo obtusangulo')
        elif n1 < 90 and n2 < 90 or n3 < 90:
            print('Esses angulos formam um triangulo acutangulo')
    else:
        print('Esses angulos nao formam um triangulo')

main()