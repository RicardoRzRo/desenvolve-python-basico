n = int(input("Digite a quantidade de experimentos registrados: "))
cont = n

total = Coelhos = Ratos = Sapos = 0

while (cont > 0):
    quant, tipo = int(input("Digite a quantidade: ")), input("Digite o animal (S, R ou C): ")
    total += quant
    if (tipo == "C"):
        Coelhos += quant
    elif (tipo == "R"):
        Ratos += quant
    elif (tipo == "S"):
        Sapos += quant
    cont = cont - 1

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {Coelhos}")
print(f"Total de ratos: {Ratos}")
print(f"Total de sapos: {Sapos}")
print(f"Percentual de coelhos: {(100/total)*Coelhos}")
print(f"Percentual de ratos: {(100/total)*Ratos}")
print(f"Percentual de sapos: {(100/total)*Sapos}")