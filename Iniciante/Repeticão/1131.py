qtdGrenais = 0
qtdVitoriasInter = 0
qtdVitoriasGremio = 0
qtdEmpates = 0
continuar = True

while continuar:
    golsInter, golsGremio = map(int, input().split())

    qtdGrenais += 1
    if golsInter > golsGremio:
        qtdVitoriasInter += 1
    elif golsGremio > golsInter:
        qtdVitoriasGremio += 1
    else:
        qtdEmpates += 0

    print("Novo grenal (1-sim 2-nao)")
    decisao = int(input())

    if decisao == 2:
        break

print(f'{qtdGrenais} grenais')
print(f'Inter:{qtdVitoriasInter}')
print(f'Gremio:{qtdVitoriasGremio}')
print(f'Empates:{qtdEmpates}')
if qtdVitoriasInter > qtdVitoriasGremio:
    print('Inter venceu mais')
elif qtdVitoriasGremio > qtdVitoriasInter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')