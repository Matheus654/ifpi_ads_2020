def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segubnda nota: '))

    verifica_media(nota1, nota2)


def verifica_media(nota1, nota2):
    media = (nota1 + nota2) / 2 
    if media == 10:
        print('Aprovado com Distincao')
    elif media > 7 or media == 7:
        print('Aprovado')
    elif media < 7:
        print('Reprovado')
    else:
        print('Media superior a 10')

main()