with open("memorial.txt", "r", encoding="utf-8") as f:
    texto = f.read()

with open("memorial_s.txt", "w", encoding="utf-8") as f:
    f.write(texto.replace("ſ", "s"))

print("Conversão realizada com sucesso!")