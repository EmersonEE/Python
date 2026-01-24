# Expresiones regulares
"""
- Busqueda avanzada: encontrar patrones especificos en textos grandes de forma rapida y precisa.
  un editor de md solo usando regex
- Validacion de datos: Asegurarte que los datos que infresa un susauro como el email, telefono, etc son correctos.

- Extraccion de informacion:

- Manipulacion de texto: Extraer, reemplazar y modificar partes de la cadena de texto facilmente



"""

# 1. Importar el modulo de expressiones regulares
import re
import os

os.system("clear")

# 2. Crear un patron que es una cadena de texto.
pattern = "Hola"
# 3. El texto donde queremos buscar
text = "Hola Mundo"
# 4. Usar la funcion de busqueda de "re"
result = re.search(pattern, text)
print(result)

if result:
    print("He encontrado el patron en el texto")
else:
    print("No he encontrado el parton en el texto")

# Metodos de re
# .group devuelve la cadena que coincide con el pattern
print(result.group())
# .start() devuelve la posicion inicial de la coincidencia
#
print(result.start())

# Ejercicio 1: Encuentre la primera ocurrencia de la palabra "IA" en el siguiente texto
# e inidica que posicion empieza y termina la coincidencia
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)
if found_ia:
    print(
        f"He encontrado el patron en el texto la posicion {found_ia.start()} y termina en la posicion {found_ia.end()}"
    )
else:
    print("No he encontrado el patron en el texto")

# Encontrar todas las coincidencias de un patron,
# .findall devuelve una lista con todas las coincidencia
#
text = "Me gusta Python. Python es lo maximo. AUnque Python no es tan dificil, ojo con Python"
pattern = "Python"
matches = re.findall(pattern, text)

print(matches)


print(len(matches))

# Metodo Iter
# iter() es para iterar todos los resultados
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group(), match.start(), match.end())


# MODIFICADORES
# los modificadores son opciones que se pueden agregar a un patron para camviar su compartamiento
# .ignorecase : ignora las mayusculas y minusculas

text = "Todo IA el mundo dice que la ia nos va a quitar el trabajo. Pero solo hace Ia falta ver como la puede iA cagar con las Regex para ir con cuidado"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)
if found:
    print(f"he Encontrado el patron {found} ")
# 5:08:00
