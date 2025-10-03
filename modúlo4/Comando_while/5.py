n = int(input("Digite a quantidade de respondentes: "))
cont = n
media = 0

while (cont > 0):
    idade = int(input("Digite a idade: "))
    media += idade
    cont = cont - 1
media = media / n
print(media)