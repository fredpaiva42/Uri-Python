nome = input('Nome do vendedor: ')
salario_fixo = float(input('Salário: '))
total_vendas = float(input('Total Vendas efetuadas em dinheiro: '))

bonus = (total_vendas * 0.15) + salario_fixo

print(f'TOTAL = R$ {bonus:.2f}')
