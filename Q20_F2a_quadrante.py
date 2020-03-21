def main():
    angulo = float(input('Digite o angulo: '))

    quadrante(angulo)


def quadrante(angulo):
    if angulo > 0 and angulo < 90:
        print('Primeiro quadrante')
    elif angulo > 90 and angulo < 180:
        print('Segundo quadrante')
    elif angulo > 180 and angulo < 270:
        print('Terceiro quadrante')
    elif angulo > 270 and angulo < 360:
        print('Quarto quadrante')
    else:
        print('ERROR')


main()