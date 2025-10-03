texto = input("Digite a string: ")
objetivo = input("Digite a palavra objetivo: ")

tamanho = len(objetivo)
anagramas = []

i = 0
while i <= len(texto) - tamanho:
    pedaco = texto[i:i+tamanho]

    # verifica se é anagrama (mesmos caracteres)
    lista_pedaco = list(pedaco)
    lista_objetivo = list(objetivo)

    lista_pedaco.sort()
    lista_objetivo.sort()

    if lista_pedaco == lista_objetivo:
        anagramas.append(pedaco)

    i = i + 1

print("Anagramas encontrados:", anagramas)