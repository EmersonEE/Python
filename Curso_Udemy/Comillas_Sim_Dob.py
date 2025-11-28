from string import printable
#Simpre usar comillas simples a menos que el texto contenga apostrofes

text = 'Hola Python'
text2 = "Hola Python"

result = text == text2

print(result)
message = 'Hola, Andres'
print(message)

message = 'EL codigo es del usuario\'s'
print(message)
message = "Le codigo es del usuario's"
print(message)

#en pyhon las variables multipalabra se separan con "_" mientras que en otros lenguajes se Mayuscula textMultiLine
#tescto con mutilineas
text_multi_line = """
Esta es una
cadena de
varias lineas
en
python
esto es muy util
"""
print(text_multi_line)
