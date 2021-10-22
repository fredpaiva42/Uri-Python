palavra, dia_inicial = input().split()
dia_inicial = int(dia_inicial)
hora_i, minuto_i, segundo_i = map(int, input().split(' : '))
palavra2, dia_final = input().split()
dia_final = int(dia_final)
hora_f, minuto_f, segundo_f = map(int, input().split(' : '))

d = 3600 * 24

tempo = ((dia_final * d) + (hora_f * 3600) + (minuto_f * 60) + segundo_f) - ((dia_inicial * d)+(hora_i * 3600) +
                                                                             (minuto_i * 60) + segundo_i)

dias = tempo // d
tempo = tempo % d
tempo_horas = tempo // 3600
tempo = tempo % 3600
tempo_minutos = tempo // 60
tempo_segundos = tempo % 60

print(f'{dias} dia(s)')
print(f'{tempo_horas} hora(s)')
print(f'{tempo_minutos} minuto(s)')
print(f'{tempo_segundos} segundo(s)')
