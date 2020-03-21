def main():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))

    resto(n1, n2)


def resto(n1, n2):
    if n1 % n2 == 0:
        pass
    elif n1 % n2 == 1:
        print(n1 + n2 + (n1 % n2))
    elif n1 % n2 == 2:
        if n1 % 2 == 0:
            print(f'{n1} é par')
        else:
            print(f'{n1} é impar')
        if n2 % 2 == 0:
            print(f'{n2} é par')
        else:
            print(f'{n2} é impar')
    elif n1 % n2 == 3:
        print((n1 * n2) + n1)
    elif n1 % n2 == 4:
        print((n1 + n2) / n2)
    else:
        print(n1 ** 2, n2 ** 2)

main()