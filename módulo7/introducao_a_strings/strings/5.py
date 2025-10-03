texto = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
contador = 0
i = 0

while i < len(texto):
    if texto[i] in vogais:
        print("Vogal", texto[i], "na posição", i)
        contador = contador + 1
    i = i + 1

print("Quantidade de vogais:", contador)