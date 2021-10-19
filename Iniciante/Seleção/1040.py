nota1, nota2, nota3, nota4 = map(float, input().split())

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + nota4) / 10

if media < 5:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
elif media > 6.9:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
else:
    recuperacao = float(input())
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {recuperacao:.1f}')
    media_final = (recuperacao + media) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {media_final:.1f}')