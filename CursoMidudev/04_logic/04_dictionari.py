# Los diccionarios son colecciones de pares clave-valor
import os

os.system("clear")

persona = {
    "nombre": "Emerson",
    "edad": 27,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {"twitter": "@x", "instagram": "@Emerson", "facebook": "@Aldair"},
}
print(persona["nombre"])
print(persona["calificaciones"][2])


# cambiar valores al acceder
persona["nombre"] = "Perez"
persona["calificaciones"][2] = 10

print(persona)
# Elimnar completamente una propiedad

del persona["edad"]
print(persona)

es_estudiaante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiaante}")
print(persona)

# sobreescirbir un valor , sobreescirbir un diccionario con otro diccionario

a = {"name": "Emerson", "age": 25}
b = {"name": "Aldair", "es_estudiante": True}
a = b

a.update(b)
print(a)


# Comprobar si existe una propiedad
print("name" in persona)  # False
print("nombre" in persona)  # True

# obtener todas las claves

print(persona.keys())
# obtener todos los valores
print(persona.values())
print(a)

for key, value in persona.items():
    print(f"{key}: {value}")
