def main():
    print('Opçoes possiveis: 1, 2, 3')
    opcao = int(input('Digite a opcao: '))
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    num3 = int(input('Digite outro numero: '))

    escolha(opcao, num1, num2, num3)


def escolha(opcao, num1, num2, num3):
    if opcao < 1 or opcao > 3:
        print('Opcao invalida')
    else:
        if opcao == 1:
            print(num1)
        elif opcao == 2:
            print(num2)
        else:
            print(num3)

main()