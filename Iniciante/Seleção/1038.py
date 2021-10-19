cardapio = [[1, 4.00], [2, 4.50], [3, 5.00], [4, 2.00], [5, 1.50]]

codigo, qtd = map(int, input().split())

if codigo == 1:
    total = cardapio[0][1] * qtd
elif codigo == 2:
    total = cardapio[1][1] * qtd
elif codigo == 3:
    total = cardapio[2][1] * qtd
elif codigo == 4:
    total = cardapio[3][1] * qtd
else:
    total = cardapio[4][1] * qtd

print(f'Total: R$ {total:.2f}')
