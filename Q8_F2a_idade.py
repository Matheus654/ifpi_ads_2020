def main():
    print('Digite conforme o meodelo: DD/MM/AAAA')
    
    data_atual = input('Digite a data atual: ')
    data_nascimento = input('Digite a data do seu nascimento: ')

    anos = idade(data_atual, data_nascimento)

    print(f'Sua idade em anos é {anos}')


def idade(data_atual, data_nascimento):
    dia_atual = int(data_atual[0] + data_atual[1])
    mes_atual = int(data_atual[3] + data_atual[4])
    ano_atual = int(data_atual[6] + data_atual[7] + data_atual[8] + data_atual[9])
    
    dia_nascimento = int(data_nascimento[0] + data_nascimento[1])
    mes_nascimento = int(data_nascimento[3] +data_nascimento[4])
    ano_nascimento = int(data_nascimento[6] + data_nascimento[7] + data_nascimento[8] + data_nascimento[9])

    anos = (ano_atual + (mes_atual / 12) + (dia_atual / 365)) - (ano_nascimento + (mes_nascimento / 12) + (dia_nascimento / 365))

    return anos

main()