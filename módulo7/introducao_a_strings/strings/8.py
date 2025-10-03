cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

# remove pontos e traço
cpf_numeros = ""
for c in cpf:
    if c.isdigit():
        cpf_numeros = cpf_numeros + c

# pega os 9 primeiros dígitos
primeiros9 = cpf_numeros[:9]

# calcular primeiro dígito
soma = 0
multiplicador = 2
i = len(primeiros9) - 1
while i >= 0:
    soma = soma + int(primeiros9[i]) * multiplicador
    multiplicador = multiplicador + 1
    i = i - 1

resto = soma % 11
if resto < 2:
    digito1 = 0
else:
    digito1 = 11 - resto

print("Primeiro dígito calculado:", digito1)

# compara com o dígito do CPF digitado
if digito1 == int(cpf_numeros[9]):
    print("CPF válido (primeiro dígito)")
else:
    print("CPF inválido")