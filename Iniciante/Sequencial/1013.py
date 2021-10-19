a, b, c = map(int, input().split())

maiorAB = (a+b+abs(a-b))/2

if c > maiorAB:
    print(f'{c} eh o maior')
else:
    print(f'{maiorAB:.0f} eh o maior')
