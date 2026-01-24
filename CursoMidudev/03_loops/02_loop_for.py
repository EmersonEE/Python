#Permita ejecutar un vloque de codigo repetidamente mientras ITERE un iterable o una lista

print("\n Bucle For")

#tirar sobre una lista
frutas = ["manzan","pera","mandarina"]
for fruta in frutas:
    print(fruta)
    
#ITerar sobre una cualqujier cosa que se iterable

cadena = "emerson"
for caracter in cadena:
    print(caracter)
    
#enumerate 

for index, fruta in enumerate(frutas):
    print(f"El indice es {index} y la fruta es {fruta}")
    

#bucles anidados

letras = ["a","b","c"]
numeros = [1,2,3]

for letra in letras:
    for numero in numeros:
        print(f"{letra} {numero}")

#break
print("\n Break")
animales = ["peroo","gato","raton","loro","pez","canario"]
for index,animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice {index}")
        break
    
#continue 
print("\nCOntinue")
animales = ["peroo","gato","raton","loro","pez","canario"]
for index,animal in enumerate(animales):
    if animal == "loro":
        continue
    print(animal)
    
# Compresion de listas list comprehension

animales = ["peroo","gato","raton","loro","pez","canario"]

animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)

#muesta los numeros pares de una lista

pares = [num for num in [1,2,3,4,5,6] if num %2 == 0]
print(pares)

#Minuo 3:16:47