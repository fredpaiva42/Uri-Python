qtd_alunos = int(input())

for aluno in range(qtd_alunos):
    notas = list(map(float, input().split()))
    media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 5)/10
    print(f'{media:.1f}')
