x, y, z = map(float, input().split())

if x > y and x > z:
    a = x
    b = y
    c = z
elif y > x and y > z:
    a = y
    b = x
    c = z
else:
    a = z
    b = x
    c = y

if a >= b + c:
    area = ((a + b)*c)/2
    print(f"Area = {area:.1f}")
else:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")