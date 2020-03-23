#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
#cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo
#e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
#compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
def main():
    print('Carnes na promocao')
    print('       FILE       ')
    print('      ALCATRA     ')
    print('      PICANHA     ')
    tipo = input('Que tipo de carne voce quer? ')
    quantidade = float(input('Quantos quilos? '))
    cartao = input('Voce vai pagar no cartao Tabajara? ')
    
    preco = verifica_preco(tipo, quantidade, cartao)
    print(f'O valor que o cliente irá pagar é de R${preco}')


def verifica_preco(tipo, quantidade, cartao):
    if tipo == 'FILE':
        if quantidade <= 5:
            valor = quantidade * 4.9
        else:
            valor = quantidade * 5.8
        if cartao == 'sim':
            valor = valor - valor * 0.05
        return valor
    elif tipo == 'ALCATRA':
        if quantidade <= 5:
            valor = quantidade * 5.9
        else:
            valor = quantidade * 6.8
        if cartao == 'sim':
            valor = valor - valor * 0.05
        return valor
    elif tipo == 'PICANHA':
        if quantidade <= 5:
            valor = quantidade * 6.9
        else:
            valor = quantidade * 7.8
        if cartao == 'sim':
            valor = valor - valor * 0.05
        return valor
    else:
        print('Tipo invalido')
    
main()