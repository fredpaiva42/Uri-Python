caracteristica1 = input().lower()
caracteristica2 = input().lower()
caracteristica3 = input().lower()

if caracteristica1 == 'vertebrado':
    if caracteristica2 == 'ave':
        if caracteristica3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if caracteristica3 == 'onivoro':
            print('homem')
        else:
            print('vaca')

else:
    if caracteristica2 == 'inseto':
        if caracteristica3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if caracteristica3 == 'onivoro':
            print('minhoca')
        else:
            print('sanguessuga')