with open("memorialanotado.xml", "r", encoding="utf-8") as f:
    texto = f.read()

entradas = texto.split('<div type="entry">')

for i, entrada in enumerate(entradas[1:], start=1):
    contagem = entrada.split("</div>", 1)[0].count("</prescription>")

    print(f"Entrada {i}: {contagem} ocorrências")

# Com este código obtemos a contagem de uma etiqueta específica por entrada (<div type="entry">). 
# Na linha 7, após "count", é colocada a etiqueta que pretendemos contar o seu número de ocorrências por divisão. 
# O código recebe o Memorial anotado e divide-o por entradas através da etiqueta "<div type="entry">".
# De seguida enumeramos as entradas, começando pela primeira e percorrendo o resto do documento até ao seu final. 
# Em cada uma das entradas, o código seleciona o conteúdo até encontrar um fecho de etiqueta de divisão (</div>) e conta as ocorrências (nessa seleção) da string que pretendemos contar, neste caso </prescription>.
