import json
import serial

ingresar = []
numeros = [12, 12, 43, 32, 232]

ser = serial.Serial()
print(ser.name)

print(ser)

for i in range(0, 6):
    dato = input("Ingrese los numeros: ")
    ingresar.append(dato)
with open("secuencia.json", "w") as f:
    json.dump(ingresar, f)
