def main(): 
    numero = int(input("Digite um número de 4 dígitos: "))

    resultado = calculo(numero)
    verificacao = verificar_se_iguais(numero,resultado)
    
    
def calculo(n):
    numero_1 = n // 100
    numero_2 = n % 100
    soma = numero_1 + numero_2
    numero_digitado = soma ** 2
    return numero_digitado


def verificar_se_iguais(num1, num2):
    if num1 == num2:
        print("Este número obedece à caraterística, pois ele é igual ao resultado do cálculo.")
    else:
        print("Este número não obedece à caraterística, pois ele não é igual ao resultado do cálculo.")

main()