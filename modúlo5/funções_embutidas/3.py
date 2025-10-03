import random

na = random.randint(1,10)
resposta = 0

while (resposta != na ):
    resposta = int(input("Adivinhe o número entre 1 e 10: "))
    if ((resposta - na) > 0 ):
        print("Muito alto, tente novamente!")
    elif ((resposta - na) < 0 ):
        print("Muito baixo, tente novamente!")
print(f"Correto! O número é {na}")