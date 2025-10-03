while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')

    if frase.lower() == "fim":
        break

    # remover espaços e pontuação
    limpa = ""
    for c in frase:
        if c.isalnum():  # só letras e números
            limpa = limpa + c.lower()

    if limpa == limpa[::-1]:
        print('"' + frase + '" é palíndromo')
    else:
        print('"' + frase + '" não é palíndromo')