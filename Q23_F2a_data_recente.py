def main():
    dia1 = int(input('Digite o primeiro dia: '))
    mes1 = int(input('Digite o primeiro mes: '))
    ano1 = int(input('Digite o primeiro ano: '))
    dia2 = int(input('Digite o segundo dia: '))
    mes2 = int(input('Digite o segundo mes: '))
    ano2 = int(input('Digite o segundo ano: '))

    data_recente(dia1, dia2, mes1, mes2, ano1, ano2)


def data_recente(dia1, dia2, mes1, mes2, ano1, ano2):
    if ano1 > ano2:
        if mes1 > mes2:
            if dia1 > dia2:
                print('A segunda data é mais recente')
            else:
                print('A primeira data é mais recente')
        else:
            print('A primeira data é mais recente')
    else:
        print('A primeira data é mais recente')


main()