x, y = [int(num) for num in input().split()]

while x != y:
    if x > y:
        print('Decrescente')
    else:
        print('Crescente')

    x, y = [int(num) for num in input().split()]