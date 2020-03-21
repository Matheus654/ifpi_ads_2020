def main():
    horas_de_aula1 = int(input('Digite a quantidade de horas que voce da aula:'))
    valor_hora1 = int(input('Digite quanto voce ganha por hora aula: '))
    horas_de_aula2 = int(input('Digite a quantidade de horas que voce da aula:'))
    valor_hora2 = int(input('Digite quanto voce ganha por hora aula: '))

    maior_salario(horas_de_aula1, horas_de_aula2, valor_hora1, valor_hora2)


def maior_salario(horas_de_aula1, horas_de_aula2, valor_hora1, valor_hora2):
    salario1 = horas_de_aula1 * valor_hora1
    salario2 = horas_de_aula2 * valor_hora2

    if salario1 > salario2:
        print('O primeiro professor ganha mais')
    else:
        print('O segundo professor ganha mais')

    
main()