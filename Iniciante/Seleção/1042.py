val1, val2, val3 = map(int, input().split())

if val1 > val2 and val1 > val3:
    ultimo = val1
    if val2 > val3:
        meio = val2
        primeiro = val3
    else:
        meio = val3
        primeiro = val2
elif val2 > val1 and val2 > val3:
    ultimo = val2
    if val1 > val3:
        meio = val1
        primeiro = val3
    else:
        meio = val3
        primeiro = val1

else:
    ultimo = val3
    if val1 > val2:
        meio = val1
        primeiro = val2
    else:
        meio = val2
        primeiro = val1

print(primeiro)
print(meio)
print(ultimo)
print()
print(val1)
print(val2)
print(val3)