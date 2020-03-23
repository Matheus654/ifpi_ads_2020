def main():
    num_litros = float(input('Digite o numero de litros vendidos: '))
    combustivel = input('Que combustivel foi vendido? A - Álcool ou G - Gasolina: ')

    preco = gasto_total(num_litros, combustivel)
    print(f'O valor a ser pago pelo cliente é de R${preco}')


def gasto_total(num_litros, combustivel):
    if combustivel == 'G':
        if num_litros <= 20:
            desc = 0.04
        else:
            desc = 0.06
        gasto = num_litros * 2.5 - 2.5 * desc
        return gasto
    elif combustivel == 'A':
        if num_litros <= 20:
            desc = 0.03
        else:
            desc = 0.05
        gasto = num_litros * 1.9 - 1.9 * desc
        return gasto
    else:
        print('Valor invalido')


main()