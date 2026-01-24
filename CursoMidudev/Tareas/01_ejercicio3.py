# Ejercicio 1: El mensaje secreto
# Data la siguiente lista
# mensaje = ["C","o","d","i","g","o"," ", "s","e","c","r","e","t","o"]
# Utilizando slicing y concatenacion crea una nueva lista que contenga solo el mensaje "secretoo"


mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print(mensaje)
print(mensaje[7::])
print(f"{mensaje[7]}{mensaje[8]}")
for letra in mensaje[7::]:
    print(f"Mensaje :{letra}")


lista1 = [1, 2, 3, 4, 5, 6]
