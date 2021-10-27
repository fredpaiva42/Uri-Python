qtd_casos = int(input())
qtd_impares = 0
for i in range(qtd_casos):
    intervalo = map(int, input().split())
    x, y = intervalo

    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x

    for n in range(menor + 1, maior):
        if n % 2 != 0:
            qtd_impares += n

    print(qtd_impares)
    qtd_impares = 0
