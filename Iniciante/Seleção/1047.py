hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

tempo = abs(((hora_final * 60) + minuto_final) - ((hora_inicial * 60) + minuto_inicial))
if tempo <= 0:
    tempo += 24 * 60

tempo_horas = tempo // 60
tempo_minutos = tempo % 60

print(f'O JOGO DUROU {tempo_horas} HORA(S) E {tempo_minutos} MINUTO(S)')
