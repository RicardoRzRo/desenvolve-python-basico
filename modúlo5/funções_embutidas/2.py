import random
import math

n = int(input("Digite o número de valores aleatórios: "))

soma = 0

for i in range(0, n):
    soma += random.randint(0,100)
    print(soma)

resultado = math.sqrt(soma)

print(f"O resultado da raíz quadrada da soma dos valores é: {resultado}")