from math import sqrt
def main():
    numero = int(input('Digite um numero de quatro digitos:'))

    verifica_quadrado(numero)

def verifica_quadrado(numero):
    numeral = str(numero)
    if len(numeral) > 4:
        print('ERROR')
    else:
        numero1 = int(numeral[0] + numeral[1])
        numero2 = int(numeral[2] + numeral[3])

        if sqrt(numero) == numero1 + numero2:
            print(f'{numero} é um quadrado perfeito.')
        else:
            print(f'O numero {numero} nao pe um quadrado perfeito')


main()