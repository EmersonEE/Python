"""
╔══════════════════════════════════════════╗
║           DÍA 3 - SEMANA 1               ║
║  Operadores aritméticos y conversión de tipos ║
╚══════════════════════════════════════════╝
"""

"""
Operador,Significado,Ejemplo,Resultado
+,Suma,5 + 3,8
-,Resta,10 - 4,6
*,Multiplicación,6 * 7,42
/,División (siempre da float),10 / 3,3.333...
//,División entera,10 // 3,3
%,Resto (módulo),10 % 3,1
**,Potencia,2 ** 3,8
"""

#Calculadora Basica

a = 15
b = 20

print(f"El valor del numero a es {a}")
print(f"El valor del numero a es {b}")

print("Suma a + b = " , a+b)
print("Resta a - b = ", a-b)
print("Multiplicacion a * b = ", a *b)
print("Division Normal a / b = ", a /b)
print("Divison entera a // b = ", a //b)
print("Modulo a % b = ", a%b)
print("Pontecia a ** b =  ", a**b)

#Convertir float a str
dinero_en_bolsillo = 3.75
print(f"tengo en mi bosillo Q{str(dinero_en_bolsillo)}")