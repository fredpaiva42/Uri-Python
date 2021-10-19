from math import sqrt, pow
ponto1 = map(float, input().split())
ponto2 = map(float, input().split())

x1, y1 = ponto1
x2, y2 = ponto2

distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f'{distancia:.4f}')