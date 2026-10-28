import re

with open("final.xml", "r", encoding="utf-8") as f:
    texto = f.read()

conditions = re.findall(r"<condition\b.*?</condition>", texto, re.DOTALL)

with open("conditions.txt", "w", encoding="utf-8") as f:
    for condition in conditions:
        f.write(condition + "\n")

print("Operação realizada com sucesso!")

# Para conseguirmos extrair as etiquetas e o seu conteúdo, foi necessário utilizar expressões regulares (em inglês, regular expressions (re)).
# O padrão utilizado para a extração, neste caso para a etiqueta <condition>, foi o seguinte: "<condition\b.*?</condition>".
# "\b" encontra o início da etiqueta, <condition (antes de quaisquer atributos).
# ".*?" seleciona todo o conteúdo até </condition>.
# Basta modificar o padrão para outra etiqueta para se proceder à extração da mesma.
# A extração é impressa num novo ficheiro txt, neste caso "conditions.txt". No entanto, é necessário mudar o nome do mesmo sempre que procedemos à sua extração, para que os ficheiros já extraídos não sejam reescritos.
# A linha 9 também deve ser alterada dependendo da etiqueta:
# <simple> - for simple in simples
# <bibl> - for bibl in bibliography
# <origin> - for origin in origins
# <person> - for person in people
