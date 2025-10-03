arquivo = "estomago.txt"

with open(arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

# primeiras 25 linhas
print("Primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

# número de linhas
print("\nNúmero de linhas:", len(linhas))

# linha mais longa
linha_maior = max(linhas, key=len)
print("\nLinha com mais caracteres:\n", linha_maior.strip())

# contagem de nomes
texto = " ".join(linhas).lower()
cont_nonato = texto.count("nonato")
cont_iria = texto.count("íria")  # atenção: acento

print("\nMenções a Nonato:", cont_nonato)
print("Menções a Íria:", cont_iria)