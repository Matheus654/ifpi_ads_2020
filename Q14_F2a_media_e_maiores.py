def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite um numero: '))
    num3 = int(input('Digite um numero: '))
    num4 = int(input('Digite um numero: '))
    num5 = int(input('Digite um numero: '))

    media_total(num1, num2, num3, num4, num5)


def media_total(num1, num2, num3, num4, num5):
    media = (num1 + num2 + num3 + num4 + num5) / 5
    if num1 > media:
        print(num1, end= ',')
    if num2 > media:
        print(num2, end= ',')
    if num3 > media:
        print(num3, end= ',')
    if num4 > media:
        print(num4, end= ',')
    else:
        print(num5, end= '')

main()