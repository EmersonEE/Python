# creacion de listas

print("\n Crear Listas")
import os

os.system("clear")

lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzana", "peras", "platanos"]
lista3 = [1, "hola", 3.13, True]  #

lista_vacia = []
lista_de_listas = [[1, 2], ["calcetin", 4]]
matrix = [[1, 2], [2, 3], [4, 5]]


print(lista1)
print(matrix)

# acceder a elementos por indice

print("\n Acceso a elementos por indice")
print(lista2[0])  # Devuelve manzanas

print(lista2[1])

print(lista2[-1])  # devuleve el ultimo -1
print(lista2[-2])

print("\n Listas de listas")
print(lista_de_listas[1][0])  # imprimo calcetni

# Rebanado de listas
# Slicing(Rebanado)
lista1 = [1, 2, 3, 4, 5]
# quiero tener una lista de 2,3,4
print(lista1[1:4])  # no toma en cuenta en indice en posicion 4
print(lista1[:3])  # Imrpime el 1,2,3
print(lista1[3:])  # imprime los dos ultimos 4,5
print(lista1[:])  # imrpime una copia
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Hay mas magia
# print(lista1[desde:hasta:paso])
print(lista1[::3])  # Que haga una copia hasta el final y vaya de dos en dos

print(lista1[::-1])  # para devolcer los indices inversos

# modificar una lista
lista1[0] = 20
print(lista1)  # Coloca el 20 en la posicion inicial

# añadir elementos a una lista
lista1 = [1, 2, 3]
# forma larka y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)
# forma corta y mas eficientel
lista1 += [7, 8, 9]


# Recuperar longitd de una lista

print("Longitud de una lista", len(lista1))
