casos_teste = int(input())

total_cobaias = 0
qtd_coelhos = 0
qtd_ratos = 0
qtd_sapos = 0

for i in range(casos_teste):
    informacoes = input().split()
    qtd_cobaias = int(informacoes[0])
    tipo = informacoes[1]
    total_cobaias += qtd_cobaias

    if tipo.upper() == 'C':
        qtd_coelhos += qtd_cobaias
    elif tipo.upper() == 'R':
        qtd_ratos += qtd_cobaias
    else:
        qtd_sapos += qtd_cobaias

percentual_coelhos = (qtd_coelhos * 100)/total_cobaias
percentual_ratos = (qtd_ratos * 100)/total_cobaias
percentual_sapos = (qtd_sapos * 100)/ total_cobaias

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {qtd_coelhos}')
print(f'Total de ratos: {qtd_ratos}')
print(f'Total de sapos: {qtd_sapos}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')