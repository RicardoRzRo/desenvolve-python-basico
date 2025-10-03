frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
nova_frase = ""

for letra in frase:
    if letra in vogais:
        nova_frase = nova_frase + "*"
    else:
        nova_frase = nova_frase + letra

print("Frase modificada:", nova_frase)