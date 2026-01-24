print("Hola como te llamas?")
nombre = input()
print(nombre)
print(f"Hola {nombre}, encantado de conocerte")

nombre = input("Hola, Como te llamas??\n")

age = input("Cuantos Años tienes")

print(f"Dentro de 20 años tendras {int(age) + 20}")

print("Obtener multiples valores a la vez") #Usar split
pais, city = input("En que pais y ciudad vives?\n").split()
print(f"Vives en {pais}, {city}")