with open("final.xml", "r", encoding="utf-8") as f:
    texto = f.read()

entradas = texto.split('<div type="entry">')

for i, entrada in enumerate(entradas[1:], start=1):
    contagem = entrada.split("</div>", 1)[0].count("<prescription")

    print(f"Entrada {i}: {contagem} ocorrências")