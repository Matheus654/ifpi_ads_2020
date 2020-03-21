def main():
    num = int(input('Digite um numero entre 1 e 100 e direi se é primo: '))
    
    verifica_primo(num)


def verifica_primo(num):
    n = num
    divisores = 0
    while n >= 1:
        if num % n == 0:
            divisores += 1
        n -= 1 
    if  divisores > 2:
        print(f'{num} nao é primo')
    else:
        print(f'{num} é primo')
main()
