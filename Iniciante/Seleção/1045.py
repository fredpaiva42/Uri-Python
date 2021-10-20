from math import pow
l1, l2, l3 = map(float, input().split())

if l1 > l2 and l3:
    a = l1
    b = l2
    c = l3
elif l2 > l1 and l2 > l3:
    a = l2
    b = l1
    c = l3
else:
    a = l3
    b = l2
    c = l1

nao_forma = a >= b + c
eh_retangulo = pow(a, 2) == (pow(b, 2) + pow(c, 2))
eh_obtusangulo = pow(a, 2) > pow(b, 2) + pow(c, 2)
eh_acutangulo = pow(a, 2) < (pow(b, 2) + pow(c, 2))
eh_equilatero = a == b == c
eh_isosceles = a == b != c or a == c != b or b == c != a

if nao_forma:
    print('NAO FORMA TRIANGULO')
else:
    if eh_retangulo:
        print('TRIANGULO RETANGULO')
    if eh_obtusangulo:
        print('TRIANGULO OBTUSANGULO')
    if eh_acutangulo:
        print('TRIANGULO ACUTANGULO')
    if eh_isosceles:
        print('TRIANGULO ISOSCELES')
    if eh_equilatero:
        print('TRIANGULO EQUILATERO')