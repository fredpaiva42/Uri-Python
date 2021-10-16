peca_1 = input().split()
codigo_peca1, qtd_peca1, valor_unitario1 = peca_1
peca_2 = input().split()
codigo_peca2, qtd_peca2, valor_unitario2 = peca_2

custo_peca1 = int(qtd_peca1) * float(valor_unitario1)
custo_peca2 = int(qtd_peca2) * float(valor_unitario2)

total = custo_peca1 + custo_peca2

print(f'VALOR TOTAL A PAGAR: R$ {total:.2f}')
