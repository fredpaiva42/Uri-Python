x, y, z = map(float, input().split())
pi = 3.14159

print(f'TRIANGULO : {(x*z)/2:.3f}')
print(f'CIRCULO : {z**2 * pi:.3f}')
print(f'TRAPEZIO : {((x+y)*z)/2:.3f}')
print(f'QUADRADO : {y**2:.3f}')
print(f'RETANGULO : {(x*y):.3f}')
