def main():
    lado1 = int(input('Digite o 1º lado do triangulo: '))
    lado2 = int(input('Digite o 2º lado do triangulo: '))
    lado3 = int(input('Digite o 3º lado do triangulo: '))

    verifica_lados(lado1, lado2, lado3)


def verifica_lados(lado1, lado2, lado3):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado3 + lado2 > lado1):
        if lado1 < lado2 + lado3:
            print('O  1º lado é a hipotenusa, e os outros sao os catetos.')
        elif lado2 < lado1 + lado3:
            print('O  2º lado é a hipotenusa, e os outros sao os catetos.')
        elif lado3 < lado1 + lado2:
            print('O  3º lado é a hipotenusa, e os outros sao os catetos.')
    else:
        print('Esses lados nao formam um triangulo.')