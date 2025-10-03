frase = input("Digite uma frase: ")

contador = 0
i = 0
while i < len(frase):
    if frase[i] == " ":
        contador = contador + 1
    i = i + 1

print("Quantidade de espaços em branco:", contador)