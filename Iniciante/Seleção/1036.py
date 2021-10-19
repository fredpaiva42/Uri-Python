from math import sqrt, pow


def verificaDelta(valA, valB, valC):
    delta = pow(valB, 2) - 4 * valA * valC
    if delta > 0 and a != 0:
        return delta
    else:
        return 'Impossivel calcular'


a, b, c = map(float, input().split())

delta = verificaDelta(a, b, c)

if delta == 'Impossivel calcular':
    print('Impossivel calcular')
else:
    r1 = (-b + sqrt(delta)) / (2 * a)
    r2 = (-b - sqrt(delta)) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
