idade_juliana = int(input("Digite a idade de Juliana: "))

idade_cris = int(input("Digite a idade de Cris: "))

verificador1 = (idade_juliana > 17) == (idade_cris > 17)

verificador2 = (idade_juliana > 17) and (idade_cris > 17)

print(verificador1)
print(verificador2)