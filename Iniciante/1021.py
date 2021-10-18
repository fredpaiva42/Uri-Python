qtd_reais = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for cedula in notas:
    qtd_notas = qtd_reais // cedula
    print(f'{qtd_notas:.0f} nota (s) de R$ {cedula:.2f}')
    qtd_reais -= qtd_notas * cedula

print('MOEDAS:')
for moeda in moedas:
    qtd_moedas = qtd_reais // moeda
    print(f'{qtd_moedas:.0f} moeda (s) de R$ {moeda:.2f}')
    qtd_reais -= qtd_moedas * moeda