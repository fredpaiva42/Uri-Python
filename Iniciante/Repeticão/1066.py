contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for i in range(5):
    num = int(input())
    if num % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    if num > 0:
        contador_positivos += 1
    else:
        if num != 0:
            contador_negativos += 1

print(f'{contador_pares} valor(es) par(es)')
print(f'{contador_impares} valor(es) impar(es)')
print(f'{contador_positivos} valor(es) positivo(s)')
print(f'{contador_negativos} valor(es) negativo(s)')