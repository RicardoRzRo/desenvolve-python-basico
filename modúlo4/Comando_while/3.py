n1 = int(input("Digite o valor 1: "))
n2 = int(input("Digite o valor 2: "))
n3 = int(input("Digite o valor 3: "))

m = (n1 + n2 + n3) / 3

if (m >= 60):
    print("Aprovado")
elif (m >= 40):
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")