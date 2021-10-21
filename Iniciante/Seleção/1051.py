renda = float(input())

if renda <= 2000:
    imposto = 0
    print("Isento")
elif 2000.01 < renda <= 3000:
    taxa8 = renda - 2000
    imposto = taxa8 * 0.08
    print("R$ {:.2f}".format(imposto))
elif 3000.01 < renda <= 4500:
    taxa8 = 1000 * 0.08
    taxa18 = renda - 3000
    imposto = (taxa18 * 0.18) + taxa8
    print("R$ {:.2f}".format(imposto))
elif renda > 4500:
    taxa8 = 1000 * 0.08
    taxa18 = 1500 * 0.18
    taxa28 = renda - 4500
    imposto = (taxa28 * 0.28)+taxa8+taxa18
    print("R$ {:.2f}".format(imposto))