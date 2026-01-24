import os

os.system("clear")
# Metodos para listas
lista1 = [1, 2, 3, 4, 5]
lista1.append(6)  # añade un elemento al final
print(lista1)

lista1.insert(1, 10)
print(lista1)
lista1 = ["a", "b", "c", "d"]
lista1.insert(
    1, "@"
)  # Inserta u nelemento en la posicion que le indiquemos como primer argumento(indice)
print(lista1)

lista1.extend(["e", "f"])  # agregar mas elementos
print(lista1)

# eliminar elemetnos de la lista

lista1.remove("@")  # Elimina la primera aparicion de la candena de texto

print(lista1)
print("Hola mundo")


ultimo = lista1.pop()  # Elimina el ultimo elemento de la lista y te lo devulve o el elemento del indice que se le ponga
print(lista1)
print(ultimo)

lista1.pop(1)  # elimnar el sengudo elemento de la lista
print(lista1)

# elimnar por lo bestia

del lista1[-1]
print(lista1)

lista1.clear()  # Elimina todos los elementos de la lista

# eliminar un rango de elementos
lista1 = [1, 2, 3, 4, 5, 6, 7]
del lista1[1:3]
print(lista1)

# odenar listas
print("\nOrdenar listas modiciando la original")
numeros = [3, 10, 310, 6, 99, 101]
numeros.sort()  # no la devuelve
print(numeros)

print("\nOrdenar listas creando una nueva lista")
numeros = [1, 2, 453, 234, 5, 32, 56]
sorted_numeros = sorted(numeros)
print(sorted_numeros)
print("\n Hola mundo como estas")
print("\n Ordenar una lista de cadenas de texto mezclando mayusculas y minusculas")
frutas = ["Manzana", "Pera", "Limon", "manzana", "pera", "limon"]
frutas.sort(key=str.lower)
print(frutas)


# Mas metodos utiles
animals = ["Oso", "PUta", "Oso"]
print(len("Oso"))
print(animals.count("Oso"))
print("Oso" in animals)  # Comprueba si una oso en la lista -> True
