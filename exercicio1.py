nomes = [""] * 5

for i in range (len(nomes)):
    nomes [i] = input("Insira um nome: ").upper()

for j in nomes:
    if 'A' in j[0]:
        print(j, end = " ")

