with open("memorialanotado.xml", "r", encoding="utf-8") as f:
    texto = f.read()

contagem = texto.count("</prescription>")

print("Número de ocorrências:", contagem)