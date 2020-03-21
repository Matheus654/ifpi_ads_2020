def main():
    senha = input('Digite sua senha: ')

    verifica_senha(senha)

def verifica_senha(senha):
    if senha == '1234':
        print('Acesso permitido')
    else:
        print('Acesso negado')
    

main()