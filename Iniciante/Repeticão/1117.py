contador = 0
media = 0
while contador < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        contador += 1
        media += nota
    if nota < 0 or nota > 10:
        print('nota invalida')
media = media / 2
print(f'media = {media:.2f}')