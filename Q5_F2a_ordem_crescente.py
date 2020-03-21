def main():
    print('Digite tres numeros diferentes.')
    n1 = int(input('Digite o 1º numero: '))
    n2 = int(input('Digite o 2º numero: '))
    n3 = int(input('Digite o 3º numero: '))
    
    ordem_decrescente(n1, n2, n3)

def ordem_decrescente(n1, n2, n3):
    if n1 < n2 < n3:
        a = print(n1, n2, n3)
    if n1 < n3 < n2:
        a = print(n1, n3, n2)
    if n2 < n1 < n3:
        a = print(n2, n1, n3)
    if n2 < n3 < n1:
        a = print(n2, n3, n1)
    if n3 < n1 < n2:
        a = print(n3, n1, n2)
    if n3 < n2 < n1:
        a = print(n3, n2, n1)
    return a

main()