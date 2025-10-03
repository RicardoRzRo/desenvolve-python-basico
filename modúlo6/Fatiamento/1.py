# Solicita números indefinidamente
numeros = []
print("Digite números inteiros (digite 'fim' para encerrar, mínimo de 4 números):")

while True:
    entrada = input()
    if entrada.lower() == "fim":
        if len(numeros) >= 4:
            break
        else:
            print("Você precisa digitar pelo menos 4 números.")
            continue
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Entrada inválida! Digite um número inteiro ou 'fim' para encerrar.")

# Impressões com fatiamento
print("\nLista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("A lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])