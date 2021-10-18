duracao_viagem = int(input())
velocidade_media = int(input())

gasto_por_km = 12

distancia_percorrida = duracao_viagem * velocidade_media

qtd_necessaria = distancia_percorrida / gasto_por_km

print(f'{qtd_necessaria:.3f}')