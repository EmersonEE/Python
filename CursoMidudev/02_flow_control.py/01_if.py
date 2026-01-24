#Sencientecias condicionales IF

import os

os.system("clear") #Con este comando puedo mandar a llamar comandos del sistema, en este caso el comando clear
print("Mi mensaje")


print("\n Sentencia simple condicional")

edad = 16

if edad >= 18:
    print("Eres Mayor de Edad")
    print("Felicidades")
print("Felicidades")


    
edad = 15

if edad >= 18:
    print("Eres Mayor de edad")
else:
    print("Eres Menor de edad")
    
    
print("\n Sentencia con elif")

nota = 7
if nota >= 9:
    print("!Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Valiste verga")
    
    
#Operadores LOGICOS

print("\n Condicionales Multiples")
edad = 25

tiene_carnet = True
if edad >= 18 and tiene_carnet:
    print("PUedes conducir")
else:
    print("Policia")


if edad >= 18 or tiene_carnet:
    print("PUedes conducir")
else:
    print("Paga a la policia")
    


es_fin_de_semana = False
if not es_fin_de_semana: #Invertir el False
    print("A ver partidos")
    
print("Anidar COndiciones")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la Disco")
    
