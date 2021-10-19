idade = int(input())

anos, m = divmod(idade, 365)
meses, dias = divmod(m, 30)

print(f'{anos} ano (s)')
print(f'{meses} mes (es)')
print(f'{dias} dia (s)')