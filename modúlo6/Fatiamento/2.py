# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Lista para armazenar os nomes dos domínios
dominios = []

# Percorre cada URL e extrai o nome do domínio
for url in urls:
    dominio = url[4:-4]  # remove os 4 primeiros e os 4 últimos caracteres
    dominios.append(dominio)

# Mostra o resultado
print(dominios)