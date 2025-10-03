import random

lista1 = []
lista2 = []

interseccao = []

for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

for i in range(20):
    if (lista1[i] in lista2):
        if (lista1[i] not in interseccao):
            interseccao += [lista1[i]]

print(f"lista1 - {lista1}")
print(f"lista2 - {lista2}")

print("Interseção - ",sorted(interseccao))

print("\nContagem:")
for valor in interseccao:
    print(f"{valor}: (lista1={lista1.count(valor)}, lista2={lista2.count(valor)})")