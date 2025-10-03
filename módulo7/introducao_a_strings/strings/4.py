celular = input("Digite o número de celular (sem traços, só números): ")

# Se tiver 8 dígitos, coloca o 9 na frente
if len(celular) == 8:
    celular = "9" + celular
# Se já tiver 9 dígitos, só confere se começa com 9
elif len(celular) == 9:
    if celular[0] != "9":
        print("Número inválido")
    else:
        print("Número válido")

# Formatar com traço depois do 5º dígito
if len(celular) == 9 and celular[0] == "9":
    celular_formatado = celular[:5] + "-" + celular[5:]
    print("Número formatado:", celular_formatado)