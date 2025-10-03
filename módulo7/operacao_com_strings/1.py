data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

partes = data.split("/")
dia = partes[0]
mes = int(partes[1])
ano = partes[2]

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

print("Você nasceu em", dia, "de", meses[mes-1], "de", ano)