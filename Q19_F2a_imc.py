def main():
    altura = float(input('DIgite a sua altura: '))
    peso = float(input('Digite o seu peso: '))

    imc(altura, peso)


def imc(altura, peso):
    if peso / (altura ** 2) < 25:
        print('Voce esta com o peso normal') 
    elif peso / (altura ** 2) > 25 and peso / (altura ** 2) < 30:
        print("Voce esta obeso")
    else:
        print('Voce esta com obeisdade morbida')

main()