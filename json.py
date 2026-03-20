import json as jss


numeros = [12, 23, 12, 14]

with open("secuencia.json", "w") as f:
    jss.dump(numeros, f)
