with open("frase.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

palavra = ""
palavras = []

for c in conteudo:
    if c.isalpha() or c == "á" or c == "é" or c == "í" or c == "ó" or c == "ú" or c == "ç":
        palavra += c
    else:
        if palavra != "":
            palavras.append(palavra)
            palavra = ""

if palavra != "":
    palavras.append(palavra)

with open("palavras.txt", "w", encoding="utf-8") as f:
    for p in palavras:
        f.write(p + "\n")

with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())