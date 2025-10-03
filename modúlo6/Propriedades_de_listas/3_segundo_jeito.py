import random

# Preenche as listas
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Interseção sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

# Impressões
print("Lista 1 - ", lista1)
print("Lista 2 - ", lista2)
print("Interseção - ", interseccao)

print("\nContagem:")
for valor in interseccao:
    print(f"{valor}: (lista1={lista1.count(valor)}, lista2={lista2.count(valor)})")