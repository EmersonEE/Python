import os

os.system("clear")

print("\n Valores booleanos Basicos: ")
print(True)
print(False)


print("\n Operadores de Comparacion: ")
print("5 > 3: ", 5 > 3) #True
print("5 < 3: ", 5 < 3) #False
print("5 == 5: ", 5 == 5) #True (Igualdad)
print("5 != 3: ", 5 != 3)  #True (Desigualdad) 
print("5 >= 5: ", 5 >= 5) #True (Mayor o igual que)
print(" 5 <= 3: ", 5 <= 3) #False (menos o igual que)


print("\n Operador de comparcion")
print("manzan < pera: ", "manzana" < "pera") #True devuelve true xq m esta antes que la p en el abecedario xd
print("'Hola' == 'hola'", "Hola" == "hola") #False


numero = 5

if numero:
    print("EL numero no es cero")
    
numero = 0

if numero:
    print("Aqui no entrara nunca, xq 0 es false en booleano")
    
if numero == 3:
    print("== es para comparar")


#Terminarias
print("\n La Condicion Ternaria: ")
#es una forma concisa de un if-else en una linea de codigo
#[codigo si comple la condicion] if [condicion ] else [condigo sin o comple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)