with open("memorialanotado.xml", "r", encoding="utf-8") as f:
    texto = f.read()

contagem = texto.count("</prescription>")

print("Número de ocorrências:", contagem)

# Na linha 4 do código colocamos entre aspas a etiqueta que queremos contar. Colocamos a etiqueta de fecho da anotação porque esta é igual em todas as anotações. 
# No entanto, devemos prestar atenção ao facto de que este código conta apenas o número total de etiquetas que ocorrem no documento anotado. 
# No caso de etiquetas com ID, para efeitos de contagem total, foram extraídas as etiquetas e os segmentos que anota e procedemos à sua contagem manual. 
