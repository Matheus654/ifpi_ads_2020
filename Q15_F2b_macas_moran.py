def main():
    qtd_maca = float(input('Digite a quantidade de Kg de maca comprada: '))
    qtd_morango = float(input('Digite  quantidade de Kg de morango comprada: '))

    preco = verifica_gasto(qtd_maca, qtd_morango)
    print(f'O cliente ira pagar R${preco}')


def verifica_gasto(qtd_maca, qtd_morango):
    a = gasto_maca(qtd_maca)
    b = gasto_morango(qtd_morango)
    gasto_total = a + b
    kg_total = qtd_maca + qtd_morango
    if kg_total > 8 or gasto_total > 20:
        gasto_total = gasto_total - gasto_total * 0.1
    return gasto_total

def gasto_maca(qtd_maca):
    if qtd_maca <= 5:
        gasto_total_maca = qtd_maca * 1.8
    else:
        gasto_total_maca = qtd_maca * 1.5
    return gasto_total_maca


def gasto_morango(qtd_morango):
    if qtd_morango <= 5:
        gasto_total_morango = qtd_morango * 1.8
    else:
        gasto_total_morango = qtd_morango * 1.5
    return gasto_total_morango



main()