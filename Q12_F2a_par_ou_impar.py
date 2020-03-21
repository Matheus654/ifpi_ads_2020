def main():
    num = int(input('Digite um numero: '))

    par_ou_impar(num)


def par_ou_impar(num):
    if num % 2 == 0:
        print('Esse numero é par')
    else:
        print('Esse numero é impar')

    
main()