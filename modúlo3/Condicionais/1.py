#n1 = int(input("Digite o primeiro número: "))
#n2 = int(input("Digite o segundo número: "))

n1, n2 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))

print("A soma dos números é um número ímpar" if ((n1 + n2) % 2) else "A soma dos números é um número par")