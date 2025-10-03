genero = input("Digite seu gênero (M ou F): ")

idade = int(input("Digite sua idade: "))

tempo_de_servico = int(input("Digite o tempo de serviço: "))

verificador = ((genero == "F") and (idade > 60)) or ((genero == "M") and (idade > 65)) or(tempo_de_servico >= 30) or ((idade == 60) and (tempo_de_servico >= 25))
print(f"Pontos de atributo consistentes com a classe escolhida: {verificador}")