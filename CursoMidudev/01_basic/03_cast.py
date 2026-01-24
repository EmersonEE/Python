#transformar tipo de un valor a otro

print("Conversion de tipoos")

print(type("100"))
print(type(int("100")))

print(int("100")+21)
print(type(str(21) + "100"))

print(float("3.1416"))
print(int(3.5616)) #No aproxima solo corta el decimal
print(round(2.5)) #redondea al par mas cercano cuando esta en el centro
print(round(3.5))
print(bool(3))
print(bool(0)) #el unico que se convierte en false es el 0
print(bool(-1))




print(bool("")) #La unica que se convierte en false es la cadena vacia
print(bool(" "))
print(bool("false"))

