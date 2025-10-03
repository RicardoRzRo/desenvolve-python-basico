distancia = int(input("Digite a distância da entrega (KM): "))
peso = int(input("Digite o peso do pacote (KG): "))
taxa = 10 if (peso > 10) else 0

if(distancia <= 100):
    print(f"O valor do frete é {peso + taxa}")
else:
    if(distancia > 100 and distancia <= 300):
        print(f"O valor do frete é {(peso*1.5) + taxa}")
    else:
        if(distancia > 300):
            print(f"O valor do frete é {(peso*2) + taxa}")
