def main():
    opcao = int(input("Escolha a operação: 1 = adição, 2 = subtração, 3 = multiplicação ou 4 = divisão: "))
    n1 = int(input("digite um número: "))
    n2 = int(input("digite outro número:"))

    operacao(opcao, n1, n2)


def operacao(opcao, n1, n2):
    if opcao == 1:
        print(n1 + n2)
    if opcao == 2:
        print(n1 - n2)
    if opcao == 3:
        print(n1 * n2)
    if opcao == 4:
        if n2 != 0:
            print(n1 / n2)
        if n2 == 0:
            print("Erro")


main()

