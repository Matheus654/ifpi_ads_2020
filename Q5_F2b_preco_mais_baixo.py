def main():
    produto1 = float(input('Digite o valor do 1º produto: '))
    produto2 = float(input('Digite o valor do 2º produto: '))
    produto3 = float(input('Digite o valor do 3º produto: '))

    verificar = menor_preco(produto1, produto2, produto3)


def menor_preco(produto1, produto2, produto3):
    if produto1 == produto2 and produto1 == produto3:
        print('Os três produtos tem o mesmo preco.')
    elif produto1 < produto2 < produto3:
        print(f'Voce deve comprar o produto que tem o preco R${produto1} por ele ser o mais barato')
    elif produto2 < produto1 < produto3:
        print(f'Voce deve comprar o produto que tem o preco R${produto2} por ele ser o mais barato')
    else:
        print(f'Voce deve comprar o produto que tem o preco R${produto3} por ele ser o mais barato')


main()