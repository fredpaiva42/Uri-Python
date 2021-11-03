contador = 0
media = 0
continuar = True

while continuar:
    nota = float(input())
    if 0 <= nota <= 10:
        contador += 1
        media += nota

        if contador == 2:
            print(f"media = {media/2:.2f}")
            contador = 0
            media = 0
            while True:
                print("novo calculo (1-sim 2-nao)")
                decisao = int(input())
                if decisao == 1:
                    continuar = True
                    break
                elif decisao == 2:
                    continuar = False
                    break
    else:
        print("nota invalida")