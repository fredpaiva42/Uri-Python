qtd = int(input())

for i in range(qtd + 1):
    if i % 2 == 0 and i != 0:
        quadrado = i ** 2
        print(f'{i}^2 = {quadrado}')