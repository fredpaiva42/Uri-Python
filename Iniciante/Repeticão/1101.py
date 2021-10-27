valores = [int(num) for num in input().split()]
soma = 0
lista = []
while True:
    if valores[0] <= 0 or valores[1] <= 0:
        break
    m = max(valores)
    n = min(valores)

    for i in range(n, m+1):
        lista.append(i)
        soma += i

    print(*lista, f"Sum={soma}")

    valores = [int(num) for num in input().split()]
    soma = 0
    lista = []