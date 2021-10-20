hora_inicial, hora_final = map(int, input().split())

tempo = abs((hora_final - hora_inicial) + 24)
if tempo > 24:
    tempo -= 24

print(f'O JOGO DUROU {tempo} HORA(S)')
