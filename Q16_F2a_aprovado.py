def main():
    nota1 = int(input('Digite sua 1º nota: '))
    nota2 = int(input('Digite sua 2º nota: '))

    aprovacao(nota1, nota2)


def aprovacao(nota1, nota2):
    media  = (nota1 + nota2) / 2
    if media > 7:
        print('Aprovado')
    else:
        recuperacao = int(input('Digite a nota da recuperacao: '))
        if recuperacao > 5:
            print('Aprovado')
        else:
            print('reprovado')

main()