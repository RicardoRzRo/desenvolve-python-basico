n = int(input("Digite o valor de repetições: "))
maior = 0

while (n>0):
    x = int(input("Digite o valor x: "))
    if (x > maior):
        maior = x
    n = n - 1
print(maior)