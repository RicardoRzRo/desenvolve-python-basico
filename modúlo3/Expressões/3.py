idade = int(input("Digite a sua idade: "))

jogos = input("Já jogou pelo menos 3 jogos de tabuleiro (True ou False)? ")

vitorias = int(input("Quantas jogos já venceu? "))

verificador = (idade >= 16 and idade <= 18) and (jogos == "True") and (vitorias > 0)

print(f"Apto para ingtessar no clube de jogos de tabuleiro: {verificador}")