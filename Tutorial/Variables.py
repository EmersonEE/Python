x = 5 # x is of type int
y = "John" # y is now of type str

print(x)
print(y)

#Si desea especificar el tipo de datos de una variable 
x = str(3) #x string
y = int(3) #y int
z = float(3) # z will be 3.0

#Obtener el tipo de variable

x = 5
y = "John"
print(type(x))
print(type(y))

# Desempaquetar una colección
# Si tienes una colección de valores en una lista, tupla, etc., 
# Python te permite extraer los valores en variables. Esto se llama desempaquetar .

fruits = ["Apple", "Banana","Cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)