ano = int(input("Digite o ano: "))

print("Bissexto" if ((ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)) else "Não Bissexto")