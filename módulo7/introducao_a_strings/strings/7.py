import random

def encrypt(lista_strings):
    n = random.randint(1, 10)  # chave
    resultado = []

    for palavra in lista_strings:
        criptografada = ""
        for c in palavra:
            codigo = ord(c)
            novo_codigo = codigo + n
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            criptografada = criptografada + chr(novo_codigo)
        resultado.append(criptografada)

    return resultado, n


# Exemplo de uso
nomes = ["ana", "joao", "maria"]
criptografados, chave = encrypt(nomes)

print("Chave:", chave)
print("Criptografados:", criptografados)