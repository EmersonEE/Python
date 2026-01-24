# Permite ejecutar un bucle siempre que sea True

print("\n bucle While ")
contador = 0

while contador < 5:
    print(contador)
    contador += 1  # Es importante para no hacer un bucle infinito


# Break para romper el bucle infinito
# while True:
#  j
# print("Hola")  # Bucle infini
# contador += 1
# if contador == 5:
#     break


while contador <= 100:
    contador += 1
    print(contador)
    if contador % 5 == 0:
        break  # Sale del bucle


# continue hace es saltar esa iteracion en concreto y continuar el bucle
print("\n Bucle Continue")
contador = 0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)


# Else que se ejecuta en bucles

print("j\n Bucle while con eslse")
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

# Ejercicio ppedirl al usuario un numero que tiene que ser + si no no deja pasarlo

numero = -1


while numero < 0:
    try:
        numero = int(input("Escrine un numero positivo: "))
        if numero < 0:
            print("EL numero debe ser positivo Intenta de nuevo")
    except:
        print("Lo que introduces debe ser un numero, que si no peta!!!!")


print(f"EL numero que has introducido es {numero}")
