import random

def imprime_enforcado(erros, enforcados):
    print(enforcados[erros])

# carregar palavras
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip() for linha in f.readlines()]

# carregar enforcado
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    estagios = f.read().split("\n\n")

palavra = random.choice(palavras)
progresso = ["_"] * len(palavra)
erros = 0
tentativas = 6

print("Palavra:", " ".join(progresso))

while erros < tentativas and "_" in progresso:
    letra = input("Digite uma letra: ").lower()

    if letra in palavra.lower():
        for i, c in enumerate(palavra.lower()):
            if c == letra:
                progresso[i] = palavra[i]
    else:
        erros += 1
        imprime_enforcado(erros, estagios)

    print("Palavra:", " ".join(progresso))

if "_" not in progresso:
    print("Parabéns, você venceu! A palavra era:", palavra)
else:
    print("Você perdeu! A palavra era:", palavra)