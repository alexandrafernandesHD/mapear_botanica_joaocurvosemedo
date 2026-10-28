import re

with open("final.xml", "r", encoding="utf-8") as f:
    texto = f.read()

conditions = re.findall(
    r"<condition\b[^>]*>.*?</condition>", texto, re.DOTALL)

with open("conditions.txt", "w", encoding="utf-8") as f:
    for condition in conditions:
        f.write(condition + "\n")

print("Operação realizada com sucesso!")