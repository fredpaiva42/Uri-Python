i = 0
j = 1

while i <= 2:
    for n in range(1, 4):
        if (i == 1.0 or i == 0.0) or (i > 1.8 or i > 2.19):
            print(f'I={i:.0f} J={j:.0f}')
        else:
            print(f'I={i:.1f} J={j:.1f}')
        j += 1
    i += 0.2
    j -= 2.8
