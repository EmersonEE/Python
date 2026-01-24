# Ranger ()
# Permite crear una secuenda de numeros, puede ser utili para for, pero no solo para eso


print("\nRange()")
nums = range(0, 5)
print(type(nums))

# Generando una secuencia de numeros de 0 al 9

for num in range(10):
    print(num)

# range (inicio, fin)
for num in range(5, 10):
    print(num)

# Range (inicio, fin, paso=)
for num in range(0, 10, 5):
    print(num)

# range puede tener numeros negativos
for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

nums = range(10)
list_of_nums = list(nums)
print(type(list_of_nums))

# Accion para repteir las veces que querramos

for _ in range(5):  # _ es una variable que no se usara es de python esto
    print("Hacer cinco veces algo")
