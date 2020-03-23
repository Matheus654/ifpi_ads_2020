def main():
    salario = float(input('Digite o valor do seu salario: R$ '))

    verifica_salario(salario)


def verifica_salario(salario):
    if salario < 280:
        salario_novo = salario + salario * 0.2
        reajuste = salario * 0.2
        print(f'O seu salario antes do reajuste era: {salario}')
        print(f'Seu reajuste sera em 20 %')
        print(f'O valor do reajuste sera de R$ {reajuste}')
        print(f'O seu salario passa a ser R$ {salario_novo}')
    elif 280 <= salario < 700:
        salario_novo = salario + salario * 0.15
        reajuste = salario * 0.15
        print(f'O seu salario antes do reajuste era: {salario}')
        print(f'Seu reajuste sera em 15 %')
        print(f'O valor do reajuste sera de R$ {reajuste}')
        print(f'O seu salario passa a ser R$ {salario_novo}')
    elif 700 <= salario < 1500:
        salario_novo = salario + salario * 0.10
        reajuste = salario * 0.10
        print(f'O seu salario antes do reajuste era: {salario}')
        print(f'Seu reajuste sera em 10 %')
        print(f'O valor do reajuste sera de R$ {reajuste}')
        print(f'O seu salario passa a ser R$ {salario_novo}')
    else:
        salario_novo = salario + salario * 0.05
        reajuste = salario * 0.05
        print(f'O seu salario antes do reajuste era: {salario}')
        print(f'Seu reajuste sera em 05 %')
        print(f'O valor do reajuste sera de R$ {reajuste}')
        print(f'O seu salario passa a ser R$ {salario_novo}')


main()