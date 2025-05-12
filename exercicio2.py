numSecreto = int(input("Usuario 1, insira um numero de 0 a 100 para o usuário 2 adivinhar: "))
num = 0
soma = 0
while num != numSecreto:
    num = int(input("Usuario 2, insira um numero para tentar adivinhar, o número secreto: "))
    num = soma + num
    if num < numSecreto:
        print("Menor! Tente novamente: ")

    elif num > numSecreto:
        print("Maior! Tente novamente: ")

    else:
        print("Você Acertou")