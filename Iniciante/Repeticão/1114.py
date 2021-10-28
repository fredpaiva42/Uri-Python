SENHAVALIDA = 2002

senha = int(input())

while senha != SENHAVALIDA:
    print("Senha Invalida")
    senha = int(input())

if senha == SENHAVALIDA:
    print("Acesso Permitido")