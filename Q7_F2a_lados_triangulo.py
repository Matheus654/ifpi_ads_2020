def main():
    l1 = int(input('Digite o tamanho do 1º lado: '))
    l2 = int(input('Digite o tamanho do 2º lado: '))
    l3 = int(input('Digite o tamanho do 3º lado: '))

    confere_lados(l1, l2, l3)


def confere_lados(l1, l2, l3):
    if (l1 + l2 > l3) and (l1 + l3 > l2) and (l3 + l2 > l1):
        if l1 == l2 or l1 == l3 or l2 == l3:
            print('Esse triangulo é isóceles')
        elif l1  == l2 and l1 == l3:
            print('Esse triangulo é equlátero')
        else:
            print('Esse triangulo é escaleno')
    else:
        print('Esses valores nao formam um triangulo.')
        
main()