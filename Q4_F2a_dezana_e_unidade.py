def main():
    numero = int(input('Digite um numero de dois digitos: '))

    dezena = numero // 10
    unidade  = numero % 10
    dezena_e_unidade(dezena, unidade)


def dezena_e_unidade(dezena, unidade):
    if dezena == unidade:
        print('O numero da dezena é igual ao da unidade')
    else:
        print('O numero da dezena é diferente do da unidade')



main()