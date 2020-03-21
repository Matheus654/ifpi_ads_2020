def main():
    print('Digite a data conforme o modelo DD/MM/AAAA')
    data = input('Digite umma data: ')

    verifica_data(data)


def verifica_data(data):
    dia = 31
    mes = 12
    dia_atual = int(data[0] + data[1])
    mes_atual = int(data[3] + data[4])
    
    if dia_atual > dia or  mes_atual > mes:
        print('Essa data nao é valida')
    else:
        print('Essa data é valida')

main()