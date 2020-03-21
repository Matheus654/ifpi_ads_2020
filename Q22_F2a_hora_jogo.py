def main():
    hora_inicio = int(input('Digite a hora de começo do jogo: '))
    minutos_inicio = int(input('Digite os minutos do comeco do jogo: '))
    hora_fim = int(input('Digite a hora do final do jogo: '))
    minutos_fim = int(input('Digite os minutos do final do jogo: '))

    duracao(hora_inicio, hora_fim, minutos_inicio, minutos_fim)


def duracao(hora_inicio, hora_fim, minutos_inicio, minutos_fim):
    hora1 = hora_inicio + minutos_inicio / 60
    hora2 = hora_fim + minutos_fim / 60

    tempo = hora2 - hora1
    tempo_hora = tempo % 10 
    tempo_minuto = tempo // 10 * 60

    if tempo_hora <= 24:
        print(f'A duracao do jogo foi de {tempo_hora} horas e {tempo_minuto} minutos.')
    else:
        print('O jogo excedeu o tempo limite de 24 horas.')

main()