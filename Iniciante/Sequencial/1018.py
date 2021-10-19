qtd_reais = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

for cedula in notas:
    qtd_notas = qtd_reais // cedula
    print(f'{qtd_notas} nota (s) de R$ {cedula:.2f}')
    qtd_reais -= qtd_notas * cedula