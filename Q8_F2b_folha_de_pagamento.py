def main():
    horas = int(input('Digite a quantidade de horas trabalhadas: '))
    valor_hora = float(input('Digite o valor recebido por hora: '))

    folha_pagamento(horas, valor_hora)


def folha_pagamento(horas, valor_hora):
    salario_bruto = horas * valor_hora
    INSS = salario_bruto * 0.1
    FGTS = salario_bruto * 0.11
    if salario_bruto <= 900:
        IR = salario_bruto * 0
        descontos = IR + INSS
        salario_liquido = salario_bruto - descontos
        print(f'Salário Bruto: ({horas} * {valor_hora})     :R$ {salario_bruto}')
        print(f'(-)IR (0%)                                  :R$ {IR}')
        print(f'(-) INSS (10%)                              :R$ {INSS}')
        print(f'FGTS(11%)                                   :R$ {FGTS}')
        print(f'Total de Descontos                          :R$ {descontos}')
        print(f'Salario Liquido                             :R$ {salario_liquido}')
    elif 900 < salario_bruto <= 1500:
        IR = salario_bruto * 0.05
        descontos = IR + INSS
        salario_liquido = salario_bruto - descontos
        print(f'Salário Bruto: ({horas} * {valor_hora})     :R$ {salario_bruto}')
        print(f'(-)IR (5%)                                  :R$ {IR}')
        print(f'(-) INSS (10%)                              :R$ {INSS}')
        print(f'FGTS(11%)                                   :R$ {FGTS}')
        print(f'Total de Descontos                          :R$ {descontos}')
        print(f'Salario Liquido                             :R$ {salario_liquido}')
    elif 1500 < salario_bruto <= 2500:
        IR = salario_bruto * 0.1
        descontos = IR + INSS
        salario_liquido = salario_bruto - descontos
        print(f'Salário Bruto: ({horas} * {valor_hora})     :R$ {salario_bruto}')
        print(f'(-)IR (10%)                                 :R$ {IR}')
        print(f'(-) INSS (10%)                              :R$ {INSS}')
        print(f'FGTS(11%)                                   :R$ {FGTS}')
        print(f'Total de Descontos                          :R$ {descontos}')
        print(f'Salario Liquido                             :R$ {salario_liquido}')
    else:
        IR = salario_bruto * 0.2
        descontos = IR + INSS
        salario_liquido = salario_bruto - descontos
        print(f'Salário Bruto: ({horas} * {valor_hora})     :R$ {salario_bruto}')
        print(f'(-)IR (20%)                                 :R$ {IR}')
        print(f'(-) INSS (10%)                              :R$ {INSS}')
        print(f'FGTS(11%)                                   :R$ {FGTS}')
        print(f'Total de Descontos                          :R$ {descontos}')
        print(f'Salario Liquido                             :R$ {salario_liquido}')

main()