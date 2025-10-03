livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["A Revolução dos Bichos", "George Orwell", 1945, 152],
    ["Grande Sertão: Veredas", "Guimarães Rosa", 1956, 624],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["Capitães da Areia", "Jorge Amado", 1937, 280],
    ["Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 208]
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        f.write(",".join([str(x) for x in livro]) + "\n")