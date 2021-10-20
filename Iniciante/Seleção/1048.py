salario = float(input())

if 400 >= salario >= 0:
    salario_final = salario + salario * 0.15
    reajuste = salario * 0.15
    percentual = 15
elif 400.01 <= salario <= 800.0:
    salario_final = salario + salario * 0.12
    reajuste = salario * 0.12
    percentual = 12
elif 800.01 <= salario <= 1200.00:
    salario_final = salario + salario * 0.10
    reajuste = salario * 0.10
    percentual = 10
elif 1200.01 <= salario <= 2000.00:
    salario_final = salario + salario * 0.07
    reajuste = salario * 0.07
    percentual = 7
else:
    salario_final = salario + salario * 0.04
    reajuste = salario * 0.04
    percentual = 4

print(f'Novo salario: {salario_final:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')

