with open("memorial.txt", "r", encoding="utf-8") as f:
    texto = f.read()

with open("memorial_s.txt", "w", encoding="utf-8") as f:
    f.write(texto.replace("ſ", "s"))

print("Conversão realizada com sucesso!")


# Na linha de código 5, entre as primeiras aspas, colocamos o caractér que desejamos substituir e, entre as segundas aspas , o caractér que o vai substituir.
# É necessário prestar atenção aos nomes dos documentos de entrada e saída. Estes devem ser diferentes para que o documento original não seja reescrito. 
