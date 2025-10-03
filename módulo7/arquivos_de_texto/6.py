arquivo = "spotify-2023.csv"

musicas_ano = {}

with open(arquivo, "r", encoding="latin-1") as f:
    cabecalho = f.readline()
    for linha in f:
        partes = linha.strip().split(",")

        # ignorar linhas com aspas
        if '"' in linha:
            continue

        nome = partes[0]
        artista = partes[1]
        ano = int(partes[3])
        streams = int(partes[8])

        if 2012 <= ano <= 2022:
            if ano not in musicas_ano or streams > musicas_ano[ano][3]:
                musicas_ano[ano] = [nome, artista, ano, streams]

resultado = [musicas_ano[ano] for ano in sorted(musicas_ano)]
print(resultado)