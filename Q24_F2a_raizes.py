def main():
    A = int(input('Digite o valor de A na equacao do segundo grau: '))
    B = int(input('Digite o valor de B na equacao do segundo grau: '))
    C = int(input('Digite o valor de C na equacao do segundo grau: '))

    bhaskara(A, B, C)


def bhaskara(A, B, C):
    delta = ((B ** 2) - 4 * A * C)
    if delta < 1:
        print('A esquacao nao tem raiz')
    elif delta > 1:
        raiz1 = (((delta ** 0.5) -B) / (2 * A))
        raiz2 = (((-1 * (delta ** 0.5)) -B) / (2 * A))
        print(f'As raizes sao {raiz1} e {raiz2}')
    else:
        raiz1 = (-B / 2 * A)
        print(f'A raiz da equacao é {raiz1}')


main()