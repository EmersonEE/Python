import os

os.system("clear")

# Ejercicio 1: Determinar el Mayor de dos numeros
# Pide al usuario que introduzca dos numeros y muestra un mensaje
# INdice cual es el mayor o si son iguales

numero_a = int(input("Introduzca un numero: "))
numero_b = int(input("Introduzca un numero: "))

print(f"Los numeros que ingreso son {numero_a} y {numero_b}")

if numero_a == numero_b:
    print(f"El numero {numero_a} es igual a el numero {numero_a}. ")
elif numero_a >= numero_b:
    print(f"El numero {numero_a} es mayor a el numero {numero_b}")
else:
    print(f"El numero {numero_b} es mayot a el numero {numero_a}")
