qtd = int(input())
divisao = 0
for i in range(qtd):
    x, y = [int(num) for num in input().split()]

    if y == 0:
        print('divisao impossivel')
    else:
        divisao = x / y
        print(f'{divisao:.1f}')

