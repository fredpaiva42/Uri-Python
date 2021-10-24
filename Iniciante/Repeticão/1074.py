qtd = int(input())

for i in range(qtd):
    numeros = int(input())

    if numeros > 0:
        if numeros % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif numeros < 0:
        if numeros % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    else:
        print('NULL')