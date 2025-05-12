senhaValida = "1234"
senha = ""
while senha != senhaValida:
    senha = input("Insira a senha: ")
    if senha != senhaValida:
        print("Tente novamente")

    else:
        print("Senha correta")