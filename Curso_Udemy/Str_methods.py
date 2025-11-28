#Manejo de Strings con metodos
from string import printable
from typing_extensions import Text


name = "Emerson Perez"
course = "Curso de Python"
#Todo EN MAYUSCULAS
print(name.upper())
name_upper = name.upper()
print(name_upper)
#Obtener un valor booleano
print(name == name_upper)
#Todo en minusculas
print(name.lower())

words = 'curso de python'
#Poner La primera letra en mayuscula
print(words.capitalize())
#Poner cada palabra de iniciio en mayuscula
print(words.title())

words = '    hola Emerson   '
#Eliminar espacios limpiar ambos lados
print(words.strip())
#Eliminar espacios a la izquierda
print(words.lstrip())
#Eliminar espacios a la derecha
print(words.rstrip())

#Reemplazar partes de texto
text = 'Hola Python'
print(text)
print(text.replace('Python','Java'))

#Separar en lista (arreglo) separado por ,
#El Indice seria = 0,1,2,3,4
text = "Emerson, Aldair, Pérez, Rivera, 201902852"
data_list = text.split(',')
print(data_list)
#Para imprimir solo un indice
print(data_list[0])
text = "Emerson Aldair Pérez Rivera 201902852"
print(text.split())
#Para imprimir solo un indice
print(text.split()[3])

#Pasar lista a cadena de texto normal
data = ['Emerson', 'Aldair', 'Pérez', 'Rivera', '201902852']
# ' ' es un string vacio con lo que se llene eso sera el separador de cada palabra
text = '_'.join(data)
print(text)

text = 'Hola, Emerson que tal estas'
#Buscar he imprimir el indice en el cual se encuentra la palabra si no se encuentra la palabra devuelve -1
print(text.find('Emerson'))
print(text.find('EmersoN'))
print(text[6])
print(text.index('que')) #Si no lo encuentra marca error

#Saber si la oracion empieza con una palabra en espcifico, devuelve un True o False
print(text.startswith("Emerson"))
#Saber si la oracion termina con una palabra en espcifico, devuelve un True o False
print(text.endswith('Emerson'))


number = '1234'
decimal = '1234.3'
text = 'Python'
mix = 'Python3'
print(number.isnumeric())
print(decimal.isdecimal())
print(mix.isalnum())
print(mix.isalpha())
print(text.isalpha())

text = '      Hola Emerson como estas, bienvenido al curso de python'
text_clean = text.strip().capitalize().title()
print(text_clean)

new_text = text_clean.replace('Curso De Python', 'Curso de Python 3')
print(new_text)
words = new_text.split()
print(words)
