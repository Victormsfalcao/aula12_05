soma = 0
for i in range(5):
    num = int(input("Insira um número: "))
    soma = soma + num
    media = soma / 5
    if media > 7:
        print("Aprovado")

    elif media < 4:
        print("Reprovado")

    else:
        print("Recuperação")