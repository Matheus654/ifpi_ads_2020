def main():
    a = input("Telefonou para a vítima?")
    b = input("Esteve no local do crime?")
    c = input("Mora perto da vítima?")
    d = input("Devia para a vítima?")
    e = input("Já trabalhou com a vítima?")

    verifica_crime(a, b, c, d, e)




def verifica_crime(a, b, c, d, e):   
    x = 0
    if a == "sim":
        x = 1
    if b == "sim":
        x += 1
    if c == "sim":
        x = x + 1
    if d =="sim":
        x += 1
    if e == "sim":
        x += 1
    if x == 5:
        print("Você é o assassino")
    if x == 4 or x == 3:
        print("Você é cúmplice")
    if x == 2:
        print("Você é suspeito")
    if x == 1 or x == 0:
        print("Você é inocente")



main()