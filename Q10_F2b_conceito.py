def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    verifica_nota(nota1, nota2)


def verifica_nota(nota1, nota2):
    media = (nota1 + nota2) / 2
    if 0 <= media < 4:
        conceito = 'E'
    elif 4 <= media < 6:
        conceito = 'D'
    elif 6 <= media < 7.5:
        conceito = 'C'
    elif 7.5 <= media < 9:
        conceito = 'B'
    else:
        conceito = 'A'

    verifica_conceito(conceito)


def verifica_conceito(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        print('APROVADO ')
    else:
        print('REPROVADO')



main()