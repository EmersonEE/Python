# bloques de codigo reutilizables y parametizables para hacer tareas especificoas

"""Definicion de una funcion

def nombre_de_la_funcion(parametro1,parametro2,....):
    # docstring para documentar
    # cuero de la funcion
    return valor_de_retorno #opcional
"""


def saludar():
    print("Hola")


saludar()

# Def con parametro1


def saludar_a(nombre):
    print(f"Hola {nombre}")


saludar_a("Emerson")
# El parametro es loque acepta la funcion
# EL argumento es lo que devuelve xd


def suma(a, b):
    suma = a + b
    return suma


result = suma(6, 1)
print(result)

# Documentar Dunciones con docstring


def restar(a, b):
    """Resta dos numeros y devulve el resultado"""
    return a - b


print(restar.__doc__)

# Parametros por defecto


def multiplicar(a, b=2):
    return a * b


multiplicar(5, 0)
# Argumentos por clave


def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre} , tengo {edad} años y me identifico como {sexo}")


describir_persona("Emerson", 25, "Hombre")


describir_persona(sexo="Hombre", nombre="Emerson", edad=55)


# argynebtos de la longitud de catiable *arg
def sumar_numeros(*arg):
    suma = 0
    for numero in arg:
        suma += numero
    return suma


sumar_numeros(1, 3, 4, 452, 23, 234)


def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
