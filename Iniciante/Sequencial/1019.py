tempo = int(input())

minutos, segundos = divmod(tempo, 60)
horas, minutos = divmod(minutos, 60)

print(f'{horas}:{minutos}:{segundos}')


