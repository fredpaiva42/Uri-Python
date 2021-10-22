contador = 0
media = 0
for i in range(6):
    num = float(input())
    if num > 0:
        contador += 1
        media += num
media_f = media / contador

print(f'{contador} valores positivos')
print(f'{media_f:.1f} valores positivos')
