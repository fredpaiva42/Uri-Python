qtd = int(input())

dentro = 0
fora = 0

for i in range(qtd):
    numero = int(input())

    if 20 >= numero >= 10:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} out')