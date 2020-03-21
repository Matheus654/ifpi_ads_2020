def main():
    numero = float(input('Digite um numero com casas decimais: '))

    arredonda(numero)


def arredonda(numero):
    if numero % 10 >= 0.5:
        digito = (numero + 1) - (numero % 10)
        print("%.2f" %digito)
    else:
        print(numero % 10)


main()