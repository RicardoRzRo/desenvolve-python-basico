# Lê a primeira lista
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print(f"Digite os {n1} elementos da lista 1:")
for _ in range(n1):
    lista1.append(int(input()))

# Lê a segunda lista
n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {n2} elementos da lista 2:")
for _ in range(n2):
    lista2.append(int(input()))

# Cria a lista intercalada
intercalada = []
menor = min(n1, n2)

# Alterna até o fim da menor lista
for i in range(menor):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])

# Adiciona os elementos restantes da maior lista
if n1 > n2:
    intercalada.extend(lista1[menor:])
else:
    intercalada.extend(lista2[menor:])

# Mostra o resultado
print("Lista intercalada:", *intercalada)
