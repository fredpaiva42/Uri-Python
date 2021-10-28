x, y = [int(num) for num in input().split()]

while True:
    if x == 0 or y == 0:
        break
    if x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    else:
        print('quarto')

    x, y = [int(num) for num in input().split()]